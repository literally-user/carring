from uuid import UUID

from src.domain.offer import Offer, OfferStatus
from .exceptions import UnitsNotFoundError

class ExpireOfferInteractor:
    def __init__(self, uow) -> None:
        self.uow = uow

    def execute(self, car_uuid: UUID, user_uuid: UUID, offer_uuid: UUID) -> Offer:
        offer = self.uow.offer_repository.get_by_uuid(offer_uuid)
        car = self.uow.car_repository.get_by_uuid(car_uuid)
        user = self.uow.user_repository.get_by_uuid(user_uuid)

        if not user and not car and not offer:
            raise UnitsNotFoundError("Car or user not found")

        offer.set_user_uuid(None)
        offer.set_car_uuid(None)
        offer.set_offer_status(OfferStatus.EXPIRED)

        car.set_offer_uuid(None)
        user.set_offer_uuid(None)

        self.uow.offer_repository.update(offer)
        self.uow.car_repository.update(car)
        self.uow.user_repository.update(user)

        self.uow.commit()

        return offer