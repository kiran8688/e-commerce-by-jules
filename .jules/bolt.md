## 2026-06-21 - [Backend] Prevent N+1 queries for unused relationships in FastAPI
**Learning:** `raiseload("*")` only prevents *lazy* loading and does not override explicit mapper-level eager loading like `lazy="selectin"`. To disable eager loads that are omitted by Pydantic models, you must use `noload("*")` to truly eliminate the wasted N+1 DB queries.
**Action:** When a router returns a strict Pydantic model (like `ProductOut`) that does not include nested relationships configured with `lazy="selectin"`, pass `noload("*")` to the service layer instead of `raiseload`.
