## 2025-05-04 - [Password Oracle Vulnerability]
**Vulnerability:** Registration endpoint was using `authenticate_user` (which verifies passwords) to check if a user already exists. If a user provided the wrong password for an existing account, the check would fail, allowing them to proceed with registration or indicating whether the password was correct.
**Learning:** Checking for user existence using authentication functions creates a password oracle vulnerability, as it inadvertently tests both existence and password correctness.
**Prevention:** Always use dedicated functions (e.g., `get_user_by_email`) that only query for existence and do not perform cryptographic verification when checking if a resource exists.
