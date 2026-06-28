## 2026-06-28 - Insecure Direct Object Reference (IDOR) on User Resources
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` endpoints lacked authorization checks, allowing any unauthenticated or authenticated user to read/modify resources of other users by simply guessing or providing another user's UUID.
**Learning:** Using UUIDs for user IDs provides unpredictability but is not a substitute for proper authorization. User-specific endpoints must explicitly verify that the authenticated user owns the requested resource.
**Prevention:** Always include `Depends(get_current_user)` on endpoints dealing with user-specific data and explicitly assert ownership (e.g., `user_id == current_user.id` or check admin privileges) before processing the request.
