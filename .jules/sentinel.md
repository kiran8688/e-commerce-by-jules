## 2026-07-08 - Fix IDOR in User-Specific Endpoints
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints, allowing unauthenticated or unauthorized users to view and modify other users' resources by guessing or knowing their UUID.
**Learning:** Endpoints were relying solely on the unpredictability of UUIDs instead of explicitly asserting authorization. While UUIDs are hard to guess, they can leak and do not replace proper access control checks.
**Prevention:** Always verify that the authenticated user owns the resource (e.g., `user_id == current_user.id`) or has admin privileges before granting access to user-specific endpoints.
