## 2026-07-02 - Keyboard Accessibility for Hover-Revealed Actions
**Learning:** In the ProductCard component, the "Quick Add" button was only revealed on `group-hover`. Keyboard users tabbing through the page could focus the button, but it remained visually hidden (opacity-0), creating a confusing "invisible focus" trap.
**Action:** Always pair `group-hover:opacity-100` with `focus-within:opacity-100` on overlay containers to ensure interactive elements become visible when receiving keyboard focus. Add clear `focus-visible` styles to interactive elements for better visibility.
