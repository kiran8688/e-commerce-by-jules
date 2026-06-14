## 2025-06-14 - Improve AppShell icon controls accessibility
**Learning:** Icon-only navigation links and toggle buttons can be confusing for sighted users without tooltips, and for keyboard/screen-reader users without proper focus states and dynamic `aria-expanded` attributes.
**Action:** Always include native `title` attributes mirroring `aria-label` for icon-only buttons, dynamically update toggles' `aria-expanded`/`aria-label`, and provide distinct `focus-visible` styling (e.g., `focus-visible:outline-none focus-visible:ring-2`).
