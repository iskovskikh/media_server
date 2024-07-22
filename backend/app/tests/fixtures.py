from punq import Container, Scope

from infrastructure.repositories.user.base import BaseUserRepository
from infrastructure.repositories.user.memory import MemoryUserRepository
from logic.init import _init_container


def init_dummy_container() -> Container:
    container = _init_container()
    container.register(BaseUserRepository, MemoryUserRepository, scope=Scope.singleton)

    return container
