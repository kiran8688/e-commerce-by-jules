## 2024-05-23 - Dynamic ARIA States for Mobile Menus
**Learning:** Icon-only toggle buttons (like mobile menu hamburgers) require dynamic `aria-label` and `title` attributes that update based on state (e.g., "Open Menu" vs "Close Menu"), along with the `aria-expanded` attribute, to ensure full accessibility for screen reader and keyboard users. Relying on a static label like "Toggle Menu" is insufficient.
**Action:** Always ensure toggle buttons dynamically update their `aria-label` and `title` to match the current state and accurately reflect `aria-expanded`.
