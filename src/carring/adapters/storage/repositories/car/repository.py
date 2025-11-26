from uuid import UUID

from carring.application.common.repositories import CarRepository
from carring.domain.car import Car


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