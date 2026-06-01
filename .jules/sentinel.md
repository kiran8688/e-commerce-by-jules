## 2024-05-24 - Fix password oracle vulnerability in registration
**Vulnerability:** The registration endpoint used `authenticate_user` to check if an email existed. Because `authenticate_user` hashes the provided password, this exposed a timing attack where an attacker could deduce if an email was registered based on response times (a password oracle).
**Learning:** Checking for user existence using an authentication function that performs cryptographic operations leaks existence via timing differences.
**Prevention:** Always use a simple database lookup (like `get_user_by_email`) that performs no cryptography to securely verify user existence during registration or password resets.
