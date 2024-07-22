from dataclasses import dataclass
from typing import Iterable

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from application.api.user.filters import GetUsersFilters
from domain.entities.user import User
from infrastructure.repositories.models.user import UserModel
from infrastructure.repositories.user.base import BaseUserRepository
from infrastructure.repositories.user.converters import convert_user_entity_to_model, convert_user_model_to_entity


@dataclass
class BasePostgresRepository:
    async_session: AsyncSession  # @ todo поправить хинтинг


@dataclass
class PostgresUserRepository(BasePostgresRepository, BaseUserRepository):

    async def add_user(self, user: User) -> None:
        async with self.async_session() as session:
            session.add(convert_user_entity_to_model(user))
            await session.commit()

    async def update_user(self, user: User) -> None:
        async with self.async_session() as session:
            user_model = await session.get(UserModel, user.oid)

            user_model.login = user.login.as_generic_type()
            user_model.password = user.password.as_generic_type()
            user_model.full_name = user.full_name
            user_model.company = user.company
            user_model.position = user.position

            await session.commit()

    async def check_user_exists_by_login(self, login: str) -> bool:
        async with self.async_session() as session:
            statement = select(UserModel).where(UserModel.login == login)
            result = await session.execute(statement)
            user = result.scalars().one_or_none()

            return bool(user)

    async def get_user_by_login(self, login: str) -> User | None:
        async with self.async_session() as session:
            statement = select(UserModel).where(UserModel.login == login)
            result = await session.execute(statement)
            user = result.scalars().one_or_none()

            if user:
                return convert_user_model_to_entity(user)

            return None

    async def get_user_by_oid(self, oid: str) -> User | None:
        async with self.async_session() as session:
            statement = select(UserModel).where(UserModel.oid == oid)
            result = await session.execute(statement)
            user = result.scalars().one_or_none()

            if user:
                return convert_user_model_to_entity(user)

            return None

    async def get_user_list(self, filters: GetUsersFilters) -> tuple[Iterable[User], int]:
        async with self.async_session() as session:
            statement = select(UserModel) \
                .order_by(UserModel.login.asc()) \
                .limit(filters.limit) \
                .offset(filters.offset)

            raw_users = await session.scalars(statement)

            user_list = [
                convert_user_model_to_entity(user)
                for user in raw_users
            ]

            count_statement = select(func.count(UserModel.oid))
            count = await session.scalar(count_statement)

            return user_list, count
