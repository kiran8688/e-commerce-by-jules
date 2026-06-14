## 2024-06-14 - Prevent wasted eager loads in FastAPI/SQLAlchemy endpoints
**Learning:** Pydantic response schemas that omit relationship fields do not stop SQLAlchemy's `lazy="selectin"` from executing eager load queries. This leads to wasted database queries fetching relationships that are ultimately discarded before serialization.
**Action:** Use `raiseload('*')` in the query options from the router when returning schemas that do not require relationship data to prevent unnecessary database queries and improve endpoint performance.
