## 2024-05-24 - Prevent Wasted Eager Loads in Pydantic List Endpoints
**Learning:** Pydantic schemas that omit relationship fields (like `ProductOut`) do not prevent SQLAlchemy models with `lazy='selectin'` from concurrently executing N+1 eager load queries.
**Action:** When returning Pydantic response models containing only primitive columns, explicitly pass `raiseload('*')` from the router to prevent massive redundant DB hits.
