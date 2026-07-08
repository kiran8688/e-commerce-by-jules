## 2026-07-08 - Added focus-within to hover-revealed elements
**Learning:** Overlay containers relying on `group-hover:opacity-100` to reveal interactive elements (like buttons) must be paired with `focus-within:opacity-100` to ensure the elements become visible to keyboard users when focused.
**Action:** Always verify keyboard focus states for UI elements that are visually hidden until hovered.
