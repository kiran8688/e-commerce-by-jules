# Code Commenting Strategy

This repository adheres to a comprehensive, "intent-driven" commenting strategy designed to ensure long-term maintainability, facilitate smooth developer onboarding, and make the codebase exceptionally easy to extend or debug.

## Philosophy

Comments in this codebase must go beyond merely describing *what* the code does (which should ideally be self-evident from variable and function names). They must address the following:

1.  **The "Why" (Design Decisions):** Why was this specific approach chosen over alternatives? What architectural pattern is being fulfilled?
2.  **Context and Constraints:** Are there external dependencies, performance considerations, or business rules dictating this implementation?
3.  **Edge Cases and Gotchas:** What non-obvious scenarios could cause this code to fail, and how are they handled (or intentionally deferred)?
4.  **Extensibility Hooks:** Where should future developers look to add new features, fields, or integrations related to the current module?

## Guidelines by Layer

### 1. Backend: Configuration & Initialization (`core/`, `main.py`)
*   **Focus:** Explain the lifecycle of the application. Document why specific middleware (e.g., CORS) is configured the way it is. Explain how environment variables cascade into application state.

### 2. Backend: Database Models (`models/`)
*   **Focus:** Detail the relational algebra. Explain *why* a relationship is configured as `lazy="selectin"` (e.g., to support async environments and prevent implicit I/O). Document constraints, indexes, and the business reality the table represents.

### 3. Backend: Services & Routers (`services/`, `routers/`)
*   **Focus:** Document the business logic flow.
    *   **Services:** Detail the "happy path," potential data mutation side-effects, and why specific ORM queries were chosen for performance.
    *   **Routers:** Focus on the API contract. Explain what the endpoint expects, what HTTP status codes it returns under various failure modes, and how it delegates to the service layer.

### 4. Frontend: API Client & Features (`api/`, `features/`)
*   **Focus:** Explain the state management and data-fetching lifecycle.
    *   **API Client:** Document error interception, token management (if applicable), and fetch abstraction rationale.
    *   **Components:** Explain component side-effects (`useEffect`), rendering decisions, and how the component connects to the broader user journey.

## Example

Instead of:
```python
# Create a user
async def create_user(db, user):
    ...
```

Write:
```python
async def create_user(db: AsyncSession, payload: UserCreate) -> User:
    """
    Persists a new user record to the database.

    Design Decision:
    We hash the password synchronously here before creating the ORM object.
    While password hashing is CPU-bound, `pwdlib` with Argon2 is fast enough
    that it doesn't currently warrant offloading to a separate thread pool
    for our expected traffic volume.

    Edge Cases Handled:
    - Unique constraint violations on the `email` field are caught at the router
      level prior to invoking this service.

    Future Enhancements:
    - If email verification is implemented, this is where the `is_active` flag
      should be forced to `False`, and the activation email dispatch should be triggered.
    """
    ...
```