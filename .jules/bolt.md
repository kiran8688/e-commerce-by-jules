## 2026-07-01 - Prevent Wasted Eager Loads
**Learning:** When returning Pydantic models (e.g., `ProductOut`) that omit relationship fields configured with `lazy='selectin'` on the SQLAlchemy model, SQLAlchemy will still eagerly load them, causing wasted N+1 queries.
**Action:** Use `.options(noload('*'))` on the query to prevent eagerly loading these omitted relationship fields.
