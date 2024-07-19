from pydantic import BaseModel

from application.api.schemas import BaseQueryResponseSchema
from domain.entities.user import User


class UserDetailSchema(BaseModel):
    oid: str
    login: str
    password: str
    bio: str
    company: str
    position: str

    @classmethod
    def from_entity(cls, user: User) -> 'UserDetailSchema':
        return cls(
            oid=user.oid,
            login=user.login.as_generic_type(),
            password=user.password.as_generic_type(),
            bio=user.bio,
            company=user.company,
            position=user.position
        )


class GetUsersQueryResponseSchema(BaseQueryResponseSchema[list[UserDetailSchema]]):
    ...


class EditUserResponseSchema(BaseModel):
    ...