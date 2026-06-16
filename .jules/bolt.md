## 2024-05-24 - [Prevent Wasted Eager Loads in API Responses]
**Learning:** Pydantic schemas that omit relationship fields (like `ProductOut`) still trigger SQLAlchemy `lazy="selectin"` queries, causing unnecessary database hits for unused data.
**Action:** When returning schemas that don't need relationships, pass `raiseload('*')` to the underlying query to prevent wasted eager loading and reduce database load.
