## 2026-07-08 - Avoid N+1 queries by disabling relationships lazy loading
**Learning:** When Pydantic response schemas omit relationship fields (e.g., `ProductOut` omitting `category`, `inventory`), eager loading relationships defined with `lazy="selectin"` on the SQLAlchemy model leads to significant performance issues due to unused queries.
**Action:** Apply `noload('*')` via specific service methods or explicit flags like `load_relationships=False` to prevent wasted queries. Do not change `lazy="selectin"` on models directly.
