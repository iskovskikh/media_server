from dataclasses import dataclass
from typing import Iterable

from domain.entities.user import User
from domain.values.user import Login, Password
from infrastructure.repositories.filters.user import GetUsersFilters
from infrastructure.repositories.user.base import BaseUserRepository
from logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetUserDetailQuery(BaseQuery):
    filters: GetUsersFilters


@dataclass(frozen=True)
class GetUsersQuery(BaseQuery):
    filters: GetUsersFilters


@dataclass(frozen=True)
class GetUsersQueryHandler(BaseQueryHandler):
    user_repository: BaseUserRepository

    async def handle(self, query: GetUsersQuery) -> tuple[Iterable[User], int]:
        await self.user_repository.add_user(User(
            login=Login('123'),
            password=Password('pass1234'),
            bio='bio', company='company',
            position='position')
        )  # Добавим пользователя чтобы swagger что-то отдавал

        return await self.user_repository.get_user_list(
            filters=query.filters
        )
