# Medtronic Brand Guidelines — Condensed Reference

Source: `1st Half Guidelines.docx`, `2nd Half Guidelines.docx`, `Style Guide.pdf` (Global Brand /
Brand Central). This is a condensed, dev-oriented summary. For anything not covered here or for
legal/regulatory copy review, defer to the full source documents in the `Archive/` folder.

## Brand hierarchy (masterbrand rule)

Every UI, deck, or document must be **visibly branded Medtronic**. Three key identifiers, in
priority order:

1. **Logo (wordmark)** — Level 1. Always present and prominent. Never go to market without it.
   If the graphic can't be used for technical reasons, the plain text "Medtronic" may substitute,
   but must still be prominent.
2. **Full-life Symbol** — optional but encouraged. Testing shows Symbol + logo together produces
   a meaningfully more positive brand impression than the wordmark alone.
3. **Tagline ("engineering the extraordinary")** — optional, level 2. Most common use is inside
   the logo lockup artwork.

## Logo rules

- The wordmark is custom artwork — **never** recreate "Medtronic" by typing it in any font.
- One logo only (masterbrand approach) — don't invent sub-brand logos for products/features.
- **Placement**: top-left is preferred. Top-right, bottom-left, bottom-right, or centered are all
  acceptable depending on composition. **Never place the logo in the middle of a layout**, trapped
  between other content.
- **Do**: use only approved logo artwork, ensure sufficient contrast against its background.
- **Don't**: recolor the logo, place it on a busy/complex background, place it on a
  low-contrast background.
- Co-branding (partner logos): horizontal lockup, 1pt/px black rule divider between logos, even
  visual scale and spacing.

Use [`assets/logos/wordmark/`](../assets/logos/wordmark/) for the standalone wordmark:
`medtronic-logo-navy.svg` (default, on white/light print/marketing contexts),
`medtronic-logo-white.svg` (reverse, on dark/color backgrounds), `medtronic-logo-black.svg`
(limited use only — see Style Guide before choosing black over navy).

**For an app/website header specifically**, use
`medtronic-logo-navy-digital.svg` (`#170F5F`) instead of the standard `medtronic-logo-navy.svg`
(`#140F4B`) — the Medtronic UI Design System explicitly warns the standard Navy fill "comes
across some screens as black, or near-black" for on-screen logo use, and never use Electric Blue
`#1010EB` for the logo. Full detail, favicon guidance, and app-header lockup measurements in
[app-header-logo-lockup.md](./app-header-logo-lockup.md).

### Official logo filename key and color/format selection rules

From Medtronic's own "Logo Selection Guide" (bundled inside `coll-art-medtronic-logos.zip` in
`Archive/`) — filenames follow `art-logo-[orientation]-[language]-[usage]-[color].[format]`:

- **Orientation**: `h` = horizontal, `v` = vertical (stacked). Plain English wordmark files have
  no orientation infix — there's only one arrangement of the wordmark itself; orientation only
  applies to lockups (logo+tagline, logo+Symbol).
- **Language**: `en` (English), `ar` (Arabic), `zs` (Chinese) — not bundled in this skill; get
  them from `art-logo-tag-all.zip` / `coll-art-medtronic-logos.zip` in `Archive/` if needed.
- **Usage**: `rgb` = digital screens, `cmyk` = standard print, `spot` = specialized print using a
  pre-mixed Pantone ink for precise, consistent color.
- **Color**, per Medtronic's own guidance, verbatim: **`bl` (blue)** — "use blue on white or
  light-color backgrounds"; **`k` (black)** — "use black logo for black-and-white situations"
  (i.e. not just "dark mode" — genuinely monochrome contexts); **`w` (white)** — "use white
  version for dark-color or image backgrounds."
- **Format**, per the same guide: `.ai`/`.eps` are vector, need design software, transparent bg —
  for professional print/design work. `.jpg` is pixelated, lossy, **white background only, no
  transparency** — avoid for web/app UI. `.png` is pixelated but lossless with transparency —
  "often a good choice for logos and icons in online and PowerPoint designs." `.svg` is vector,
  "intended specifically for websites and app design software" — **prefer `.svg` for React/
  Streamlit/web work**, falling back to `.png` only where SVG isn't supported.

This confirms the format choice already made for every asset bundled in this skill (SVG primary,
PNG fallback) and is the authoritative source if you're ever choosing among the unbundled
`Archive/` files directly.

