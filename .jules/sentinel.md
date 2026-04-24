## 2025-02-26 - Password Oracle in User Registration
**Vulnerability:** The user registration endpoint `POST /api/v1/auth/register` checked for existing users by calling `authenticate_user(db, email, password)`. If the provided email existed but the password didn't match, `authenticate_user` would return `None`. This meant the registration endpoint would attempt to create a new user with that same email. This would result in an unhandled database exception (UniqueViolation), manifesting as a 500 error to the client, while successfully returning a 409 Conflict if they happened to guess the password right.

**Learning:** Reusing authentication methods for simple user existence checks inadvertently introduces side channels and unexpected logic branches. A user existence check should strictly verify existence without evaluating other sensitive credentials like passwords.

**Prevention:** Create dedicated functions for single-purpose checks, such as `get_user_by_email`, and ensure authentication flows and validation flows are decoupled to avoid oracle attacks or leaking state via exception handling.
