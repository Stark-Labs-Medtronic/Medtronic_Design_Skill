# Carbon Design System (third-party, supplementary layout reference)

**Source:** IBM's **Carbon Design System** (`carbondesignsystem.com`), a separate, independent,
open-source design system (Apache License 2.0) — **not** a Medtronic-authored source. Bundled
here as a full site crawl (356 pages, cleaned text + metadata; plus icons, pictograms, images,
documents, and data files) at
[assets/third-party/carbon-design-system/](../assets/third-party/carbon-design-system/).

## Why this is in a Medtronic branding skill

Two reasons, both traced to explicit Medtronic guidance rather than assumed:

1. **App icons:** [application-icons.md](./application-icons.md) documents that Medtronic's own
   Application Icon Template "uses the Carbon library as a baseline" — custom app icons should
   match Carbon's visual style (stroke weight, information density). The bundled
   `assets/third-party/carbon-design-system/assets/icons/` (2739 SVGs) and `.../pictograms/`
   (1565 SVGs) are exactly that reference icon set.
2. **Outer/page layout:** Medtronic's own UI Design System gives breakpoints, an 8px spacing grid,
   and a 12-column responsive grid at a summary level (see
   [composition.md](./composition.md)), but doesn't publish a full named grid-system spec (mini
   units, fixed/fluid/hybrid box rules, aspect-ratio guidance, per-breakpoint column/margin
   tables). Carbon's **2x Grid** and **Spacing** systems fill that gap as a generic, well-reasoned
   supplementary layout framework — use them for *structural* page-layout decisions Medtronic's
   own docs don't cover, never for colors/logo/typography (Medtronic's own tokens always win there).

**Precedence rule: Medtronic's own specs always take priority.** Only reach for Carbon's grid/
spacing system when building general page-shell/grid structure and nothing in
`composition.md`/`layout-and-spacing.md`/`sizing-standard.md` already covers it. Never substitute
Carbon's colors, type, icons (for anything other than app-icon baselining), or component visual
style for Medtronic's own — this file is layout-structure guidance only.

## The 2x Grid

IBM's foundational geometric system — "divide or multiply by two" to build visual rhythm.

- **Mini unit:** the base unit is an **8px square**. Margins, padding, and fixed-box dimensions
  are always multiples of the mini unit.
- **Three grid types:**
  - **Fluid grid** — divides available width by two repeatedly (column count fixed per
    breakpoint, column width scales with viewport). Best for editorial content, dashboards,
    images, data viz — anything better served by scaling size than scaling item count.
  - **Fixed grid** — tiles fixed-size boxes (from the sizing scale below); column count grows
    with viewport width, tiles wrap. Best for icon toolbars, card grids.
  - **Hybrid grid** — one dimension fixed, one fluid (no aspect ratio applied) — e.g. a header
    (fluid width, fixed height), a side panel (fixed width, fluid height).
- **Padding** is always 16px at all standard breakpoints; always align type to the edge of the
  padding, never place type *on* padding.
- **Gutters** = margin-around-each-box matching its padding, for a total 32px gutter between
  boxes when gutters are used at all (a gutterless grid is valid for closely related content).

### Breakpoints (2x Grid)

| Breakpoint | Value (px / rem) | Columns | Margin | Padding |
| --- | --- | --- | --- | --- |
| Small | 320 / 20 | 4 | 0 | 16px |
| Medium | 672 / 42 | 8 | 16px | 16px |
| Large | 1056 / 66 | 16 | 16px | 16px |
| X-Large | 1312 / 82 | 16 | 16px | 16px |
| Max | 1584 / 99 | 16 | 24px | 16px |

**These are Carbon's own breakpoints, distinct from Medtronic's** (1440/1200/768/375px in
`composition.md`) — don't mix the two breakpoint tables in one project. Pick one system per
project and stay consistent; default to Medtronic's own breakpoints unless the task specifically
calls for Carbon's finer-grained 5-tier system.

