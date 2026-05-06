## 2024-05-06 - [Icon-Only Button Accessibility]
**Learning:** Sighted users without screen readers benefit from `title` attributes on icon-only buttons as native tooltips, while screen readers rely on `aria-label`. For toggle buttons, updating `aria-expanded` and contextually changing the label/title (e.g., "Open menu" vs "Close menu") significantly improves clarity for all users.
**Action:** Always pair `aria-label` with `title` for icon-only interactive elements and ensure toggle states correctly reflect their current state via `aria-expanded` and dynamic labels.
