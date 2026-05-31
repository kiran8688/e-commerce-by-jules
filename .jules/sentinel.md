## 2024-05-23 - Password Oracle Vulnerability in Registration
**Vulnerability:** The registration endpoint used `authenticate_user` to check if a user already existed.
**Learning:** `authenticate_user` performs cryptographic operations (password hashing) which take a measurable amount of time. Attackers could use timing differences to determine if an email address exists in the system (a password oracle vulnerability).
**Prevention:** Always use a simple database lookup like `get_user_by_email` to securely verify user existence. `authenticate_user` must strictly be used for login validation.