### Sizing scale (fixed base units)

| Size (px) | Mini units |
| --- | --- |
| 8 | 1x |
| 16 | 2x |
| 24 | 3x |
| 32 | 4x |
| 48 | 6x |
| 64 | 8x |
| 80 | 10x |

Pick a base size, then scale boxes by a consistent aspect ratio: **1:1, 2:1, 2:3, 3:2, 4:3, or
16:9** — constraining box dimensions to one of these ratios keeps a layout feeling unified.

### Screen regions and panel behavior

Standard named layout zones: Header, Global sidenav, Local sidenav, Dropdown menu, Content,
Footer, Dialog. Three panel behaviors:

- **Flexible panels** — fixed-width expanded state, collapse/expand on hover; pushes or condenses
  content when expanded.
- **Fixed panels** — static width, never collapses, sits outside the responsive grid entirely.
- **Floating panels** — float above content without affecting the grid, must be dismissible
  (tooltips/dropdowns/inline menus are also this category).

## Spacing scale

Complements the 2x Grid using multiples of 2, 4, and 8 — used *within* components (unlike the 2x
Grid's mini units, which are more about page/box structure):

| Token | rem | px |
| --- | --- | --- |
| `$spacing-01` | 0.125 | 2 |
| `$spacing-02` | 0.25 | 4 |
| `$spacing-03` | 0.5 | 8 |
| `$spacing-04` | 0.75 | 12 |
| `$spacing-05` | 1 | 16 |
| `$spacing-06` | 1.5 | 24 |
| `$spacing-07` | 2 | 32 |
| `$spacing-08` | 2.5 | 40 |
| `$spacing-09` | 3 | 48 |
| `$spacing-10` | 4 | 64 |
| `$spacing-11` | 5 | 80 |
| `$spacing-12` | 6 | 96 |
| `$spacing-13` | 10 | 160 |

Non-token spacing options also exist: `center` (fluidly center between two edges), `auto`
(one-sided growable/shrinkable space, typically asymmetric), `gutter` (space between the 12-column
grid's columns specifically).

## What's bundled, and what was deliberately excluded

| Bundled | Not bundled | Why |
| --- | --- | --- |
| `pages/**/content.md` + `meta.json` (cleaned text + metadata, ~9MB, 350 pages) | `pages/**/page.html` (raw rendered DOM) | The raw HTML alone was **~997MB** — almost entirely duplicated inline SVG icon-gallery markup already available standalone in `assets/icons/`/`assets/pictograms/`. Pure bloat with no unique content over `content.md`. |
| `assets/icons/*.svg` (2739 files), `assets/pictograms/*.svg` (1565 files) | — | The actual Carbon icon-baseline referenced by `application-icons.md` |
| `assets/images/*`, `assets/documents/*` (IBM color palettes, Carbon builder tool, MCP extension), `assets/data/*` (`llms.txt`, Carbon's own AI-agent instructions) | — | Kept per explicit instruction to bundle the full crawl |
| `catalog/*` (manifest.json, icons-manifest.json, pictograms-manifest.json, asset-index.json, external-resources.json, REPORT.md) | — | Indices needed to actually look up an icon/pictogram by name |
| — | A handful of malformed page folders derived from broken links in Carbon's own site content (URLs with query strings that produced pathological folder names) | Explicitly flagged in the crawl's own `catalog/broken-links.json` as dead links, not real content |

Use `catalog/icons-manifest.json` / `catalog/pictograms-manifest.json` to look up a specific icon's
file path by name rather than guessing a filename.

## Licensing note

Carbon Design System is IBM's open-source project, published under the **Apache License 2.0**.
This is separate from Medtronic's own proprietary brand assets bundled elsewhere in this skill —
don't present Carbon icons/patterns as Medtronic-original work, and don't apply Medtronic's
"never fabricate a brand fact" rule to Carbon content as if it were Medtronic's own (it's IBM's
published, public documentation, reproduced here for reference/baseline purposes only).
