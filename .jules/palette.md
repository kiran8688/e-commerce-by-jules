## 2024-06-10 - 🎨 Palette: Improve accessibility of AppShell icon controls
**Learning:** Icon-only controls must include native `title` attributes mirroring `aria-label`s for sighted users, and toggle buttons need accurate `aria-expanded` state along with dynamic labels. Visible focus rings are essential for keyboard accessibility.
**Action:** Always add `title`, dynamic `aria-label`/`aria-expanded` (for toggles), and consistent `focus-visible` styles (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4]`) to interactive elements.
