## 2026-06-29 - [Fix IDOR in user specific endpoints]
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints.
**Learning:** Endpoints were incorrectly assuming that UUID unpredictability provides sufficient authorization. An authenticated user could access another user's cart or order by guessing their ID.
**Prevention:** Always verify that `user_id == current_user.id` or that `current_user.is_admin` is True when securing resources mapped directly to a specific user.