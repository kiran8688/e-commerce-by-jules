import pytest
from app.api.v1.deps import get_current_active_admin
from app.main import app
from app.models.user import User
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_admin_dashboard_no_token():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/admin/dashboard")
    # OAuth2PasswordBearer returns 401 Unauthorized when no token is provided
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_admin_dashboard_with_mock_user():
    async def override_get_current_active_admin():
        return User(is_admin=True, is_active=True)

    app.dependency_overrides[get_current_active_admin] = override_get_current_active_admin

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/admin/dashboard")

    assert response.status_code == 200
    assert response.json() == {"message": "Admin dashboard functionality"}

    del app.dependency_overrides[get_current_active_admin]

@pytest.mark.asyncio
async def test_admin_dashboard_forbidden_for_non_admin():
    async def override_get_current_active_admin():
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="The user doesn't have enough privileges"
        )

    app.dependency_overrides[get_current_active_admin] = override_get_current_active_admin

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/admin/dashboard")

    assert response.status_code == 403
    del app.dependency_overrides[get_current_active_admin]
