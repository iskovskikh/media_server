import pytest
from faker import Faker

from domain.exceptions.user import PasswordTooLongException, \
    PasswordTooShortException, PasswordWrongFormatException
from domain.values.user import Password


def test_create_password_success(faker: Faker):
    text = faker.bothify(text='###???')
    login = Password(text)

    assert login.as_generic_type() == text


def test_create_password_failed(faker: Faker):
    with pytest.raises(PasswordTooShortException):
        Password('')
    with pytest.raises(PasswordTooLongException):
        Password(faker.lexify(text='?' * 10))


def test_create_password_format_failed(faker: Faker):
    with pytest.raises(PasswordWrongFormatException):
        Password(faker.bothify(text='####'))
    with pytest.raises(PasswordWrongFormatException):
        Password(faker.bothify(text='????'))
