## 2026-06-29 - [Added Focus Visible Styles to AppShell]
**Learning:** Keyboard navigation on interactive elements like links and buttons in the header lacked clear visual feedback, making it difficult for keyboard users to track focus.
**Action:** Added explicit `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:rounded-sm` classes to all interactive elements in `AppShell.jsx` to ensure consistent, brand-aligned focus indicators.
