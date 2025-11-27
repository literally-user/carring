from uuid import UUID
from datetime import datetime, UTC
from sqlalchemy import text

from carring.application.common.repositories import UserRepository
from carring.domain.user import User


class UserRepositoryImpl(UserRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> User | None:
        result = self.connection.execute(
            text("""
                SELECT *
                FROM users
                WHERE user_uuid = :user_uuid
            """),
            {"user_uuid": str(uuid)}
        )

        row = result.fetchone()
        if row is None:
            return None

        return User(**dict(row))

    def create(self, user: User) -> None:
        self.connection.execute(
            text("""
                INSERT INTO users (
                    user_uuid,
                    user_privilege,
                    user_state,
                    first_name,
                    last_name,
                    username,
                    password,
                    email,
                    created_at,
                    updated_at,
                    offer_uuid
                )
                VALUES (
                    :user_uuid,
                    :user_privilege,
                    :user_state,
                    :first_name,
                    :last_name,
                    :username,
                    :password,
                    :email,
                    :created_at,
                    :updated_at,
                    :offer_uuid
                )
            """),
            {
                "user_uuid": str(user.user_uuid),
                "user_privilege": user.user_privilege.value,
                "user_state": user.user_state.value,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "offer_uuid": str(user.offer_uuid) if user.offer_uuid else None,
            }
        )

    def update(self, user: User) -> None:
        self.connection.execute(
            text("""
                UPDATE users
                SET
                    user_privilege = :user_privilege,
                    user_state     = :user_state,
                    first_name     = :first_name,
                    last_name      = :last_name,
                    username       = :username,
                    password       = :password,
                    email          = :email,
                    updated_at     = :updated_at,
                    offer_uuid     = :offer_uuid
                WHERE user_uuid = :user_uuid
            """),
            {
                "user_uuid": str(user.user_uuid),
                "user_privilege": user.user_privilege.value,
                "user_state": user.user_state.value,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "updated_at": datetime.now(UTC),
                "offer_uuid": str(user.offer_uuid) if user.offer_uuid else None,
            }
        )

    def delete(self, user: User) -> None:
        self.connection.execute(
            text("""
                DELETE FROM users
                WHERE user_uuid = :user_uuid
            """),
            {"user_uuid": str(user.user_uuid)}
        )
