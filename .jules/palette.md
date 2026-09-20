## 2026-07-06 - Improve accessibility for focus-hidden elements
**Learning:** Elements that rely solely on `group-hover:opacity-100` are inaccessible to keyboard users as they don't appear on focus.
**Action:** Pair `group-hover:opacity-100` with `focus-within:opacity-100` to ensure interactive elements become visible to keyboard users.

## 2026-09-19 - Improve keyboard accessibility for hero buttons
**Learning:** Hero buttons that trigger scroll actions need clear focus states to ensure keyboard users can navigate to and interact with them effectively.
**Action:** Always add explicit `focus-visible` ring styles to primary call-to-action buttons, especially on colored backgrounds.

## 2026-09-20 - Add skip-to-content link for better keyboard navigation
**Learning:** Single page applications without skip links force keyboard users to navigate through all header links on every page transition.
**Action:** Always provide a visually hidden skip-to-content link at the top of the AppShell that bypasses navigation.
