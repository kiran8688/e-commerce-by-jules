## 2024-06-22 - Consistent Keyboard Navigation Focus Rings
**Learning:** Icon-only interactive elements in the AppShell lacked visible focus states. Relying on default browser outlines can cause inconsistent and visually unappealing focus rings that don't match the design system.
**Action:** Implemented a standard focus ring pattern for interactive elements using `rounded-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4]` to ensure clear, brand-aligned keyboard navigation.
