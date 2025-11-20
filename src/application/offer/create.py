from datetime import datetime, UTC
from uuid import uuid4, UUID

from src.domain.offer import Offer, OfferStatus
from .exceptions import UnitsNotFoundError
from .dto import OfferDTO

class CreateOfferInteractor:
    def __init__(self, uow) -> None:
        self.uow = uow

    def execute(self, car_uuid: UUID, user_uuid: UUID, offer: OfferDTO) -> Offer:
        car = self.uow.cars.get_by_uuid(car_uuid)
        user = self.uow.users.get_by_uuid(user_uuid)

        if not user and not car:
            raise UnitsNotFoundError("Car or user not found")

        offer_model = Offer(
            offer_uuid=uuid4(),
            car_uuid=car_uuid,
            user_uuid=user_uuid,

            offer_status=OfferStatus.ACTIVE,
            expiration_date=offer.expiration_date,

            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )

        car.set_offer_uuid(offer_model.offer_uuid)
        user.set_offer_uuid(offer_model.offer_uuid)

        self.uow.offer_repository.create(offer_model)
        self.uow.car_repository.update(car)
        self.uow.user_repository.update(user)

        self.uow.commit()

        return offer_model