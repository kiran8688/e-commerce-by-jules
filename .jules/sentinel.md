## 2024-06-20 - Fix missing authentication/authorization on order and cart endpoints
**Vulnerability:** Cart and Order endpoints (`/carts/{user_id}` and `/orders/{user_id}`) do not verify if the requester is authenticated or actually the owner of the `user_id`.
**Learning:** Insecure Direct Object References (IDOR). Relying solely on UUIDs for security without validating authentication or authorization allows any user to read/modify any other user's carts or orders by guessing or knowing their UUID.
**Prevention:** Always use `get_current_user` dependency for endpoints dealing with user-specific data and explicitly check `user_id == current_user.id`.
