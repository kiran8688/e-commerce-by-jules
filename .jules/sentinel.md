## 2024-04-16 - Prevent User Enumeration / Password Oracle in Registration
**Vulnerability:** The `/register` endpoint used `authenticate_user` (which expects both an email and a correct password) to check if an email already existed. This exposed an enumeration vector and acted as a password oracle (returning 409 only on correct guess, or a 500 DB error on incorrect password but existing email).
**Learning:** Checking for existing records must be decoupled from authentication. Reusing authentication functions for existence checks inadvertently binds two separate logical paths.
**Prevention:** Always use a specific lookup function (e.g., `get_user_by_email`) that only validates the identifier (email) when performing pre-creation conflict checks.

## 2024-04-16 - IDOR/BOLA Architectural Gap in Orders/Carts
**Vulnerability:** Endpoints such as `create_order`, `list_orders`, `read_cart`, and `add_item_to_cart` rely purely on a `{user_id}` path parameter and currently lack server-side authorization checks ensuring the authenticated user owns that ID.
**Learning:** Currently, the frontend client does not appear to pass the `Authorization` bearer token in its API requests (via `client.js`), meaning we cannot strictly enforce IDOR protection on these endpoints yet without breaking frontend functionality.
**Prevention:** Future security work must update the frontend to pass the JWT, and subsequently, backend routes must use `get_current_user` to validate that the requested `user_id` matches `current_user.id` or that the user is an admin.
