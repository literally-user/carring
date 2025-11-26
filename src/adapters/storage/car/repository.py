from typing import Protocol
from abc import abstractmethod
from uuid import UUID

from src.domain.car import Car

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

class CarRepositoryImpl(CarRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> Car | None:
        pass

    def create(self, car: Car) -> None:
        pass

    def update(self, car: Car) -> None:
        pass

    def delete(self, car: Car) -> None:
        pass