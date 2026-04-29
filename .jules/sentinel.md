## 2025-04-29 - [Password Oracle Vulnerability]
**Vulnerability:** The account registration endpoint checked for user existence by calling `authenticate_user` with the provided email and a potentially dummy password, causing a password oracle and unneeded bcrypt overhead when checking existence.
**Learning:** Checking for user existence using authentication endpoints/logic can lead to a timing attack / password oracle due to the long computation time of password hashing.
**Prevention:** Use a dedicated database lookup strictly by unique identifier (e.g., `get_user_by_email`) without involving password verification logic for existence checks.
