## 2026-07-04 - Keyboard Accessibility for Hover Overlays
**Learning:** Overlay containers in product cards that use `group-hover:opacity-100` to reveal interactive elements (like "Quick Add" buttons) hide these elements from keyboard users because they lack focus states.
**Action:** Always pair `group-hover:opacity-100` with `focus-within:opacity-100` on overlay containers to ensure interactive elements become visible during keyboard navigation. Additionally, apply explicit `focus-visible` styles to the elements.
