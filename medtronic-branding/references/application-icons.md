# Application icons (App Store / Play Store)

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Application Icons"
page) — handed to this skill directly by a user with authenticated access, pasted verbatim as
data. Scope: the actual app-icon graphic submitted to the App Store/Play Store — not in-app
functional/thematic icons (see [brand-guidelines.md](./brand-guidelines.md) Iconography section for those) and not the
general Full-life Symbol used in logos/lockups (see [sizing-standard.md](./sizing-standard.md)).

## Overview

- App icons use a template baselined on the **Carbon design system** icon library
  ([carbondesignsystem.com/elements/icons/library](https://carbondesignsystem.com/elements/icons/library/),
  [Figma kit](https://carbondesignsystem.com/designing/kits/figma)) — use Carbon icons as-is, or
  as a starting point for a custom icon. Custom icons should match Carbon's visual style (stroke
  weight, information density) to stay consistent.
- Approved background options: **Gradient, Electric Blue, Navy, White**.
- Design tools: a Figma template (duplicate to your own Drafts to edit — ask Global Brand/Design
  Systems for the current link, not reproduced here since it requires an authenticated Figma
  account) and an Illustrator-and-other-tools ZIP template with a README (same access model).
  This skill does not bundle either template — they're design-tool source files, not final
  brand assets, and go stale quickly. Point a user to the Design System page directly if they need
  the actual template.

## Simplified Symbol (mobile app icons only)

A simplified version of the Full-life Symbol exists **specifically and only for mobile app icon
design** — reduced complexity for small sizes, while keeping the original's visual energy/forward
motion. Before using it, confirm no near-identical icon already exists for the same audience (to
avoid user confusion between apps).

Bundled at `assets/symbol/mobile-app-icon/`:

| File | Fill color (verified via grep) | Notes |
| --- | --- | --- |
| `simplified-symbol-electric-blue.svg` | `#1010EB` | Matches the standard Electric Blue token exactly |
| `simplified-symbol-navy.svg` | `#140F4B` | Matches the standard Navy token exactly |
| `simplified-symbol-white.svg` | `#FFFFFF` | |

This is a **different asset** from the general-purpose Symbol files in `assets/symbol/` (e.g.
`symbol-electric-blue.svg`) — don't substitute one for the other; the general Symbol is for
logo/lockup use, this simplified one is for mobile app icon canvases specifically.

## Best practices

- Do maintain consistent stroke weights, color schemes, layouts, and backgrounds — use the
  template as a guide rather than freehanding a new style.
- Do keep icons simple, concise, minimalistic, and uniform.
- Do stay within the template's supplied margins, and test the design cropped into **both** an
  iOS rounded-square mask and Android's circle (and other) masks.
- Do export icons for development **uncropped**, at the template's full canvas — the OS/device
  applies the mask crop itself, and your dev team may need multiple export sizes.
- Don't change the stroke weight, add fills, use colors outside the approved set, or edit/remove
  the wordmark.
- Don't add unnecessary detail, visual noise, borders, or variable stroke weights.
- Don't release an app icon without testing the Android crop, or without following the template's
  margins.
- Don't export pre-cropped icons — they risk App Store/Play Store rejection, or being re-cropped/
  misaligned by the platform.

**Gap:** the source page doesn't give exact pixel export dimensions (e.g. 1024×1024) or exact
margin/safe-area measurements — those live only in the Figma/Illustrator template files
themselves, not as text on this page. Don't invent a specific number; point the user at the
official template for exact measurements.
