from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class LoginTooShortException(ApplicationException):
    login: str

    @property
    def message(self):
        return f'Логин "{self.login}" слишком короткий'


@dataclass(frozen=True, eq=False)
class LoginTooLongException(ApplicationException):
    login: str

    @property
    def message(self):
        return f'Логин "{self.login}" слишком длинный'


@dataclass(frozen=True, eq=False)
class PasswordTooShortException(ApplicationException):
    @property
    def message(self):
        return f'Пароль слишком короткий'


@dataclass(frozen=True, eq=False)
class PasswordTooLongException(ApplicationException):

    @property
    def message(self):
        return f'Пароль слишком длинный'


@dataclass(frozen=True, eq=False)
class PasswordWrongFormatException(ApplicationException):

    @property
    def message(self):
        return f'Пароль должен содержать буквы и цифры'
