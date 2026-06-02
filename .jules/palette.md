## 2023-11-20 - AppShell Icon Accessibility
**Learning:** Icon-only navigation controls required explicit tooltips (`title`) matching `aria-label`s to assist sighted users, and responsive elements like the mobile menu toggle must dynamically reflect their state using `aria-expanded` and contextual labels for proper screen reader support.
**Action:** Always include `focus-visible` classes with proper `outline-none` overrides, dynamic `aria-expanded` attributes for toggles, and matching `title`/`aria-label` pairs for icon-only buttons.
