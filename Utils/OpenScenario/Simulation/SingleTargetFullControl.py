import math
from collections.abc import Mapping
from dataclasses import dataclass
from enum import Enum, auto
from logging import warning
from typing import Callable

import numpy as np

import lib.esminiLib as esmini
from Utils.OpenScenario.Simulation.SimulationSUL import SimulationSUL

from Utils.OpenScenario.SimulationUtils import get_object_state, RMPosition, LookAheadMode


@dataclass
class RelativeAction:
  acceleration : float
  lateral_speed : float

@dataclass
class AbsoluteAction:
  x : float
  y : float

class OverrideMode(Enum):
  Always = auto()
  OnFirstDeviation = auto()
  Never = auto()

class SingleTargetFullControl(SimulationSUL) :
  def __init__(self, osc_filename, time_step : float = 0, visualize = False, target_id=1, ego_id=0, vmin=0, vmax=140, override_mode : OverrideMode = OverrideMode.OnFirstDeviation):
    self.target_id = target_id
    self.ego_id = ego_id

    super().__init__(osc_filename, time_step, visualize)

    # TODO option for taking parameters from vehicle specification
    self.velocity_max = vmax / 3.6
    self.velocity_min = vmin / 3.6

    self.override_mode = override_mode

    self.override_active = None

  def reset(self):
    super().reset()
    self.override_active = self.override_mode == OverrideMode.Always

  def relative_step(self, action: RelativeAction):
    # TODO: currently this treats self.velocity as longitudinal velocity. Should probably be total.
    info = get_object_state(self.target_id)

    velocity = info.speed

    lane_offset = info.laneOffset + self.time_step * action.lateral_speed
    # esmini.SE_ReportObjectLateralLanePosition(self.target_id, target_info.laneId, lane_offset)

    delta_vel = action.acceleration * self.time_step
    velocity += delta_vel
    velocity = max(self.velocity_min, min(velocity, self.velocity_max))
    distance = (velocity + delta_vel / 2) * self.time_step

    position = RMPosition()
    position.set_lane_position(info.roadId, info.laneId, lane_offset, info.s, False)
    lane_info = position.get_lane_info(distance, LookAheadMode.LOOKAHEADMODE_AT_CURRENT_LATERAL_OFFSET, True)

    heading = lane_info.heading + math.atan2(action.lateral_speed, velocity - delta_vel / 2)

    esmini.SE_ReportObjectSpeed(self.target_id, velocity)
    esmini.SE_ReportObjectPosXYH(self.target_id, 0, lane_info.pos.x, lane_info.pos.y, heading)

  def absolute_step(self, action : AbsoluteAction):
    old_pos = get_object_state(self.target_id)

    diff_x = action.x - old_pos.x
    diff_y = action.y - old_pos.y
    heading = math.atan2(diff_y, diff_x)

    # calculate distance in road/lane coordinates (?) to get the longitudinal distance.
    new_pos = RMPosition().set_global_position_XYH(action.x, action.y, heading)
    distance = RMPosition.from_other(old_pos).distance_to_other(new_pos).ds

    # calculate distance in world coordinates. not compatible with (current) longitudinal view. shortest path neglecting trajectory.
    # distance = math.sqrt(diff_x**2 + diff_y**2)

    esmini.SE_ReportObjectSpeed(self.target_id, distance / self.time_step)
    esmini.SE_ReportObjectPosXYH(self.target_id, 0, action.x, action.y, heading)

  def step(self, action : RelativeAction | AbsoluteAction = None):
    if esmini.SE_GetQuitFlag():
      return None

    self.override_active |= action is not None and self.override_mode == OverrideMode.OnFirstDeviation
    if action is None and self.override_active:
      action = RelativeAction(0,0)

    if isinstance(action, RelativeAction):
      self.relative_step(action)
    elif isinstance(action, AbsoluteAction):
      self.absolute_step(action)
    elif action is not None:
      raise ValueError("Invalid action")

    self.sim_step()
    return self.get_object_dict()

class LaneChangeAction(Enum):
  Left = "Left"
  Right = "Right"

  def __str__(self):
    return self.value

class LaneChangeAbstraction(Mapping):
  warned_lane_hack = False

  def __len__(self):
    return len(LaneChangeAction)

  def __iter__(self):
    yield from LaneChangeAction

  def __contains__(self, item):
    return isinstance(item, LaneChangeAction)

  def __init__(self, vehicle_id_or_name : int | str, time_step : float, duration : float = 3, dynamics : Callable[[float], float] = None):
    self.vehicle_id = vehicle_id_or_name
    self.duration = duration
    self.lane_change_dynamics = dynamics or self.default_dynamics
    self.time_step = time_step

  @staticmethod
  def default_dynamics(normalized_time):
    return (math.sin((normalized_time * math.pi) - math.pi/2) + 1) * 0.5

  def __getitem__(self, item):
    if not isinstance(item, LaneChangeAction):
      raise KeyError(f"key {item} not in {LaneChangeAction}")
    return self.get_(item) # indirection to avoid KeyErrors in wrong places. necessary since get_ is a generator

  def get_(self, item):
    if isinstance(self.vehicle_id, str):
      self.vehicle_id = esmini.SE_GetIdByName(self.vehicle_id)

    vehicle_info = get_object_state(self.vehicle_id)
    original_road = vehicle_info.roadId
    original_lane = vehicle_info.laneId
    velocity_sign = int(np.sign(original_lane) * (-1 if item == LaneChangeAction.Left else 1))
    target_lane = original_lane + velocity_sign

    position = RMPosition(True)
    position.set_lane_position(original_road, target_lane, 0, vehicle_info.s, True)
    position_data = position.get_data()

    if np.sign(original_lane) != np.sign(target_lane) or not position.is_road(target_lane):
      if not self.__class__.warned_lane_hack:
        self.__class__.warned_lane_hack = True
        warning("Lane changes are restricted same direction.")
      return
      #raise NotImplementedError("Lane changes across the middle lane are not supported")

    diff_x = position_data.x - vehicle_info.x
    diff_y = position_data.y - vehicle_info.y
    target_lane_initial_offset = -velocity_sign * math.sqrt(diff_x**2 + diff_y**2)

    # calculate position in terms of the target lane, thereby setting a reference line wrt the longitudinal behavior.
    position.set_lane_position(original_road, target_lane, target_lane_initial_offset, vehicle_info.s, True)
    current_time = 0

    while current_time < self.duration:
      vehicle_info = get_object_state(self.vehicle_id)
      current_time += self.time_step # This used to be dynamic. However, there is no proper way of getting the current step in simulated time

      # advance longitudinally along the reference line
      # detail: setting LookAheadMode to road center creates larger deviation from the theoretically correct position.
      # however, it is also (implicitly) used in difference calculations
      lane_info = position.get_lane_info(self.time_step * vehicle_info.speed, LookAheadMode.LOOKAHEADMODE_AT_ROAD_CENTER, True)
      lane_info.laneId = position.get_data().laneId
      # set the lane offset according to the specified dynamics
      lane_info.laneOffset = target_lane_initial_offset * (1-self.lane_change_dynamics(current_time / self.duration))
      position.set_lane_position(lane_info.roadId, lane_info.laneId, lane_info.laneOffset, lane_info.s, True)
      new_position = position.get_data()

      yield AbsoluteAction(new_position.x, new_position.y)
