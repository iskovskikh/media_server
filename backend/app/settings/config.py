from pathlib import Path

from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent


class JWTSettings(BaseModel):
    private_key_path: Path = BASE_DIR / 'certs' / 'private.pem'
    public_key_path: Path = BASE_DIR / 'certs' / 'public.pem'
    algorithm: str = 'RS256'


class Config(BaseSettings):
    postgresql_connection_uri: str = Field(
        default="postgresql+asyncpg://postgres:password@localhost:5432/postgres",
        alias='POSTGRES_DB_URL',
    )

    jwt: JWTSettings = JWTSettings()
