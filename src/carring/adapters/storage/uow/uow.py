from typing import Any

from carring.application.common.uow import UnitOfWork


class UnitOfWorkImpl(UnitOfWork):
    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass

    def register_dirty(self, model: Any) -> None:
        pass

    def register_clean(self, model: Any) -> None:
        pass

    def register_new(self, model: Any) -> None:
        pass

    def register_delete(self, model: Any) -> None:
        pass