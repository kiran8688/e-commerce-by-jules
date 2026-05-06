## 2024-05-06 - [Avoid N+1 queries using raiseload('*') for lists with selectin relationships]
**Learning:** Using `.options(raiseload('*'))` prevents silent performance degradation from default `lazy='selectin'` relationships when fetching lists of objects.
**Action:** When querying lists of objects with SQLAlchemy that contain fields mapped with `lazy='selectin'`, apply `.options(raiseload('*'))` to prevent unnecessary eager loading.
