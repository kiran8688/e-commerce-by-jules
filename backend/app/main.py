"""
Main application entry point for the FastAPI backend.

This module initializes the FastAPI application instance, configures global middleware,
and registers all the modular API routers.

Design Decision:
We use a prefix-based routing strategy (e.g., `/api/v1`) loaded from the central `settings` object.
This makes future versioning (e.g., `/api/v2`) seamless without requiring changes to the
core app logic.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routers import admin, auth, carts, orders, products, reviews, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Middleware Configuration
# Why CORS? The frontend (React Vite) operates on a different origin (e.g., localhost:3000)
# during development and potentially in production. This middleware explicitly whitelists
# allowed origins to prevent browser-enforced Cross-Origin Resource Sharing errors.
# Security Note: Methods and headers are explicitly whitelisted via `settings`
# instead of using wildcards `["*"]` to follow security best practices.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

# Router Registration
# We map all feature-specific routers under the common API version prefix.
app.include_router(auth.router, prefix=settings.API_V1_PREFIX)
app.include_router(products.router, prefix=settings.API_V1_PREFIX)
app.include_router(carts.router, prefix=settings.API_V1_PREFIX)
app.include_router(orders.router, prefix=settings.API_V1_PREFIX)
app.include_router(admin.router, prefix=settings.API_V1_PREFIX)
app.include_router(reviews.router, prefix=settings.API_V1_PREFIX)
app.include_router(users.router, prefix=settings.API_V1_PREFIX)


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Provides a simple infrastructure health check endpoint.

    Why this exists: Container orchestration systems (like Docker Compose, Kubernetes, or AWS ECS)
    use endpoints like this to determine if the container is ready to receive traffic or needs
    to be restarted.
    """
    return {"status": "ok"}
