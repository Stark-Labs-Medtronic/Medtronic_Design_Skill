# UI components — badges, segmented buttons, carousels, accordions, flags, hero banners, key-value pairs, user avatars

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide) — handed to this skill
directly by a user with authenticated access, pasted verbatim as data. Covers several smaller
component pages: "Alerts - Badges", "Segmented buttons", "Carousels", "Expansion Panels", "Flags",
"Hero Banners", "Key value pairs", "User avatars".

## Badges

A badge is a small circle (or pill, for text) near an anchor element, showing a count or drawing
attention.

| Variant | Size (W×H) | Notes |
| --- | --- | --- |
| Dot notification | 24×24px | Generic attention-getter, no count |
| Number notification | 24×24px | Shows a count |
| Notification on text | 51×24px | Badge attached to a text label rather than an icon |

- **Two types:** numbered (has an associated count) vs dot (generic, just draws attention — no
  count needed).
- **Default position:** upper-right of the anchor element.
  - Numbered badge on a 24px icon inside a 48px bounding box: **2px padding** from the top-right
    edge of that bounding box.
  - Dot badge on a 24px icon: **1px padding** from the top-right edge of the icon's own 24×24
    bounding box (not a separate touch-space box).
- **Extended number:** badge width grows to fit its content (not fixed at 24px wide). For large
  counts, show **"99+"** or **"999+"** rather than the literal number.

## Segmented buttons

Serve as either an alternative to checkbox/radio-button behavior, or as a tertiary navigation
control (switching between views/tabs without a full tab bar).

Two background contexts, each with 3 content-density variants:

| Variant | Size (W×H) | Context |
| --- | --- | --- |
| Standard simple | 375×32px | Light/standard background |
| Small text simple | 162×24px | Light/standard background, compact text-only |
| Icon simple | 288×40px | Light/standard background, icon-bearing |
| Standard contrast | 375×32px | Contrast (dark) background |
| Small text contrast | 162×24px | Contrast (dark) background, compact text-only |
| Icon contrast | 288×40px | Contrast (dark) background, icon-bearing |

All sizes above are reference-example widths — segmented buttons should size to their content/
container, not be hardcoded to these exact widths.

## Carousels

Slideshows that page through a set of same-sized images or banners.

- **Carousel spinner** (page indicator): 240×32px, 1px inside border.
- Shows the current page/position and lets the user page to the previous or next image.
- Placement: centered **below** the images, or overlaid within them at the bottom.

## Expansion panels (accordions)

Deliver large amounts of content in limited space — user sees an abstract/title, expands for
detail.

**Two behavior types — pick deliberately, don't default without thinking:**

- **Single-open accordion:** only one section can be expanded at a time; expanding a new section
  auto-collapses the previously-open one. Use when each section's content should be focused on
  individually and there's no need to compare/view multiple sections at once.
- **Multi-open accordion:** any number of sections can be expanded simultaneously; collapsing
  requires an explicit user action per section. Use when users may want to view multiple sections
  side-by-side.

| Variant | Size (W×H, reference example) | Notes |
| --- | --- | --- |
| Bordered (default) | 496×329px | Horizontal rule divides each panel; title/content height adjusts to fit content |
| Alt | 496×329px | Content area further differentiated with an "atmospheric white" content box |
| Filled | 496×345px | |

## Flags

Small colored indicators for tagging/labeling (distinct from `General.Semantic.*` status flags in
`ui-design-system-colors.md` — these are generic tag/label chips, not semantic-status indicators).

| Variant | Size (W×H) | Fill | Border radius |
| --- | --- | --- | --- |
| With accent | 51×24px | `#F5F5F5` (`Standard colors.Neutral.10`) | 4px |
| Without accent | 47×24px | `#F5F5F5` (`Standard colors.Neutral.10`) | 4px |

Both use a 1px inside border. Sizes are reference examples for their example label text — actual
flag width should fit its label content.

## Hero banners

Naming convention: **[Header treatment] + [Size] + [Background theme]** — read it as three
independent choices, not a fixed enum of named presets.

- **Header treatment:** `Transparent` (hero image extends behind/behind a see-through header —
  desktop/tablet only) vs `Below Nav` (hero sits below a normal opaque header, optional
  breadcrumbs above it — the only pattern used on mobile).
- **Size:** `Large` or `Medium` (no exact pixel heights were given in the source page).
- **Background theme:** `Light` or `Dark` (pick per `ui-design-system-colors.md` /
  `dark-mode-ui-colors.md` text/icon tokens for correct contrast).

| Breakpoint | Available combinations |
| --- | --- |
| Desktop | Transparent Large Light, Transparent Medium Light, Below Nav Medium Light, Transparent Large Dark, Transparent Medium Dark, Below Nav Medium Dark |
| Tablet | Transparent Large Dark, Transparent Large Light |
| Mobile | Below Nav Medium Light, Below Nav Large Dark |

**Gap:** no exact pixel heights for Large vs Medium were given in the source text (only shown in
diagrams) — don't invent specific numbers; ask for/confirm against the Figma file if an exact
height is required.

## Key-value pairs

Displays a set of attributes/parameters belonging to an object (e.g. a label + its value, stacked
or side-by-side). Two reference sizes: standard 41×48px, small 36×41px — treat as example sizes
for their sample content, not fixed dimensions (a key-value pair should size to its label/value
text).

## User avatars

Supplementary visual identifier for a person. All three styles share a 40×40px footprint and a
90px border radius (fully circular at this size, same idea as a 9999px radius elsewhere in this
system):

| Style | Fill / border | Notes |
| --- | --- | --- |
| Icon | Fill `#100D78` (`Text & Icon.Normal.Accent`) | Generic person icon on a solid accent-color circle |
| Initials | Fill `#100D78` | User's initials on a solid accent-color circle; used extensively in the Global Header/Application Shell/Mobile shell (confirms the avatar's home is the header, per `global-header.md`'s avatar-popover mention) |
| Profile picture | 2px border in `#100D78` (no fill) | Frames an actual user photo instead of a color fill |
