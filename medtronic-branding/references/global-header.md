# Global header

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Global Header" page) —
handed to this skill directly by a user with authenticated access, pasted verbatim as data.

## The one hard rule

**The header bar is always exactly 64px tall, on every platform.** This is deliberate: keeping the
header height identical across an app's different surfaces (and across different Medtronic apps)
avoids a visual "jump" when a user moves from one app/page to another. Don't scale the header
height responsively — only its *contents* (logo, app name, search) adapt; the 64px bar itself
never changes, mobile included.

> **This governs the 64px header bar itself, not a page's entire top chrome.**
> [navigation.md](./navigation.md)'s website-style top-nav footprint is documented as 1440×121px —
> that's this same 64px header **plus** a separate ~56px nav row stacked directly under it
> (confirmed in the real shipped CSS,
> [mdt-app-template.css](../assets/code-templates/html-css-framework/css/mdt-app-template.css):
> `grid-template-rows: 64px 56px` once a nav row is present, ≈120px + a 1px border ≈ 121px). A page
> with both a header and a below-header nav row is not a violation of the 64px rule — the rule
> governs the header row in isolation. Logged in `SKILL.md`'s Contradiction Ledger.

## Two header styles

Both are 64px tall, fill `#F5F5F5` (`General.Surface.level 1`), 1px inside border. Background can
be white, gray, or transparent in either style.

| Style | Width behavior | Content alignment |
| --- | --- | --- |
| **Application style** | Expands to 100% of viewport width | Edge-to-edge; hamburger menu (left) toggles the side nav; avatar component (right) opens a popover (profile / user prefs / log out) |
| **Website style** | Has a max-width | Content centered, with auto-expanding left/right margins |

App name is optional but recommended next to the logo — see `app-header-logo-lockup.md` for the
exact logo+app-name lockup measurements (baseline alignment, cap-height matching).

## Responsive behavior

As viewport width shrinks:

- The app name and Medtronic logo shrink and become **stacked** (vertically) rather than staying
  inline side-by-side.
- A search field can be replaced with a compact search **button** that expands into a full search
  field on focus, instead of always showing a full-width input.
- Mobile header footprint: 375×64px — same 64px height rule as desktop, only the content inside
  adapts.

Working header HTML examples (no-nav, simple-nav, dropdown-nav variants) are bundled at
[assets/code-templates/html-css-framework/](../assets/code-templates/html-css-framework/) —
`header-no-nav.html`, `header-simple-nav.html`, `header-dropdown-nav.html`.
