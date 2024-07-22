import pytest
from punq import Container

from infrastructure.repositories.user.base import BaseUserRepository
from logic.mediator.base import Mediator
from tests.fixtures import init_dummy_container


@pytest.fixture(scope='function')
def container() -> Container:
    return init_dummy_container()


@pytest.fixture()
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)


@pytest.fixture()
def user_repository(container: Container) -> BaseUserRepository:
    return container.resolve(BaseUserRepository)
