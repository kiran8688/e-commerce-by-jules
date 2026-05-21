## 2024-05-21 - Fix password oracle timing attack in registration
**Vulnerability:** The `/register` endpoint used `authenticate_user` to check if a user already existed. This function performs a cryptographic password verification. The registration endpoint only needed to know if the email was registered.
**Learning:** Using `authenticate_user` to check for account existence introduces a timing attack vulnerability. The response time will vary based on whether the user exists (causing a slow password hash check) or not, leaking account existence to unauthenticated users.
**Prevention:** Always use a simple database query (`get_user_by_email`) that does not perform cryptographic operations when only checking for existence, and strictly reserve `authenticate_user` for login validation.
