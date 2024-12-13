import itertools
from dataclasses import dataclass
from enum import Enum

import numpy as np

from Utils.OpenScenario.Simulation.SmallStepBigStepSUL import SmallStepBigStepSUL
from Utils.AALpy.SULs.CacheSUL import CachedSinkStateSUL
from Utils.AALpy.SULs.WrappingSUL import ConditionalSinkStateSUL
from Utils.CompositeMapping import CompositeMapping
from Utils.OpenScenario.SimulationUtils import get_object_state, RMPosition
from Utils.OpenScenario.KPIs import (
  get_same_lane_TTC, AccelerationKPI, GenericStatefulKPI, get_bounding_box_distance, get_distance_RM
)
from Utils.OpenScenario.Simulation.SingleTargetFullControl import (
  SingleTargetFullControl, LaneChangeAbstraction, RelativeAction, LaneChangeAction
)
from Utils.AALpy.SULs.AbstractionSULs import discretization
from Utils.GeneralUtils import Slice, SimpleEnum

import lib.esminiLib as esmini


################################
#   Definition of Parameters   #
################################

# scenario to examine
scenario_name = "ScenarioACC"
path_to_scenario = f"OpenScenarioFiles/{scenario_name}.xosc"

# names of traffic participants
ego_name = "Ego"
target_name = "OverTaker"

# settings related to simulation time steps
simulation_time_step = 0.025#0.25
action_time_step = 0.5

repeats = int(action_time_step / simulation_time_step)
action_time_step = repeats * simulation_time_step
print(f"Exploration time step = {action_time_step}s")

# define which KPIs to track
def compose(kpi_name, obj_name):
  return f"{obj_name} {kpi_name}"

bb_distance_kpi = GenericStatefulKPI(get_bounding_box_distance, [ego_name, target_name], "distance (b.box)", "m")
ttc_kpi = GenericStatefulKPI(get_same_lane_TTC, [ego_name, target_name], "TTC", "s")
ds_KPI =  GenericStatefulKPI(lambda x, y: get_distance_RM(x,y).ds, [ego_name, target_name], "distance (long.)", "m")
dt_KPI =  GenericStatefulKPI(lambda x, y: get_distance_RM(x,y).dt, [ego_name, target_name], "distance (lat.)", "m")

ego_vel_KPI = GenericStatefulKPI(lambda x: x.speed, [ego_name], compose("velocity", "Ego"), "m/s")
target_vel_KPI = GenericStatefulKPI(lambda x: x.speed, [target_name], compose("velocity", "GVT"), "m/s")
ego_accel_kpi = AccelerationKPI(ego_name, compose("acceleration", "Ego"))
target_accel_kpi = AccelerationKPI(target_name, compose("acceleration", "GVT"))

kpis = [
  ego_accel_kpi, target_accel_kpi,
  #GenericStatefulKPI(get_same_lane_distance, [ego_name, target_name], "distance (same lane)", "m"),
  ds_KPI, dt_KPI, ego_vel_KPI, target_vel_KPI, ttc_kpi, bb_distance_kpi,
]

@dataclass(frozen=True)
class AccelerationAction:
  accel : float

  def __str__(self):
    return f"{self.accel} m/s^2"

class OtherActions(Enum):
  Prefix = "Prefix"

  def __str__(self):
    return self.value

BigStepAction = AccelerationAction | LaneChangeAction | OtherActions

# definition and abstraction of actions
acceleration_actions = [AccelerationAction(x) for x in [-10, -5, 0, 5]]
alphabet = list(itertools.chain(acceleration_actions, LaneChangeAction))

# definition of output abstraction
target_ttc = 0.5 # 0.35 leads to crash
target_ttc_tolerance = 0.2

disc_steps = [
  "too close", (1 - target_ttc_tolerance) * target_ttc,
  "critical", (1 + target_ttc_tolerance) * target_ttc,
  "close", target_ttc * 10,
  "far"
]
output_discretization = discretization(disc_steps)

class SinkState(SimpleEnum):
  LaneViolation = "Lane Violation"
  LaneInvasion = "Lane Invasion"
  VelocityViolation = "Velocity Violation"
  SlowLaneChange = "Slow Lane Change"
  RearEndCollision = "Rear End Collision"
  Crash = "Crash"

