from datetime import datetime, UTC
from uuid import UUID
from typing import Iterable
from sqlalchemy import Connection, text

from carring.application.common.repositories import CarRepository
from carring.domain.car import Car, FilterBy


class CarRepositoryImpl(CarRepository):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> Car | None:
        result = self.connection.execute(
            text("SELECT * FROM cars WHERE uuid = :uuid"),
            {"uuid": str(uuid)}
        )

        row = result.fetchone()
        if row is None:
            return None

        return Car(**dict(row))

    def filter_by(self, filter_by_param: FilterBy) -> Iterable[Car] | None:
        conditions = []
        params = {}

        if filter_by_param.car_class is not None:
            conditions.append("car_class = :car_class")
            params["car_class"] = filter_by_param.car_class.value  # если Enum

        if filter_by_param.car_status is not None:
            conditions.append("car_status = :car_status")
            params["car_status"] = filter_by_param.car_status.value

        if filter_by_param.min_price is not None:
            conditions.append("price >= :min_price")
            params["min_price"] = filter_by_param.min_price

        if filter_by_param.max_price is not None:
            conditions.append("price <= :max_price")
            params["max_price"] = filter_by_param.max_price

        where_clause = ""
        if conditions:
            where_clause = " WHERE " + " AND ".join(conditions)

        query = text(f"""
            SELECT id, model, car_class, car_status, price
            FROM cars
            {where_clause}
        """)

        result = self.connection.execute(query, params)
        rows = result.fetchall()

        return [Car(**dict(row)) for row in rows]

    def create(self, car: Car) -> None:
        query = text("""
                     INSERT INTO cars (car_uuid,
                                       car_model,
                                       car_number,
                                       car_status,
                                       car_class,
                                       created_at,
                                       updated_at,
                                       offer_uuid)
                     VALUES (:car_uuid,
                             :car_model,
                             :car_number,
                             :car_status,
                             :car_class,
                             :created_at,
                             :updated_at,
                             :offer_uuid)
                     """)

        params = {
            "car_uuid": str(car.car_uuid),
            "car_model": car.car_model,
            "car_number": car.car_number,
            "car_status": car.car_status.value,
            "car_class": car.car_class.value,
            "created_at": car.created_at,
            "updated_at": car.updated_at,
            "offer_uuid": str(car.offer_uuid) if car.offer_uuid else None,
        }

        self.connection.execute(query, params)

    def update(self, car: Car) -> None:
        query = text("""
                     UPDATE cars
                     SET car_model  = :car_model,
                         car_number = :car_number,
                         car_status = :car_status,
                         car_class  = :car_class,
                         updated_at = :updated_at,
                         offer_uuid = :offer_uuid
                     WHERE car_uuid = :car_uuid
                     """)

        params = {
            "car_uuid": str(car.car_uuid),
            "car_model": car.car_model,
            "car_number": car.car_number,
            "car_status": car.car_status.value,
            "car_class": car.car_class.value,
            "updated_at": datetime.now(UTC),  # обычно обновляется при update
            "offer_uuid": str(car.offer_uuid) if car.offer_uuid else None,
        }

        self.connection.execute(query, params)

    def delete(self, car: Car) -> None:
        query = text("""
                     DELETE
                     FROM cars
                     WHERE car_uuid = :car_uuid
                     """)

        self.connection.execute(query, {"car_uuid": str(car.car_uuid)})
