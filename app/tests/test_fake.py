from fastapi.testclient import TestClient


class TestFake(object):
    def test_homepage(self, client: TestClient):
        response = client.get(url="/")
        assert response.status_code == 200
