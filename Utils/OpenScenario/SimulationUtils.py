from __future__ import annotations

import ctypes
from enum import Flag, Enum
from typing import Iterable, Callable, Any

from lib.esminiLib import (
  SE_ScenarioObjectState,
  SE_GetDistanceToObject, SE_PositionDiff,
  SE_GetObjectState, SE_GetId, SE_GetObjectName, SE_GetNumberOfObjects,
  SE_GetIdByName,
)

import lib.esminiRMLib as RM

ObjectState = SE_ScenarioObjectState

SimulationDataPoint = dict[str, ObjectState]
ObjectBehavior = Iterable[ObjectState]
Local_KPI_Function = Callable[[SimulationDataPoint], Any]
Reduce_KPI_Function = Callable[[Iterable], Any]
StopCondition = Callable[[SimulationDataPoint], bool]

ObjectStateOrId = ObjectState | int

class LaneType(Flag):
  LANE_TYPE_NONE = (1 << 0)
  LANE_TYPE_DRIVING = (1 << 1)
  LANE_TYPE_STOP = (1 << 2)
  LANE_TYPE_SHOULDER = (1 << 3)
  LANE_TYPE_BIKING = (1 << 4)
  LANE_TYPE_SIDEWALK = (1 << 5)
  LANE_TYPE_BORDER = (1 << 6)
  LANE_TYPE_RESTRICTED = (1 << 7)
  LANE_TYPE_PARKING = (1 << 8)
  LANE_TYPE_BIDIRECTIONAL = (1 << 9)
  LANE_TYPE_MEDIAN = (1 << 10)
  LANE_TYPE_SPECIAL1 = (1 << 11)
  LANE_TYPE_SPECIAL2 = (1 << 12)
  LANE_TYPE_SPECIAL3 = (1 << 13)
  LANE_TYPE_ROADMARKS = (1 << 14)
  LANE_TYPE_TRAM = (1 << 15)
  LANE_TYPE_RAIL = (1 << 16)
  LANE_TYPE_ENTRY = (1 << 17)
  LANE_TYPE_EXIT = (1 << 18)
  LANE_TYPE_OFF_RAMP = (1 << 19)
  LANE_TYPE_ON_RAMP = (1 << 20)
  LANE_TYPE_CURB = (1 << 21)
  LANE_TYPE_CONNECTING_RAMP = (1 << 22)

  LANE_TYPE_REFERENCE_LINE = (1 << 0)
  LANE_TYPE_ANY_DRIVING = LANE_TYPE_DRIVING | LANE_TYPE_ENTRY | LANE_TYPE_EXIT | LANE_TYPE_OFF_RAMP | LANE_TYPE_ON_RAMP
  LANE_TYPE_ANY_ROAD = LANE_TYPE_ANY_DRIVING | LANE_TYPE_RESTRICTED | LANE_TYPE_STOP
  LANE_TYPE_ANY = (0xFFFFFFFF)

class LookAheadMode(Enum):
  LOOKAHEADMODE_AT_LANE_CENTER = 0
  LOOKAHEADMODE_AT_ROAD_CENTER = 1
  LOOKAHEADMODE_AT_CURRENT_LATERAL_OFFSET = 2

class ReturnCode(Enum):
  ERROR_OFF_ROAD = -5
  ERROR_NOT_ON_ROUTE = -4
  ERROR_END_OF_ROUTE = -3
  ERROR_END_OF_ROAD = -2
  ERROR_GENERIC = -1
  OK = 0
  ENTERED_NEW_ROAD = 1
  MADE_JUNCTION_CHOICE = 2

def is_initialized() -> bool:
  # TODO this is a hack
  return SE_GetNumberOfObjects() != -1

def get_object_state(obj_or_id : ObjectStateOrId) -> ObjectState:
  if isinstance(obj_or_id, ObjectState):
    return obj_or_id
  target_info = ObjectState()
  match SE_GetObjectState(obj_or_id, ctypes.byref(target_info)):
    case 0: return target_info
    case 1: raise RuntimeError("Failed to obtain object state")

def get_object_diff(obj_id_1 : int, obj_id_2 : int, free_space : bool) -> SE_PositionDiff:
  info = SE_PositionDiff()
  match SE_GetDistanceToObject(obj_id_1, obj_id_2, free_space, ctypes.byref(info)):
    case 0: return info
    case -2: return None
    case -1: raise RuntimeError("Failed to obtain distance between objects")
    case _: raise RuntimeError("Unexpected return value")

