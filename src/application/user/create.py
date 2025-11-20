from datetime import datetime, UTC
from uuid import uuid4

from src.domain.user import User, UserPrivilege, UserState
from .dto import UserDTO

class CreateUserInteractor:
    def __init__(self, repository) -> None:
        self.repository = repository

    def execute(self, user: UserDTO) -> User:
        user_model = User(
            user_uuid=uuid4(),

            first_name=user.first_name,
            last_name=user.last_name,

            offer_uuid=None,

            username=user.username,
            password=user.password,
            email=user.email,

            user_privilege=UserPrivilege.USER,
            user_state=UserState.ACTIVE,

            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )
        return self.repository.create(user_model)