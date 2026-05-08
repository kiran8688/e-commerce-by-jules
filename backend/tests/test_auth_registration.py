import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_register_duplicate_user():
    # Because we're writing a simple integration test, let's just make sure the
    # mock behavior when a user exists returns a 409

    # We will mock `get_user_by_email` to return an existing user
    from app.models.user import User
    from app.api.v1.routers import auth

    async def override_get_user_by_email(db, email):
        return User(email=email)

    import app.api.v1.routers.auth as auth_router
    original_get_user_by_email = auth_router.get_user_by_email
    auth_router.get_user_by_email = override_get_user_by_email

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            payload = {
                "email": "test@example.com",
                "password": "Password123!",
                "full_name": "Test User"
            }
            response = await ac.post("/api/v1/auth/register", json=payload)

            assert response.status_code == 409
            assert response.json() == {"detail": "User already exists"}
    finally:
        auth_router.get_user_by_email = original_get_user_by_email
