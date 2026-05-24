## 2026-05-24 - User Enumeration via Timing Attacks
**Vulnerability:** The registration endpoint was using `authenticate_user` (which performs password hashing and verification) to check if a user already existed. This allows attackers to determine if an email is registered by measuring the server response time (timing attack).
**Learning:** `authenticate_user` leaks user existence via timing attacks when used for existence checks instead of just for login validation.
**Prevention:** Always use a fast, direct database query like `get_user_by_email` when you only need to verify if a user exists, rather than reusing full authentication functions that include expensive cryptographic operations.
