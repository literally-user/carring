from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID
import re

from .exceptions import (UsernameFormatInvalid,
                         PasswordFormatInvalid,
                         EmailFormatInvalid,
                         UserStateInvalid,
                         FirstNameFormatInvalid,
                         LastNameFormatInvalid)

from .enumerations import (UserPrivilege,
                           UserState,)

@dataclass
class User:
    user_uuid: UUID
    user_privilege: UserPrivilege
    user_state: UserState

    first_name: str
    last_name: str

    username: str
    password: str
    email: str

    created_at: datetime
    updated_at: datetime

    offer_uuid: Optional[UUID]

    def attach_offer(self, offer: UUID) -> None:
        self._set_offer_uuid(offer)

    def detach_offer(self) -> None:
        self._set_offer_uuid(None)

    def _set_user_privilege(self, privilege: UserPrivilege) -> UserPrivilege:
        self.user_privilege = privilege
        return self.user_privilege

    def _set_user_state(self, state: UserState) -> UserState:
        if state != UserState.ACTIVE:
            raise UserStateInvalid("The user must be created with the state ACTIVE only.")
        self.user_state = state
        return self.user_state

    def _set_user_uuid(self, uuid: UUID) -> UUID:
        self.user_uuid = uuid
        return self.user_uuid

    def _set_first_name(self, first_name: str) -> str:
        if len(first_name) < 3 or len(first_name) > 12:
            raise FirstNameFormatInvalid("The first name must be at least 3 and less than 12 characters long.")
        self.first_name = first_name
        return self.first_name

    def _set_last_name(self, last_name: str) -> str:
        if len(last_name) < 3 or len(last_name) > 12:
            raise LastNameFormatInvalid("The last name must be at least 3 and less than 12 characters long.")
        self.last_name = last_name
        return self.last_name

    def _set_username(self, username: str) -> str:
        if len(username) < 5 or len(username) > 13:
            raise UsernameFormatInvalid("Username must be over then 5 and less then 13 characters long")
        for i in username:
            if not i.isascii():
                raise UsernameFormatInvalid("Username must contain only ASCII characters")
        self.username = username
        return self.username

    def _set_password(self, password: str) -> str:
        if len(password) < 8 or len(password) > 25:
            raise PasswordFormatInvalid("Password must be over then 8 and less then 25 characters long")
        for i in password:
            if not i.isascii():
                raise PasswordFormatInvalid("Password must contain only ASCII characters")
        self.password = password
        return self.password

    def _set_email(self, email: str) -> str:
        if not re.search( r'^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$', email):
            raise EmailFormatInvalid("Email address format is invalid")
        self.email = email
        return self.email

    def _set_created_at(self, created_at: datetime) -> datetime:
        self.created_at = created_at
        return self.created_at

    def _set_updated_at(self, updated_at: datetime) -> datetime:
        self.updated_at = updated_at
        return self.updated_at

    def _set_offer_uuid(self, offer_uuid: UUID | None) -> UUID | None:
        self.offer_uuid = offer_uuid
        return self.offer_uuid


    def __post_init__(self) -> None:
        self.user_uuid = self._set_user_uuid(self.user_uuid)
        self.first_name = self._set_first_name(self.first_name)
        self.last_name = self._set_last_name(self.last_name)
        self.username = self._set_username(self.username)
        self.password = self._set_password(self.password)
        self.email = self._set_email(self.email)
        self.created_at = self._set_created_at(self.created_at)
        self.updated_at = self._set_updated_at(self.updated_at)