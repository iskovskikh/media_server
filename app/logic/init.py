from functools import lru_cache

from punq import Container, Scope
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from infrastructure.repositories.user.base import BaseUserRepository
from infrastructure.repositories.user.memory import MemoryUserRepository
from infrastructure.repositories.user.postgres import PostgresUserRepository
from logic.mediator import Mediator
from logic.queries.user import GetUsersQueryHandler, GetUsersQuery
from settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)
    config: Config = container.resolve(Config)


    def create_postgresql_session_maker():
        engine: AsyncEngine = create_async_engine(url=config.postgresql_connection_uri)
        session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
        return session_maker

    container.register(AsyncSession, factory=create_postgresql_session_maker)

    async_session = container.resolve(AsyncSession)

    def init_user_postgres_repository() -> PostgresUserRepository:
        return PostgresUserRepository(
            async_session=async_session
        )

    def init_user_memory_repository() -> MemoryUserRepository:
        return MemoryUserRepository()

    container.register(BaseUserRepository, factory=init_user_memory_repository, scope=Scope.singleton)

    container.register(GetUsersQueryHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_query(
            query=GetUsersQuery,
            query_handler=container.resolve(GetUsersQueryHandler)
        )
        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
