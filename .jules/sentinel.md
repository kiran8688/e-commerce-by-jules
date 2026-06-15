## 2024-06-15 - IDOR via UUID Resource Identifiers
**Vulnerability:** User-specific endpoints like `/carts/{user_id}` and `/orders/{user_id}` relied solely on the unpredictability of UUIDs without explicit authorization checks, exposing an IDOR vulnerability.
**Learning:** Assuming UUIDs are sufficiently unpredictable for security leads to IDOR vulnerabilities when user scopes are not enforced via the authenticated session.
**Prevention:** Always explicitly assert authorization by verifying `user_id == current_user.id` or checking for admin privileges on user-specific resources.
