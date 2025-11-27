from enum import Enum, auto

class CarStatus(Enum):
    BLOCKED = auto()
    OFFERED = auto()
    FREE    = auto()

class CarClass(Enum):
    VIP       = auto()
    BUSINESS  = auto()
    PREMIUM   = auto()
    PRIMITIVE = auto()