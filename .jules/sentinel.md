## 2026-07-07 - Insecure Direct Object Reference (IDOR) on User Resources
**Vulnerability:** Cart and Order API endpoints (`/carts/{user_id}` and `/orders/{user_id}`) accepted a `user_id` without verifying that the authenticated user actually owned that ID, allowing any user to read/modify carts and orders of others.
**Learning:** We cannot rely solely on the unpredictability of UUIDs for security. Relying on UUIDs as a security boundary is insufficient since they can be exposed or leaked.
**Prevention:** Always explicitly check authorization on user-specific resources by ensuring `current_user.id == target_user_id` or that the user has admin privileges.
