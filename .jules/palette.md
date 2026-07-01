## 2026-07-01 - Revealing Interactive Overlays for Keyboard Users
**Learning:** Overlay containers using `group-hover:opacity-100` to hide interactive elements (like Quick Add buttons) make those elements invisible to keyboard users who tab to them, as hover isn't triggered.
**Action:** Always pair `group-hover:opacity-100` with `focus-within:opacity-100` on the container, and add visible focus styles (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4]`) to the button itself.
