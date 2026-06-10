## 2024-10-24 - IDOR Vulnerability in User Endpoints
**Vulnerability:** User-specific endpoints (`/carts/{user_id}` and `/orders/{user_id}`) lacked authorization checks, allowing unauthenticated users or any authenticated user to access and modify other users' data by specifying their UUID.
**Learning:** Relying solely on the unpredictability of UUIDs is insufficient for security. We must explicitly assert authorization by verifying the authenticated user owns the resource or has admin privileges to prevent Insecure Direct Object References (IDOR).
**Prevention:** Always use `Depends(get_current_user)` on sensitive endpoints and explicitly check that `user_id == current_user.id` or that `current_user.is_admin` is True.
