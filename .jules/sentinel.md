## 2024-06-11 - Prevent IDOR on Carts and Orders Endpoints
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` API endpoints lacked authorization checks, allowing any user to read/modify carts and orders of other users by providing their UUIDs (IDOR vulnerability).
**Learning:** Even with unpredictable UUIDs, explicitly verifying that the authenticated user owns the resource is critical. Never rely solely on unpredictability of identifiers for security.
**Prevention:** Always assert authorization explicitly (e.g., `user_id == current_user.id or current_user.is_admin`) in endpoints accessing user-specific data.
