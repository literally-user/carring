from dataclasses import dataclass
from datetime import datetime
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

    def expire(self):
        self._set_offer_status(OfferStatus.EXPIRED)

    def _set_created_at(self, created_at: datetime) -> datetime:
        self.created_at = created_at
        return self.created_at

    def _set_updated_at(self, updated_at: datetime) -> datetime:
        self.updated_at = updated_at
        return self.updated_at

    def _set_expiration_date(self, expiration_date: datetime) -> datetime:
        self.expiration_date = expiration_date
        return self.expiration_date

    def _set_offer_status(self, offer_status: OfferStatus) -> OfferStatus:
        self.offer_status = offer_status
        return self.offer_status

    def _set_car_uuid(self, car_uuid: UUID) -> UUID:
        self.car_uuid = car_uuid
        return self.car_uuid

    def _set_user_uuid(self, user_uuid: UUID) -> UUID:
        self.user_uuid = user_uuid
        return self.user_uuid

    def _set_offer_uuid(self, offer_uuid: UUID) -> UUID:
        self.offer_uuid = offer_uuid
        return self.offer_uuid

    def __post_init__(self) -> None:
        self.created_at = self._set_created_at(self.created_at)
        self.updated_at = self._set_updated_at(self.updated_at)
        self.expiration_date = self._set_expiration_date(self.expiration_date)
        self.offer_status = self._set_offer_status(self.offer_status)
        self.car_uuid = self._set_car_uuid(self.car_uuid)
        self.user_uuid = self._set_user_uuid(self.user_uuid)
        self.offer_uuid = self._set_offer_uuid(self.offer_uuid)