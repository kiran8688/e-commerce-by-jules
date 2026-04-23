## 2025-02-23 - [Authentication] Fixed Password Oracle Vulnerability in Registration
**Vulnerability:** The `/register` endpoint used `authenticate_user(db, payload.email, payload.password)` to check if a user existed. This caused the endpoint to verify the provided password instead of just checking for the email, creating a password oracle where attackers could enumerate accounts or verify passwords.
**Learning:** `authenticate_user` should only be used for login. Re-using authentication logic for existence checks leads to severe security and logic flaws.
**Prevention:** Always introduce an explicit existence check function like `get_user_by_email` that skips password verification when checking if a user exists during registration or similar flows.
