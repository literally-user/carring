from datetime import datetime, UTC
from uuid import uuid4, UUID

from src.domain.offer import Offer, OfferStatus
from .exceptions import UnitsNotFoundError
from .dto import OfferDTO

class CreateOfferInteractor:
    def __init__(self, uow, user_repository, car_repository) -> None:
        self.uow = uow
        self.user_repository = user_repository
        self.car_repository = car_repository

    def execute(self, car_uuid: UUID, user_uuid: UUID, offer: OfferDTO) -> Offer:
        car = self.car_repository.get_by_uuid(car_uuid)
        user = self.car_repository.get_by_uuid(user_uuid)

        if not car:
            raise UnitsNotFoundError(f"Car {car_uuid} not found")
        if not user:
            raise UnitsNotFoundError(f"User {user_uuid} not found")

        if car.offer_uuid is not None:
            raise ValueError(f"Car {car_uuid} is already have an offer")
        if user.offer_uuid is not None:
            raise ValueError(f"User {user_uuid} is already have an offer")

        offer_model = Offer(
            offer_uuid=uuid4(),
            car_uuid=car_uuid,
            user_uuid=user_uuid,

            offer_status=OfferStatus.ACTIVE,
            expiration_date=offer.expiration_date,

            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )

        car.attach_offer(offer_model.offer_uuid)
        user.attach_offer(offer_model.offer_uuid)

        self.uow.register_clean(car)
        self.uow.register_clean(user)
        self.uow.register_dirty(car)
        self.uow.register_dirty(user)
        self.uow.register_new(offer)

        self.uow.commit()

        return offer_model