from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from domain.events.base import BaseEvent
from logic.commands.base import CommandHandler, CT, CR, BaseCommand
from logic.events.base import EventHandler, ET, ER
from logic.exceptions.mediator import EventHandlersNotRegisteredException, CommandHandlersNotRegisteredException
from logic.queries.base import QT, BaseQueryHandler, QR, BaseQuery


@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, list[EventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    commands_map: dict[CT, list[CommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    queries_map: dict[QT, BaseQueryHandler] = field(
        default_factory=dict,
        kw_only=True
    )

    def register_event(self, event: type[ET], event_handlers: Iterable[EventHandler[ET, ER]]):
        self.events_map[event].extend(event_handlers)

    def register_command(self, command: type[CT], command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.commands_map[command].extend(command_handlers)

    def register_query(self, query: type[QT], query_handler: BaseQueryHandler[QT, QR]):
        self.queries_map[query] = query_handler

    async def publish(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        event_type = events.__class__
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        result = []
        for event in events:
            result.extend([await handler.handle(event) for handler in handlers])

        return result

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handle(command) for handler in handlers]

    async def handle_query(self, query: BaseQuery) -> QR:
        return await self.queries_map[query.__class__].handle(query)
