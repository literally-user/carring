from typing import Protocol
from abc import abstractmethod
from uuid import UUID

from src.domain.user import User

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

class UserRepositoryImpl(UserRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> User | None:
        pass

    def create(self, user: User) -> None:
        pass

    def update(self, user: User) -> None:
        pass

    def delete(self, user: User) -> None:
        pass