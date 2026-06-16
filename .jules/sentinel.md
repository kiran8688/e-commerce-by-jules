## 2024-06-16 - Fix IDOR in User Carts and Orders Endpoints
**Vulnerability:** Insecure Direct Object Reference (IDOR) / Missing Authentication. User-specific endpoints `/carts/{user_id}` and `/orders/{user_id}` lacked authentication, allowing anyone to view/modify other users' carts and orders simply by knowing their UUID.
**Learning:** Even when using unguessable UUIDs for resources, relying solely on them without explicit ownership/authorization checks leaves the endpoints fundamentally unauthenticated and open to unauthorized access.
**Prevention:** Always inject the authenticated `current_user` dependency in endpoints handling user-specific data and explicitly assert authorization (e.g., `user_id == current_user.id` or `current_user.is_admin`).
