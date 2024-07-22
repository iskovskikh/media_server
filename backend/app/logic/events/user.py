import logging
from dataclasses import dataclass

from domain.events.user import NewUserCreatedEvent, UserUpdatedEvent
from logic.events.base import EventHandler

logget = logging.getLogger(__name__)


@dataclass()
class NewUserCreatedEventHandler(EventHandler[NewUserCreatedEvent, None]):

    def handle(self, event: NewUserCreatedEvent) -> None:
        logget.info(f'Пользователь {event.login} ({event.oid}) создан')


class UserUpdatedEventHandler(EventHandler[UserUpdatedEvent, None]):

    def handle(self, event: UserUpdatedEvent) -> None:
        logget.info(f'Пользователь {event.login} ({event.oid}) обновлен')
