## 2026-06-30 - Hover Overlays and Keyboard Accessibility
**Learning:** Overlay actions (like Quick Add buttons) that rely solely on `group-hover` for visibility become hidden traps for keyboard users. When a user tabs into the hidden button, they cannot see what they have focused on.
**Action:** Always pair `group-hover:opacity-100` with `focus-within:opacity-100` on overlay containers to ensure the UI reveals itself when internal interactive elements receive focus.
