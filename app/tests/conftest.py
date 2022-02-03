from typing import Generator, Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture(scope="function")
def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    """Initialize the TestClient with the FastApi fixture.
    Each function will have its own request client
    """
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI, Any, None]:
    """Initialize FastApi fixture. Scope is set to session so that one instance will be used throughout"""
    app: FastAPI = create_app()
    yield app
