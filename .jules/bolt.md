## 2026-09-19 - Unnecessary Eager Loading in Cart Operations
**Learning:** The SQLAlchemy models rely heavily on `lazy="selectin"` for async compatibility, which forces N+1 secondary DB queries on every standard read. Models like `Cart` load their parent `User`, and `Product` loads `images`, `reviews`, and `inventory` by default, even during simple operations like adding an item to the cart where only IDs and prices are needed.
**Action:** Always selectively disable eager loading using `.options(noload('*'))` or target specific relations with `noload(Model.relation)` in service functions when secondary data is unnecessary for the immediate schema response or logic, significantly reducing DB hits.
## 2026-09-20 - Prevent eager loading on list orders
**Learning:** Returning `OrderOut` from `list_orders` triggered N+1 queries for unused relations like `User` and `Payment`.
**Action:** Added `.options(noload(Order.user), noload(Order.payment))` to the `select` statement to prevent eager loading.
## 2026-09-21 - [Preventing Unnecessary ProductCard Re-renders]
**Learning:** In a product listing grid, child components like ProductCard frequently re-render unnecessarily when the parent (Catalog) updates its state (e.g., when the product list is fetched or pagination changes). Even with simple props, new function references (like inline `onAddToCart={() => {}}`) trigger re-renders.
**Action:** Always wrap heavy list item components in `React.memo` AND ensure all callback props passed to them from the parent are memoized using `useCallback` to maintain stable references.