def output_abstraction(segment: list):
  kpi_slice = Slice[-len(segment):]

  for idx in range(-len(segment), 0):
    if bb_distance_kpi.data[idx] < 0.01:
      if ego_vel_KPI.data[idx] < target_vel_KPI.data[idx] and abs(dt_KPI.data[idx]) < 2 and ds_KPI.data[idx] < 0:
        return SinkState.RearEndCollision
      return SinkState.Crash
    if ego_accel_kpi.data[idx] < -15:
      return SinkState.Crash

  min_ttc = min(ttc_kpi.data[kpi_slice])
  return output_discretization(min_ttc)


target_outputs = ["critical", "too close", SinkState.Crash]
print(f"target outputs are: {target_outputs}")
print("")

class SinkStateOnDomainViolationSUL(ConditionalSinkStateSUL):
  def __init__(self, sul, EGO_id_or_name, GVT_id_or_name):
    super().__init__(sul, list(SinkState))
    self.GVT_id = GVT_id_or_name
    self.EGO_id = EGO_id_or_name

  def check_sink(self, letter):
    if letter is None:
      return False

    if isinstance(self.GVT_id, str):
      self.GVT_id = esmini.SE_GetIdByName(self.GVT_id)
    if isinstance(self.EGO_id, str):
      self.EGO_id = esmini.SE_GetIdByName(self.EGO_id)

    gvt_state = get_object_state(self.GVT_id)

    match letter:
      case AccelerationAction(accel) :
        if gvt_state.speed < 0.1 and accel < 0:
          return SinkState.VelocityViolation
      case LaneChangeAction():
        original_road = gvt_state.roadId
        original_lane = gvt_state.laneId
        velocity_sign = int(np.sign(original_lane) * (-1 if letter == LaneChangeAction.Left else 1))
        target_lane = original_lane + velocity_sign

        if gvt_state.speed < 1:
          return SinkState.SlowLaneChange

        gvt_position = RMPosition(True)
        gvt_position.set_lane_position(original_road, target_lane, 0, gvt_state.s, True)

        if np.sign(original_lane) != np.sign(target_lane) or not gvt_position.is_road(target_lane):
          return SinkState.LaneViolation

        d_t = 3 # TODO should be parametric

        ego_state = get_object_state(self.EGO_id)
        ego_position = RMPosition.from_other(ego_state)
        diff_before = gvt_position.distance_to_other(ego_position)

        gvt_position.move_forward(d_t * gvt_state.speed, 0)
        ego_position.move_forward(d_t * ego_state.speed, 0)
        diff_after = gvt_position.distance_to_other(ego_position)

        laterally_close_after_lc = diff_after.dt < 1 # hack for "they moved to the same lane"
        changed_order = np.sign(diff_after.ds) != np.sign(diff_before.ds) # previously in front is now behind

        longitudinally_close = []
        for diff in [diff_after, diff_before]:
          min_gvt_interval = diff.ds + gvt_state.centerOffsetX - gvt_state.length / 2
          max_gvt_interval = diff.ds + gvt_state.centerOffsetX + gvt_state.length / 2
          min_ego_interval = ego_state.centerOffsetX - ego_state.length / 2
          max_ego_interval = ego_state.centerOffsetX + ego_state.length / 2
          cond = not (max_gvt_interval < min_ego_interval or max_ego_interval < min_gvt_interval)
          longitudinally_close.append(cond)

        if laterally_close_after_lc and (changed_order or any(longitudinally_close)):
          return SinkState.LaneInvasion
    return False

def get_sul(cache = None):
  # create new internal sul
  internal_sul = SingleTargetFullControl(path_to_scenario, simulation_time_step)

  # define SUL
  extended_action_dict = {action : [RelativeAction(action.accel, 0)] * repeats for action in acceleration_actions}
  extended_action_dict[None] = [None]

  lane_change_actions = LaneChangeAbstraction(target_name, simulation_time_step, 3, None)
  extended_action_dict = CompositeMapping([extended_action_dict, lane_change_actions])

  def cache_wrapper(sul):
    ss_sul = SinkStateOnDomainViolationSUL(sul, 0, 1)
    return CachedSinkStateSUL(ss_sul, cache, list(SinkState))
  ssbs_sul = SmallStepBigStepSUL(internal_sul, extended_action_dict, output_abstraction, kpis, None, cache_wrapper)
  return ssbs_sul