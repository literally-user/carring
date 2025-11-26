from uuid import UUID

from carring.application.common.repositories import OfferRepository
from carring.domain.offer import Offer


class OfferRepositoryImpl(OfferRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> Offer | None:
        pass

    def create(self, offer: Offer) -> None:
        pass

    def update(self, offer: Offer) -> None:
        pass

    def delete(self, offer: Offer) -> None:
        pass