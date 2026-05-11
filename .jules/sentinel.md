## 2024-05-19 - [Password Oracle / Timing Attack]
**Vulnerability:** The registration endpoint originally used `authenticate_user` (which calls `verify_password`) to check if a user already existed.
**Learning:** `verify_password` performs cryptographic operations that take a measurable amount of time. If an attacker submits requests to register an account with a known email and variable passwords, the difference in response times can reveal whether the user exists, exposing a password oracle vulnerability.
**Prevention:** Always use a simple database lookup function like `get_user_by_email` to verify existence securely without involving password hashing algorithms. `authenticate_user` must be strictly reserved for login validation.
