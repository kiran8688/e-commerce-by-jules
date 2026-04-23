## 2024-04-23 - Prevent N+1 queries with noload in list endpoints
**Learning:** In SQLAlchemy, relationships configured with `lazy="selectin"` are eagerly loaded by default, causing unnecessary secondary queries and over-fetching if the data is not needed by the Pydantic response schema (e.g. `ProductOut`, `CategoryOut`).
**Action:** When querying lists that do not require relationship data, always use `.options(noload(...))` to explicitly prevent the eager loading of those specific relationships, saving multiple round-trips to the database per request.
