## 2025-06-15 - Prevent N+1 eager loads in Pydantic serialization
**Learning:** When returning Pydantic response schemas (like `ProductOut`) that omit relationship fields, the underlying SQLAlchemy model might still perform wasted N+1 eager loads (e.g., caused by `lazy='selectin'`).
**Action:** Prevent these wasted queries by passing `raiseload('*')` from the router as `load_options` to the service method when we know relationship fields are not required in the response schema.
