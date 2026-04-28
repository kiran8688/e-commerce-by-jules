## 2024-05-24 - [SQLAlchemy Selectin N+1 Over-fetching]
**Learning:** Defaulting to `lazy="selectin"` on SQLAlchemy model relationships globally causes severe over-fetching on list endpoints (like `/products`) when the respective Pydantic response schemas do not include those relationships, executing multiple unnecessary queries per request.
**Action:** Use `.options(noload(Model.relationship))` explicitly on list queries to skip eager loading and improve database performance.
