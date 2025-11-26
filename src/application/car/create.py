from datetime import datetime, UTC
from uuid import uuid4

from src.domain.car import Car, CarStatus
from src.adapters.storage.car import CarRepository
from .dto import CarDTO


class CreateCarInteractor:
    def __init__(self, repository: CarRepository) -> None:
        self.repository = repository

    def execute(self, car: CarDTO) -> Car:
        car_model = Car(
            car_uuid=uuid4(),

            car_model=car.car_model,
            car_number=car.car_number,
            car_status=CarStatus.FREE,

            offer_uuid=None,

            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )
        self.repository.create(car_model)

        return car_model