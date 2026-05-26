## 2023-10-27 - Initial
**Learning:** Initial entry
**Action:** Nothing

## 2023-10-27 - Icon-only Control Accessibility
**Learning:** Icon-only controls (such as navigation links or mobile menu toggles) must include native `title` attributes that mirror their `aria-label`s to provide tooltips for sighted users. Additionally, toggle buttons must dynamically update their `aria-label` and `title` attributes and maintain an accurate `aria-expanded` state. Interactive elements should also utilize `focus-visible` branding utility classes (e.g., `focus-visible:ring-2 focus-visible:ring-[#0050d4]`) for keyboard accessibility.
**Action:** Always mirror `aria-label` with `title` for icon-only buttons/links, dynamically update accessibility properties for toggle elements, and apply `focus-visible` styling patterns for interactive controls.
