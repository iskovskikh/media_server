import pytest
from faker import Faker

from domain.exceptions.user import LoginTooShortException, LoginTooLongException
from domain.values.user import Login


def test_create_login_success(faker: Faker):
    text = faker.text(max_nb_chars=50)
    login = Login(text)

    assert login.as_generic_type() == text


def test_create_login_failed(faker: Faker):
    with pytest.raises(LoginTooShortException):
        Login('')
    with pytest.raises(LoginTooLongException):
        Login(faker.lexify(text='?'*300))
