from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID
import re

from .enumerations import CarStatus
from .exceptions import PlateNumberFormatInvalid

@dataclass
class Car:
    car_uuid: UUID

    car_model: str
    car_number: str

    car_status: CarStatus

    created_at: datetime
    updated_at: datetime

    offer_uuid: Optional[UUID] = None


    def set_car_uuid(self, uuid: UUID) -> UUID:
        self.car_uuid = uuid
        return self.car_uuid

    def set_car_model(self, model: str) -> str:
        self.car_model = model
        return self.car_model

    def set_car_number(self, number: str) -> str:
        RUS_LETTERS = "АВЕКМНОРСТУХ"

        pattern = re.compile(
            rf"^[{RUS_LETTERS}]\d{{3}}[{RUS_LETTERS}]{{2}}\s?\d{{2,3}}$"
        )

        if pattern.match(number):
            self.car_number = number
            return self.car_number

        raise PlateNumberFormatInvalid("Invalid plate number format")

    def set_car_status(self, state: CarStatus) -> CarStatus:
        self.car_status = state
        return self.car_status

    def set_created_at(self, created_at: datetime) -> datetime:
        self.created_at = created_at
        return self.created_at

    def set_updated_at(self, updated_at: datetime) -> datetime:
        self.updated_at = updated_at
        return self.updated_at

    def set_offer_uuid(self, offer_uuid: UUID) -> UUID:
        self.offer_uuid = offer_uuid
        return self.offer_uuid

    def __post_init__(self) -> None:
        self.updated_at = self.set_updated_at(self.updated_at)
        self.created_at = self.set_created_at(self.created_at)

        self.offer_uuid = self.set_offer_uuid(self.offer_uuid)
        self.car_uuid = self.set_car_uuid(self.car_uuid)

        self.car_status = self.set_car_status(self.car_status)
        self.car_model = self.set_car_model(self.car_model)
        self.car_number = self.set_car_number(self.car_number)