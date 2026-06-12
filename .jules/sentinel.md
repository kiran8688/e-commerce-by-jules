## 2025-02-27 - IDOR in User-Specific Endpoints
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` endpoints relied solely on the unpredictability of UUIDs without asserting that the authenticated user actually owned the requested resource. This allowed any user knowing another's UUID to read/modify their cart and orders.
**Learning:** UUIDs are not a substitute for access control. Even if UUIDs are hard to guess, they can be leaked in UI, logs, or other APIs. We must explicitly verify ownership or admin privileges for all user-specific resources.
**Prevention:** Always use `Depends(get_current_user)` on user-specific routes and explicitly check `user_id == current_user.id` or `current_user.is_admin` before processing the request.
