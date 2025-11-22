from uuid import UUID

from .exceptions import UnitsNotFoundError
from src.domain.offer import Offer

class ExpireOfferInteractor:
    def __init__(self, offer_repository) -> None:
        self.offer_repository = offer_repository

    def execute(self, offer_uuid: UUID) -> Offer:
        offer = self.offer_repository.get_by_uuid(offer_uuid)

        if not offer:
            raise UnitsNotFoundError(f"Offer {offer_uuid} not found")

        offer.expire()
        self.offer_repository.update(offer)

        return offer