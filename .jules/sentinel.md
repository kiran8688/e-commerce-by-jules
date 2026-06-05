## 2025-06-05 - IDOR in User-Specific Endpoints
**Vulnerability:** User-specific endpoints (`/carts/{user_id}` and `/orders/{user_id}`) lacked authorization checks, allowing any user to access or modify carts and orders of other users.
**Learning:** The application architecture previously relied solely on the unpredictability of UUIDs for user-specific endpoints rather than explicit authentication.
**Prevention:** Always use `Depends(get_current_user)` on sensitive endpoints and explicitly assert `user_id == current_user.id` or `current_user.is_admin` before processing the request.
