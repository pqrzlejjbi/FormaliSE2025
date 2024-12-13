import math
from abc import abstractmethod
from typing import Any, Callable

import numpy as np

from Utils.Decorators import wrap_hinted_types
from Utils.NumpyUtils import Box

from Utils.OpenScenario.SimulationUtils import get_object_state, get_object_diff, ObjectStateOrId, SimulationDataPoint, RMPosition

import lib.esminiLib as esmini

KPIFun = Callable[[ObjectStateOrId, ...], Any]
SingleVehicleKPI = Callable[[ObjectStateOrId], Any]
TwoVehicleKPI = Callable[[ObjectStateOrId, ObjectStateOrId], Any]

wrap_ObjectId = wrap_hinted_types({ObjectStateOrId : get_object_state})

@wrap_ObjectId
def get_bounding_box(obj : ObjectStateOrId) :
  return Box([obj.length, obj.width], [obj.x, obj.y], obj.h)

@wrap_ObjectId
def get_center_distance(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId) :
  return math.sqrt((obj2.x - obj1.x) ** 2 + (obj2.y - obj1.y) ** 2)

@wrap_ObjectId
def get_distance_RM(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId):
  return RMPosition.from_other(obj1).distance_to_other(RMPosition.from_other(obj2))

def get_distance(obj1_id : int, obj2_id : int, free_space : bool):
  return get_object_diff(obj1_id, obj2_id, free_space)

@wrap_ObjectId
def get_bounding_box_distance(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId) :
  obj1, obj2 = (get_bounding_box(obj) for obj in (obj1,obj2))
  return obj1.distance_to_other(obj2)

@wrap_ObjectId
def get_longitudinal_offset_in_lane(obj : ObjectStateOrId):
  raise NotImplementedError()

@wrap_ObjectId
def get_same_lane_distance(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId, right_hand_driving=True, account_for_length=True):
  assert obj1.roadId == obj2.roadId
  if obj1.laneId != obj2.laneId :
    return np.inf
  # lanes with negative id are on the right of the directed reference curve
  handedness_factor = -1 if right_hand_driving else 1
  direction_factor = handedness_factor * np.sign(obj1.laneId)
  bbox_center_1, bbox_center_2 = (obj.s + direction_factor * obj.centerOffsetX for obj in (obj1, obj2))
  distance = (bbox_center_2 - bbox_center_1) * direction_factor
  if account_for_length:
    distance -= np.sign(distance) * (obj1.length + obj2.length) / 2
  return distance

@wrap_ObjectId
def get_same_lane_time_gap(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId) :
  distance = get_same_lane_distance(obj1, obj2)
  if obj1.speed == 0:
    return np.inf
  return distance / obj1.speed

@wrap_ObjectId
def get_same_lane_TTC(obj1 : ObjectStateOrId, obj2 : ObjectStateOrId):
  distance = get_same_lane_distance(obj1, obj2)
  # TODO some form of lateral speed to avoid jumps on lane changes?
  if distance == np.inf:
    return np.inf
  speed_diff = obj1.speed - obj2.speed
  if np.sign(speed_diff) != np.sign(distance):
    return np.inf
  return distance / speed_diff

def ego_deceleration(time_step) -> SingleVehicleKPI:
  raise NotImplementedError()
  prev = None # TODO this is evil

  @wrap_ObjectId
  def fun(ego: ObjectStateOrId):
    nonlocal prev
    if prev is None:
      prev = ego.speed
    a = (ego.speed - prev) / time_step
    prev = ego.speed
    return a

  return fun

def crash(limit_acc, limit_vel, time_step) -> SingleVehicleKPI:
  decel = ego_deceleration(time_step)

  @wrap_ObjectId
  def fun(ego: ObjectStateOrId):
    return decel(ego) < limit_acc and ego.speed < limit_vel

  return fun

def emergency_braking_gap(a_min=-10) -> TwoVehicleKPI:
  if 0 <= a_min:
    raise ValueError("a_min has to be negative")

  @wrap_ObjectId
  def fun(ego: ObjectStateOrId, target: ObjectStateOrId):
    d0 = get_same_lane_distance(ego, target)
    delta_v0 = ego.speed - target.speed
    if d0 < 0 or delta_v0 < 0:
      return np.inf
    return (ego.speed/-a_min * (target.speed - ego.speed/2) + d0) / delta_v0
  return fun

class StatefulKPI:
  def __init__(self, name = None, unit = None):
    self.name = name
    self.unit = unit
    self.data = []
    self.time_stamps = []

  def reset(self):
    self.data = []
    self.time_stamps = []

  def __call__(self, data : SimulationDataPoint, time_stamp = None):
    if data is None:
      return None

    if time_stamp is None:
      time_stamp = esmini.SE_GetSimulationTime()
    self.time_stamps.append(time_stamp)

    ret = self.compute(data)
    self.data.append(ret)
    return ret

  @abstractmethod
  def compute(self, data : SimulationDataPoint):
    pass

class GenericStatefulKPI(StatefulKPI):
  def __init__(self, fun: KPIFun, argument_object_names: list[str], name=None, unit=None):
    super().__init__(name, unit)
    self.fun = fun
    self.arg_names = argument_object_names

  def compute(self, data : SimulationDataPoint):
    return self.fun(*(data[name] for name in self.arg_names))

class AccelerationKPI(StatefulKPI):
  def __init__(self, object_name, name=None):
    super().__init__(name or "acceleration", "m/s²")
    self.object_name = object_name

    self.prev_vel = None

  def reset(self):
    super().reset()
    self.prev_vel = None

  def compute(self, data : SimulationDataPoint):
    pts = 0 if len(self.time_stamps) < 2 else self.time_stamps[-2]
    time_step = self.time_stamps[-1] - pts

    if time_step == 0:
      return self.data[-1]

    obj = data[self.object_name]
    if self.prev_vel is None:
      self.prev_vel = obj.speed
    ret = (obj.speed - self.prev_vel) / time_step
    self.prev_vel = obj.speed
    return ret
