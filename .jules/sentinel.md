## 2024-06-27 - Insecure Direct Object Reference (IDOR) on Carts and Orders Endpoints
**Vulnerability:** The `/carts/{user_id}` and `/orders/{user_id}` endpoints did not require authentication or authorization, allowing anyone to access and modify another user's cart and order data by providing their UUID.
**Learning:** Relying solely on the unpredictability of UUIDs is insufficient for securing user-specific resources. Authentication (verifying identity) and authorization (verifying ownership or permissions) are both required.
**Prevention:** Always use a `Depends(get_current_user)` dependency to enforce authentication, and explicitly assert authorization by checking `user_id == current_user.id` or verifying admin privileges to prevent IDOR vulnerabilities.
