## 2026-04-16 - Auth Form Accessibility & UX
**Learning:** Found that the Auth form lacked basic HTML semantics like `htmlFor` on labels, `type="submit"` on buttons, and focus states. This prevents password managers from auto-filling correctly and makes keyboard navigation difficult.
**Action:** Always ensure that form inputs have associated labels (`htmlFor` matching `id`), use `type="submit"` for the primary action button to allow Enter key submission, add `autoComplete` attributes, and include clear focus states (`focus:ring-2`) for keyboard users.
