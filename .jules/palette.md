## 2026-07-06 - Improve accessibility for focus-hidden elements
**Learning:** Elements that rely solely on `group-hover:opacity-100` are inaccessible to keyboard users as they don't appear on focus.
**Action:** Pair `group-hover:opacity-100` with `focus-within:opacity-100` to ensure interactive elements become visible to keyboard users.

## 2026-09-19 - Improve keyboard accessibility for hero buttons
**Learning:** Hero buttons that trigger scroll actions need clear focus states to ensure keyboard users can navigate to and interact with them effectively.
**Action:** Always add explicit `focus-visible` ring styles to primary call-to-action buttons, especially on colored backgrounds.

## 2026-09-20 - Add skip-to-content link for better keyboard navigation
**Learning:** Single page applications without skip links force keyboard users to navigate through all header links on every page transition.
**Action:** Always provide a visually hidden skip-to-content link at the top of the AppShell that bypasses navigation.
## 2026-09-23 - Add navigation active states

**Learning:** Users need a clear visual indicator to understand which page they are currently on. `react-router-dom`'s `NavLink` provides a clean way to implement this while automatically adding the `aria-current="page"` attribute for screen readers, improving both visual feedback and accessibility simultaneously.
**Action:** Whenever building navigation menus, prefer `NavLink` over `Link` to easily manage active states and ensure proper accessibility attributes are applied.
## 2026-09-24 - Provide password visibility toggle for authentication
**Learning:** Found that the password input was lacking a visibility toggle. This small micro-UX improvement significantly improves usability and accessibility, reducing cognitive load on users trying to ensure they typed complex passwords correctly, especially on mobile.
**Action:** Always include a show/hide password toggle on all standard password inputs, equipped with clear `aria-label` attributes for screen readers.

## 2026-09-25 - Provide helpful guidance in empty states
**Learning:** Generic bare-text empty states leave users at a dead end and feel unpolished, reducing the perceived quality of the interface.
**Action:** Always replace bare text empty states with stylized containers featuring an illustrative icon, a clear heading, and helpful body text to improve user guidance and maintain engagement.

## 2026-09-28 - Add loading states to asynchronous form submissions
**Learning:** Forms that lack explicit loading states on their submission buttons leave users uncertain if their action registered, often leading to duplicate clicks, errors, and a degraded perception of reliability.
**Action:** Always pair asynchronous form submissions with a clear visual loading indicator (e.g., a spinner and updated text like "Submitting...") and apply a disabled state to the button to prevent multiple submissions.
## 2026-09-29 - Mobile Menu Keyboard Accessibility
**Learning:** Native Escape key dismissal and explicitly linking toggle buttons to dropdown menus via aria-controls are crucial for mobile menu accessibility.
**Action:** Always implement Escape key listeners for modal/dropdown closures and use aria-controls to programmatically associate trigger elements with the content they control.
## 2026-10-01 - Consistent Directional Micro-Interactions on CTAs
**Learning:** Found that applying consistent directional arrows (ArrowRight for navigation, ArrowDown for scroll) with transform hover effects (`group-hover:translate-x-1`, `group-hover:translate-y-1`) establishes a clear, predictable interaction pattern for primary CTAs throughout the application.
**Action:** Always pair navigational CTAs with a directional icon and apply a `transition-transform` group hover effect to reinforce the action's outcome, while ensuring the icon is hidden from screen readers (`aria-hidden="true"`).
## 2026-10-02 - Missing Focus Visible on Text Links
**Learning:** The desktop navigation, mobile navigation, and footer text links in `AppShell.jsx` lacked `focus-visible` styles, making keyboard navigation difficult for accessibility.
**Action:** Ensure all text-based interactive links (`<Link>`, `<NavLink>`, `<a>`) include `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm` (or similar standard focus styling) so keyboard users can clearly see the active element.
## 2026-10-03 - Fix WCAG 2.5.3 Label in Name violation on Product Cards
**Learning:** Overriding visible text inside buttons with `aria-label` (e.g., visible "Quick Add", aria-label "Add to cart") breaks WCAG 2.5.3. Voice dictation users who say "Click Quick Add" will fail because the software only sees the `aria-label`.
**Action:** Use visually hidden text (`sr-only`) appended to the visible text instead of overwriting with `aria-label` to ensure the accessible name contains the visible text.
## 2026-10-04 - Manage Focus on Smooth Scroll Links
**Learning:** When building "Explore" or "Scroll down" buttons that navigate to different sections of the same page, keyboard users are left behind if focus isn't programmatically moved. Even though the page visually scrolls, their tab position remains at the top.
**Action:** Always add `tabIndex={-1}` and `className="focus:outline-none scroll-mt-6"` to the target container, and explicitly call `target.focus({ preventScroll: true })` after scrolling to sync the keyboard focus with the visual viewport.
## 2026-10-05 - Add Disabled States to Auth Form Interactions
**Learning:** Forforms simulating async processes (`isLoading`), failing to disable text inputs and toggle buttons alongside the submit button creates a confusing experience and risks unexpected form state mutations.
**Action:** Always comprehensively disable interactive form elements (inputs, toggles, selects) using `disabled={isLoading}` along with appropriate `disabled:` visual styles to ensure user interaction is completely paused during submission.
## 2026-10-06 - Improve accessibility for dynamic content
**Learning:** Users relying on screen readers need immediate feedback when interactive elements like password visibility toggles change state. Without it, the interface can feel unresponsive or confusing.
**Action:** Always include an `aria-live` region to announce dynamic state changes (e.g., "Password is now visible") and use `aria-pressed` on toggle buttons to explicitly convey the current state to assistive technologies.
## 2026-10-07 - Do not rely solely on color for active navigation states
**Learning:** Relying solely on color changes (e.g., changing text from gray to blue) to indicate the active navigation state violates WCAG 1.4.1 (Use of Color), making it difficult for users with visual impairments to discern the active page.
**Action:** Always provide an additional structural or visual indicator for active navigation states, such as an underline (`underline decoration-2`), font weight change (`font-semibold`), or a distinct background color (`bg-[#eef1f3]`).

