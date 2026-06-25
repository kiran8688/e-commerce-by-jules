## 2026-06-25 - Improve AppShell Header Accessibility
**Learning:** Keyboard accessibility (focus rings) and precise ARIA controls (expanded state, dynamic labels, and region controls) are critical for complex navigation components like header bars and mobile menus, preventing screen reader users from losing context.
**Action:** Add `focus-visible` utility classes to all interactive header elements, dynamically manage `aria-expanded` and `aria-label` for toggles, and link the toggle to the menu region using `aria-controls` and `id`.
