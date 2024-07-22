from dataclasses import dataclass, asdict

from domain.entities.user import User
from infrastructure.repositories.user.base import BaseUserRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.user import UserNotFoundException, UserLoginAlreadyExistsException


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    login: str
    password: str
    full_name: str
    company: str
    position: str


@dataclass()
class CreateUserCommandHandler(CommandHandler[CreateUserCommand, User]):
    user_repository: BaseUserRepository

    async def handle(self, command: CreateUserCommand) -> User:
        if await self.user_repository.check_user_exists_by_login(command.login):
            raise UserLoginAlreadyExistsException(login=command.login)

        # user = User(
        #     login=Login(command.login),
        #     password=Password(command.password),
        #     full_name=command.full_name,
        #     company=command.company,
        #     position=command.position
        # )

        user = User.create_user(
            **asdict(command)
        )

        await self.user_repository.add_user(user=user)

        # await self._mediator.publish(user.pull_events())

        return user


@dataclass(frozen=True)
class UpdateUserCommand(BaseCommand):
    user_oid: str
    login: str
    password: str
    full_name: str
    company: str
    position: str


@dataclass()
class UpdateUserCommandHandler(CommandHandler[UpdateUserCommand, User]):
    user_repository: BaseUserRepository

    async def handle(self, command: UpdateUserCommand) -> User:
        user = await self.user_repository.get_user_by_oid(command.user_oid)

        if not user:
            raise UserNotFoundException(user_oid=command.user_oid)

        other_user = await self.user_repository.get_user_by_login(command.login)

        if bool(other_user) and other_user.oid != command.user_oid:
            raise UserLoginAlreadyExistsException(login=command.login)

        user.user_update(
            login=command.login,
            password=command.password,
            full_name=command.full_name,
            company=command.company,
            position=command.position,
        )

        await self.user_repository.update_user(user=user)

        # await self._mediator.publish(user.pull_events())

        return user
