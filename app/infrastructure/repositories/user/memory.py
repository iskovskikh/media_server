from dataclasses import dataclass, field
from typing import Iterable

from domain.entities.user import User
from infrastructure.repositories.filters.user import GetUsersFilters
from infrastructure.repositories.user.base import BaseUserRepository


@dataclass
class MemoryUserRepository(BaseUserRepository):
    _saved_user_list: list[User] = field(default_factory=list, kw_only=True)

    async def add_user(self, user: User) -> None:
        self._saved_user_list.append(user)

    async def check_user_exists_by_login(self, login: str) -> bool:
        try:
            return bool(next(
                user for user in self._saved_user_list if user.login.as_generic_type() == login
            ))
        except StopIteration:
            return False

    async def get_user_by_oid(self, oid: str) -> User | None:
        try:
            return next(
                user for user in self._saved_user_list if user.oid == oid
            )
        except StopIteration:
            return None

    async def get_user_list(self, filters: GetUsersFilters) -> tuple[Iterable[User], int]:
        # @todo pagination
        return self._saved_user_list, len(self._saved_user_list)
