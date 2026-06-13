## 2024-05-24 - [Fix IDOR in user endpoints]
**Vulnerability:** IDOR (Insecure Direct Object Reference) in endpoints receiving user_id via path parameter (e.g., carts, orders). User IDs were trusted from the URL without verifying if the authenticated user owned the ID.
**Learning:** Endpoints using unguessable identifiers (UUIDs) can still be exploited if those identifiers leak. Relying solely on the unpredictability of UUIDs without explicit authorization checks (verifying `user_id == current_user.id` or `current_user.is_admin`) causes IDOR vulnerabilities.
**Prevention:** Always assert authorization for sensitive resource access by verifying the logged-in user owns the requested resource ID, and pass the auth token correctly from the frontend.
