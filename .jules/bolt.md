## 2024-05-04 - [Optimize catalog query loading]
**Learning:** Using `noload("*")` to prevent eager loading can lead to silent data omission if related fields are inadvertently accessed downstream.
**Action:** Use `raiseload("*")` instead of `noload("*")` for safe query optimization; this correctly fails loudly by throwing an exception if relationships are required and accessed, thus preventing silent failures while still ensuring performance against unintended eager loading.
