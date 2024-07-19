from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.values.user import Login, Password


@dataclass(eq=False, kw_only=True)
class User(BaseEntity):
    login: Login
    password: Password
    bio: str
    company: str
    position: str

    def set_password(self, password: str) -> None:
        self.password = Password(password)
