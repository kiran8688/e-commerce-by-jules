## 2024-05-18 - Prevent Password Oracle via Authentication Timing Attack
**Vulnerability:** The `/register` endpoint uses `authenticate_user` (which hashes passwords) to check if a user exists. This makes account existence checks vulnerable to timing attacks (password oracle).
**Learning:** Checking for user existence by performing expensive cryptographic operations leaks information about whether an account exists.
**Prevention:** Always use a simple database lookup (`get_user_by_email`) that doesn't involve cryptographic hashing when only verifying existence.
