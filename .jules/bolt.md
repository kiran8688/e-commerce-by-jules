# Bolt's Journal
## 2025-05-09 - [Prevent Unnecessary Eager Loading in FastAPI]
**Learning:** `lazy="selectin"` on SQLAlchemy relationships causes the relationships to be eager loaded by default. This creates unnecessary database queries if the endpoints return schemas without the relations (e.g. `ProductOut`).
**Action:** Use `.options(raiseload('*'))` in SQLAlchemy `select()` lists that only need flat tabular data, throwing an exception early if related data is accidentally requested instead of making an invisible N+1 query.
