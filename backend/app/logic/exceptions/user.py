from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class UserLoginAlreadyExistsException(LogicException):
    login: str

    @property
    def message(self):
        return f'Пользователя с логином "{self.login}" уже существует'


@dataclass(frozen=True, eq=False)
class UserNotFoundException(LogicException):
    user_oid: str

    @property
    def message(self):
        return f'Пользователя с oid "{self.user_oid}" не существует'
