## 2024-06-02 - Prevent unnecessary eager loading with raiseload
**Learning:** Pydantic schemas that omit relationship fields don't automatically prevent SQLAlchemy from eagerly loading them if they are configured with `lazy="selectin"`. This causes unnecessary queries.
**Action:** Pass `raiseload('*')` as an option to the query from the router to prevent these wasted eager loads when returning data that doesn't need relationships. Pass load options as arguments to service layer functions to avoid breaking other callers.
