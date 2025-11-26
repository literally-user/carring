import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from .enumerations import (UserPrivilege,
                           UserState, )
from .exceptions import (UsernameFormatInvalid,
                         PasswordFormatInvalid,
                         EmailFormatInvalid,
                         UserStateInvalid,
                         FirstNameFormatInvalid,
                         LastNameFormatInvalid)


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

    def _set_user_privilege(self, privilege: UserPrivilege) -> None:
        self.user_privilege = privilege

    def _set_user_state(self, state: UserState) -> None:
        if state != UserState.ACTIVE:
            raise UserStateInvalid("The user must be created with the state ACTIVE only.")
        self.user_state = state

    def _set_user_uuid(self, uuid: UUID) -> None:
        self.user_uuid = uuid

    def _set_first_name(self, first_name: str) -> None:
        if len(first_name) < 3 or len(first_name) > 12:
            raise FirstNameFormatInvalid("The first name must be at least 3 and less than 12 characters long.")
        self.first_name = first_name

    def _set_last_name(self, last_name: str) -> None:
        if len(last_name) < 3 or len(last_name) > 12:
            raise LastNameFormatInvalid("The last name must be at least 3 and less than 12 characters long.")
        self.last_name = last_name

    def _set_username(self, username: str) -> None:
        if len(username) < 5 or len(username) > 13:
            raise UsernameFormatInvalid("Username must be over then 5 and less then 13 characters long")
        for i in username:
            if not i.isascii():
                raise UsernameFormatInvalid("Username must contain only ASCII characters")
        self.username = username

    def _set_password(self, password: str) -> None:
        if len(password) < 8 or len(password) > 25:
            raise PasswordFormatInvalid("Password must be over then 8 and less then 25 characters long")
        for i in password:
            if not i.isascii():
                raise PasswordFormatInvalid("Password must contain only ASCII characters")
        self.password = password

    def _set_email(self, email: str) -> None:
        if not re.search( r'^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$', email):
            raise EmailFormatInvalid("Email address format is invalid")
        self.email = email
        return self.email

    def _set_created_at(self, created_at: datetime) -> None:
        self.created_at = created_at

    def _set_updated_at(self, updated_at: datetime) -> None:
        self.updated_at = updated_at

    def _set_offer_uuid(self, offer_uuid: UUID | None) -> None:
        self.offer_uuid = offer_uuid


    def __post_init__(self) -> None:
        self._set_user_uuid(self.user_uuid)
        self._set_first_name(self.first_name)
        self._set_last_name(self.last_name)
        self._set_username(self.username)
        self._set_password(self.password)
        self._set_email(self.email)
        self._set_created_at(self.created_at)
        self._set_updated_at(self.updated_at)