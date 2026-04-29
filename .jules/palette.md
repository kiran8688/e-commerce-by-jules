## 2026-03-05 - [Accessible Icon Buttons & Toggle States]
**Learning:** Icon-only buttons must pair `aria-label` with `title` attributes to support both screen readers and sighted users natively. Toggle states like mobile menus require dynamic `aria-expanded` and `aria-label` attributes to correctly communicate their current state.
**Action:** Always include both `aria-label` and `title` for icon-only buttons, and use dynamic `aria-*` attributes for any stateful toggle components. Also ensure `focus-visible` states are present for keyboard accessibility.
