from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.user import User


class UserRepository(Protocol):
    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass