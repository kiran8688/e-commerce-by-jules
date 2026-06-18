## 2025-02-24 - Wasted Eager Loads in Pydantic Responses
**Learning:** Returning Pydantic schemas that omit relationship fields (like `ProductOut`) does not automatically prevent the underlying SQLAlchemy models from performing N+1 eager loads (caused by `lazy='selectin'`). This results in wasted database queries for data that is never serialized.
**Action:** Pass `raiseload('*')` from the router to the service method when fetching records whose relationships are omitted by the response schema.
