import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from .enumerations import CarStatus
from .exceptions import (PlateNumberFormatInvalid,
                         CarStatusInvalid)


@dataclass
class Car:
    car_uuid: UUID

    car_model: str
    car_number: str

    car_status: CarStatus

    created_at: datetime
    updated_at: datetime

    offer_uuid: Optional[UUID] = None

    def attach_offer(self, offer_uuid: UUID) -> None:
        self._set_offer_uuid(offer_uuid)

    def detach_offer(self) -> None:
        self._set_offer_uuid(None)

    def _set_car_uuid(self, uuid: UUID) -> None:
        self.car_uuid = uuid

    def _set_car_model(self, model: str) -> None:
        self.car_model = model

    def _set_car_number(self, number: str) -> None:
        RUS_LETTERS = "АВЕКМНОРСТУХ"

        pattern = re.compile(
            rf"^[{RUS_LETTERS}]\d{{3}}[{RUS_LETTERS}]{{2}}\s?\d{{2,3}}$"
        )

        if pattern.match(number):
            self.car_number = number

        raise PlateNumberFormatInvalid("Invalid plate number format")

    def _set_car_status(self, status: CarStatus) -> None:
        if status != CarStatus.FREE:
            raise CarStatusInvalid("The car must be created with the status FREE only.")

        self.car_status = status

    def _set_created_at(self, created_at: datetime) -> None:
        self.created_at = created_at

    def _set_updated_at(self, updated_at: datetime) -> None:
        self.updated_at = updated_at

    def _set_offer_uuid(self, offer_uuid: UUID | None) -> None:
        self.offer_uuid = offer_uuid

    def __post_init__(self) -> None:
        self._set_updated_at(self.updated_at)
        self._set_created_at(self.created_at)

        self._set_offer_uuid(self.offer_uuid)
        self._set_car_uuid(self.car_uuid)

        self._set_car_status(self.car_status)
        self._set_car_model(self.car_model)
        self._set_car_number(self.car_number)