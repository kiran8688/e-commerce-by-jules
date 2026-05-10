## 2024-05-10 - Enhancing Icon-Only Button Accessibility and UX

**Learning:** When using icon-only buttons, relying solely on `aria-label` only benefits screen reader users. Sighted users (and users with cognitive disabilities) often need native tooltips to understand the icon's purpose. Furthermore, toggle buttons (like a mobile menu) must dynamically update their `aria-expanded` and `aria-label` (and `title`) to accurately reflect their current state.

**Action:** Always pair `aria-label` with a matching `title` attribute on icon-only interactive elements. For toggle buttons, bind `aria-expanded` to the state variable and dynamically update both the `aria-label` and `title` to describe the action that will occur (e.g., "Open Menu" vs. "Close Menu"). Additionally, ensure a visible focus state using `focus-visible` classes (e.g., `focus-visible:ring-2 focus-visible:outline-none`) to support keyboard navigation.
