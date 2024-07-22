import pytest
from faker import Faker
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response

from domain.entities.user import User
from logic.commands.user import CreateUserCommand
from logic.mediator.base import Mediator


# @ todo 400 нет пользователя с таким oid
@pytest.mark.skip
@pytest.mark.asyncio
async def test_update_success(
        app: FastAPI,
        client: TestClient,
        mediator: Mediator,
        faker: Faker
):
    user: User
    user, *_ = await mediator.handle_command(
        CreateUserCommand(
            login=faker.bothify(text='###???'),
            password=faker.bothify(text='###???'),
            full_name=faker.name(),
            company=faker.text(),
            position=faker.text(),
        )
    )

    url = app.url_path_for('update_user_handler', user_oid=user.oid)
    data = dict(
        password=faker.bothify(text='###???'),
        full_name=faker.name(),
        company=faker.text(),
        position=faker.text(),
    )
    response: Response = client.post(url=url, json=data)
    assert response.is_success, response.text
    json_data = response.json()
    assert json_data['password'] == data['password']
    assert json_data['full_name'] == data['full_name']
    assert json_data['company'] == data['company']
    assert json_data['position'] == data['position']
