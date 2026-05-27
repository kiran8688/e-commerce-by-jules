## 2025-05-27 - Password Oracle Vulnerability via Authentication Checks
**Vulnerability:** A timing attack and behavior oracle existed on the `/register` endpoint because `authenticate_user` was used to check if an email already exists.
**Learning:** Checking for user existence using a function that also hashes passwords (`authenticate_user`) creates a vulnerability. It leaks whether the user exists via the time it takes to compute the hash and it fails to detect existing users if a wrong password is provided.
**Prevention:** Always use a dedicated function that only queries the database for the user by email (`get_user_by_email`) when checking for user existence.
