"""
tests.conftest.py

Global conftest file for shared pytest fixtures
"""

import pytest
from async_asgi_testclient import TestClient as AsyncTestClient
from fastapi.testclient import TestClient

from app.main import APP

try:
    from unittest.mock import AsyncMock
except ImportError:
    # Python 3.7 backwards compat
    from asyncmock import AsyncMock

try:
    from contextlib import asynccontextmanager
except ImportError:
    # Python 3.6 backwards compat
    from async_generator import asynccontextmanager


@pytest.fixture
def api_client():
    """
    Returns a fastapi.testclient.TestClient.
    The test client uses the requests library for making http requests.
    """
    return TestClient(APP)


@pytest.fixture
async def async_api_client():
    """
    Returns an async_asgi_testclient.TestClient.
    """
    return AsyncTestClient(APP)
