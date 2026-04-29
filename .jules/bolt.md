## 2024-05-15 - SQLAlchemy `lazy='selectin'` Over-fetching Pattern
**Learning:** In list queries, SQLAlchemy relationships mapped with `lazy='selectin'` cause severe over-fetching by running additional background queries even when the related data is not serialized in the response schemas (e.g., `ProductOut`).
**Action:** When querying lists with SQLAlchemy, use `.options(noload(...))` to prevent eager loading of relationships that are not included in the respective Pydantic response schema.
