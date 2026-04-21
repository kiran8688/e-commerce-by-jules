## 2024-04-21 - Icon-Only Buttons Accessibility
**Learning:** Icon-only buttons (like Search, Account, Cart) in the navigation lack textual context, creating usability issues for both screen readers and sighted users.
**Action:** Pair `aria-label` with `title` attributes (native tooltips) on all icon-only buttons to support both screen readers and sighted users. Also ensure interactive state updates (e.g. `aria-expanded`) and `focus-visible` styling is applied for keyboard accessibility.
