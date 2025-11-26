from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from carring.domain.car import Car


class CarRepository(Protocol):
    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Car:
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