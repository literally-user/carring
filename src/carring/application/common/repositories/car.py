from typing import Protocol, Iterable
from abc import abstractmethod
from uuid import UUID

from carring.domain.car import Car, FilterBy


class CarRepository(Protocol):
    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Car:
        pass

    @abstractmethod
    def filter_by(self, filter_by_param: FilterBy) -> Iterable[Car] | None:
        pass

    @abstractmethod
    def create(self, car: Car) -> None:
        pass

    @abstractmethod
    def update(self, car: Car) -> None:
        pass

    @abstractmethod
    def delete(self, car: Car) -> None:
        pass