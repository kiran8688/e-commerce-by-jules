## 2024-05-10 - [SQLAlchemy Eager Loading Overhead]
**Learning:** Default eager loading strategies like `lazy="selectin"` on relationships trigger multiple background background queries even when the Pydantic response schemas only serialize scalar columns, introducing significant database N+1-like overhead.
**Action:** Use `.options(raiseload('*'))` in SQLAlchemy query definitions for endpoints that list/serialize collections to prevent unintended eager-loading cascades and save multiple queries per request.
