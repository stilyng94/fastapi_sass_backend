from fastapi.testclient import TestClient


class TestContact(object):
    def test_contact_route_success(self, client: TestClient):
        """TestClient for successful contact endpoint"""
        response = client.post(url="/api/contact", json={"email": "pablo@mail.com", "message": "hello pablo"})
        assert response.status_code == 200
        json_data = response.json()
        assert "success" in json_data["message"]

    def test_contact_route_wrong_mail(self, client: TestClient):
        """TestClient wrong email for contact endpoint"""
        response = client.post(url="/api/contact", json={"email": "pablomail.com", "message": "hello pablo"})
        assert response.status_code == 422
