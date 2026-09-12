# Composition — breakpoints, grid, and UI shell selection

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Composition" page) —
handed to this skill directly by a user with authenticated access, pasted verbatim as data.
Breakpoint content-area widths are cross-validated against the real `mdt-app-template.css`
(`max-width: 1312px` at desktop, mobile-first `min-width` media queries at 480/768/1200px) — see
[typography.md](./typography.md)'s source note for the same code kit.

## Breakpoints

All padding is **inside** the specified artboard width — subtract it to get the content area.

| Tier | Artboard width | L-R padding | Content area | Breakpoint range |
| --- | --- | --- | --- | --- |
| Desktop | 1440px (max-width) | 64px (`4rem`) | 1312px | `> 1200px` |
| Laptop + tablet landscape | 1200px | 48px (`3rem`) | 1104px | `768px–1200px` |
| Tablet portrait | 768px | 32px (`2rem`) | 704px | `480px–768px` |
| Mobile | 375px | 16px (`1rem`) | 343px | `240px–480px` |

```css
/* Base styles (mobile) — no query needed, this is the default */
/* Tablet portrait and up */
@media (min-width: 480px) { ... }
/* Tablet landscape / laptop and up */
@media (min-width: 768px) { ... }
/* Desktop and up */
@media (min-width: 1200px) { ... }
```

Mobile-first, matching the real shipped `mdt-app-template.css` exactly (`min-width: 480px`,
`min-width: 768px`, `min-width: 1200px`). An earlier revision of this snippet used desktop-first
`max-width` queries, which is the opposite cascade direction from the CSS this file claims to be
cross-validated against — corrected. If you write `max-width` queries instead, they must cascade in
the opposite pixel order (widest first) or later rules silently win over earlier ones.

This **supersedes** the generic 3-tier breakpoint convention previously documented in
[layout-and-spacing.md](./layout-and-spacing.md) §3 for anything built to this Design System — use these four exact
tiers/pixel values instead of the simplified generic ones.

## Grid and spacing scale

8px grid: spacing between UI elements should be multiples of 8px. Smaller components (icons,
type) may align to a 4px grid instead.

> **`[MANDATORY]` These are gap/padding/margin values only.** Never use a value from this table as
> the width or height of a logo, lockup, Symbol, or icon. Brand-asset dimensions come from
> [sizing-standard.md](./sizing-standard.md) §0 and nowhere else — a 4px logo is always a bug.

| Spacing | Value | Sass variable |
| --- | --- | --- |
| None | 0 | `$spacing-none` |
| xxs | 4px (`0.25rem`) | `$spacing-xxs` |
| xs | 8px (`0.5rem`) | `$spacing-xs` |
| s | 16px (`1.0rem`) | `$spacing-s` |
| m | 24px (`1.5rem`) | `$spacing-m` |
| l | 32px (`2.0rem`) | `$spacing-l` |
| xl | 40px (`2.5rem`) | `$spacing-xl` |

Each tier maps to numbered utility classes (`.p-0`…`.p-6`, `.m-0`…`.m-6`, and their
`t`/`b`/`l`/`r`/`x`/`y` directional variants) — e.g. `$spacing-s` (16px) = `.p-3`/`.m-3`.

**Responsive layout:** a 12-column grid made of margins, columns, and gutters. Margin and column
widths stay fixed to keep spacing consistent as the layout responds.

## The pixel, defined

"Pixel"/"px" in this Design System always means a **software/virtual pixel** (a CSS px / density-
independent point), not a physical hardware pixel — high-DPI/Retina-style displays render more
physical pixels per software pixel via a scaling factor. When choosing an artboard size, use the
OS/device's coordinate-system size (e.g. a 12.9" iPad Pro is 2732×2048 hardware pixels at a 2.0x
scale factor, so design at 1366×1024).

## Choosing a UI shell

Two distinct shell patterns — pick based on what the product *is*, not by default:

| Shell | Top nav behavior | Best for |
| --- | --- | --- |
| **Website-style** | Top global nav sticks as content scrolls beneath it | Content-driven platforms (marketing sites, docs, informational pages) |
| **Web app-style** | Static top nav + a collapsible/expandable side nav (toggled via the header's hamburger menu), with a floating main-content card | Actionable, data/interaction-driven platforms (dashboards, tools, admin UIs) |

Both have documented background-treatment variants (gray header + white body, white header + gray
body, transparent header + full link-farm footer, gray header + full link-farm footer) — these are
purely visual skins, pick based on the page's content density and desired emphasis, not a hard
rule.

**Mobile:** both shell styles converge to the same mobile layout (nav hidden behind a hamburger
menu that slides out full-width when tapped) — see [global-header.md](./global-header.md) and
[navigation.md](./navigation.md) for the exact side-nav mobile behavior.
