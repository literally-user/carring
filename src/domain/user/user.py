from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID
import re

from .exceptions import (UsernameFormatInvalid,
                         PasswordFormatInvalid,
                         EmailFormatInvalid,)

from .enumerations import (UserPrivilege,
                           UserState,)

@dataclass
class User:
    user_uuid: UUID
    user_privilege: UserPrivilege
    user_state: UserState

    offer_uuid: Optional[UUID]

    first_name: str
    last_name: str

    username: str
    password: str
    email: str

    created_at: datetime
    updated_at: datetime

    offer_uuid: Optional[UUID] = None


    def set_user_privilege(self, privilege: UserPrivilege) -> UserPrivilege:
        self.user_privilege = privilege
        return self.user_privilege

    def set_user_state(self, state: UserState) -> UserState:
        self.user_state = state
        return self.user_state

    def set_user_uuid(self, uuid: UUID) -> UUID:
        self.user_uuid = uuid
        return self.user_uuid

    def set_first_name(self, first_name: str) -> str:
        self.first_name = first_name
        return self.first_name

    def set_last_name(self, last_name: str) -> str:
        self.last_name = last_name
        return self.last_name

    def set_username(self, username: str) -> str:
        if len(username) < 5 or len(username) > 13:
            raise UsernameFormatInvalid("Username must be over then 5 and less then 13 characters long")
        for i in username:
            if not i.isascii():
                raise UsernameFormatInvalid("Username must contain only ASCII characters")
        self.username = username
        return self.username

    def set_password(self, password: str) -> str:
        if len(password) < 8 or len(password) > 25:
            raise PasswordFormatInvalid("Password must be over then 8 and less then 25 characters long")
        for i in password:
            if not i.isascii():
                raise PasswordFormatInvalid("Password must contain only ASCII characters")
        self.password = password
        return self.password

    def set_email(self, email: str) -> str:
        if not re.search(r'/^((?!\.)[\w-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/gim;', email):
            raise EmailFormatInvalid("Email address format is invalid")
        self.email = email
        return self.email

    def set_created_at(self, created_at: datetime) -> datetime:
        self.created_at = created_at
        return self.created_at

    def set_updated_at(self, updated_at: datetime) -> datetime:
        self.updated_at = updated_at
        return self.updated_at

    def set_offer_uuid(self, offer_uuid: UUID) -> UUID:
        self.offer_uuid = offer_uuid
        return self.offer_uuid


    def __post_init__(self):
        self.user_uuid = self.set_uuid(self.user_uuid)
        self.first_name = self.set_first_name(self.first_name)
        self.last_name = self.set_last_name(self.last_name)
        self.username = self.set_username(self.username)
        self.password = self.set_password(self.password)
        self.email = self.set_email(self.email)
        self.created_at = self.set_created_at(self.created_at)
        self.updated_at = self.set_updated_at(self.updated_at)