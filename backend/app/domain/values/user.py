from dataclasses import dataclass

import bcrypt

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
    value: bytes

    def as_generic_type(self) -> bytes:
        return self.value

    def get_hidden(self) -> str:
        return '******'

    def validate(self):
        pass

    def validate_password(self, unhashed_password: str) -> bool:
        return bcrypt.checkpw(
            password=unhashed_password.encode(),
            hashed_password=self.value
        )

    @staticmethod
    def validate_unhashed_password(unhashed_password: str):
        if len(unhashed_password) < 3:
            raise PasswordTooShortException()

        if len(unhashed_password) > 8:
            raise PasswordTooLongException()

        if not (any(map(str.isdigit, unhashed_password)) and any(map(str.isalpha, unhashed_password))):
            raise PasswordWrongFormatException()

    @staticmethod
    def hash_password(unhashed_password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(
            password=unhashed_password.encode(),
            salt=salt
        )
        return hashed_password

    @classmethod
    def create_password(cls, unhashed_password: str):

        cls.validate_unhashed_password(unhashed_password)

        hashed_password = cls.hash_password(unhashed_password)

        return cls(hashed_password)
