from enum import Enum, auto

class CarStatus(Enum):
    BLOCKED = auto()
    OFFERED = auto()
    FREE    = auto()