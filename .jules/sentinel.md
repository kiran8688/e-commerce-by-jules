## 2024-06-08 - [IDOR in User Resource Endpoints]
**Vulnerability:** Endpoints handling user-specific resources (e.g., carts, orders) relied solely on the `user_id` path parameter without any authentication or authorization checks, allowing an attacker to read or modify resources of other users by guessing their UUID.
**Learning:** Relying on the unpredictability of UUIDs is not a substitute for proper access controls. Endpoints acting on user-owned data must verify that the authenticated user actually owns that data.
**Prevention:** Always use a dependency like `get_current_user` on protected endpoints, and explicitly assert that `user_id == current_user.id` (or the user is an admin) before accessing or modifying the resource.
