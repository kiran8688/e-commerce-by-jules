import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from unittest.mock import patch

@pytest.mark.asyncio
@patch("app.api.v1.routers.auth.get_user_by_email")
async def test_register_existing_user_different_password_fails(mock_get_user):
    """
    Ensure that attempting to register an existing user with a different password
    returns a 409 Conflict (User already exists) and does not try to authenticate
    them or leak whether the password was correct.
    """
    # Mock that the user exists
    mock_get_user.return_value = {"id": "123", "email": "test@example.com"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "email": "test@example.com",
            "password": "wrongpassword123",
            "full_name": "Test User",
            "phone": "1234567890"
        }
        response = await ac.post("/api/v1/auth/register", json=payload)

    # It should say User already exists, NOT try to check the password and fail
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exists"
