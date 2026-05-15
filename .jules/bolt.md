
## 2024-05-15 - [Prevent N+1 Queries in SQLAlchemy AsyncSession with raiseload]
**Learning:** In asynchronous SQLAlchemy (`AsyncSession`), accessing relationships that default to eager loading (e.g., `lazy='selectin'`) when they aren't needed leads to significant N+1 queries or heavy joins. Synchronous lazy-loading is not possible and raises `MissingGreenletError`.
**Action:** Always explicitly use `.options(raiseload('*'))` when querying lists of entities where the relationships are not needed by the output schema, preventing silent eager loads.