Both orientations of the logo+tagline lockup are bundled:
[`assets/logos/tagline-lockup-horizontal/`](../assets/logos/tagline-lockup-horizontal/) (logo
left, tagline wraps to its right — for wide headers/footers) and
[`assets/logos/tagline-lockup-vertical/`](../assets/logos/tagline-lockup-vertical/) (logo on top,
tagline below, left-aligned — for narrow sidebars, mobile layouts, or square social/app tiles).
The source zip also has centered-stacked variants (`c`/`c1`) that look near-identical to the
vertical one at a glance; they're not bundled since they don't add a meaningfully different
layout option — get them from `art-logo-tag-all.zip` in `Archive/` if a centered-not-left-aligned
stacked lockup is specifically needed.

## Tagline rules ("engineering the extraordinary")

- Always lowercase/sentence case, never all caps, never italic, never translated outside
  approved translations.
- Preferred use is inside the **logo + tagline lockup** artwork (horizontal or vertical, see
  above), placed at the very beginning and/or very end of a page/flow (reinforces it's an
  enterprise-level statement, not a specific product claim).
- Can be used as a standalone hero headline (Avenir Next World, sentence case, in Electric Blue
  on light backgrounds or white on dark backgrounds) — but don't also show the tagline logo lockup
  on the same page if you do this (avoid repetition).
- **Never** use the tagline to make a product claim, describe patient outcomes, or in permanent
  physical signage/uniforms/vehicles.
- Never change its wording, color, case, or emphasize part of it when locked up with the logo.

## Full-life Symbol rules

- The Symbol is a complementary mark, **not a substitute for the logo** — don't ship a screen with
  only the Symbol and no wordmark/text "Medtronic" anywhere.
- Prefer full-color version on light/simple backgrounds; full-color-reverse on Electric
  Blue/Navy/dark simple backgrounds; white one-color version on complex or small dark contexts.
  One-color electric-blue/light-blue/pink/black variants exist for constrained media — for
  UI/web work, prefer full-color or white/black over the accent one-color variants.
- **Never**: recolor/modify the artwork, crop it (only use pre-approved crops), tile/repeat it
  as a pattern, use more than one instance on a single screen, or layer text/UI on top of it.
- When combining Symbol + logo, use the Symbol's own clear space (not the logo's "M" space), and
  keep their relative size flexible as long as both stay legible.
- The guidelines describe a **separate, distinct mark** — the "integrated Full-life Symbol +
  logo (wordmark)" — that fuses the Symbol and wordmark into one inseparable graphic. Per the
  source guidance this variant is **intended for social media and favicon use only**; do not use
  it as a general-purpose logo lockup in page headers/nav bars (use the plain wordmark or the
  standard logo+Symbol lockup below for that instead).
- There is also a documented "Simplified Full-life Symbol for mobile application icons" —
  the guidelines point to a separate "UI Design System" resource for it that is **not included**
  in any of the source zips in this workspace. Don't invent a simplified variant; tell the user
  it needs to be sourced from Medtronic's UI Design System directly if a mobile app icon is needed.

Assets: [`assets/symbol/`](../assets/symbol/) (`symbol-full-color`, `symbol-full-color-reverse`,
`symbol-white`, `symbol-black`, plus one-color `symbol-electric-blue` / `symbol-light-blue` /
`symbol-pink`). Pre-built horizontal lockups combining logo + Symbol are in
[`assets/logos/logo-symbol-combo/`](../assets/logos/logo-symbol-combo/); the logo + tagline +
Symbol triple combo is in
[`assets/logos/logo-tagline-symbol-combo/`](../assets/logos/logo-tagline-symbol-combo/). The
social-media/favicon-only integrated mark is in
[`assets/logos/social-favicon-mark/`](../assets/logos/social-favicon-mark/) — use this one for
**social profile images**. For an actual browser-tab `favicon.ico`, prefer
[`assets/favicon/favicon.ico`](../assets/favicon/favicon.ico) instead — Medtronic's own live
production favicon (white "M" on Electric Blue), per the UI Design System; see
[app-header-logo-lockup.md](./app-header-logo-lockup.md) for detail.

## Typography

- Primary (and only) typeface: **Avenir Next World**. It is a licensed/proprietary font — it is
  **not bundled** in this skill (no font files ship in the source zips either, only a license
  agreement doc). See "Typography without the licensed font" below for what to actually do in
  React/Streamlit.
