from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.events.user import NewUserCreatedEvent, UserUpdatedEvent
from domain.values.user import Login, Password


@dataclass(eq=False)
class User(BaseEntity):
    login: Login
    password: Password
    full_name: str
    company: str
    position: str

    @classmethod
    def create_user(
            cls,
            login: str,
            password: str,
            full_name: str,
            company: str,
            position: str
    ) -> 'User':
        new_user = cls(
            login=Login(login),
            password=Password.hash_password(password),
            full_name=full_name,
            company=company,
            position=position,
        )
        new_user.register_event(NewUserCreatedEvent(oid=new_user.oid, login=new_user.login.as_generic_type()))
        return new_user

    def user_update(
            self,
            login: str,
            password: str,
            full_name: str,
            company: str,
            position: str
    ) -> 'User':
        self.login = Login(login)
        self.password = Password.hash_password(password)
        self.full_name = full_name
        self.company = company
        self.position = position

        self.register_event(UserUpdatedEvent(
            oid=self.oid,
            login=self.login.as_generic_type(),
            full_name=self.full_name,
            company=self.company,
            position=self.position,
        ))

        return self
