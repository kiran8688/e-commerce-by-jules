## 2024-06-22 - Prevent N+1 eager loading in catalog queries
**Learning:** When returning Pydantic response schemas (like `ProductOut`) that omit relationship fields configured with `lazy='selectin'`, passing `noload('*')` to the underlying SQLAlchemy query prevents wasted N+1 eager DB queries.
**Action:** Use `noload('*')` in `select` statements when the result is mapped to schemas that do not require the lazy-loaded relationships.
