## 2026-05-12 - Icon-only buttons accessibility
**Learning:** Icon-only buttons (like the header actions and quick add to cart buttons) require `aria-label` and `title` attributes for full accessibility and visible tooltip. In React, they also need proper focus management (e.g. `focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none`) to provide clear visual feedback during keyboard navigation.
**Action:** Added `aria-label`, `title`, and `focus-visible` classes to all icon-only buttons in `AppShell.jsx` and `ProductCard.jsx`.