- Headlines are **sentence case**, never title case or ALL CAPS.
- Use Regular, Demi, or Bold weight for headlines; avoid Thin weight if it hurts legibility.
  `[MANDATORY]` **This skill resolves that to `AvenirNextWorld-Bold` for `h1`–`h3`.** This rule
  outranks both the framework starter CSS (`mdt-variables.css`, which ships Thin) and the UI Design
  System Colors page's "large thin fonts" prose — see the resolution at the top of
  [typography.md](./typography.md).
- Don't apply outlines/strokes to type. Don't use more than two colors/styles of emphasis in one
  block of text.
- Body/disclaimer text colors: `#3C3C3C` (body), `#777777` (disclaimer/fine print) — see
  [color-tokens.md](./color-tokens.md).
- Headline color: blue (Electric Blue `#1010EB`, or the digital-safe Navy `#170F5F`) on light
  backgrounds, or white on dark backgrounds. The electric-blue-to-blue gradient is allowed for
  **bold headlines ≥18pt on light backgrounds only**.

### Typography without the licensed font

Avenir Next World is **not free-to-use artwork** — it's a commercially licensed typeface, and per
`doc-avenir-next-world-agreement.docx` the license Medtronic holds *does* extend to vendors and
3rd parties, but only after a specific process:

1. The vendor/3rd party fills out the agreement doc with their name/email, their Medtronic
   contact's name/email, and what the font will be used for.
2. The vendor must confirm they have a confidentiality or service-level agreement with Medtronic.
3. The vendor agrees to use the font **only on Medtronic materials** and to remove it from their
   device(s) once the project or contract ends.
4. The completed form is returned to Medtronic's Global Brand team, who then provisions the font.

The actual font files are **not included** in any of the brand asset zips in this workspace — they
are provisioned separately, only after that agreement is completed. Don't tell the user the font
is simply unavailable; tell them it requires filling out `doc-avenir-next-world-agreement.docx`
and returning it to their Medtronic Global Brand contact, and that the font must be removed from
their machine once the engagement ends. Until that's done, use this fallback stack for
prototyping and say explicitly that it's a substitute, not the real brand font:

```css
font-family: "Avenir Next World", "Avenir Next", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
```

## Iconography

Two families: **thematic** (Medtronic/industry-specific concepts) and **functional** (generic UI
actions, e.g., search, close, download).

- Icons are drawn on a 24×24 grid, 1-unit stroke, squared line endings, ≥1-unit padding.
- **One color per icon** — never mix multiple fill colors on one icon.
- White icons on any color/gradient background; navy icons only on the light-blue-to-teal
  gradient specifically.
- Functional icons: use grays or semantic colors depending on UI context (not fixed to brand
  blue) — treat like a standard neutral UI icon set.
- If bundled icons don't cover a need, the brand guidelines explicitly approve two external
  libraries: **Carbon Design System** (Apache 2.0) and **Health Icons** (CC0) — both SVG,
  outlined style. Prefer these two over any other icon library for a Medtronic-branded product.

> **`[MANDATORY]` This skill's default differs from the sentence above.** Brand Central treats
> Carbon as a fallback; **this skill uses Carbon as the default icon system for all UI icons.** See
> the Local Overrides table in `SKILL.md` and the Icons section of
> [carbon-design-system.md](./carbon-design-system.md). The Medtronic **thematic** set remains the
> preferred choice for brand/editorial moments. This is a recorded skill-owner decision, not a
> Medtronic brand fact — don't cite it as one.

Bundled: [`assets/icons/functional/`](../assets/icons/functional/) (286 SVGs, gray) and
[`assets/icons/thematic/`](../assets/icons/thematic/) (91 SVGs, blue), plus **2,739 Carbon icons**
at `assets/third-party/carbon-design-system/assets/icons/`. Full Medtronic icon set (all colors,
plus AI source + PNG) is in `coll-icons-png-svg.zip` / `coll-icons-ai.zip` in `Archive/`
if a specific icon or color variant isn't in the bundled subset.

## Composition & layout

- Generous open (white) space; don't overstuff layouts.
- Strong contrast in scale (mix large hero elements with small supporting ones).
- Grid: multiples of 4 units (common: 8-unit grid w/ .5-unit margins & .25-unit gutter, or
  12-unit grid). Don't align text directly to grid lines instead of margins/gutters; don't use
  every grid line; don't overstructure.
- Buttons: **pill-shaped** — full circular radius on both ends, not just rounded corners.
- Dotted/dashed lines: circular dots, gap = 2× the line weight (e.g. 3pt line → 6pt gap). Use to
  convey motion/direction, not purely decoratively.

## Data visualization

- Lead with blues + gray first; add tints before introducing more hues; add a single accent
  color family before using multiple accent colors.
