## 2024-06-07 - Fix IDOR in user-specific endpoints
**Vulnerability:** IDOR in `carts` and `orders` endpoints. Any user (or even unauthenticated users) could provide an arbitrary `user_id` and view/modify other users' data.
**Learning:** When creating routes like `/carts/{user_id}`, explicitly assert authorization by verifying the authenticated user owns the resource or checking for admin privileges. UUIDs alone do not provide security.
**Prevention:** Always require authentication (`Depends(get_current_user)`) on endpoints acting on user-owned data and explicitly check `user_id == current_user.id`.
