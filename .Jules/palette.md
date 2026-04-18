## 2024-04-18 - [Auth Form Accessibility]
**Learning:** Forms missing `htmlFor` on labels and explicit `id` attributes on inputs break screen reader accessibility and label-clicking focus. Missing `focus-visible` ring styles hinder keyboard navigability.
**Action:** Always ensure 1:1 `id` to `htmlFor` mapping in forms, set inputs as `required` when applicable, provide descriptive placeholders, and include clear focus states (`focus-visible:ring-2`, `focus:outline-none`) for interactive elements.
