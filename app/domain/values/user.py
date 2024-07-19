from dataclasses import dataclass

from domain.exceptions.user import LoginTooLongException, LoginTooShortException, PasswordTooShortException, \
    PasswordTooLongException, PasswordWrongFormatException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Login(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) < 3:
            raise LoginTooShortException(self.value)

        if len(self.value) > 255:
            raise LoginTooLongException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Password(BaseValueObject):
    value: str

    def validate(self):

        if len(self.value) < 3:
            raise PasswordTooShortException()

        if len(self.value) > 8:
            raise PasswordTooLongException()

        if not any(map(str.isdigit, self.value)) and     any(map(str.isalpha, self.value)):
            raise PasswordWrongFormatException()

    def as_generic_type(self) -> str:
        return str('******')
