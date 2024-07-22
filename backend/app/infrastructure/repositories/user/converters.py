from domain.entities.user import User
from domain.values.user import Login, Password
from infrastructure.repositories.models import UserModel


def convert_user_entity_to_model(user: User) -> UserModel:
    return UserModel(
        oid=user.oid,
        login=user.login.as_generic_type(),
        password=user.password.as_generic_type(),
        full_name=user.full_name,
        company=user.company,
        position=user.position
    )


def convert_user_model_to_entity(user_model: UserModel) -> User:
    return User(
        oid=user_model.oid,
        login=Login(user_model.login),
        password=Password(user_model.password),
        full_name=user_model.full_name,
        company=user_model.company,
        position=user_model.position
    )
