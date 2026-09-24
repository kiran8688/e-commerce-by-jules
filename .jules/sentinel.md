## 2026-07-08 - Fix IDOR in User-Specific Endpoints
**Vulnerability:** Insecure Direct Object Reference (IDOR) on `/carts/{user_id}` and `/orders/{user_id}` endpoints, allowing unauthenticated or unauthorized users to view and modify other users' resources by guessing or knowing their UUID.
**Learning:** Endpoints were relying solely on the unpredictability of UUIDs instead of explicitly asserting authorization. While UUIDs are hard to guess, they can leak and do not replace proper access control checks.
**Prevention:** Always verify that the authenticated user owns the resource (e.g., `user_id == current_user.id`) or has admin privileges before granting access to user-specific endpoints.

## 2026-09-19 - Incomplete Duplicate Email Validation
**Vulnerability:** The registration endpoint overloaded the `authenticate_user` function to check for duplicate emails. This bypasses uniqueness constraint validation if the user submits an existing email with an incorrect password, leading to 500 errors and potential denial of service or user enumeration.
**Learning:** Authentication checks should not be repurposed for resource existence checks. They silently fail validation when credentials don't match, masking the actual existence of the resource.
**Prevention:** Always use dedicated database queries (e.g., `get_user_by_email`) for resource existence validation to properly enforce application constraints independent of authentication logic.
## 2026-09-24 - Missing Input Validation in Cart Quantity
**Vulnerability:** The application lacks validation for `quantity` in `CartItemBase`. Currently, users can submit negative quantities when adding an item to their cart, allowing them to exploit it and deduct from their order total.
**Learning:** Never trust client-provided input even for straightforward numeric properties. Missing basic boundary checks can lead to serious logic flaws.
**Prevention:** Always define explicit input validations on Pydantic models using `Field(gt=0, ...)` where applicable.
