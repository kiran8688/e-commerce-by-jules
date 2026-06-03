## 2024-06-03 - [Fix IDOR in User-Specific Endpoints]
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints. They accepted a `user_id` path parameter without authenticating the user or verifying that the requested `user_id` matches the authenticated session.
**Learning:** Relying on the unpredictability of UUIDs as a security mechanism is insufficient. Endpoints must always explicitly assert that the currently authenticated user has the right to access the referenced resource ID.
**Prevention:** Always inject `current_user = Depends(get_current_user)` in user-specific endpoints and validate `user_id == current_user.id` or implement proper Role-Based Access Control (RBAC).
