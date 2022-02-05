from fastapi import APIRouter, Body
from pydantic.networks import EmailStr

contact_router = APIRouter(prefix="/contact")


@contact_router.post("", status_code=200)
def contact(*, email: EmailStr = Body(None), message: str = Body(None)):
    from app.worker import deliver_contact_email
    deliver_contact_email.delay(email, message)
    return {"message": "success"}
