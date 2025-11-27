from dataclasses import dataclass

from carring.domain.car import CarClass


@dataclass(frozen=True, slots=True)
class CarDTO:
    car_class: CarClass
    car_model: str
    car_number: str