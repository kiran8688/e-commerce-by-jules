## 2024-05-15 - [Fix] Password Oracle Vulnerability in Registration
**Vulnerability:** The `/api/v1/auth/register` endpoint used `authenticate_user` (which hashes the provided password and compares it to the database) simply to check if an email already existed. This allows an attacker to enumerate valid email addresses via timing attacks because hashing is significantly slower than a simple DB lookup.
**Learning:** Cryptographic functions should strictly be used for authentication. Using them for existence checks leaks information via side channels and wastes compute resources.
**Prevention:** Always use dedicated retrieval functions like `get_user_by_email` when verifying user existence without authenticating.
