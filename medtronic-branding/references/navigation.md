# Navigation components

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Navigation" and
"Footer" pages) — handed to this skill directly by a user with authenticated access, pasted
verbatim as data. Figma component links from the source are preserved as citations, not fetched
(they require an authenticated Figma seat this skill doesn't have).

## Top nav (website-style shell)

- **Flat header:** 1440×121px (64px header + 56px nav row, per `global-header.md`'s 64px hard
  rule — see that file's reconciling note; this is not a violation of it), 1px inside border, no
  fill specified (transparent/inherits page bg).
- **Floating header:** same 1440×121px footprint, fill `#F5F5F5` (`General.Surface.level 1`), 1px
  inside border, plus a 3-layer drop shadow:
  `0 3px 5px rgba(0,0,0,0.1)`, `0 1px 18px rgba(0,0,0,0.06)`, `0 6px 10px rgba(0,0,0,0.06)`
  (stacked, low-to-high blur — gives a soft "floating card" elevation look).
- Can optionally open a **flyout menu** with multiple levels of links (subnav). Subnav items have
  hover/active/default visual states (no new tokens beyond the standard interactive-state colors
  in `ui-design-system-colors.md`).

## Side nav (web app-style shell)

- Expands/collapses via the hamburger menu in the global header (see `global-header.md`).
- Desktop application shell: 1440×1024px, fill `#FFFFFF` (`General.Surface.level 0`), 1px inside
  border — same footprint whether nav is expanded or collapsed (the side nav overlays/pushes
  content, doesn't resize the shell).
- Mobile shell: 375×812px. On mobile the side nav is **fully hidden** inside the hamburger menu;
  tapping it slides the nav out to fill the entire screen width (not a partial-width drawer).

## Breadcrumbs

| Variant | Size (W×H) | Notes |
| --- | --- | --- |
| Standard (desktop) | 271×40px | 1px inside border |
| Mobile/Simple | 81×40px | Shows a back arrow in Electric Blue + only the previous page's name |
| Overflow | 167×40px | For long crumb trails |

Rules:

- Never shown on the Home or primary landing page — only on second-level pages and deeper.
- The current page is **not** shown as a clickable crumb — the trail ends in a bare `/`, and the
  current page's title displays immediately below the breadcrumb bar using the page-title text
  style (`h1`/`.txt07-headline`, see `typography.md`).
- Every segment in the trail is clickable and navigates to that level.

## Tabs

Tabs swap the content in a content area below them — they must **not** reload the whole page,
only that content section.

| Variant | Size (W×H) | Fill |
| --- | --- | --- |
| Filled style | 800×56px | `#F5F5F5` (`General.Surface.level 1`) |
| Outline style | 800×56px | none (border only) |

Both use a 1px inside border. 800px is the reference/example width, not a fixed constraint — tabs
should size to their container.

## Popover menus

Generic anchored container that opens from a triggering element (usually a button).

- Size (reference example): 240×224px, fill `#FFFFFF` (`General.Surface.level 0 elevated`), 1px
  inside border.
- Drop shadow (3-layer, use together as one recipe):
  `0 1px 8px rgba(0,0,0,0.12)`, `0 3px 4px rgba(0,0,0,0.14)`, `0 3px 3px rgba(0,0,0,0.2)`.
- Variants: plain container, nested/secondary menu (use a right-chevron icon to indicate further
  expansion), grouped items (visual sections within one popover), and a checkbox-list popover.
- This shadow recipe is reusable for any dropdown/menu/select-panel component, not just this
  specific popover — it's the Design System's general "elevated floating surface" treatment.

## Anchor links

- Float above page content, positioned in the **bottom** portion of the viewport (not top/side).
- Do **not** indicate current scroll position — they're bookmarks to a scroll position on the
  current page only, not a "you are here" indicator.
- Pair with a **"Back to top"** button, floating bottom-right, at the same horizontal position as
  the anchor links — it scrolls the user back to the top of the page.
- Optional: the anchor-link cluster can be mostly hidden (showing only a small visible edge) and
  slide fully into view on hover.

## Footer

Three named variants exist: **Footer** (standard), **Footer with link farm** (`.com`-style, dense
multi-column link list), **Footer (minimal)**. The source page gave names/screenshots only, no
exact size/color tokens — but the real `mdt-app-footer.css` (bundled at
[assets/code-templates/html-css-framework/css/mdt-app-footer.css](../assets/code-templates/html-css-framework/css/mdt-app-footer.css))
confirms the footer is a **dark surface with white text** (`--mdtTextWhite`, white-bordered
dividers, hover links turn `--mdtTextLinkDkBg` `#86A9FF` with a dashed underline) — this
corroborates the white-logo-on-footer guidance in `app-header-logo-lockup.md` over the
navy-text-showing reference screenshot flagged there as a likely mismatch.

Two working footer HTML examples are bundled at
[assets/code-templates/html-css-framework/footer-standard.html](../assets/code-templates/html-css-framework/footer-standard.html)
and
[footer-minimal.html](../assets/code-templates/html-css-framework/footer-minimal.html).
