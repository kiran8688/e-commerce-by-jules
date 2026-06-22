## 2024-06-22 - [IDOR Vulnerability on User-Specific Endpoints]
**Vulnerability:** Missing authorization on user-specific endpoints (`/carts/{user_id}` and `/orders/{user_id}`). The endpoints assumed that because UUIDs were unguessable, no authorization check was needed.
**Learning:** Relying solely on the unpredictability of UUIDs is insufficient for securing user-owned resources, leading to Insecure Direct Object References (IDOR).
**Prevention:** Always explicitly assert authorization by verifying the authenticated user owns the requested resource (e.g., `user_id == current_user.id`) or checking for administrative privileges.
