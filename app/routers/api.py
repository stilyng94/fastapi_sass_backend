from fastapi import APIRouter

from app.routers import contact_router

api_router = APIRouter()
api_router.include_router(contact_router.contact_router, tags=["contact"])
