## 2023-10-27 - Icon-only Navigation Enhancements
**Learning:** In standard React Router setups (like in `AppShell.jsx`), `<Link>` components inherently lack tooltips and focus indicators when they only contain icons. A single focus ring style (`focus-visible:ring-[#0050d4]`) vastly improves keyboard accessibility for navigation components.
**Action:** Always verify that icon-only navigation elements (including `Link` tags from React Router) have explicit `title` attributes that mirror their `aria-label`s, along with high-contrast visible focus rings (`focus-visible`).
