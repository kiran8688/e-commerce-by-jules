## 2024-05-29 - Prevent Password Oracle Vulnerabilities in Registration
**Vulnerability:** The `/register` endpoint used `authenticate_user` to check if a user existed. Because `authenticate_user` performs a slow cryptographic hash if the user exists but the password is wrong, this allowed an attacker to determine if an email is registered by measuring response times (a password oracle vulnerability).
**Learning:** Using an authentication method for existence checks leaks user presence due to the time difference between querying the database and performing cryptographic operations.
**Prevention:** Always use `get_user_by_email` from `auth_service.py` to securely verify user existence without performing timing-dependent cryptographic operations.
