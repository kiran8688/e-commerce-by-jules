## 2024-05-15 - [Icon-Only Button Accessibility]
**Learning:** Sighted users without screen readers don't benefit from `aria-label`. For icon-only buttons, pairing `aria-label` with the native `title` attribute provides an accessible tooltip. Also, mobile toggle buttons must dynamically update `aria-expanded` and labels for proper screen reader context.
**Action:** Always pair `aria-label` with `title` for icon-only interactive elements and ensure toggle states are dynamically reflected in ARIA attributes.
