## 2026-07-02 - IDOR in User-Specific Endpoints
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints where no authorization validation was performed beyond UUID path matching.
**Learning:** Endpoints that include resource identifiers as part of the path must explicitly check that the authenticated user owns that resource (or has admin privileges). Do not rely solely on the unpredictability of UUIDs to secure endpoints.
**Prevention:** Always assert ownership by checking `user_id == current_user.id` or by validating admin status in the endpoint logic.
