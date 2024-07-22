from functools import lru_cache

from punq import Container, Scope
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from domain.events.user import NewUserCreatedEvent, UserUpdatedEvent
from infrastructure.repositories.user.base import BaseUserRepository
from infrastructure.repositories.user.postgres import PostgresUserRepository
from logic.commands.user import UpdateUserCommandHandler, UpdateUserCommand, CreateUserCommandHandler, CreateUserCommand
from logic.events.user import NewUserCreatedEventHandler, UserUpdatedEventHandler
from logic.mediator.base import Mediator
from logic.queries.user import GetUsersQueryHandler, GetUsersQuery, GetUserDetailQueryHandler, GetUserDetailQuery
from settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # config
    container.register(Config, instance=Config(), scope=Scope.singleton)
    config: Config = container.resolve(Config)

    # db
    def create_postgresql_session_maker():
        engine: AsyncEngine = create_async_engine(url=config.postgresql_connection_uri, echo=True)
        session_maker = async_sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
        return session_maker

    # @todo вынести в db_helper???
    container.register(AsyncSession, factory=create_postgresql_session_maker)

    async_session = container.resolve(AsyncSession)

    # repos
    def init_user_postgres_repository() -> PostgresUserRepository:
        return PostgresUserRepository(async_session=async_session)

    container.register(BaseUserRepository, factory=init_user_postgres_repository, scope=Scope.singleton)

    # command handlers
    container.register(CreateUserCommandHandler)
    container.register(UpdateUserCommandHandler)

    # query handlers
    container.register(GetUsersQueryHandler)
    container.register(GetUserDetailQueryHandler)

    # mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        # events
        mediator.register_event(
            NewUserCreatedEvent,
            [NewUserCreatedEventHandler(), ],
        )
        mediator.register_event(
            UserUpdatedEvent,
            [UserUpdatedEventHandler(), ],
        )

        # command handlers
        create_user_handler = CreateUserCommandHandler(
            _mediator=mediator,
            user_repository=container.resolve(BaseUserRepository),
        )

        update_user_handler = UpdateUserCommandHandler(
            _mediator=mediator,
            user_repository=container.resolve(BaseUserRepository),
        )

        # commands
        mediator.register_command(
            CreateUserCommand,
            [create_user_handler]
        )
        mediator.register_command(
            UpdateUserCommand,
            [update_user_handler]
        )

        # queries
        mediator.register_query(
            GetUsersQuery,
            container.resolve(GetUsersQueryHandler)
        )
        mediator.register_query(
            GetUserDetailQuery,
            container.resolve(GetUserDetailQueryHandler)
        )

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
