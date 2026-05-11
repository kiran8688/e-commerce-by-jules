import pytest
from app.main import app
from httpx import ASGITransport, AsyncClient


@pytest.mark.asyncio
async def test_cors_preflight_restricted():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        headers = {
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "TRACE",
            "Access-Control-Request-Headers": "X-Vulnerable-Header",
        }
        response = await ac.options("/api/v1/products/", headers=headers)

    # In newer FastAPI versions, restricted preflights return 400
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_cors_valid_origin():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        headers = {
            "Origin": "http://localhost:3000",
        }
        response = await ac.get("/health", headers=headers)
        assert response.status_code == 200
