## 2025-06-08 - Prevent Wasted Eager Loads in Pydantic Responses
**Learning:** When returning Pydantic schemas (e.g., `ProductOut`) that omit relationship fields, the underlying SQLAlchemy models with `lazy='selectin'` will still trigger N+1 eager loads for those relationships, wasting DB resources.
**Action:** Pass load options like `raiseload('*')` from the router when invoking service-layer functions to strip these unnecessary loads without altering the global behavior of the service functions.
