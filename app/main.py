from fastapi import FastAPI, APIRouter
from app.config import settings


def create_app():
    app = FastAPI(title=settings.title, description=settings.description)

    # Other initializations

    @app.get("/", status_code=200)
    def index():
        return "successful"

    return app
