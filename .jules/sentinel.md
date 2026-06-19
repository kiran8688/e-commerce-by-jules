## 2024-06-19 - [IDOR in Carts and Orders Endpoints]
**Vulnerability:** Insecure Direct Object Reference (IDOR) where `/carts/{user_id}` and `/orders/{user_id}` endpoints lacked authorization checks.
**Learning:** Do not rely solely on the unpredictability of UUIDs to secure endpoints. Unauthenticated endpoints or those lacking ownership verification allow attackers to access or modify other users' data if the UUID is known or leaked.
**Prevention:** Always explicitly assert authorization by verifying the authenticated user owns the resource (e.g., `user_id == current_user.id`) or checking for admin privileges.
