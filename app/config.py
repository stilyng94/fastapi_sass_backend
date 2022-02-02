from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_NAME: str
    title: str
    description: str

    class Config:
        env_file = ".env"


settings = Settings()
