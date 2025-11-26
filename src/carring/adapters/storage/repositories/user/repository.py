from uuid import UUID

from carring.application.common.repositories import UserRepository
from carring.domain.user import User


class UserRepositoryImpl(UserRepository):
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_by_uuid(self, uuid: UUID) -> User | None:
        pass

    def create(self, user: User) -> None:
        pass

    def update(self, user: User) -> None:
        pass

    def delete(self, user: User) -> None:
        pass