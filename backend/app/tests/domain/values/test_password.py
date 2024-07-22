import pytest
from faker import Faker

from domain.exceptions.user import PasswordTooLongException, \
    PasswordTooShortException, PasswordWrongFormatException
from domain.values.user import Password


def test_create_password_success(faker: Faker):
    text = faker.bothify(text='###???')
    password = Password.create_password(text)

    assert password.validate_password(text)


def test_create_password_failed(faker: Faker):
    with pytest.raises(PasswordTooShortException):
        Password.create_password('')
    with pytest.raises(PasswordTooLongException):
        Password.create_password(faker.lexify(text='?' * 10))


def test_create_password_format_failed(faker: Faker):
    with pytest.raises(PasswordWrongFormatException):
        Password.create_password(faker.bothify(text='####'))
    with pytest.raises(PasswordWrongFormatException):
        Password.create_password(faker.bothify(text='????'))
