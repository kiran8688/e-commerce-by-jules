## 2026-07-03 - IDOR on Cart and Order Endpoints
**Vulnerability:** Cart and Order endpoints allowed any user to access and modify other users' resources by providing their UUID in the path parameter because there were no authorization checks ensuring the user owns the resource.
**Learning:** We cannot rely solely on the unpredictability of UUIDs to secure user-specific backend endpoints (e.g., `/carts/{user_id}` or `/orders/{user_id}`). A malicious user could potentially discover a UUID and gain unauthorized access.
**Prevention:** Explicitly assert authorization by verifying the authenticated user owns the resource (e.g., `user_id == current_user.id`) or checking for admin privileges to prevent IDOR vulnerabilities.
