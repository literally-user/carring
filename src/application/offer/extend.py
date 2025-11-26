from datetime import timedelta
from uuid import UUID

from domain.offer import Offer
from application.common.repositories import OfferRepository
from .exceptions import UnitsNotFoundError

class ExtendOfferInteractor:
    def __init__(self, offer_repository: OfferRepository) -> None:
        self.offer_repository = offer_repository

    def execute(self, offer_uuid: UUID, extend_time: timedelta) -> Offer:
        offer = self.offer_repository.get_by_uuid(offer_uuid)
        if not offer:
            raise UnitsNotFoundError("Offer not found")

        offer.extend(extend_time)

        self.offer_repository.update(offer)

        return offer