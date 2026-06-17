## 2024-06-17 - Fix IDOR in user carts and orders
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints, which relied solely on UUID unpredictability without asserting ownership via `get_current_user`.
**Learning:** Using UUIDs for resource IDs does not replace explicit access controls. Any user could guess or brute-force UUIDs (or leak them via other channels) to view or modify other users' carts and orders.
**Prevention:** Always explicitly check ownership (`user_id == current_user.id`) or admin status before allowing access to user-specific endpoints, even if the primary keys are UUIDs.
