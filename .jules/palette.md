## 2026-07-06 - Improve accessibility for focus-hidden elements
**Learning:** Elements that rely solely on `group-hover:opacity-100` are inaccessible to keyboard users as they don't appear on focus.
**Action:** Pair `group-hover:opacity-100` with `focus-within:opacity-100` to ensure interactive elements become visible to keyboard users.

## 2026-09-19 - Improve keyboard accessibility for hero buttons
**Learning:** Hero buttons that trigger scroll actions need clear focus states to ensure keyboard users can navigate to and interact with them effectively.
**Action:** Always add explicit `focus-visible` ring styles to primary call-to-action buttons, especially on colored backgrounds.

## 2026-09-20 - Add skip-to-content link for better keyboard navigation
**Learning:** Single page applications without skip links force keyboard users to navigate through all header links on every page transition.
**Action:** Always provide a visually hidden skip-to-content link at the top of the AppShell that bypasses navigation.
## 2026-09-23 - Add navigation active states

**Learning:** Users need a clear visual indicator to understand which page they are currently on. `react-router-dom`'s `NavLink` provides a clean way to implement this while automatically adding the `aria-current="page"` attribute for screen readers, improving both visual feedback and accessibility simultaneously.
**Action:** Whenever building navigation menus, prefer `NavLink` over `Link` to easily manage active states and ensure proper accessibility attributes are applied.
## 2026-09-24 - Provide password visibility toggle for authentication
**Learning:** Found that the password input was lacking a visibility toggle. This small micro-UX improvement significantly improves usability and accessibility, reducing cognitive load on users trying to ensure they typed complex passwords correctly, especially on mobile.
**Action:** Always include a show/hide password toggle on all standard password inputs, equipped with clear `aria-label` attributes for screen readers.
