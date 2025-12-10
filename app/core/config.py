from pydantic import BaseModel
from functools import lru_cache


class Settings(BaseModel):
    JWT_SECRET: str = "supersecret-change-in-prod"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    PASSWORD_HASH_SCHEME: str = "bcrypt"


@lru_cache
def get_settings() -> Settings:
    return Settings()
