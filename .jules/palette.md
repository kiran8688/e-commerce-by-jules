## 2026-07-06 - Improve accessibility for focus-hidden elements
**Learning:** Elements that rely solely on `group-hover:opacity-100` are inaccessible to keyboard users as they don't appear on focus.
**Action:** Pair `group-hover:opacity-100` with `focus-within:opacity-100` to ensure interactive elements become visible to keyboard users.
