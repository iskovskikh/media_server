from dataclasses import dataclass

from domain.events.base import BaseEvent


@dataclass(frozen=True)
class NewUserCreatedEvent(BaseEvent):
    oid: str
    login: str


@dataclass(frozen=True)
class UserUpdatedEvent(BaseEvent):
    oid: str
    login: str
    full_name: str
    company: str
    position: str
