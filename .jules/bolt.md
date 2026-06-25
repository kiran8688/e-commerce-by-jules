## 2025-06-25 - Prevent N+1 eager queries on list endpoints
**Learning:** Returning Pydantic schemas (like `ProductOut`) that omit relationship fields configured with `lazy="selectin"` results in wasted N+1 eager DB queries, because `lazy="selectin"` automatically fetches relationships asynchronously regardless of whether the output schema needs them.
**Action:** Use `.options(noload('*'))` on the underlying SQLAlchemy select queries when fetching models for schemas that do not require relationship data to significantly reduce database query load and execution time.
