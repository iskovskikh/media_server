from dataclasses import dataclass
from typing import Iterable

from domain.entities.user import User
from infrastructure.repositories.filters.user import GetUsersFilters
from infrastructure.repositories.user.base import BaseUserRepository
from logic.exceptions.user import UserNotFoundException
from logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetUserDetailQuery(BaseQuery):
    user_oid: str


@dataclass(frozen=True)
class GetUserDetailQueryHandler(BaseQueryHandler):
    user_repository: BaseUserRepository

    async def handle(self, query: GetUserDetailQuery) -> User:
        user = await self.user_repository.get_user_by_oid(query.user_oid)

        if not user:
            raise UserNotFoundException(user_oid=query.user_oid)

        return user

@dataclass(frozen=True)
class GetUsersQuery(BaseQuery):
    filters: GetUsersFilters


@dataclass(frozen=True)
class GetUsersQueryHandler(BaseQueryHandler):
    user_repository: BaseUserRepository

    async def handle(self, query: GetUsersQuery) -> tuple[Iterable[User], int]:

        return await self.user_repository.get_user_list(
            filters=query.filters
        )
