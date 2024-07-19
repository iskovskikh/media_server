import pytest
from punq import Container

from infrastructure.repositories.chat.base import BaseChatRepository
from logic.mediator import Mediator
from tests.fixtures import init_dummy_container


@pytest.fixture(scope='function')
def container() -> Container:
    return init_dummy_container()


@pytest.fixture()
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)


@pytest.fixture()
def chat_repository(container: Container) -> BaseChatRepository:
    return container.resolve(BaseChatRepository)
