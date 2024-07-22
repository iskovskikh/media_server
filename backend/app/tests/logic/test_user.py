import pytest
from faker import Faker

from domain.entities.user import User
from logic.commands.user import CreateUserCommand
from logic.mediator.base import Mediator


@pytest.mark.asyncio
async def test_create_user_command_success(
        user_repository,
        mediator: Mediator,
        faker: Faker
):
    user: User
    user, *_ = await mediator.handle_command(
        CreateUserCommand(
            login=faker.bothify(text='###???'),
            password=faker.bothify(text='###???'),
            full_name=faker.name(),
            company=faker.text(),
            position=faker.text(),
        )
    )

    assert await user_repository.check_user_exists_by_login(user.login.as_generic_type())
