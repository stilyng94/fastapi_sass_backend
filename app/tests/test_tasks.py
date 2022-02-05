from fastapi.testclient import TestClient
from app.worker import deliver_contact_email


class TestTasks(object):
    def test_delivery_contact_mail(self, client: TestClient):
        """TestClient for delivery of email for contact mail task"""
        json_data = {"email": "task@mail.com", "message": "hello pablo"}
        response = deliver_contact_email(json_data.get("email"), json_data.get("message"))
        assert response is not None
