## 2024-10-24 - Optimal Keyboard Accessibility Focus Rings
**Learning:** Using default browser focus outlines often conflicts with custom styles or branding, especially on icon buttons and navigation elements. Using `focus-visible` classes ensures visible focus rings only when navigating via keyboard, without cluttering the UI on mouse clicks.
**Action:** Always include `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm` on interactive elements to align with project branding and provide clear keyboard navigation feedback.
