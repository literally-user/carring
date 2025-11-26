from typing import Protocol
from abc import abstractmethod
from uuid import UUID

from src.domain.offer import Offer

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