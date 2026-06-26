## 2024-05-24 - [N+1 Prevention with noload]
**Learning:** Returning Pydantic response schemas (like `ProductOut`) that omit relationship fields configured with `lazy='selectin'` causes wasted N+1 eager DB queries.
**Action:** When returning lists of models where relationship fields are intentionally omitted from the response schema, explicitly pass `noload('*')` to the underlying SQLAlchemy query to prevent wasteful eager loading.
