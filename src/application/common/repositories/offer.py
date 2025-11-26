from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from domain.offer import Offer


class OfferRepository(Protocol):
    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> Offer:
        pass

    @abstractmethod
    def create(self, offer: Offer) -> None:
        pass

    @abstractmethod
    def update(self, offer: Offer) -> None:
        pass

    @abstractmethod
    def delete(self, offer: Offer) -> None:
        pass