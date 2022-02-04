from celery import Celery

CELERY_TASKS = [
    "app.worker"
]


def create_celery_app() -> Celery:
    from app.config import settings
    celery = Celery(__name__, broker=settings.CELERY_BROKER_URL, include=CELERY_TASKS,
                    backend=settings.CELERY_RESULT_BACKEND)
    return celery
