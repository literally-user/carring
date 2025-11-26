from datetime import datetime, timedelta
from dataclasses import dataclass
from uuid import UUID

from .enumerations import OfferStatus

@dataclass
class Offer:
    offer_uuid: UUID

    car_uuid: UUID
    user_uuid: UUID

    offer_status: OfferStatus
    expiration_date: datetime

    created_at: datetime
    updated_at: datetime

    def start_renting(self, car_uuid: UUID, user_uuid: UUID) -> None:
        self._set_car_uuid(car_uuid)
        self._set_user_uuid(user_uuid)

    def expire(self) -> None:
        self._set_offer_status(OfferStatus.EXPIRED)

    def extend(self, extend_time: timedelta) -> None:
        self.expiration_date += extend_time

    def _set_created_at(self, created_at: datetime) -> None:
        self.created_at = created_at

    def _set_updated_at(self, updated_at: datetime) -> None:
        self.updated_at = updated_at

    def _set_expiration_date(self, expiration_date: datetime) -> None:
        self.expiration_date = expiration_date

    def _set_offer_status(self, offer_status: OfferStatus) -> None:
        self.offer_status = offer_status

    def _set_car_uuid(self, car_uuid: UUID) -> None:
        self.car_uuid = car_uuid

    def _set_user_uuid(self, user_uuid: UUID) -> None:
        self.user_uuid = user_uuid

    def _set_offer_uuid(self, offer_uuid: UUID) -> None:
        self.offer_uuid = offer_uuid

    def __post_init__(self) -> None:
        self._set_created_at(self.created_at)
        self._set_updated_at(self.updated_at)
        self._set_expiration_date(self.expiration_date)
        self._set_offer_status(self.offer_status)
        self._set_car_uuid(self.car_uuid)
        self._set_user_uuid(self.user_uuid)
        self._set_offer_uuid(self.offer_uuid)