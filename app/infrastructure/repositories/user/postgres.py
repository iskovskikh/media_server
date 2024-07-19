from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from application.api.user.filters import GetUsersFilters
from domain.entities.user import User
from infrastructure.repositories.models.user import UserModel
from infrastructure.repositories.user.base import BaseUserRepository


@dataclass
class BasePostgresRepository:
    async_session: AsyncSession


@dataclass
class PostgresUserRepository(BasePostgresRepository, BaseUserRepository):

    async def add_user(self, user: User) -> None:
        ...

    async def check_user_exists_by_login(self, login: str) -> bool:
        ...

    async def get_user_by_oid(self, oid: str) -> User | None:
        ...

    async def get_user_list(self, filters: GetUsersFilters) -> tuple[Iterable[User], int]:
        async with self.async_session as session:
            statement = select(UserModel).order_by(UserModel.login.desc()).limit(filters.limit).offset(filters.offset)

            count = session.query(func.count(User.oid)).scalar()

            users = session.query(User)\
                .order_by(UserModel.login.desc())\
                .limit(filters.limit)\
                .offset(filters.offset).scalar()

            return users, count
