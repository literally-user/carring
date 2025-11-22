from typing import Protocol, TypeVar
from abc import abstractmethod
from uuid import UUID

T = TypeVar('T')

class Repository(Protocol):
    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> T | None:
        pass

    @abstractmethod
    def remove(self, model: T) -> None:
        pass

    @abstractmethod
    def create(self, model: T) -> None:
        pass

    @abstractmethod
    def update(self, model: T) -> None:
        pass