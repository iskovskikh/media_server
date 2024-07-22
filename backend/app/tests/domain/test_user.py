from domain.entities.user import User
from domain.events.user import NewUserCreatedEvent


def test_new_user_events(faker):
    user = User.create_user(
        login=faker.bothify(text='###???'),
        password=faker.bothify(text='###???'),
        full_name=faker.name(),
        company=faker.text(),
        position=faker.text(),
    )

    events = user.pull_events()
    pulled_events = user.pull_events()

    assert not pulled_events, pulled_events
    assert len(events) == 1, events

    new_event = events[0]

    assert isinstance(new_event, NewUserCreatedEvent), new_event
    assert new_event.oid == user.oid
    assert new_event.login == user.login.as_generic_type()
