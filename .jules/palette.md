## 2024-05-13 - [AppShell Header Accessibility]
**Learning:** When modifying `aria-label` or adding interactive semantic attributes (like `title`, `aria-expanded`, or `aria-controls`) to core navigation components (like `AppShell.jsx`), it is vital to pair icon-only interactive elements with `focus-visible` styling (`focus-visible:ring-2`) to ensure sighted keyboard users can navigate.
**Action:** Always add `title` and `focus-visible` utility classes to icon-only interactive elements to serve both screen readers and keyboard users.
