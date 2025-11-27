from typing import Iterable

from carring.domain.car import Car, FilterBy
from carring.application.common.repositories import CarRepository


class FindCarInteractor:
    def __init__(self, car_repository: CarRepository) -> None:
        self.car_repository = car_repository

    def execute(self, filter_by_params: FilterBy) -> Iterable[Car] | None:
        return self.car_repository.filter_by(filter_by_params)