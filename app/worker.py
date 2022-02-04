import os
from app.config import settings
from app.core.celery_ext import create_celery_app
from app.utils.mail_util import send_email

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email: str, message: str):
    project_name = settings.title
    subject = f"{project_name} - Test email"
    with open(os.path.join("app", "templates", "email_templates", "test_email.html")) as f:
        template_str = f.read()
    return send_email(
        email_to=email,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": settings.title, "email": email, "message": message},
    )
