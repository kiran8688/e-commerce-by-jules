import pytest
from app.core.config import settings
from app.main import app
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_cors_preflight_restricted():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Preflight request for a method NOT in our whitelist (e.g., HEAD if not in list)
        # Note: If we want to test restriction, we need something not in settings.CORS_METHODS
        # For now, let's assume we want to ensure it DOES NOT allow everything.
        headers = {
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "TRACE",
            "Access-Control-Request-Headers": "X-Vulnerable-Header",
        }
        response = await ac.options("/api/v1/products/", headers=headers)

    # In newer versions of FastAPI/Starlette, CORSMiddleware returns 400 Bad Request
    # for disallowed CORS preflight (OPTIONS) requests.
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_cors_preflight_allowed():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Preflight request for allowed method and header
        headers = {
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type",
        }
        response = await ac.options("/api/v1/products/", headers=headers)

    assert response.status_code == 200
    # CORSMiddleware returns all allowed methods/headers
    allowed_methods = response.headers.get("Access-Control-Allow-Methods", "")
    for method in settings.CORS_METHODS:
        assert method in allowed_methods

    allowed_headers = response.headers.get("Access-Control-Allow-Headers", "")
    for header in settings.CORS_HEADERS:
        assert header in allowed_headers
