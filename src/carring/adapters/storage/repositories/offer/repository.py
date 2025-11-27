from uuid import UUID
from sqlalchemy import text
from carring.application.common.repositories import OfferRepository
from carring.domain.offer import Offer
from datetime import datetime, UTC


class OfferRepositoryImpl(OfferRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> Offer | None:
        result = self.connection.execute(
            text("""
                SELECT *
                FROM offers
                WHERE offer_uuid = :offer_uuid
            """),
            {"offer_uuid": str(uuid)}
        )

        row = result.fetchone()
        if row is None:
            return None

        return Offer(**dict(row))


    def create(self, offer: Offer) -> None:
        query = text("""
            INSERT INTO offers (
                offer_uuid,
                car_uuid,
                user_uuid,
                offer_status,
                expiration_date,
                created_at,
                updated_at,
                price
            )
            VALUES (
                :offer_uuid,
                :car_uuid,
                :user_uuid,
                :offer_status,
                :expiration_date,
                :created_at,
                :updated_at,
                :price
            )
        """)

        params = {
            "offer_uuid": str(offer.offer_uuid),
            "car_uuid": str(offer.car_uuid),
            "user_uuid": str(offer.user_uuid),
            "offer_status": offer.offer_status.value,
            "expiration_date": offer.expiration_date,
            "created_at": offer.created_at,
            "updated_at": offer.updated_at,
            "price": offer.price,
        }

        self.connection.execute(query, params)


    def update(self, offer: Offer) -> None:
        query = text("""
            UPDATE offers
            SET
                car_uuid        = :car_uuid,
                user_uuid       = :user_uuid,
                offer_status    = :offer_status,
                expiration_date = :expiration_date,
                updated_at      = :updated_at,
                price           = :price
            WHERE offer_uuid = :offer_uuid
        """)

        params = {
            "offer_uuid": str(offer.offer_uuid),
            "car_uuid": str(offer.car_uuid),
            "user_uuid": str(offer.user_uuid),
            "offer_status": offer.offer_status.value,
            "expiration_date": offer.expiration_date,
            "updated_at": datetime.now(UTC),
            "price": offer.price,
        }

        self.connection.execute(query, params)


    def delete(self, offer: Offer) -> None:
        self.connection.execute(
            text("""
                DELETE FROM offers
                WHERE offer_uuid = :offer_uuid
            """),
            {"offer_uuid": str(offer.offer_uuid)}
        )