- Solid fills only — no gradients, patterns, or 3D/dimensional charts/graphs.
- Use a thin background-colored line between adjoining data segments for contrast; gray/white
  text for labels.

## Voice & editorial style (brief)

Full writing rules live in `Style Guide.pdf` (49-page A–Z glossary of terminology, grammar, and
usage). Key defaults if writing UI copy or marketing text:

- Active voice preferred.
- Sentence case for headlines (matches visual typography rule above).
- Spell out acronyms on first use, except very common ones (CEO, OR).
- American English spelling by default (British for regional/local content only).

### Trademarks and copyright (exact rules from the Style Guide)

Apply these any time UI copy, a footer, or a marketing surface names a specific Medtronic
product — this is a real legal/compliance requirement, not a style preference:

- Confirm the exact spelling/wording of a trademarked product name against the official
  Medtronic trademark list before using it — don't guess capitalization from a datasheet or
  memory (the trademark list itself is typed in all caps, but you should **not** write product
  names in all caps in actual communications).
- Place the `™` symbol immediately after the trademarked mark name, **no space** before it.
  If only part of a product name is trademarked, put `™` right after that part, keep the rest of
  the official product name in title case, then a lowercase generic noun.
  Examples: `Axium™ Prime soft detachable coil`, `BIS™ Advance monitor`, `TurboHawk™ device`.
- Third-party trademarks get an asterisk instead, placed after the `™`/`®` if both apply:
  `Third-Party Trademark™* name`.
- Always include a copyright statement for any material produced on Medtronic's behalf — for the
  current legally-approved wording, defer to Medtronic's "Global Trademark and Copyright
  Requirements for Advertising and Promotional Materials" (not included in this workspace's
  files — don't invent boilerplate legal/copyright text yourself).
- On a webpage, the standard copyright statement and trademark attribution statement belong as an
  **endnote** (bottom-of-page footer text, unnumbered) — this is the natural home for that legal
  text in a React/Streamlit app's footer, not a modal or tooltip.

### Content gaps in the source guideline documents (don't fabricate these)

Be upfront about what genuinely isn't covered rather than inventing plausible-sounding rules:

- **Photography, Simple illustration, and Medical illustration** appear in Brand Central's
  navigation menu (between "Graphic elements" and "Iconography") but their page content was not
  captured in `1st Half Guidelines.docx`/`2nd Half Guidelines.docx` — likely lost in the original
  web-to-Word export. If a task needs photography/illustration style rules specifically, say so
  and suggest checking Brand Central directly rather than guessing.
- **Exact numeric clear-space and minimum-size values** for the logo, tagline, and Symbol (e.g.,
  "clear space = height of the M") live only in graphical diagrams in the source guidelines —
  the underlying Word docs have no extractable text/captions for those numbers. Don't invent a
  specific unit/ratio; describe the rule qualitatively (e.g., "use the Symbol's own clear space,
  not the logo's M-space") as documented above, and flag that a pixel-exact value isn't available
  from these files.
- **Brand messaging, Brand voice** (tone-of-voice guidance beyond the Style Guide glossary), and
  the "You & our brand"/"Business of Brand"/"Experience" nav sections also have no captured
  content in these documents.
- **The exact dark-mode desaturated Electric Blue value — resolved for product UI, still open for
  marketing.** These guidelines state the rule ("For dark mode, we use less saturated Electric
  Blue to improve legibility") without a hex value for marketing/print dark surfaces (Navy Dark
  preset still uses the exact unmodified `#1010EB` there — see `theme-presets.md`). For
  product/app UI specifically, the separate Medtronic UI Design System *does* have an official
  dark-mode blue (`#4A7DFF`) — see [dark-mode-ui-colors.md](./dark-mode-ui-colors.md) and the
  App Dark Mode preset in `theme-presets.md`. Don't assume the two contexts share one answer
  without confirming with Global Brand.

## Dos and don'ts quick list (cross-cutting)

- Do lead with blue and white; don't build a layout dominated by heavy color blocks.
- Do use sentence case everywhere in headlines; don't use title case or all caps.
- Do keep icons flat/one-color; don't add gradients/dimension/effects to icons.
- Do use the Symbol as a complement to the logo; don't use it as a logo replacement.
- Do use only the brand color palette (including tint stacks); don't introduce new colors.
- Do use the two approved external icon libraries (Carbon, Health Icons) if you need more icons;
  don't pull icons from unapproved/random libraries for a Medtronic-branded surface.
