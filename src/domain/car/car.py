from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from .enumerations import CarStatus

@dataclass
class Car:
    car_uuid: UUID

    car_model: str

    car_status: CarStatus

    created_at: datetime
    updated_at: datetime

    offer_uuid: Optional[UUID] = None


    def set_uuid(self, uuid: UUID) -> UUID:
        self.car_uuid = uuid
        return self.car_uuid

    def set_car_model(self, model: str) -> str:
        self.car_model = model
        return self.car_model

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