from enum import Enum, auto

class UserState(Enum):
    BLOCKED = auto()
    ACTIVE  = auto()

class UserPrivilege(Enum):
    USER  = auto()
    ADMIN = auto()