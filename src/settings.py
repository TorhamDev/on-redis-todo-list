from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "TestSecret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"


def get_settings():
    return Settings()