## 2026-07-06 - Missing Authorization on User-Specific Endpoints
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` endpoints completely lacked authentication and authorization checks, allowing any user to view or modify the carts and orders of other users simply by knowing their UUID (IDOR).
**Learning:** We cannot rely solely on the unpredictability of UUIDs to secure endpoints. Authentication (`get_current_user`) and explicit authorization (verifying the authenticated user owns the resource or is an admin) must always be applied.
**Prevention:** Consistently apply `Depends(get_current_user)` on endpoints accessing user-specific resources, and explicitly assert authorization (e.g., `user_id == current_user.id`).
