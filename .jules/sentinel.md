## 2026-06-26 - Prevent IDOR on User Resources
**Vulnerability:** Insecure Direct Object Reference (IDOR) on /carts/{user_id} and /orders/{user_id} endpoints. Endpoints were relying solely on the unpredictability of UUIDs for security.
**Learning:** UUID unpredictability is not a substitute for proper authorization. Without explicitly checking if the authenticated user owns the resource (or is an admin), any user could theoretically access or modify another user's cart or orders if they guessed or leaked the UUID.
**Prevention:** Always secure user-specific endpoints by adding authentication (`Depends(get_current_user)`) and explicitly asserting authorization (e.g., `user_id == current_user.id or current_user.is_admin`).
