## 2024-05-19 - Password Oracle in Registration
**Vulnerability:** The `/register` endpoint used `authenticate_user` to check if a user already exists. This exposed a password oracle via timing attacks, as the password hashing function was only called if the email existed in the database.
**Learning:** Cryptographic functions like password verification take a measurable amount of time. If they are conditionally executed based on the existence of a resource (like a user), attackers can use timing differences to enumerate which resources exist.
**Prevention:** Always use a simple database lookup without cryptographic operations (like `get_user_by_email`) when verifying the existence of a user during registration or password resets.
