from enum import Enum, auto

class CarStatus(Enum):
    BLOCKED = auto()
    OFFERED = auto()
    FREE    = auto()


class CarClass(Enum):
    PRIMITIVE = (1, 1.0)
    BUSINESS = (2, 2.0)
    PREMIUM = (3, 3.0)
    VIP = (4, 4.0)

    def __init__(self, id: int, multiplier: float):
        self.id = id
        self.multiplier = multiplier