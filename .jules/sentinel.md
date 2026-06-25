## 2024-05-24 - IDOR Vulnerability via Predictable Resource URLs
**Vulnerability:** Critical IDOR vulnerability on `/carts/{user_id}` and `/orders/{user_id}`. The endpoints accepted any valid UUID `user_id` without verifying if the authenticated user owned the resource, allowing anyone to view or modify other users' carts and orders.
**Learning:** Using unpredictable UUIDs does not replace proper authorization checks. Security through obscurity (assuming UUIDs can't be guessed) fails when UUIDs are exposed.
**Prevention:** Always explicitly assert authorization on user-specific resources by verifying `user_id == current_user.id` or checking for admin privileges.
