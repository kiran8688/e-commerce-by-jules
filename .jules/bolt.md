## 2026-06-27 - Prevent wasted eager DB queries for omitted relationship fields
**Learning:** Pydantic response schemas (like `ProductOut`) that omit relationship fields configured with `lazy='selectin'` can cause wasted N+1 eager DB queries. Passing `noload('*')` to the underlying SQLAlchemy query prevents this by overriding the default mapper-level eager loading logic.
**Action:** Always check if a Pydantic schema omits eager-loaded relationships and apply `noload('*')` to the underlying SQLAlchemy query to optimize performance by avoiding unnecessary database reads.
