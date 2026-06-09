## 2024-05-24 - IDOR in User-Specific Endpoints
**Vulnerability:** Endpoints like `/carts/{user_id}` and `/orders/{user_id}` relied solely on the unpredictability of UUIDs and lacked proper authorization checks, allowing IDOR (Insecure Direct Object Reference).
**Learning:** Always assert that the authenticated user owns the resource being accessed (e.g., `user_id == current_user.id`) or has admin privileges, even when using UUIDs.
**Prevention:** Implement strict ownership assertions alongside authentication dependencies for all user-specific resources.