## 2026-10-08 - Provide visual feedback for list-level actions
**Learning:** Actions taken on items within a list or grid (like "Add to Cart" on a product card) often lack feedback, leaving the user uncertain if their action succeeded without navigating to a separate view (like the cart page).
**Action:** Always provide inline, transient visual feedback for list-level actions (e.g., briefly changing the button state to "Added!" with a checkmark) and pair it with an `aria-live` region to inform screen reader users of the success.
## 2026-10-10 - SPA Navigation Accessibility
**Learning:** Single Page Applications (SPAs) built with raw React Router often fail to announce page changes to screen readers and trap keyboard focus on the navigation link that was just clicked, leading to a confusing accessibility experience.
**Action:** Always implement a route-change listener that updates the `document.title` and programmatically shifts focus to the `#main-content` container (using `tabIndex={-1}`) to simulate native multi-page navigation behavior.

## 2026-10-12 - Improve hit area and active states for header icon buttons
**Learning:** Icon-only buttons often suffer from small clickable hit areas on touch/mouse, and relying solely on color changes for active states violates WCAG 1.4.1 (Use of Color). Furthermore, internal SVG icons without `aria-hidden="true"` can be redundantly announced by screen readers when wrapped in a button with an `aria-label`.
**Action:** Always wrap icon buttons with a minimum padding (e.g., `p-2`), provide a subtle hover background color (`hover:bg-[#eef1f3]`), use background color to indicate active states (`bg-[#eef1f3]`), and ensure internal SVGs have `aria-hidden="true"`.
## 2026-10-13 - Add Caps Lock Warning to Authentication Form
**Learning:** Users often enter their passwords with Caps Lock mistakenly on, leading to frustrating failed login attempts.
**Action:** Always include a visual warning (e.g., "Caps Lock is on") associated with password inputs, utilizing `e.getModifierState("CapsLock")` and `aria-describedby` for accessibility.
## 2026-10-14 - Smooth Image Loading Reveals and Tooltips
**Learning:** Images loading abruptly can cause a jarring pop-in effect that reduces perceived UI quality. Truncated text via `line-clamp` makes it impossible for users to read the full content if it is cut off.
**Action:** Always wrap images with a state-driven opacity transition (`opacity-0` to `opacity-100` on load) for a smoother reveal, and provide a `title` attribute for truncated text elements so users can hover to read the full text.
## 2026-10-16 - SPA Scroll Restoration
**Learning:** Single Page Applications built with React Router don't automatically reset the scroll position to the top on page navigation. This leaves users scrolled halfway down the page when they land on a new route, which feels broken and confusing compared to native multi-page applications.
**Action:** Always implement a route-change listener that explicitly calls `window.scrollTo({ top: 0, left: 0, behavior: 'instant' })` to restore scroll position predictably on every navigation event.
## 2026-10-17 - Keyboard shortcuts for common actions
**Learning:** Adding keyboard shortcuts (like '/' for search) significantly improves navigation speed for power users and keyboard-reliant users. Visual cues like `<kbd>` tags help discoverability.
**Action:** Implement global keydown listeners for primary actions (Search, Cart) and visually indicate the shortcut in the UI and via `aria-keyshortcuts`.
## 2026-10-18 - Mobile Menu Click-Outside Dismissal
**Learning:** Relying solely on a close button or the Escape key for mobile menus leaves out users who naturally try to tap outside the menu to dismiss it. Not having click-outside handling creates a frustrating "trap" UX on touch devices.
**Action:** Always implement a click-outside handler (`mousedown` and `touchstart`) for custom dropdown menus and modals, ensuring it checks if the click occurred outside both the menu itself and its toggle button.
## 2026-10-19 - Mobile Menu Backdrop Stacking
**Learning:** Adding a full-screen backdrop to a mobile dropdown menu without portal complexity requires precise z-index coordination.
**Action:** Place the `fixed z-40` backdrop as a sibling immediately preceding the `sticky z-50` header. This ensures the header and its internal dropdown remain accessible and layered above the obscured main content.

## 2026-10-20 - Prevent scroll bleed on mobile menu
**Learning:** When a full-screen mobile menu or backdrop is open, allowing the underlying `<body>` to scroll creates a disorienting user experience, often referred to as "scroll bleed". This makes the interface feel unpolished and confusing to navigate, especially on touch devices.
**Action:** Always apply `overflow: hidden` to the `document.body` when a full-screen modal or mobile menu backdrop is active to prevent background scrolling, and ensure it is cleaned up on unmount or closure.

## 2026-10-21 - Restore Focus After Mobile Menu Closure
**Learning:** When users dismiss a mobile dropdown menu using the Escape key, simply closing the menu causes focus to be lost (resetting to the `body`). This forces keyboard and screen reader users to navigate from the top of the page again.
**Action:** Always restore focus programmatically to the toggle button (e.g., using `document.querySelector('[aria-controls="menu-id"]').focus()`) immediately after a user dismisses its associated menu or modal via the Escape key.
