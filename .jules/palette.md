## 2025-06-17 - AppShell Focus Rings
**Learning:** Interactive header elements (icon buttons, text links) lacked visible keyboard focus indicators, making the navigation visually inaccessible for keyboard users. Default browser outlines clashed with the UI.
**Action:** Established a reusable pattern using `rounded-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:ring-offset-4` to provide clear, branded focus states that only appear on keyboard navigation.
