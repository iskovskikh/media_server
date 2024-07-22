from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.repositories.models.base import Base


class UserModel(Base):
    __tablename__ = "users"
    oid: Mapped[str] = mapped_column(primary_key=True)
    login: Mapped[str]
    full_name: Mapped[str]
    password: Mapped[str]
    company: Mapped[str]
    position: Mapped[str]
