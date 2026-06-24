## 2024-06-24 - Fix IDOR in User Endpoints
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints where any user could access or modify another user's data due to missing authorization checks.
**Learning:** Relying solely on the unpredictability of UUIDs without asserting authorization is insufficient to secure user-specific endpoints, as UUIDs can be leaked or guessed.
**Prevention:** Always use dependency injection (e.g., `Depends(get_current_user)`) to explicitly assert that the authenticated user owns the requested resource (`current_user.id == user_id`) or has administrative privileges.
