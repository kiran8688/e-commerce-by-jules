from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration object.

    Why this exists:
    - Keeps secrets out of source code.
    - Gives one canonical place for DB, JWT, and app settings.
    - Reads from environment variables and .env automatically.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    PROJECT_NAME: str = "E-Commerce API"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = Field(..., description="PostgreSQL connection string")

    JWT_SECRET_KEY: str = Field(..., description="JWT signing key")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
