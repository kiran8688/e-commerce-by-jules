mkdir -p .jules
cat << 'MD' > .jules/palette.md
## 2024-06-27 - Keyboard Inaccessibility of Hover-Only Elements
**Learning:** Interactive elements (like "Quick Add" buttons) hidden via `opacity-0` and revealed only on `group-hover` remain invisible when receiving keyboard focus, breaking accessibility for non-mouse users.
**Action:** Always pair `group-hover:opacity-100` with `focus-within:opacity-100` (or `group-focus-within:opacity-100`) on the containing element to ensure keyboard navigation reveals the interactive elements.
MD
