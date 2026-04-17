## 2026-04-17 - Accessible Auth Form
**Learning:** Discovered that form inputs in the auth components were missing semantic linkages (htmlFor/id) to their labels, which is critical for screen reader a11y. Forms also lacked required attributes for native validation and focus styles for keyboard navigation.
**Action:** When building or updating forms in this app, ensure every label has a `htmlFor` matching the input's `id`, add `required` attributes where appropriate, and always include `focus:ring-2 focus:outline-none` classes to maintain strong visual indicators for keyboard users.
