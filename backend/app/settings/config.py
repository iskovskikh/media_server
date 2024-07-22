from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    postgresql_connection_uri: str = Field(
        default="postgresql+asyncpg://postgres:password@localhost:5432/postgres",
        alias='POSTGRES_DB_URL',
    )
