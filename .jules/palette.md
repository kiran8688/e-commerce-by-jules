## 2024-05-24 - [Title attributes for Icon Buttons]
**Learning:** Icon-only navigation buttons in the `AppShell.jsx` (such as Search, Account, and Cart) rely entirely on `aria-label` for screen readers, but lack visible tooltips for sighted mouse users. Adding the native `title` attribute matching the `aria-label` makes their function clear to all users when hovered.
**Action:** When adding new icon-only controls, always include a `title` attribute alongside the `aria-label` for full accessibility.

## 2024-05-24 - [Mobile Menu Dynamic Aria State]
**Learning:** The mobile menu toggle lacked a dynamic `aria-expanded` state. Screen readers need to know whether the menu is open or closed, so toggling `aria-expanded` dynamically based on state, along with updating the `aria-label` and `title`, provides essential context.
**Action:** Always implement `aria-expanded` and state-aware accessible names on toggle buttons that control expanding/collapsing sections.

## 2024-05-24 - [Keyboard Focus Visibility]
**Learning:** Interactive elements like the `Link` components used for navigation icons and the `button` element for search lacked visible focus indicators, making keyboard navigation difficult to track.
**Action:** Use `focus-visible:ring-2` and `focus-visible:ring-[color]` utility classes to ensure a clear, customized focus ring appears during keyboard navigation, without disrupting mouse interactions.