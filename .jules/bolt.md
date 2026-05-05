## 2024-05-05 - [Optimize catalog list queries]
**Learning:** `lazy='selectin'` causes hidden performance issues on list endpoints by executing unnecessary eager load queries for relationships that are not needed by the API response schema.
**Action:** Use `.options(raiseload('*'))` on simple list `select()` queries to prevent these N+1 eager loads.
