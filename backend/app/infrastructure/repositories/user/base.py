from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from domain.entities.user import User
from infrastructure.repositories.filters.user import GetUsersFilters

@dataclass
class BaseUserRepository(ABC):

    @abstractmethod
    async def add_user(self, user: User) -> None:
        ...

    @abstractmethod
    async def update_user(self, user: User) -> None:
        ...

    @abstractmethod
    async def check_user_exists_by_login(self, login: str) -> bool:
        ...

    @abstractmethod
    async def get_user_by_login(self, login: str) -> User | None:
        ...

    @abstractmethod
    async def get_user_by_oid(self, oid: str) -> User | None:
        ...

    @abstractmethod
    async def get_user_list(self, filters: GetUsersFilters) -> tuple[Iterable[User], int]:
        ...
