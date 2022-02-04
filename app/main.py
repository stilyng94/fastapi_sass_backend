from fastapi import FastAPI
from app.config import settings


def create_app():
    app = FastAPI(title=settings.title, description=settings.description)

    from app.routers.api import api_router
    app.include_router(api_router, prefix="/api")

    # Other initializations

    @app.get("/", status_code=200)
    def index():
        return "successful!!"

    return app