def get_vehicle_idx_by_name(name):
  ret = SE_GetIdByName(name)
  if ret == -1:
    raise ValueError(f"couldn't find vehicle {name}")

def get_vehicle_name_by_idx(idx):
  if idx < SE_GetNumberOfObjects():
    return ctypes.string_at(SE_GetObjectName(SE_GetId(idx))).decode("ascii")
  else:
    raise ValueError(f"vehicle index {idx} out of bounds")

class RMPosition:
  def __init__(self, lock_to_lane = False):
    self.handle = RM.RM_CreatePosition()
    if self.handle == -1:
      self.handle = None
      raise RuntimeError("Could not create RM position. Maybe you forgot to initialize RM.")
    self.lock_to_lane(lock_to_lane)

  def lock_to_lane(self, lock):
    if 0 != RM.RM_SetLockOnLane(self.handle, lock):
      raise RuntimeError("Error locking RM position on lane")

  def __del__(self):
    if self.handle is None:
      return
    if 0 != RM.RM_DeletePosition(self.handle):
      pass #raise RuntimeError("Error deleting position")

  @staticmethod
  def from_other(other : ObjectState | RMPosition | RM.RM_PositionData) -> RMPosition:
    ret = RMPosition()
    if isinstance(other, RMPosition):
      other = other.get_data()
    return ret.set_global_position_from_other(other)

  @staticmethod
  def handle_return_code(ret):
    ret = ReturnCode(ret)
    if ret.value < 0:
      raise RuntimeError(f"Error setting position: {ret.name}")

  def set_lane_position(self, roadId, laneId, lane_offset, s, align=True):
    self.handle_return_code(RM.RM_SetLanePosition(self.handle, roadId, laneId, lane_offset, s, align))
    return self

  def set_lane_position_from_other(self, other, align=True):
    return self.set_lane_position(other.roadId, other.laneId, other.laneOffset, other.s, align)

  def set_global_position(self, x, y, z, h, p, r):
    self.handle_return_code(RM.RM_SetWorldPosition(self.handle, x, y, z, h, p, r))
    return self

  def set_global_position_from_other(self, other):
    return self.set_global_position(other.x, other.y, other.z, other.h, other.p, other.r)

  def set_global_position_XYH(self, x, y, h):
    self.handle_return_code(RM.RM_SetWorldXYHPosition(self.handle, x, y, h))
    return self

  def set_global_position_XYH_from_other(self, other):
    return self.set_global_position_XYH(other.x, other.y, other.h)

  def get_data(self) -> RM.RM_PositionData:
    data = RM.RM_PositionData()
    if 0 != RM.RM_GetPositionData(self.handle, ctypes.byref(data)):
      raise RuntimeError("Failed to get position data")
    return data

  def get_lane_info(self, lookahead_distance, look_ahead_mode : LookAheadMode, in_driving_direction) -> RM.RM_RoadLaneInfo:
    data = RM.RM_RoadLaneInfo()
    if 0 != RM.RM_GetLaneInfo(self.handle, lookahead_distance, ctypes.byref(data), look_ahead_mode.value, in_driving_direction) :
      raise RuntimeError("Failed to get lane info")
    return data

  def move_forward(self, distance, junction_selector_angle):
    self.handle_return_code(RM.RM_PositionMoveForward(self.handle, distance, junction_selector_angle))

  def distance_to_other(self, other : RMPosition) -> RM.RM_PositionDiff:
    if not isinstance(other, RMPosition):
      raise ValueError("expected other RMPosition")

    info = RM.RM_PositionDiff()
    match RM.RM_SubtractAFromB(self.handle, other.handle, ctypes.byref(info)):
      case  0: return info
      case -2: return None
      case -1: raise RuntimeError("Failed to obtain distance between objects")
      case  _: raise RuntimeError("Unexpected return value")

  def get_lane_type(self, lane_id) -> LaneType:
    ret = RM.RM_GetLaneType(self.handle, lane_id)
    if ret == 0:
      raise RuntimeError("Failed to get lane type. Lane does probably not exist.")
    return LaneType(ret)

  def is_road(self, lane_id) -> bool:
    return bool(self.get_lane_type(lane_id) & LaneType.LANE_TYPE_ANY_ROAD)