from typing import Protocol, Any
from abc import abstractmethod


class UnitOfWork(Protocol):
    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def register_dirty(self, model: Any) -> None:
        pass

    @abstractmethod
    def register_clean(self, model: Any) -> None:
        pass

    @abstractmethod
    def register_new(self, model: Any) -> None:
        pass

    @abstractmethod
    def register_delete(self, model: Any) -> None:
        pass