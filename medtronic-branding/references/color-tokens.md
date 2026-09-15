# Medtronic Color Tokens

Source: `doc-color-palette-breakdown.pdf` (Global Brand). Values below are exact — do not
approximate or invent new colors. If a needed color/shade isn't listed, use the closest tint
from a tint stack below rather than picking an arbitrary value ("Don't add new colors" is an
explicit brand rule).

## Primary palette

| Name | Hex | RGB | CMYK | Notes |
| --- | --- | --- | --- | --- |
| Electric Blue | `#1010EB` | 16, 16, 235 | 100, 74, 0, 4 | Primary brand color. Digital-first — looks best on screen. Use thoughtfully, don't overuse (it's vibrant/loud). Pantone 286 C. |
| Navy Blue | `#140F4B` | 20, 15, 75 | 100, 97, 0, 58 | Foundational secondary blue. Pantone 2766 C. |
| Navy Blue (digital text variant) | `#170F5F` | 23, 15, 95 | — | Use this specific value (not `#140F4B`) for headlines/text on digital surfaces for better legibility. |
| White | `#FFFFFF` | 255, 255, 255 | 0,0,0,0 | Primary canvas color — layouts should be light and bright, generous white space. |
| Atmospheric White | `#F5F5F5` | 245, 245, 245 | 0,0,0,7 | Off-white for subtle section backgrounds / cards, not pure white. |

## Text / neutral

| Name | Hex | RGB | CMYK |
| --- | --- | --- | --- |
| Body Text Dark Gray | `#3C3C3C` | 60, 60, 60 | 0,0,0,80 |
| Disclaimer Dark Gray (tint) | `#777777` | 119, 119, 119 | 0,0,0,55 |

## Accent palette

Use accents **sparingly** — for callouts, infographic segments, chart series, alerts, illustration
color, or small secondary-headline labels (eyebrows/captions). Never as a primary brand color,
never for product-name text, never as the dominant color of a layout.

| Name | Hex | RGB | CMYK |
| --- | --- | --- | --- |
| Light Blue | `#0FC9F7` | 15, 201, 247 | 86, 2, 0, 0 |
| Teal | `#00DCB9` | 0, 220, 185 | 73, 0, 43, 0 |
| Green | `#7ECA2A` | 126, 202, 42 | 50, 0, 100, 0 |
| Orange | `#FFAD00` | 255, 173, 0 | 0, 32, 100, 0 |
| Pink | `#E5057F` | 229, 5, 127 | 0, 100, 0, 0 |
| Purple | `#C529BB` | 197, 41, 187 | 34, 90, 0, 0 |
| Lavender | `#654BDD` | 101, 75, 221 | 73, 68, 0, 0 |
| Red | `#ED002A` | 237, 0, 42 | 0, 100, 94, 0 |
| Brown | `#7B4D35` | 123, 77, 53 | 27, 63, 71, 45 |

## Tint stacks (10-step, dark → light)

Use tints instead of opacity/alpha tricks when you need a lighter/darker variant of a brand
color (e.g., chart series, hover states, subtle backgrounds). Order is darkest (index 0, "shade
900"-ish) to lightest (index 9, "shade 50"-ish).

**Light Blue family** (the `#0FC9F7` accent's tint stack — **not** the Medtronic Blues / Navy stack;
for Navy and Electric Blue tints see the `Medtronic Blues` stack in [ui-design-system-colors.md](./ui-design-system-colors.md)):
`#082542, #083C71, #0A5694, #0073B4, #009BDA, #0FC9F7, #48D6F9, #86E4FB, #C2F1FD, #E1F8FE`

**Teal**:
`#002922, #003D33, #006655, #008F77, #00B899, #00DCB9, #00F5CC, #66FFE2, #AAFAF0, #D6FFF8`

**Green**:
`#1C2A0A, #26460F, #376415, #599518, #64AD28, #7ECA2A, #9EDD5A, #BEE891, #DFF4C8, #EFF9E3`

**Orange**:
`#331D05, #4A2D00, #8C5300, #CC7A00, #F59300, #FFAD00, #FFC240, #FFD780, #FFEBBF, #FFF5DF`

**Pink, Purple, Lavender, Red, and Brown tint stacks are already published in full** in
[ui-design-system-colors.md](./ui-design-system-colors.md) — read them there.

## Usage rules (from brand guidelines)

- **Lead with blue.** Blue + white should dominate every layout. Don't build layouts dominated by
  heavy blocks of accent color.
- **Gradients**: `electric-blue → blue` or `light-blue → teal` linear gradients are allowed for
  graphic fills, bold strokes, and bold-weight headlines ≥18pt on light backgrounds. Use
  sparingly — not on body text, not overused.
- **Dark mode**: use a *less saturated* Electric Blue for text/UI on dark surfaces (full-strength
  `#1010EB` vibrates/is harder to read on dark backgrounds). Don't use the desaturated variant
  outside dark mode.
- **Accessibility**: the palette was chosen to meet WCAG/ADA contrast standards, but you must
  still verify any color+size combination you use (especially accent-on-white or white-on-accent)
  with a WCAG AA contrast checker — don't assume every pairing passes.
- **Never invent new brand colors.** If a design need isn't covered by this palette, use a tint
  from the stacks above.

## Design-tool swatches

Adobe Swatch Exchange files (import into Illustrator/Figma-via-plugin) are bundled at
[`../assets/colors/`](../assets/colors/): `RGB_Medtronic_color_swatches.ase`,
`CMYK_Medtronic_color_swatches.ase`, `PANTONE_Medtronic_color_swatches.ase`.
