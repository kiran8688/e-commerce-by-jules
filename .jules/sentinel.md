## 2026-04-26 - [User Enumeration via Timing Attack in Registration]
**Vulnerability:** The `/register` endpoint used `authenticate_user` to check for existing users, causing a password oracle vulnerability.
**Learning:** `authenticate_user` hashes the provided password to check against existing users. This takes significantly more time compared to a simple query for the user. An attacker can exploit this time difference to determine if an email is registered or not.
**Prevention:** Use a dedicated function like `get_user_by_email` that performs a simple SELECT without hashing the password to check for user existence during registration or password resets.
