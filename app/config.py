from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_NAME: str
    title: str
    description: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    CELERY_ACCEPT_CONTENT: str
    CELERY_TASK_SERIALIZER: str
    CELERY_RESULT_SERIALIZER: str
    CELERY_REDIS_MAX_CONNECTIONS: int
    SMTP_TLS: bool = False
    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 1025
    EMAILS_FROM_NAME: str
    EMAILS_FROM_EMAIL: str

    class Config:
        env_file = ".env"


settings = Settings()
