from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CarDTO:
    car_model: str
    car_number: str