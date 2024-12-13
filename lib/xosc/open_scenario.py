from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


@dataclass
class AbsoluteTargetLane:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class AbsoluteTargetLaneOffset:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AbsoluteTargetSpeed:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ActivateControllerAction:
    controller_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "controllerRef",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    lateral: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    longitudinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    animation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    lighting: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AnimationState:
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class AutomaticGearTypeValue(Enum):
    N = "n"
    P = "p"
    R = "r"
    D = "d"


@dataclass
class Axle:
    max_steering: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxSteering",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    position_x: Optional[str] = field(
        default=None,
        metadata={
            "name": "positionX",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    position_z: Optional[str] = field(
        default=None,
        metadata={
            "name": "positionZ",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    track_width: Optional[str] = field(
        default=None,
        metadata={
            "name": "trackWidth",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    wheel_diameter: Optional[str] = field(
        default=None,
        metadata={
            "name": "wheelDiameter",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Brake:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Center:
    x: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    y: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    z: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class CentralSwarmObject:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Clothoid:
    position: Optional["Position"] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    curvature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    curvature_dot: Optional[str] = field(
        default=None,
        metadata={
            "name": "curvatureDot",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    length: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    stop_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "stopTime",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    curvature_prime: Optional[str] = field(
        default=None,
        metadata={
            "name": "curvaturePrime",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class CloudStateValue(Enum):
    CLOUDY = "cloudy"
    FREE = "free"
    OVERCAST = "overcast"
    RAINY = "rainy"
    SKY_OFF = "skyOff"


@dataclass
class ColorCmyk:
    cyan: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    magenta: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    yellow: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ColorRgb:
    red: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    green: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    blue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class ColorTypeValue(Enum):
    OTHER = "other"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    VIOLET = "violet"
    ORANGE = "orange"
    BROWN = "brown"
    BLACK = "black"
    GREY = "grey"
    WHITE = "white"


class ConditionEdgeValue(Enum):
    FALLING = "falling"
    NONE = "none"
    RISING = "rising"
    RISING_OR_FALLING = "risingOrFalling"


@dataclass
class ControlPoint:
    position: Optional["Position"] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class ControllerTypeValue(Enum):
    LATERAL = "lateral"
    LONGITUDINAL = "longitudinal"
    LIGHTING = "lighting"
    ANIMATION = "animation"
    MOVEMENT = "movement"
    APPEARANCE = "appearance"
    ALL = "all"


class CoordinateSystemValue(Enum):
    ENTITY = "entity"
    LANE = "lane"
    ROAD = "road"
    TRAJECTORY = "trajectory"


@dataclass
class CustomCommandAction:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class DeleteEntityAction:
    pass


@dataclass
class Dimensions:
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    length: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class DirectionOfTravelDistribution:
    same: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    opposite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class DirectionalDimensionValue(Enum):
    LONGITUDINAL = "longitudinal"
    LATERAL = "lateral"
    VERTICAL = "vertical"


@dataclass
class Directory:
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class DistributionSetElement:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class DynamicConstraints:
    max_acceleration: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxAcceleration",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_acceleration_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxAccelerationRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_deceleration: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxDeceleration",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_deceleration_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxDecelerationRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_speed: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxSpeed",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class DynamicsDimensionValue(Enum):
    DISTANCE = "distance"
    RATE = "rate"
    TIME = "time"


class DynamicsShapeValue(Enum):
    CUBIC = "cubic"
    LINEAR = "linear"
    SINUSOIDAL = "sinusoidal"
    STEP = "step"


@dataclass
class EndOfRoadCondition:
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class EntityRef:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ExternalObjectReference:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class File:
    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


class FollowingModeValue(Enum):
    FOLLOW = "follow"
    POSITION = "position"


class FractionalCloudCoverValue(Enum):
    ZERO_OKTAS = "zeroOktas"
    ONE_OKTAS = "oneOktas"
    TWO_OKTAS = "twoOktas"
    THREE_OKTAS = "threeOktas"
    FOUR_OKTAS = "fourOktas"
    FIVE_OKTAS = "fiveOktas"
    SIX_OKTAS = "sixOktas"
    SEVEN_OKTAS = "sevenOktas"
    EIGHT_OKTAS = "eightOktas"
    NINE_OKTAS = "nineOktas"


@dataclass
class Knot:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class LateralDisplacementValue(Enum):
    ANY = "any"
    LEFT_TO_REFERENCED_ENTITY = "leftToReferencedEntity"
    RIGHT_TO_REFERENCED_ENTITY = "rightToReferencedEntity"


@dataclass
class License:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    spdx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "spdxId",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


class LightModeValue(Enum):
    ON = "on"
    OFF = "off"
    FLASHING = "flashing"


class LongitudinalDisplacementValue(Enum):
    ANY = "any"
    TRAILING_REFERENCED_ENTITY = "trailingReferencedEntity"
    LEADING_REFERENCED_ENTITY = "leadingReferencedEntity"


@dataclass
class ManualGear:
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class MiscObjectCategoryValue(Enum):
    BARRIER = "barrier"
    BUILDING = "building"
    CROSSWALK = "crosswalk"
    GANTRY = "gantry"
    NONE = "none"
    OBSTACLE = "obstacle"
    PARKING_SPACE = "parkingSpace"
    PATCH = "patch"
    POLE = "pole"
    RAILING = "railing"
    ROAD_MARK = "roadMark"
    SOUND_BARRIER = "soundBarrier"
    STREET_LAMP = "streetLamp"
    TRAFFIC_ISLAND = "trafficIsland"
    TREE = "tree"
    VEGETATION = "vegetation"
    WIND = "wind"


@dataclass
class NoneType:
    class Meta:
        name = "None"


class ObjectTypeValue(Enum):
    MISCELLANEOUS = "miscellaneous"
    PEDESTRIAN = "pedestrian"
    VEHICLE = "vehicle"
    EXTERNAL = "external"


@dataclass
class OffroadCondition:
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class OverrideClutchAction:
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class OverrideSteeringWheelAction:
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_torque: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxTorque",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class OverrideThrottleAction:
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ParameterAddValueRule:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ParameterAssignment:
    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ParameterMultiplyByValueRule:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ParameterSetAction:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


class ParameterTypeValue(Enum):
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    DOUBLE = "double"
    INTEGER = "integer"
    STRING = "string"
    UNSIGNED_INT = "unsignedInt"
    UNSIGNED_SHORT = "unsignedShort"
    INT = "int"


class PedestrianCategoryValue(Enum):
    ANIMAL = "animal"
    PEDESTRIAN = "pedestrian"
    WHEELCHAIR = "wheelchair"


class PedestrianGestureTypeValue(Enum):
    PHONE_CALL_RIGHT_HAND = "phoneCallRightHand"
    PHONE_CALL_LEFT_HAND = "phoneCallLeftHand"
    PHONE_TEXT_RIGHT_HAND = "phoneTextRightHand"
    PHONE_TEXT_LEFT_HAND = "phoneTextLeftHand"
    WAVING_RIGHT_ARM = "wavingRightArm"
    WAVING_LEFT_ARM = "wavingLeftArm"
    UMBRELLA_RIGHT_HAND = "umbrellaRightHand"
    UMBRELLA_LEFT_HAND = "umbrellaLeftHand"
    CROSS_ARMS = "crossArms"
    COFFEE_RIGHT_HAND = "coffeeRightHand"
    COFFEE_LEFT_HAND = "coffeeLeftHand"
    SANDWICH_RIGHT_HAND = "sandwichRightHand"
    SANDWICH_LEFT_HAND = "sandwichLeftHand"


class PedestrianMotionTypeValue(Enum):
    STANDING = "standing"
    SITTING = "sitting"
    LYING = "lying"
    SQUATTING = "squatting"
    WALKING = "walking"
    RUNNING = "running"
    REELING = "reeling"
    CRAWLING = "crawling"
    CYCLING = "cycling"
    JUMPING = "jumping"
    DUCKING = "ducking"
    BENDING_DOWN = "bendingDown"


@dataclass
class Performance:
    max_acceleration: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxAcceleration",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_acceleration_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxAccelerationRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_deceleration: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxDeceleration",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_deceleration_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxDecelerationRate",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    max_speed: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxSpeed",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class PositionInLaneCoordinates:
    lane_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "laneId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    lane_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "laneOffset",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    path_s: Optional[str] = field(
        default=None,
        metadata={
            "name": "pathS",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class PositionInRoadCoordinates:
    path_s: Optional[str] = field(
        default=None,
        metadata={
            "name": "pathS",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class PositionOfCurrentEntity:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


class PrecipitationTypeValue(Enum):
    DRY = "dry"
    RAIN = "rain"
    SNOW = "snow"


class PriorityValue(Enum):
    OVERWRITE = "overwrite"
    OVERRIDE = "override"
    PARALLEL = "parallel"
    SKIP = "skip"


@dataclass
class ProbabilityDistributionSetElement:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Property:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Range:
    lower_limit: Optional[str] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    upper_limit: Optional[str] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class ReferenceContextValue(Enum):
    ABSOLUTE = "absolute"
    RELATIVE = "relative"


class RelativeDistanceTypeValue(Enum):
    LATERAL = "lateral"
    LONGITUDINAL = "longitudinal"
    CARTESIAN_DISTANCE = "cartesianDistance"
    EUCLIDIAN_DISTANCE = "euclidianDistance"


@dataclass
class RelativeLaneRange:
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeTargetLane:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeTargetLaneOffset:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class RoleValue(Enum):
    NONE = "none"
    AMBULANCE = "ambulance"
    CIVIL = "civil"
    FIRE = "fire"
    MILITARY = "military"
    POLICE = "police"
    PUBLIC_TRANSPORT = "publicTransport"
    ROAD_ASSISTANCE = "roadAssistance"


class RouteStrategyValue(Enum):
    FASTEST = "fastest"
    LEAST_INTERSECTIONS = "leastIntersections"
    RANDOM = "random"
    SHORTEST = "shortest"


class RoutingAlgorithmValue(Enum):
    ASSIGNED_ROUTE = "assignedRoute"
    FASTEST = "fastest"
    LEAST_INTERSECTIONS = "leastIntersections"
    SHORTEST = "shortest"
    UNDEFINED = "undefined"


class RuleValue(Enum):
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    LESS_THAN = "lessThan"
    GREATER_OR_EQUAL = "greaterOrEqual"
    LESS_OR_EQUAL = "lessOrEqual"
    NOT_EQUAL_TO = "notEqualTo"


@dataclass
class SensorReference:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class SpeedProfileEntry:
    speed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class SpeedTargetValueTypeValue(Enum):
    DELTA = "delta"
    FACTOR = "factor"


@dataclass
class StandStillCondition:
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class StoryboardElementStateValue(Enum):
    COMPLETE_STATE = "completeState"
    END_TRANSITION = "endTransition"
    RUNNING_STATE = "runningState"
    SKIP_TRANSITION = "skipTransition"
    STANDBY_STATE = "standbyState"
    START_TRANSITION = "startTransition"
    STOP_TRANSITION = "stopTransition"


class StoryboardElementTypeValue(Enum):
    ACT = "act"
    ACTION = "action"
    EVENT = "event"
    MANEUVER = "maneuver"
    MANEUVER_GROUP = "maneuverGroup"
    STORY = "story"


@dataclass
class Sun:
    azimuth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    elevation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    intensity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    illuminance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TargetDistanceSteadyState:
    distance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TargetTimeSteadyState:
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TimeOfDay:
    animation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalCondition:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalControllerAction:
    traffic_signal_controller_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "trafficSignalControllerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalControllerCondition:
    traffic_signal_controller_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "trafficSignalControllerRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalGroupState:
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalState:
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    traffic_signal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "trafficSignalId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignalStateAction:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficStopAction:
    pass


@dataclass
class TraveledDistanceCondition:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class TriggeringEntitiesRuleValue(Enum):
    ALL = "all"
    ANY = "any"


@dataclass
class UserDefinedAnimation:
    user_defined_animation_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "userDefinedAnimationType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class UserDefinedComponent:
    user_defined_component_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "userDefinedComponentType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class UserDefinedDistribution:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class UserDefinedLight:
    user_defined_light_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "userDefinedLightType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VariableAddValueRule:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class VariableMultiplyByValueRule:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class VariableSetAction:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


class VehicleCategoryValue(Enum):
    BICYCLE = "bicycle"
    BUS = "bus"
    CAR = "car"
    MOTORBIKE = "motorbike"
    SEMITRAILER = "semitrailer"
    TRAILER = "trailer"
    TRAIN = "train"
    TRAM = "tram"
    TRUCK = "truck"
    VAN = "van"


class VehicleComponentTypeValue(Enum):
    HOOD = "hood"
    TRUNK = "trunk"
    DOOR_FRONT_RIGHT = "doorFrontRight"
    DOOR_FRONT_LEFT = "doorFrontLeft"
    DOOR_REAR_RIGHT = "doorRearRight"
    DOOR_REAR_LEFT = "doorRearLeft"
    WINDOW_FRONT_RIGHT = "windowFrontRight"
    WINDOW_FRONT_LEFT = "windowFrontLeft"
    WINDOW_REAR_RIGHT = "windowRearRight"
    WINDOW_REAR_LEFT = "windowRearLeft"
    SIDE_MIRRORS = "sideMirrors"
    SIDE_MIRROR_RIGHT = "sideMirrorRight"
    SIDE_MIRROR_LEFT = "sideMirrorLeft"


class VehicleLightTypeValue(Enum):
    DAYTIME_RUNNING_LIGHTS = "daytimeRunningLights"
    LOW_BEAM = "lowBeam"
    HIGH_BEAM = "highBeam"
    FOG_LIGHTS = "fogLights"
    FOG_LIGHTS_FRONT = "fogLightsFront"
    FOG_LIGHTS_REAR = "fogLightsRear"
    BRAKE_LIGHTS = "brakeLights"
    WARNING_LIGHTS = "warningLights"
    INDICATOR_LEFT = "indicatorLeft"
    INDICATOR_RIGHT = "indicatorRight"
    REVERSING_LIGHTS = "reversingLights"
    LICENSE_PLATE_ILLUMINATION = "licensePlateIllumination"
    SPECIAL_PURPOSE_LIGHTS = "specialPurposeLights"


@dataclass
class Vertex:
    position: Optional["Position"] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


class WetnessValue(Enum):
    DRY = "dry"
    MOIST = "moist"
    WET_WITH_PUDDLES = "wetWithPuddles"
    LOW_FLOODED = "lowFlooded"
    HIGH_FLOODED = "highFlooded"


@dataclass
class Wind:
    direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    speed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class WorldPosition:
    h: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    p: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    x: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    y: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    z: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AbsoluteSpeed:
    target_distance_steady_state: Optional[TargetDistanceSteadyState] = field(
        default=None,
        metadata={
            "name": "TargetDistanceSteadyState",
            "type": "Element",
            "namespace": "",
        }
    )
    target_time_steady_state: Optional[TargetTimeSteadyState] = field(
        default=None,
        metadata={
            "name": "TargetTimeSteadyState",
            "type": "Element",
            "namespace": "",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AccelerationCondition:
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    direction: Optional[Union[str, DirectionalDimensionValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Actors:
    entity_ref: List[EntityRef] = field(
        default_factory=list,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
        }
    )
    select_triggering_entities: Optional[str] = field(
        default=None,
        metadata={
            "name": "selectTriggeringEntities",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AnimationFile:
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeOffset",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AutomaticGear:
    gear: Optional[Union[str, AutomaticGearTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Axles:
    front_axle: Optional[Axle] = field(
        default=None,
        metadata={
            "name": "FrontAxle",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rear_axle: Optional[Axle] = field(
        default=None,
        metadata={
            "name": "RearAxle",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    additional_axle: List[Axle] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAxle",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class BoundingBox:
    center: Optional[Center] = field(
        default=None,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dimensions: Optional[Dimensions] = field(
        default=None,
        metadata={
            "name": "Dimensions",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ByObjectType:
    type_value: Optional[Union[str, ObjectTypeValue]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ByType:
    object_type: Optional[Union[str, ObjectTypeValue]] = field(
        default=None,
        metadata={
            "name": "objectType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Color:
    color_rgb: Optional[ColorRgb] = field(
        default=None,
        metadata={
            "name": "ColorRgb",
            "type": "Element",
            "namespace": "",
        }
    )
    color_cmyk: Optional[ColorCmyk] = field(
        default=None,
        metadata={
            "name": "ColorCmyk",
            "type": "Element",
            "namespace": "",
        }
    )
    color_type: Optional[Union[str, ColorTypeValue]] = field(
        default=None,
        metadata={
            "name": "colorType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ControllerCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DistributionRange:
    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    step_width: Optional[str] = field(
        default=None,
        metadata={
            "name": "stepWidth",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class DistributionSet:
    element: List[DistributionSetElement] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class DomeImage:
    dome_file: Optional[File] = field(
        default=None,
        metadata={
            "name": "DomeFile",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    azimuth_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "azimuthOffset",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class EnvironmentCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class HistogramBin:
    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class InRoutePosition:
    from_current_entity: Optional[PositionOfCurrentEntity] = field(
        default=None,
        metadata={
            "name": "FromCurrentEntity",
            "type": "Element",
            "namespace": "",
        }
    )
    from_road_coordinates: Optional[PositionInRoadCoordinates] = field(
        default=None,
        metadata={
            "name": "FromRoadCoordinates",
            "type": "Element",
            "namespace": "",
        }
    )
    from_lane_coordinates: Optional[PositionInLaneCoordinates] = field(
        default=None,
        metadata={
            "name": "FromLaneCoordinates",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LaneChangeTarget:
    relative_target_lane: Optional[RelativeTargetLane] = field(
        default=None,
        metadata={
            "name": "RelativeTargetLane",
            "type": "Element",
            "namespace": "",
        }
    )
    absolute_target_lane: Optional[AbsoluteTargetLane] = field(
        default=None,
        metadata={
            "name": "AbsoluteTargetLane",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LaneOffsetActionDynamics:
    dynamics_shape: Optional[Union[str, DynamicsShapeValue]] = field(
        default=None,
        metadata={
            "name": "dynamicsShape",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    max_lateral_acc: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxLateralAcc",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class LaneOffsetTarget:
    relative_target_lane_offset: Optional[RelativeTargetLaneOffset] = field(
        default=None,
        metadata={
            "name": "RelativeTargetLaneOffset",
            "type": "Element",
            "namespace": "",
        }
    )
    absolute_target_lane_offset: Optional[AbsoluteTargetLaneOffset] = field(
        default=None,
        metadata={
            "name": "AbsoluteTargetLaneOffset",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LateralDistanceAction:
    dynamic_constraints: Optional[DynamicConstraints] = field(
        default=None,
        metadata={
            "name": "DynamicConstraints",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    continuous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    distance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    displacement: Optional[Union[str, LateralDisplacementValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class LongitudinalDistanceAction:
    dynamic_constraints: Optional[DynamicConstraints] = field(
        default=None,
        metadata={
            "name": "DynamicConstraints",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    continuous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    distance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    time_gap: Optional[str] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    displacement: Optional[Union[str, LongitudinalDisplacementValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ManeuverCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MiscObjectCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ModifyRule:
    add_value: Optional[ParameterAddValueRule] = field(
        default=None,
        metadata={
            "name": "AddValue",
            "type": "Element",
            "namespace": "",
        }
    )
    multiply_by_value: Optional[ParameterMultiplyByValueRule] = field(
        default=None,
        metadata={
            "name": "MultiplyByValue",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NormalDistribution:
    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "",
        }
    )
    expected_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "expectedValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    variance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Nurbs:
    control_point: List[ControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "ControlPoint",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )
    knot: List[Knot] = field(
        default_factory=list,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )
    order: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Orientation:
    h: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    p: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    type_value: Optional[Union[str, ReferenceContextValue]] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class OverrideBrakeAction:
    brake_percent: Optional[Brake] = field(
        default=None,
        metadata={
            "name": "BrakePercent",
            "type": "Element",
            "namespace": "",
        }
    )
    brake_force: Optional[Brake] = field(
        default=None,
        metadata={
            "name": "BrakeForce",
            "type": "Element",
            "namespace": "",
        }
    )
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class OverrideParkingBrakeAction:
    brake_percent: Optional[Brake] = field(
        default=None,
        metadata={
            "name": "BrakePercent",
            "type": "Element",
            "namespace": "",
        }
    )
    brake_force: Optional[Brake] = field(
        default=None,
        metadata={
            "name": "BrakeForce",
            "type": "Element",
            "namespace": "",
        }
    )
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ParameterAssignments:
    parameter_assignment: List[ParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ParameterAssignment",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ParameterCondition:
    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ParameterValueSet:
    parameter_assignment: List[ParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ParameterAssignment",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class PedestrianCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class PedestrianGesture:
    gesture: Optional[Union[str, PedestrianGestureTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Phase:
    traffic_signal_state: List[TrafficSignalState] = field(
        default_factory=list,
        metadata={
            "name": "TrafficSignalState",
            "type": "Element",
            "namespace": "",
        }
    )
    traffice_signal_group_state: Optional[TrafficSignalGroupState] = field(
        default=None,
        metadata={
            "name": "TrafficeSignalGroupState",
            "type": "Element",
            "namespace": "",
        }
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class PoissonDistribution:
    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "",
        }
    )
    expected_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "expectedValue",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Polyline:
    vertex: List[Vertex] = field(
        default_factory=list,
        metadata={
            "name": "Vertex",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )


@dataclass
class Precipitation:
    intensity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    precipitation_type: Optional[Union[str, PrecipitationTypeValue]] = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    precipitation_intensity: Optional[str] = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ProbabilityDistributionSet:
    element: List[ProbabilityDistributionSetElement] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Properties:
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "",
        }
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "",
        }
    )
    custom_content: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CustomContent",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RelativeClearanceCondition:
    relative_lane_range: List[RelativeLaneRange] = field(
        default_factory=list,
        metadata={
            "name": "RelativeLaneRange",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: List[EntityRef] = field(
        default_factory=list,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
        }
    )
    opposite_lanes: Optional[str] = field(
        default=None,
        metadata={
            "name": "oppositeLanes",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    distance_forward: Optional[str] = field(
        default=None,
        metadata={
            "name": "distanceForward",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    distance_backward: Optional[str] = field(
        default=None,
        metadata={
            "name": "distanceBackward",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    free_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "freeSpace",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeDistanceCondition:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    relative_distance_type: Optional[Union[str, RelativeDistanceTypeValue]] = field(
        default=None,
        metadata={
            "name": "relativeDistanceType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    routing_algorithm: Optional[Union[str, RoutingAlgorithmValue]] = field(
        default=None,
        metadata={
            "name": "routingAlgorithm",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class RelativeSpeedCondition:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    direction: Optional[Union[str, DirectionalDimensionValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class RelativeSpeedToMaster:
    target_distance_steady_state: Optional[TargetDistanceSteadyState] = field(
        default=None,
        metadata={
            "name": "TargetDistanceSteadyState",
            "type": "Element",
            "namespace": "",
        }
    )
    target_time_steady_state: Optional[TargetTimeSteadyState] = field(
        default=None,
        metadata={
            "name": "TargetTimeSteadyState",
            "type": "Element",
            "namespace": "",
        }
    )
    speed_target_value_type: Optional[Union[str, SpeedTargetValueTypeValue]] = field(
        default=None,
        metadata={
            "name": "speedTargetValueType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeTargetSpeed:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    continuous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    speed_target_value_type: Optional[Union[str, SpeedTargetValueTypeValue]] = field(
        default=None,
        metadata={
            "name": "speedTargetValueType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RouteCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SensorReferenceSet:
    sensor_reference: List[SensorReference] = field(
        default_factory=list,
        metadata={
            "name": "SensorReference",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SimulationTimeCondition:
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class SpeedCondition:
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    direction: Optional[Union[str, DirectionalDimensionValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class SpeedProfileAction:
    dynamic_constraints: Optional[DynamicConstraints] = field(
        default=None,
        metadata={
            "name": "DynamicConstraints",
            "type": "Element",
            "namespace": "",
        }
    )
    speed_profile_entry: List[SpeedProfileEntry] = field(
        default_factory=list,
        metadata={
            "name": "SpeedProfileEntry",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    following_mode: Optional[Union[str, FollowingModeValue]] = field(
        default=None,
        metadata={
            "name": "followingMode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class StoryboardElementStateCondition:
    storyboard_element_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "storyboardElementRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    state: Optional[Union[str, StoryboardElementStateValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    storyboard_element_type: Optional[Union[str, StoryboardElementTypeValue]] = field(
        default=None,
        metadata={
            "name": "storyboardElementType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TimeHeadwayCondition:
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    along_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "alongRoute",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    relative_distance_type: Optional[Union[str, RelativeDistanceTypeValue]] = field(
        default=None,
        metadata={
            "name": "relativeDistanceType",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    routing_algorithm: Optional[Union[str, RoutingAlgorithmValue]] = field(
        default=None,
        metadata={
            "name": "routingAlgorithm",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TimeOfDayCondition:
    date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Timing:
    domain_absolute_relative: Optional[Union[str, ReferenceContextValue]] = field(
        default=None,
        metadata={
            "name": "domainAbsoluteRelative",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    scale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TrafficSignalAction:
    traffic_signal_controller_action: Optional[TrafficSignalControllerAction] = field(
        default=None,
        metadata={
            "name": "TrafficSignalControllerAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_signal_state_action: Optional[TrafficSignalStateAction] = field(
        default=None,
        metadata={
            "name": "TrafficSignalStateAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TrajectoryCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TrajectoryFollowingMode:
    following_mode: Optional[Union[str, FollowingModeValue]] = field(
        default=None,
        metadata={
            "name": "followingMode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TransitionDynamics:
    dynamics_dimension: Optional[Union[str, DynamicsDimensionValue]] = field(
        default=None,
        metadata={
            "name": "dynamicsDimension",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    dynamics_shape: Optional[Union[str, DynamicsShapeValue]] = field(
        default=None,
        metadata={
            "name": "dynamicsShape",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    following_mode: Optional[Union[str, FollowingModeValue]] = field(
        default=None,
        metadata={
            "name": "followingMode",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TriggeringEntities:
    entity_ref: List[EntityRef] = field(
        default_factory=list,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    triggering_entities_rule: Optional[Union[str, TriggeringEntitiesRuleValue]] = field(
        default=None,
        metadata={
            "name": "triggeringEntitiesRule",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class UniformDistribution:
    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class UserDefinedAction:
    custom_command_action: Optional[CustomCommandAction] = field(
        default=None,
        metadata={
            "name": "CustomCommandAction",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class UserDefinedValueCondition:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ValueConstraint:
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VariableCondition:
    variable_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VariableDeclaration:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    variable_type: Optional[Union[str, ParameterTypeValue]] = field(
        default=None,
        metadata={
            "name": "variableType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VariableModifyRule:
    add_value: Optional[VariableAddValueRule] = field(
        default=None,
        metadata={
            "name": "AddValue",
            "type": "Element",
            "namespace": "",
        }
    )
    multiply_by_value: Optional[VariableMultiplyByValueRule] = field(
        default=None,
        metadata={
            "name": "MultiplyByValue",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class VehicleCatalogLocation:
    directory: Optional[Directory] = field(
        default=None,
        metadata={
            "name": "Directory",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class VehicleCategoryDistributionEntry:
    category: Optional[Union[str, VehicleCategoryValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class VehicleComponent:
    vehicle_component_type: Optional[Union[str, VehicleComponentTypeValue]] = field(
        default=None,
        metadata={
            "name": "vehicleComponentType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VehicleLight:
    vehicle_light_type: Optional[Union[str, VehicleLightTypeValue]] = field(
        default=None,
        metadata={
            "name": "vehicleLightType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class VehicleRoleDistributionEntry:
    role: Optional[Union[str, RoleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Waypoint:
    position: Optional["Position"] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    route_strategy: Optional[Union[str, RouteStrategyValue]] = field(
        default=None,
        metadata={
            "name": "routeStrategy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ByValueCondition:
    parameter_condition: Optional[ParameterCondition] = field(
        default=None,
        metadata={
            "name": "ParameterCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    time_of_day_condition: Optional[TimeOfDayCondition] = field(
        default=None,
        metadata={
            "name": "TimeOfDayCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    simulation_time_condition: Optional[SimulationTimeCondition] = field(
        default=None,
        metadata={
            "name": "SimulationTimeCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    storyboard_element_state_condition: Optional[StoryboardElementStateCondition] = field(
        default=None,
        metadata={
            "name": "StoryboardElementStateCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_value_condition: Optional[UserDefinedValueCondition] = field(
        default=None,
        metadata={
            "name": "UserDefinedValueCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_signal_condition: Optional[TrafficSignalCondition] = field(
        default=None,
        metadata={
            "name": "TrafficSignalCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_signal_controller_condition: Optional[TrafficSignalControllerCondition] = field(
        default=None,
        metadata={
            "name": "TrafficSignalControllerCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    variable_condition: Optional[VariableCondition] = field(
        default=None,
        metadata={
            "name": "VariableCondition",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CatalogLocations:
    vehicle_catalog: Optional[VehicleCatalogLocation] = field(
        default=None,
        metadata={
            "name": "VehicleCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    controller_catalog: Optional[ControllerCatalogLocation] = field(
        default=None,
        metadata={
            "name": "ControllerCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    pedestrian_catalog: Optional[PedestrianCatalogLocation] = field(
        default=None,
        metadata={
            "name": "PedestrianCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    misc_object_catalog: Optional[MiscObjectCatalogLocation] = field(
        default=None,
        metadata={
            "name": "MiscObjectCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    environment_catalog: Optional[EnvironmentCatalogLocation] = field(
        default=None,
        metadata={
            "name": "EnvironmentCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    maneuver_catalog: Optional[ManeuverCatalogLocation] = field(
        default=None,
        metadata={
            "name": "ManeuverCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    trajectory_catalog: Optional[TrajectoryCatalogLocation] = field(
        default=None,
        metadata={
            "name": "TrajectoryCatalog",
            "type": "Element",
            "namespace": "",
        }
    )
    route_catalog: Optional[RouteCatalogLocation] = field(
        default=None,
        metadata={
            "name": "RouteCatalog",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CatalogReference:
    parameter_assignments: Optional[ParameterAssignments] = field(
        default=None,
        metadata={
            "name": "ParameterAssignments",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "catalogName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    entry_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "entryName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class CollisionCondition:
    entity_ref: Optional[EntityRef] = field(
        default=None,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
        }
    )
    by_type: Optional[ByObjectType] = field(
        default=None,
        metadata={
            "name": "ByType",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ComponentAnimation:
    vehicle_component: Optional[VehicleComponent] = field(
        default=None,
        metadata={
            "name": "VehicleComponent",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    user_defined_component: Optional[UserDefinedComponent] = field(
        default=None,
        metadata={
            "name": "UserDefinedComponent",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DeterministicSingleParameterDistribution:
    distribution_set: Optional[DistributionSet] = field(
        default=None,
        metadata={
            "name": "DistributionSet",
            "type": "Element",
            "namespace": "",
        }
    )
    distribution_range: Optional[DistributionRange] = field(
        default=None,
        metadata={
            "name": "DistributionRange",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_distribution: Optional[UserDefinedDistribution] = field(
        default=None,
        metadata={
            "name": "UserDefinedDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class FileHeader:
    license: Optional[License] = field(
        default=None,
        metadata={
            "name": "License",
            "type": "Element",
            "namespace": "",
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    rev_major: Optional[str] = field(
        default=None,
        metadata={
            "name": "revMajor",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rev_minor: Optional[str] = field(
        default=None,
        metadata={
            "name": "revMinor",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class FinalSpeed:
    absolute_speed: Optional[AbsoluteSpeed] = field(
        default=None,
        metadata={
            "name": "AbsoluteSpeed",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_speed_to_master: Optional[RelativeSpeedToMaster] = field(
        default=None,
        metadata={
            "name": "RelativeSpeedToMaster",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Fog:
    bounding_box: Optional[BoundingBox] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "",
        }
    )
    visual_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "visualRange",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class GeoPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    latitude_deg: Optional[str] = field(
        default=None,
        metadata={
            "name": "latitudeDeg",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    longitude_deg: Optional[str] = field(
        default=None,
        metadata={
            "name": "longitudeDeg",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    altitude: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Histogram:
    bin: List[HistogramBin] = field(
        default_factory=list,
        metadata={
            "name": "Bin",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class InfrastructureAction:
    traffic_signal_action: Optional[TrafficSignalAction] = field(
        default=None,
        metadata={
            "name": "TrafficSignalAction",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class LaneChangeAction:
    lane_change_action_dynamics: Optional[TransitionDynamics] = field(
        default=None,
        metadata={
            "name": "LaneChangeActionDynamics",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lane_change_target: Optional[LaneChangeTarget] = field(
        default=None,
        metadata={
            "name": "LaneChangeTarget",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    target_lane_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetLaneOffset",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class LaneOffsetAction:
    lane_offset_action_dynamics: Optional[LaneOffsetActionDynamics] = field(
        default=None,
        metadata={
            "name": "LaneOffsetActionDynamics",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    lane_offset_target: Optional[LaneOffsetTarget] = field(
        default=None,
        metadata={
            "name": "LaneOffsetTarget",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    continuous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class LanePosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    lane_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "laneId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class LightState:
    color: Optional[Color] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
            "namespace": "",
        }
    )
    mode: Optional[Union[str, LightModeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    luminous_intensity: Optional[str] = field(
        default=None,
        metadata={
            "name": "luminousIntensity",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    flashing_on_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "flashingOnDuration",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    flashing_off_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "flashingOffDuration",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class LightType:
    vehicle_light: Optional[VehicleLight] = field(
        default=None,
        metadata={
            "name": "VehicleLight",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    user_defined_light: Optional[UserDefinedLight] = field(
        default=None,
        metadata={
            "name": "UserDefinedLight",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class OverrideGearAction:
    manual_gear: Optional[ManualGear] = field(
        default=None,
        metadata={
            "name": "ManualGear",
            "type": "Element",
            "namespace": "",
        }
    )
    automatic_gear: Optional[AutomaticGear] = field(
        default=None,
        metadata={
            "name": "AutomaticGear",
            "type": "Element",
            "namespace": "",
        }
    )
    active: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class ParameterModifyAction:
    rule: Optional[ModifyRule] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class PedestrianAnimation:
    pedestrian_gesture: List[PedestrianGesture] = field(
        default_factory=list,
        metadata={
            "name": "PedestrianGesture",
            "type": "Element",
            "namespace": "",
        }
    )
    motion: Optional[Union[str, PedestrianMotionTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    user_defined_pedestrian_animation: Optional[str] = field(
        default=None,
        metadata={
            "name": "userDefinedPedestrianAnimation",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class RelativeLanePosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    d_lane: Optional[str] = field(
        default=None,
        metadata={
            "name": "dLane",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    ds: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    ds_lane: Optional[str] = field(
        default=None,
        metadata={
            "name": "dsLane",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeObjectPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    dx: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    dy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    dz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeRoadPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    ds: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    dt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RelativeWorldPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    dx: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    dy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    dz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RoadCondition:
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
        }
    )
    friction_scale_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "frictionScaleFactor",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    wetness: Optional[Union[str, WetnessValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class RoadPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    road_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class SelectedEntities:
    entity_ref: List[EntityRef] = field(
        default_factory=list,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
        }
    )
    by_type: List[ByType] = field(
        default_factory=list,
        metadata={
            "name": "ByType",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Shape:
    polyline: Optional[Polyline] = field(
        default=None,
        metadata={
            "name": "Polyline",
            "type": "Element",
            "namespace": "",
        }
    )
    clothoid: Optional[Clothoid] = field(
        default=None,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "",
        }
    )
    nurbs: Optional[Nurbs] = field(
        default=None,
        metadata={
            "name": "Nurbs",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SpeedActionTarget:
    relative_target_speed: Optional[RelativeTargetSpeed] = field(
        default=None,
        metadata={
            "name": "RelativeTargetSpeed",
            "type": "Element",
            "namespace": "",
        }
    )
    absolute_target_speed: Optional[AbsoluteTargetSpeed] = field(
        default=None,
        metadata={
            "name": "AbsoluteTargetSpeed",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TimeReference:
    none: Optional[NoneType] = field(
        default=None,
        metadata={
            "name": "None",
            "type": "Element",
            "namespace": "",
        }
    )
    timing: Optional[Timing] = field(
        default=None,
        metadata={
            "name": "Timing",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TrafficSignalController:
    phase: List[Phase] = field(
        default_factory=list,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "",
        }
    )
    delay: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ValueConstraintGroup:
    value_constraint: List[ValueConstraint] = field(
        default_factory=list,
        metadata={
            "name": "ValueConstraint",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ValueSetDistribution:
    parameter_value_set: List[ParameterValueSet] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValueSet",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class VariableDeclarations:
    variable_declaration: List[VariableDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "VariableDeclaration",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class VariableModifyAction:
    rule: Optional[VariableModifyRule] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class VehicleCategoryDistribution:
    vehicle_category_distribution_entry: List[VehicleCategoryDistributionEntry] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCategoryDistributionEntry",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class VehicleRoleDistribution:
    vehicle_role_distribution_entry: List[VehicleRoleDistributionEntry] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRoleDistributionEntry",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class VisibilityAction:
    sensor_reference_set: Optional[SensorReferenceSet] = field(
        default=None,
        metadata={
            "name": "SensorReferenceSet",
            "type": "Element",
            "namespace": "",
        }
    )
    graphics: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    sensors: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    traffic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AnimationType:
    component_animation: Optional[ComponentAnimation] = field(
        default=None,
        metadata={
            "name": "ComponentAnimation",
            "type": "Element",
            "namespace": "",
        }
    )
    pedestrian_animation: Optional[PedestrianAnimation] = field(
        default=None,
        metadata={
            "name": "PedestrianAnimation",
            "type": "Element",
            "namespace": "",
        }
    )
    animation_file: Optional[AnimationFile] = field(
        default=None,
        metadata={
            "name": "AnimationFile",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_animation: Optional[UserDefinedAnimation] = field(
        default=None,
        metadata={
            "name": "UserDefinedAnimation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DeterministicMultiParameterDistribution:
    value_set_distribution: Optional[ValueSetDistribution] = field(
        default=None,
        metadata={
            "name": "ValueSetDistribution",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class EntitySelection:
    members: Optional[SelectedEntities] = field(
        default=None,
        metadata={
            "name": "Members",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class LateralAction:
    lane_change_action: Optional[LaneChangeAction] = field(
        default=None,
        metadata={
            "name": "LaneChangeAction",
            "type": "Element",
            "namespace": "",
        }
    )
    lane_offset_action: Optional[LaneOffsetAction] = field(
        default=None,
        metadata={
            "name": "LaneOffsetAction",
            "type": "Element",
            "namespace": "",
        }
    )
    lateral_distance_action: Optional[LateralDistanceAction] = field(
        default=None,
        metadata={
            "name": "LateralDistanceAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LightStateAction:
    light_type: Optional[LightType] = field(
        default=None,
        metadata={
            "name": "LightType",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    light_state: Optional[LightState] = field(
        default=None,
        metadata={
            "name": "LightState",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    transition_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "transitionTime",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class OverrideControllerValueAction:
    throttle: Optional[OverrideThrottleAction] = field(
        default=None,
        metadata={
            "name": "Throttle",
            "type": "Element",
            "namespace": "",
        }
    )
    brake: Optional[OverrideBrakeAction] = field(
        default=None,
        metadata={
            "name": "Brake",
            "type": "Element",
            "namespace": "",
        }
    )
    clutch: Optional[OverrideClutchAction] = field(
        default=None,
        metadata={
            "name": "Clutch",
            "type": "Element",
            "namespace": "",
        }
    )
    parking_brake: Optional[OverrideParkingBrakeAction] = field(
        default=None,
        metadata={
            "name": "ParkingBrake",
            "type": "Element",
            "namespace": "",
        }
    )
    steering_wheel: Optional[OverrideSteeringWheelAction] = field(
        default=None,
        metadata={
            "name": "SteeringWheel",
            "type": "Element",
            "namespace": "",
        }
    )
    gear: Optional[OverrideGearAction] = field(
        default=None,
        metadata={
            "name": "Gear",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ParameterAction:
    set_action: Optional[ParameterSetAction] = field(
        default=None,
        metadata={
            "name": "SetAction",
            "type": "Element",
            "namespace": "",
        }
    )
    modify_action: Optional[ParameterModifyAction] = field(
        default=None,
        metadata={
            "name": "ModifyAction",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ParameterDeclaration:
    constraint_group: List[ValueConstraintGroup] = field(
        default_factory=list,
        metadata={
            "name": "ConstraintGroup",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    parameter_type: Optional[Union[str, ParameterTypeValue]] = field(
        default=None,
        metadata={
            "name": "parameterType",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class SpeedAction:
    speed_action_dynamics: Optional[TransitionDynamics] = field(
        default=None,
        metadata={
            "name": "SpeedActionDynamics",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    speed_action_target: Optional[SpeedActionTarget] = field(
        default=None,
        metadata={
            "name": "SpeedActionTarget",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class StochasticDistribution:
    probability_distribution_set: Optional[ProbabilityDistributionSet] = field(
        default=None,
        metadata={
            "name": "ProbabilityDistributionSet",
            "type": "Element",
            "namespace": "",
        }
    )
    normal_distribution: Optional[NormalDistribution] = field(
        default=None,
        metadata={
            "name": "NormalDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    uniform_distribution: Optional[UniformDistribution] = field(
        default=None,
        metadata={
            "name": "UniformDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    poisson_distribution: Optional[PoissonDistribution] = field(
        default=None,
        metadata={
            "name": "PoissonDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    histogram: Optional[Histogram] = field(
        default=None,
        metadata={
            "name": "Histogram",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_distribution: Optional[UserDefinedDistribution] = field(
        default=None,
        metadata={
            "name": "UserDefinedDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "parameterName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficSignals:
    traffic_signal_controller: List[TrafficSignalController] = field(
        default_factory=list,
        metadata={
            "name": "TrafficSignalController",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class VariableAction:
    set_action: Optional[VariableSetAction] = field(
        default=None,
        metadata={
            "name": "SetAction",
            "type": "Element",
            "namespace": "",
        }
    )
    modify_action: Optional[VariableModifyAction] = field(
        default=None,
        metadata={
            "name": "ModifyAction",
            "type": "Element",
            "namespace": "",
        }
    )
    variable_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Weather:
    sun: Optional[Sun] = field(
        default=None,
        metadata={
            "name": "Sun",
            "type": "Element",
            "namespace": "",
        }
    )
    fog: Optional[Fog] = field(
        default=None,
        metadata={
            "name": "Fog",
            "type": "Element",
            "namespace": "",
        }
    )
    precipitation: Optional[Precipitation] = field(
        default=None,
        metadata={
            "name": "Precipitation",
            "type": "Element",
            "namespace": "",
        }
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "name": "Wind",
            "type": "Element",
            "namespace": "",
        }
    )
    dome_image: Optional[DomeImage] = field(
        default=None,
        metadata={
            "name": "DomeImage",
            "type": "Element",
            "namespace": "",
        }
    )
    cloud_state: Optional[Union[str, CloudStateValue]] = field(
        default=None,
        metadata={
            "name": "cloudState",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    atmospheric_pressure: Optional[str] = field(
        default=None,
        metadata={
            "name": "atmosphericPressure",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    temperature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    fractional_cloud_cover: Optional[Union[str, FractionalCloudCoverValue]] = field(
        default=None,
        metadata={
            "name": "fractionalCloudCover",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class AnimationAction:
    animation_type: Optional[AnimationType] = field(
        default=None,
        metadata={
            "name": "AnimationType",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    animation_state: Optional[AnimationState] = field(
        default=None,
        metadata={
            "name": "AnimationState",
            "type": "Element",
            "namespace": "",
        }
    )
    loop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    animation_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "animationDuration",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Deterministic:
    deterministic_multi_parameter_distribution: List[DeterministicMultiParameterDistribution] = field(
        default_factory=list,
        metadata={
            "name": "DeterministicMultiParameterDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    deterministic_single_parameter_distribution: List[DeterministicSingleParameterDistribution] = field(
        default_factory=list,
        metadata={
            "name": "DeterministicSingleParameterDistribution",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class LongitudinalAction:
    speed_action: Optional[SpeedAction] = field(
        default=None,
        metadata={
            "name": "SpeedAction",
            "type": "Element",
            "namespace": "",
        }
    )
    longitudinal_distance_action: Optional[LongitudinalDistanceAction] = field(
        default=None,
        metadata={
            "name": "LongitudinalDistanceAction",
            "type": "Element",
            "namespace": "",
        }
    )
    speed_profile_action: Optional[SpeedProfileAction] = field(
        default=None,
        metadata={
            "name": "SpeedProfileAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ParameterDeclarations:
    parameter_declaration: List[ParameterDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "ParameterDeclaration",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Stochastic:
    stochastic_distribution: List[StochasticDistribution] = field(
        default_factory=list,
        metadata={
            "name": "StochasticDistribution",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    number_of_test_runs: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfTestRuns",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    random_seed: Optional[str] = field(
        default=None,
        metadata={
            "name": "randomSeed",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AppearanceAction:
    light_state_action: Optional[LightStateAction] = field(
        default=None,
        metadata={
            "name": "LightStateAction",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    animation_action: Optional[AnimationAction] = field(
        default=None,
        metadata={
            "name": "AnimationAction",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Controller:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    controller_type: Optional[Union[str, ControllerTypeValue]] = field(
        default=None,
        metadata={
            "name": "controllerType",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Environment:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    time_of_day: Optional[TimeOfDay] = field(
        default=None,
        metadata={
            "name": "TimeOfDay",
            "type": "Element",
            "namespace": "",
        }
    )
    weather: Optional[Weather] = field(
        default=None,
        metadata={
            "name": "Weather",
            "type": "Element",
            "namespace": "",
        }
    )
    road_condition: Optional[RoadCondition] = field(
        default=None,
        metadata={
            "name": "RoadCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class MiscObject:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    bounding_box: Optional[BoundingBox] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mass: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    misc_object_category: Optional[Union[str, MiscObjectCategoryValue]] = field(
        default=None,
        metadata={
            "name": "miscObjectCategory",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    model3d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ParameterValueDistribution:
    scenario_file: Optional[File] = field(
        default=None,
        metadata={
            "name": "ScenarioFile",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    deterministic: Optional[Deterministic] = field(
        default=None,
        metadata={
            "name": "Deterministic",
            "type": "Element",
            "namespace": "",
        }
    )
    stochastic: Optional[Stochastic] = field(
        default=None,
        metadata={
            "name": "Stochastic",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Pedestrian:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    bounding_box: Optional[BoundingBox] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    mass: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    pedestrian_category: Optional[Union[str, PedestrianCategoryValue]] = field(
        default=None,
        metadata={
            "name": "pedestrianCategory",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    model3d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    role: Optional[Union[str, RoleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Route:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    waypoint: List[Waypoint] = field(
        default_factory=list,
        metadata={
            "name": "Waypoint",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )
    closed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Trajectory:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    shape: Optional[Shape] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    closed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Vehicle:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    bounding_box: Optional[BoundingBox] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    performance: Optional[Performance] = field(
        default=None,
        metadata={
            "name": "Performance",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    axles: Optional[Axles] = field(
        default=None,
        metadata={
            "name": "Axles",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    vehicle_category: Optional[Union[str, VehicleCategoryValue]] = field(
        default=None,
        metadata={
            "name": "vehicleCategory",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    role: Optional[Union[str, RoleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    mass: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    model3d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class AssignControllerAction:
    controller: Optional[Controller] = field(
        default=None,
        metadata={
            "name": "Controller",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    activate_lateral: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateLateral",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    activate_longitudinal: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateLongitudinal",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    activate_animation: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateAnimation",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    activate_lighting: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateLighting",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class AssignRouteAction:
    route: Optional[Route] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ControllerDistributionEntry:
    controller: Optional[Controller] = field(
        default=None,
        metadata={
            "name": "Controller",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    weight: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class EnvironmentAction:
    environment: Optional[Environment] = field(
        default=None,
        metadata={
            "name": "Environment",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ObjectController:
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    controller: Optional[Controller] = field(
        default=None,
        metadata={
            "name": "Controller",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RouteRef:
    route: Optional[Route] = field(
        default=None,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TrajectoryRef:
    trajectory: Optional[Trajectory] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ControllerAction:
    assign_controller_action: Optional[AssignControllerAction] = field(
        default=None,
        metadata={
            "name": "AssignControllerAction",
            "type": "Element",
            "namespace": "",
        }
    )
    override_controller_value_action: Optional[OverrideControllerValueAction] = field(
        default=None,
        metadata={
            "name": "OverrideControllerValueAction",
            "type": "Element",
            "namespace": "",
        }
    )
    activate_controller_action: Optional[ActivateControllerAction] = field(
        default=None,
        metadata={
            "name": "ActivateControllerAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ControllerDistribution:
    controller_distribution_entry: List[ControllerDistributionEntry] = field(
        default_factory=list,
        metadata={
            "name": "ControllerDistributionEntry",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class FollowTrajectoryAction:
    trajectory: Optional[Trajectory] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    time_reference: Optional[TimeReference] = field(
        default=None,
        metadata={
            "name": "TimeReference",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    trajectory_following_mode: Optional[TrajectoryFollowingMode] = field(
        default=None,
        metadata={
            "name": "TrajectoryFollowingMode",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    trajectory_ref: Optional[TrajectoryRef] = field(
        default=None,
        metadata={
            "name": "TrajectoryRef",
            "type": "Element",
            "namespace": "",
        }
    )
    initial_distance_offset: Optional[str] = field(
        default=None,
        metadata={
            "name": "initialDistanceOffset",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class RoutePosition:
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    in_route_position: Optional[InRoutePosition] = field(
        default=None,
        metadata={
            "name": "InRoutePosition",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ScenarioObject:
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "",
        }
    )
    pedestrian: Optional[Pedestrian] = field(
        default=None,
        metadata={
            "name": "Pedestrian",
            "type": "Element",
            "namespace": "",
        }
    )
    misc_object: Optional[MiscObject] = field(
        default=None,
        metadata={
            "name": "MiscObject",
            "type": "Element",
            "namespace": "",
        }
    )
    external_object_reference: Optional[ExternalObjectReference] = field(
        default=None,
        metadata={
            "name": "ExternalObjectReference",
            "type": "Element",
            "namespace": "",
        }
    )
    object_controller: List[ObjectController] = field(
        default_factory=list,
        metadata={
            "name": "ObjectController",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrajectoryPosition:
    orientation: Optional[Orientation] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "",
        }
    )
    trajectory_ref: Optional[TrajectoryRef] = field(
        default=None,
        metadata={
            "name": "TrajectoryRef",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class Entities:
    scenario_object: List[ScenarioObject] = field(
        default_factory=list,
        metadata={
            "name": "ScenarioObject",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_selection: List[EntitySelection] = field(
        default_factory=list,
        metadata={
            "name": "EntitySelection",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Position:
    world_position: Optional[WorldPosition] = field(
        default=None,
        metadata={
            "name": "WorldPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_world_position: Optional[RelativeWorldPosition] = field(
        default=None,
        metadata={
            "name": "RelativeWorldPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_object_position: Optional[RelativeObjectPosition] = field(
        default=None,
        metadata={
            "name": "RelativeObjectPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    road_position: Optional[RoadPosition] = field(
        default=None,
        metadata={
            "name": "RoadPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_road_position: Optional[RelativeRoadPosition] = field(
        default=None,
        metadata={
            "name": "RelativeRoadPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    lane_position: Optional[LanePosition] = field(
        default=None,
        metadata={
            "name": "LanePosition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_lane_position: Optional[RelativeLanePosition] = field(
        default=None,
        metadata={
            "name": "RelativeLanePosition",
            "type": "Element",
            "namespace": "",
        }
    )
    route_position: Optional[RoutePosition] = field(
        default=None,
        metadata={
            "name": "RoutePosition",
            "type": "Element",
            "namespace": "",
        }
    )
    geo_position: Optional[GeoPosition] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "",
        }
    )
    trajectory_position: Optional[TrajectoryPosition] = field(
        default=None,
        metadata={
            "name": "TrajectoryPosition",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TrafficDefinition:
    vehicle_category_distribution: Optional[VehicleCategoryDistribution] = field(
        default=None,
        metadata={
            "name": "VehicleCategoryDistribution",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    vehicle_role_distribution: Optional[VehicleRoleDistribution] = field(
        default=None,
        metadata={
            "name": "VehicleRoleDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    controller_distribution: Optional[ControllerDistribution] = field(
        default=None,
        metadata={
            "name": "ControllerDistribution",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class AcquirePositionAction:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class AddEntityAction:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DistanceCondition:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    along_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "alongRoute",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    relative_distance_type: Optional[Union[str, RelativeDistanceTypeValue]] = field(
        default=None,
        metadata={
            "name": "relativeDistanceType",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    routing_algorithm: Optional[Union[str, RoutingAlgorithmValue]] = field(
        default=None,
        metadata={
            "name": "routingAlgorithm",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ReachPositionCondition:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tolerance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class SynchronizeAction:
    target_position_master: Optional[Position] = field(
        default=None,
        metadata={
            "name": "TargetPositionMaster",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    target_position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "TargetPosition",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    final_speed: Optional[FinalSpeed] = field(
        default=None,
        metadata={
            "name": "FinalSpeed",
            "type": "Element",
            "namespace": "",
        }
    )
    master_entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "masterEntityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    target_tolerance_master: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetToleranceMaster",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    target_tolerance: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetTolerance",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TeleportAction:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TimeToCollisionConditionTarget:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[EntityRef] = field(
        default=None,
        metadata={
            "name": "EntityRef",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TrafficSinkAction:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    traffic_definition: Optional[TrafficDefinition] = field(
        default=None,
        metadata={
            "name": "TrafficDefinition",
            "type": "Element",
            "namespace": "",
        }
    )
    radius: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TrafficSourceAction:
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    traffic_definition: Optional[TrafficDefinition] = field(
        default=None,
        metadata={
            "name": "TrafficDefinition",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    radius: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    velocity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    speed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class TrafficSwarmAction:
    central_object: Optional[CentralSwarmObject] = field(
        default=None,
        metadata={
            "name": "CentralObject",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    traffic_definition: Optional[TrafficDefinition] = field(
        default=None,
        metadata={
            "name": "TrafficDefinition",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    initial_speed_range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "InitialSpeedRange",
            "type": "Element",
            "namespace": "",
        }
    )
    direction_of_travel_distribution: Optional[DirectionOfTravelDistribution] = field(
        default=None,
        metadata={
            "name": "DirectionOfTravelDistribution",
            "type": "Element",
            "namespace": "",
        }
    )
    inner_radius: Optional[str] = field(
        default=None,
        metadata={
            "name": "innerRadius",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    number_of_vehicles: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    semi_major_axis: Optional[str] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    semi_minor_axis: Optional[str] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    velocity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )


@dataclass
class UsedArea:
    position: List[Position] = field(
        default_factory=list,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )


@dataclass
class EntityAction:
    add_entity_action: Optional[AddEntityAction] = field(
        default=None,
        metadata={
            "name": "AddEntityAction",
            "type": "Element",
            "namespace": "",
        }
    )
    delete_entity_action: Optional[DeleteEntityAction] = field(
        default=None,
        metadata={
            "name": "DeleteEntityAction",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class RoadNetwork:
    logic_file: Optional[File] = field(
        default=None,
        metadata={
            "name": "LogicFile",
            "type": "Element",
            "namespace": "",
        }
    )
    scene_graph_file: Optional[File] = field(
        default=None,
        metadata={
            "name": "SceneGraphFile",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_signals: Optional[TrafficSignals] = field(
        default=None,
        metadata={
            "name": "TrafficSignals",
            "type": "Element",
            "namespace": "",
        }
    )
    used_area: Optional[UsedArea] = field(
        default=None,
        metadata={
            "name": "UsedArea",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RoutingAction:
    assign_route_action: Optional[AssignRouteAction] = field(
        default=None,
        metadata={
            "name": "AssignRouteAction",
            "type": "Element",
            "namespace": "",
        }
    )
    follow_trajectory_action: Optional[FollowTrajectoryAction] = field(
        default=None,
        metadata={
            "name": "FollowTrajectoryAction",
            "type": "Element",
            "namespace": "",
        }
    )
    acquire_position_action: Optional[AcquirePositionAction] = field(
        default=None,
        metadata={
            "name": "AcquirePositionAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TimeToCollisionCondition:
    time_to_collision_condition_target: Optional[TimeToCollisionConditionTarget] = field(
        default=None,
        metadata={
            "name": "TimeToCollisionConditionTarget",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    along_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "alongRoute",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    freespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    rule: Optional[Union[str, RuleValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    relative_distance_type: Optional[Union[str, RelativeDistanceTypeValue]] = field(
        default=None,
        metadata={
            "name": "relativeDistanceType",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    coordinate_system: Optional[Union[str, CoordinateSystemValue]] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    routing_algorithm: Optional[Union[str, RoutingAlgorithmValue]] = field(
        default=None,
        metadata={
            "name": "routingAlgorithm",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class TrafficAction:
    traffic_source_action: Optional[TrafficSourceAction] = field(
        default=None,
        metadata={
            "name": "TrafficSourceAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_sink_action: Optional[TrafficSinkAction] = field(
        default=None,
        metadata={
            "name": "TrafficSinkAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_swarm_action: Optional[TrafficSwarmAction] = field(
        default=None,
        metadata={
            "name": "TrafficSwarmAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_stop_action: Optional[TrafficStopAction] = field(
        default=None,
        metadata={
            "name": "TrafficStopAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "trafficName",
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class EntityCondition:
    end_of_road_condition: Optional[EndOfRoadCondition] = field(
        default=None,
        metadata={
            "name": "EndOfRoadCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    collision_condition: Optional[CollisionCondition] = field(
        default=None,
        metadata={
            "name": "CollisionCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    offroad_condition: Optional[OffroadCondition] = field(
        default=None,
        metadata={
            "name": "OffroadCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    time_headway_condition: Optional[TimeHeadwayCondition] = field(
        default=None,
        metadata={
            "name": "TimeHeadwayCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    time_to_collision_condition: Optional[TimeToCollisionCondition] = field(
        default=None,
        metadata={
            "name": "TimeToCollisionCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    acceleration_condition: Optional[AccelerationCondition] = field(
        default=None,
        metadata={
            "name": "AccelerationCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    stand_still_condition: Optional[StandStillCondition] = field(
        default=None,
        metadata={
            "name": "StandStillCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    speed_condition: Optional[SpeedCondition] = field(
        default=None,
        metadata={
            "name": "SpeedCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_speed_condition: Optional[RelativeSpeedCondition] = field(
        default=None,
        metadata={
            "name": "RelativeSpeedCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    traveled_distance_condition: Optional[TraveledDistanceCondition] = field(
        default=None,
        metadata={
            "name": "TraveledDistanceCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    reach_position_condition: Optional[ReachPositionCondition] = field(
        default=None,
        metadata={
            "name": "ReachPositionCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    distance_condition: Optional[DistanceCondition] = field(
        default=None,
        metadata={
            "name": "DistanceCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_distance_condition: Optional[RelativeDistanceCondition] = field(
        default=None,
        metadata={
            "name": "RelativeDistanceCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    relative_clearance_condition: Optional[RelativeClearanceCondition] = field(
        default=None,
        metadata={
            "name": "RelativeClearanceCondition",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GlobalAction:
    environment_action: Optional[EnvironmentAction] = field(
        default=None,
        metadata={
            "name": "EnvironmentAction",
            "type": "Element",
            "namespace": "",
        }
    )
    entity_action: Optional[EntityAction] = field(
        default=None,
        metadata={
            "name": "EntityAction",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_action: Optional[ParameterAction] = field(
        default=None,
        metadata={
            "name": "ParameterAction",
            "type": "Element",
            "namespace": "",
        }
    )
    infrastructure_action: Optional[InfrastructureAction] = field(
        default=None,
        metadata={
            "name": "InfrastructureAction",
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_action: Optional[TrafficAction] = field(
        default=None,
        metadata={
            "name": "TrafficAction",
            "type": "Element",
            "namespace": "",
        }
    )
    variable_action: Optional[VariableAction] = field(
        default=None,
        metadata={
            "name": "VariableAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PrivateAction:
    longitudinal_action: Optional[LongitudinalAction] = field(
        default=None,
        metadata={
            "name": "LongitudinalAction",
            "type": "Element",
            "namespace": "",
        }
    )
    lateral_action: Optional[LateralAction] = field(
        default=None,
        metadata={
            "name": "LateralAction",
            "type": "Element",
            "namespace": "",
        }
    )
    visibility_action: Optional[VisibilityAction] = field(
        default=None,
        metadata={
            "name": "VisibilityAction",
            "type": "Element",
            "namespace": "",
        }
    )
    synchronize_action: Optional[SynchronizeAction] = field(
        default=None,
        metadata={
            "name": "SynchronizeAction",
            "type": "Element",
            "namespace": "",
        }
    )
    activate_controller_action: Optional[ActivateControllerAction] = field(
        default=None,
        metadata={
            "name": "ActivateControllerAction",
            "type": "Element",
            "namespace": "",
        }
    )
    controller_action: Optional[ControllerAction] = field(
        default=None,
        metadata={
            "name": "ControllerAction",
            "type": "Element",
            "namespace": "",
        }
    )
    teleport_action: Optional[TeleportAction] = field(
        default=None,
        metadata={
            "name": "TeleportAction",
            "type": "Element",
            "namespace": "",
        }
    )
    routing_action: Optional[RoutingAction] = field(
        default=None,
        metadata={
            "name": "RoutingAction",
            "type": "Element",
            "namespace": "",
        }
    )
    appearance_action: Optional[AppearanceAction] = field(
        default=None,
        metadata={
            "name": "AppearanceAction",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Action:
    global_action: Optional[GlobalAction] = field(
        default=None,
        metadata={
            "name": "GlobalAction",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_action: Optional[UserDefinedAction] = field(
        default=None,
        metadata={
            "name": "UserDefinedAction",
            "type": "Element",
            "namespace": "",
        }
    )
    private_action: Optional[PrivateAction] = field(
        default=None,
        metadata={
            "name": "PrivateAction",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ByEntityCondition:
    triggering_entities: Optional[TriggeringEntities] = field(
        default=None,
        metadata={
            "name": "TriggeringEntities",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    entity_condition: Optional[EntityCondition] = field(
        default=None,
        metadata={
            "name": "EntityCondition",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Private:
    private_action: List[PrivateAction] = field(
        default_factory=list,
        metadata={
            "name": "PrivateAction",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    entity_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityRef",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Condition:
    by_entity_condition: Optional[ByEntityCondition] = field(
        default=None,
        metadata={
            "name": "ByEntityCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    by_value_condition: Optional[ByValueCondition] = field(
        default=None,
        metadata={
            "name": "ByValueCondition",
            "type": "Element",
            "namespace": "",
        }
    )
    condition_edge: Optional[Union[str, ConditionEdgeValue]] = field(
        default=None,
        metadata={
            "name": "conditionEdge",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    delay: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class InitActions:
    global_action: List[GlobalAction] = field(
        default_factory=list,
        metadata={
            "name": "GlobalAction",
            "type": "Element",
            "namespace": "",
        }
    )
    user_defined_action: List[UserDefinedAction] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedAction",
            "type": "Element",
            "namespace": "",
        }
    )
    private: List[Private] = field(
        default_factory=list,
        metadata={
            "name": "Private",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ConditionGroup:
    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Init:
    actions: Optional[InitActions] = field(
        default=None,
        metadata={
            "name": "Actions",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Trigger:
    condition_group: List[ConditionGroup] = field(
        default_factory=list,
        metadata={
            "name": "ConditionGroup",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Event:
    action: List[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    start_trigger: Optional[Trigger] = field(
        default=None,
        metadata={
            "name": "StartTrigger",
            "type": "Element",
            "namespace": "",
        }
    )
    maximum_execution_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "maximumExecutionCount",
            "type": "Attribute",
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )
    priority: Optional[Union[str, PriorityValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Maneuver:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    event: List[Event] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Catalog:
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "",
        }
    )
    controller: List[Controller] = field(
        default_factory=list,
        metadata={
            "name": "Controller",
            "type": "Element",
            "namespace": "",
        }
    )
    pedestrian: List[Pedestrian] = field(
        default_factory=list,
        metadata={
            "name": "Pedestrian",
            "type": "Element",
            "namespace": "",
        }
    )
    misc_object: List[MiscObject] = field(
        default_factory=list,
        metadata={
            "name": "MiscObject",
            "type": "Element",
            "namespace": "",
        }
    )
    environment: List[Environment] = field(
        default_factory=list,
        metadata={
            "name": "Environment",
            "type": "Element",
            "namespace": "",
        }
    )
    maneuver: List[Maneuver] = field(
        default_factory=list,
        metadata={
            "name": "Maneuver",
            "type": "Element",
            "namespace": "",
        }
    )
    trajectory: List[Trajectory] = field(
        default_factory=list,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "",
        }
    )
    route: List[Route] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class ManeuverGroup:
    actors: Optional[Actors] = field(
        default=None,
        metadata={
            "name": "Actors",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    catalog_reference: List[CatalogReference] = field(
        default_factory=list,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
            "namespace": "",
        }
    )
    maneuver: List[Maneuver] = field(
        default_factory=list,
        metadata={
            "name": "Maneuver",
            "type": "Element",
            "namespace": "",
        }
    )
    maximum_execution_count: Optional[str] = field(
        default=None,
        metadata={
            "name": "maximumExecutionCount",
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][{][ A-Za-z0-9_\+\-\*/%$\(\)\.,]*[\}]",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Act:
    maneuver_group: List[ManeuverGroup] = field(
        default_factory=list,
        metadata={
            "name": "ManeuverGroup",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    start_trigger: Optional[Trigger] = field(
        default=None,
        metadata={
            "name": "StartTrigger",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    stop_trigger: Optional[Trigger] = field(
        default=None,
        metadata={
            "name": "StopTrigger",
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Story:
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    act: List[Act] = field(
        default_factory=list,
        metadata={
            "name": "Act",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[$][A-Za-z_][A-Za-z0-9_]*",
        }
    )


@dataclass
class Storyboard:
    init: Optional[Init] = field(
        default=None,
        metadata={
            "name": "Init",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    story: List[Story] = field(
        default_factory=list,
        metadata={
            "name": "Story",
            "type": "Element",
            "namespace": "",
        }
    )
    stop_trigger: Optional[Trigger] = field(
        default=None,
        metadata={
            "name": "StopTrigger",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class OpenScenario1:
    class Meta:
        name = "OpenScenario"

    file_header: Optional[FileHeader] = field(
        default=None,
        metadata={
            "name": "FileHeader",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    parameter_declarations: Optional[ParameterDeclarations] = field(
        default=None,
        metadata={
            "name": "ParameterDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    variable_declarations: Optional[VariableDeclarations] = field(
        default=None,
        metadata={
            "name": "VariableDeclarations",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog_locations: Optional[CatalogLocations] = field(
        default=None,
        metadata={
            "name": "CatalogLocations",
            "type": "Element",
            "namespace": "",
        }
    )
    road_network: Optional[RoadNetwork] = field(
        default=None,
        metadata={
            "name": "RoadNetwork",
            "type": "Element",
            "namespace": "",
        }
    )
    entities: Optional[Entities] = field(
        default=None,
        metadata={
            "name": "Entities",
            "type": "Element",
            "namespace": "",
        }
    )
    storyboard: Optional[Storyboard] = field(
        default=None,
        metadata={
            "name": "Storyboard",
            "type": "Element",
            "namespace": "",
        }
    )
    catalog: Optional[Catalog] = field(
        default=None,
        metadata={
            "name": "Catalog",
            "type": "Element",
            "namespace": "",
        }
    )
    parameter_value_distribution: Optional[ParameterValueDistribution] = field(
        default=None,
        metadata={
            "name": "ParameterValueDistribution",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class OpenScenario(OpenScenario1):
    class Meta:
        name = "OpenSCENARIO"
