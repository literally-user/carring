from datetime import timedelta
from uuid import UUID

from carring.domain.offer import Offer, OfferStatus
from carring.application.common.repositories import OfferRepository, CarRepository
from .exceptions import UnitsNotFoundError, OfferExpired

class ExtendOfferInteractor:
    def __init__(self, offer_repository: OfferRepository, car_repository: CarRepository) -> None:
        self.offer_repository = offer_repository
        self.car_repository = car_repository

    def execute(self, offer_uuid: UUID, extend_time: timedelta) -> Offer:
        offer = self.offer_repository.get_by_uuid(offer_uuid)
        car = self.car_repository.get_by_uuid(offer.car_uuid)

        if offer.offer_status == OfferStatus.EXPIRED:
            raise OfferExpired("Offer expired")

        if not offer:
            raise UnitsNotFoundError("Offer not found")

        offer.extend(extend_time)
        offer.calculate_price(car.car_class)

        self.offer_repository.update(offer)

        return offer