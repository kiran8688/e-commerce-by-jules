## 2026-07-04 - IDOR and Missing Auth on User-Specific Endpoints
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` endpoints lacked authentication and authorization, allowing anyone to access or modify resources if they knew or guessed a UUID.
**Learning:** The application mistakenly relied on the unpredictability of UUIDs as a substitute for access control, assuming unguessable IDs provided sufficient security against unauthorized access.
**Prevention:** Always explicitly enforce authentication using dependencies like `get_current_user` and assert authorization by verifying the authenticated user owns the resource (e.g., `user_id == current_user.id`) or has admin privileges, regardless of primary key type.
