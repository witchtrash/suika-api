from functools import lru_cache
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn = None

    # Build the Postgres DSN string before validating it
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def create_postgres_dsn(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            path=f'/{values.get("DATABASE_NAME")}',
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


@lru_cache()
def get_test_settings():
    return Settings(_env_file=".env.testing")
