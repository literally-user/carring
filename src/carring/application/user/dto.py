from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class UserDTO:
    first_name: str
    last_name: str

    username: str
    password: str
    email: str
