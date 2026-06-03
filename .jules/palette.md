## 2024-05-18 - AppShell Icon Control Accessibility
**Learning:** Icon-only controls need native `title` attributes (mirroring `aria-label`) to provide tooltips for sighted users. Toggles must dynamically update their `aria-label` and `title` based on state and include `aria-expanded` to convey state to screen readers.
**Action:** Always pair `aria-label` with `title` on icon-only interactive elements, dynamically bind both to state for toggles, add `aria-expanded` to toggles, and use `focus-visible` classes to ensure visible focus rings without conflicting with default browser outlines.
