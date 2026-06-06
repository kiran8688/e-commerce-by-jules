## 2024-06-06 - Prevent wasted eager loading via selectin
**Learning:** Returning Pydantic schemas that omit relationship fields can still trigger wasted N+1 queries if the SQLAlchemy models use `lazy="selectin"` for async compatibility. This blindly eager loads associated relationships.
**Action:** Always check Pydantic schemas against SQLAlchemy relationships. If the schema omits the relationships, pass `load_options=[raiseload('*')]` from the router endpoint into the service layer to prevent the execution of unused queries.
