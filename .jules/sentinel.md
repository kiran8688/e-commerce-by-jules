## 2026-04-18 - [Fix Password Oracle Vulnerability]
**Vulnerability:** The `/register` endpoint used `authenticate_user` to check for existing users. This allowed an attacker to guess a user's password because a correct guess returned `409 Conflict` (User already exists), while an incorrect guess bypassed the check and failed on a database unique constraint.
**Learning:** Checking for user existence during registration must strictly use the unique identifier (email) and NEVER attempt to validate the password. Utilizing `authenticate_user` for this purpose created a password oracle vulnerability.
**Prevention:** Always separate authentication functions from existence check functions. Implemented `get_user_by_email` specifically for checking existence safely.
