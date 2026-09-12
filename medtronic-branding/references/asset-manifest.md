# Asset manifest — what's bundled vs. what's not part of this skill

This skill bundles a **curated subset** (~151 MB, most of which is the third-party Carbon Design
System reference below) of the full Medtronic brand kit plus supplementary layout/icon reference
material for day-to-day UI work. The remaining source material (some individual files are 100s of
MB — video, animated, and AI vector source) was used to build this skill's condensed references
but is **not** included in it and isn't reachable from it at runtime. Where something below isn't
bundled, that's a genuine gap — say so and point to Global Brand/Brand Central, per the Hard Rule
in `SKILL.md`, rather than trying to retrieve or approximate it.

**A second, separate source exists as of `dark-mode-ui-colors.md`**: Medtronic's internal **UI
Design System** (hosted on Zeroheight, access-controlled). This is a different corpus from the
`Archive/` Brand Central docs — it covers product/app UI specifically (dark-mode tokens,
component specs, application icons) rather than marketing/brand identity. Content from it only
enters this skill when a user with authenticated access pastes/hands over the specific data
(this skill does not and should not autonomously crawl that site) — see `dark-mode-ui-colors.md`
for the current example of that process.

**A third, independent source**: IBM's **Carbon Design System** (`carbondesignsystem.com`),
bundled as a full site crawl at `assets/third-party/carbon-design-system/` — third-party,
Apache-2.0-licensed, open-source, used only as a supplementary generic layout-grid framework and
app-icon baseline per Medtronic's own explicit pointer to it. See
[carbon-design-system.md](./carbon-design-system.md) for the full breakdown and precedence rules.

## Bundled in this skill (`assets/`)

| Path | Contents |
| --- | --- |
| `assets/logos/wordmark/` | Plain Medtronic wordmark, no tagline: `medtronic-logo-{navy,white,black}.{svg,png}`, plus `medtronic-logo-navy-digital.svg` (`#170F5F`, for app/website headers specifically) |
| `assets/logos/tagline-lockup-horizontal/` | Logo + "engineering the extraordinary" tagline, horizontal lockup: `medtronic-logo-tagline-{navy,white,black}.{svg,png}` |
| `assets/logos/tagline-lockup-vertical/` | Same lockup, vertical/stacked (logo on top, tagline below, left-aligned) — for narrow sidebars, mobile, or square tiles |
| `assets/logos/logo-symbol-combo/` | Logo + Full-life Symbol horizontal lockup, full color + reverse (general-purpose "combining the logo + Symbol" lockup from the guidelines) |
| `assets/logos/logo-tagline-symbol-combo/` | Logo + tagline + Full-life Symbol triple lockup, horizontal, full color + reverse |
| `assets/logos/social-favicon-mark/` | The **integrated** Symbol+logo mark — a single fused graphic. Per the guidelines this is for **social media profile images**, not general logo use. Full color, full-color-reverse, white. |
| `assets/favicon/favicon.ico` | Medtronic's actual live production favicon (white "M" on Electric Blue), fetched directly from `medtronic.com`'s live site — prefer this for real browser-tab favicons over the social-favicon-mark |
| `assets/symbol/` | Full-life Symbol: `symbol-full-color`, `symbol-full-color-reverse`, `symbol-white`, `symbol-black`, `symbol-electric-blue`, `symbol-light-blue`, `symbol-pink` — each as `.svg` + `.png` |
| `assets/symbol/mobile-app-icon/` | Simplified Symbol variant, **mobile app icon canvases only** (not general logo/lockup use): `simplified-symbol-{electric-blue,navy,white}.svg` |
| `assets/icons/functional/` | 286 generic UI SVG icons (gray, for light backgrounds) — search, close, calendar, alerts, devices, etc. |
| `assets/icons/functional-white/` | The same 286 functional icons in white, for dark/color backgrounds (Navy Dark preset, gradients) |
| `assets/icons/thematic/` | 91 Medtronic/health-themed SVG icons (blue, for light backgrounds) — clinical, treatment, and industry concepts |
| `assets/fonts/avenir-next-world/` | All 8 real Avenir Next World `.ttf` weights (Regular, Italic, Thin, ThinIt, Demi, DemiIt, Bold, BoldIt) — self-host these, don't rely on a system-font fallback |
| `assets/code-templates/html-css-framework/` | Medtronic's own official starter code: `css/mdt-variables.css` (tokens + full type scale), `css/mdt-components.css` (buttons/cards), `css/mdt-app-template.css` (grid/breakpoints), `css/mdt-app-footer.css`, plus working `header-*.html`/`footer-*.html`/`page-template.html` examples. Headline weight (Bold, not the original Thin) is baked into `mdt-variables.css` as a documented Local Override — see `SKILL.md` |
| `assets/icons/thematic-white/` | The same 91 thematic icons in white, for dark/color backgrounds |
| `assets/colors/` | Adobe `.ase` swatch files: RGB, CMYK, Pantone — for design-tool import |
| `assets/third-party/carbon-design-system/` | IBM Carbon Design System crawl (third-party, Apache-2.0): `pages/**/content.md`+`meta.json`, `assets/icons/` (2739 SVGs), `assets/pictograms/` (1565 SVGs), `assets/images/`, `assets/documents/`, `assets/data/` (`llms.txt` etc.), `catalog/` (manifests + `REPORT.md`). See [carbon-design-system.md](./carbon-design-system.md) for the full breakdown |
| `references/color-tokens.md` | Exact hex/RGB/CMYK for every brand color + tint stacks |
| `references/theme-presets.md` | Six ready-made combinations — Signature Light / Atmospheric Light / App Dark Mode / Navy Dark / Navy Header Light / Gradient Hero — tying tokens + rules + the correct asset variant together, plus the `[MANDATORY]` blue-sidebar anti-pattern rule |
| `references/dark-mode-ui-colors.md` | Official dark-mode UI tokens (surfaces, interactive/action colors, borders, text/icon opacity system, semantic, accent/data-viz) for product/app dark mode specifically |
| `references/ui-design-system-colors.md` | Official **light-mode** UI tokens: same categories as `dark-mode-ui-colors.md` plus the full Neutral/Brown/Green/Lavender/Light-blue/Medtronic-Blues/Orange/Pink/Purple/Red/Teal tint stacks and raw JSON design tokens — resolves the dark-mode file's previously-unresolved accent/semantic aliases |
| `references/accessibility.md` | APCA contrast standard, 200% text-scaling requirement, official Medtronic touch-target minimums (48×48px essential, 32×32px non-essential spacing, 24×24px+4px-margin icon exception) |
| `references/application-icons.md` | App Store/Play Store icon guidance: Carbon-baselined template, approved backgrounds (Gradient/Electric Blue/Navy/White), Simplified Symbol usage rule, Do/Don't for stroke weight/margins/platform-crop testing/export |
| `references/typography.md` | Full official type scale (h1–h4, `.txt01`–`.txt09` utility classes) extracted directly from the real `mdt-variables.css`, the `@font-face` declarations, the **headline-weight resolution (Bold, not Thin — Brand Central over framework CSS)**, the Weight Context Matrix, and the `[MANDATORY]` never-use-`font-weight` rule |
| `references/composition.md` | Exact breakpoints (1440/1200/768/375px with padding + content-area widths), 8px grid + spacing scale, 12-column responsive grid, UI shell selection guide (website-style vs web app-style) |
| `references/navigation.md` | Top nav (121px, floating-header shadow recipe), side nav shell dims, breadcrumb rules + sizes, tabs, popover-menu shadow recipe, anchor links, footer (dark/white-text confirmed via real CSS) |
| `references/global-header.md` | The 64px-fixed-height header rule, application-style vs website-style header behavior, mobile responsive stacking |
| `references/ui-components.md` | Badges, segmented buttons, carousels, expansion panels/accordions, flags, hero banners, key-value pairs, user avatars — sizes, variants, and usage rules |
| `references/forms-and-inputs.md` | Text fields/areas, select dropdowns, multi-select, autocomplete, checkboxes/radios, toggles, date picker, number picker, slider, search field — sizes, states, and real reference CSS |
| `references/carbon-design-system.md` | **The default icon system** (2,739 `currentColor` icons + manifest lookup procedure + sizing/coloring rules), plus IBM Carbon's 2x Grid (mini units, fluid/fixed/hybrid boxes, breakpoints, sizing scale, aspect ratios) and Spacing scale (`$spacing-01`–`13`) as supplementary "outer layout" guidance, and precedence rules vs Medtronic's own specs |
| `references/streamlit-layout.md` | Streamlit **structure** (authoritative): page shell + `layout` choice per archetype, the 64px header recipe, `[MANDATORY]` `gap`/`vertical_alignment` rules, column-ratio discipline, container/card patterns with fixed heights, the 8px-grid→Streamlit spacing translation table (including where no mechanism exists), multi-page `st.navigation`, and a 17-point alignment pre-flight. Distinct from `streamlit-integration.md`, which covers theming only |
| `references/design-intuition.md` | Composition/consistency layer: brief-read step, VARIANCE/MOTION/DENSITY dials calibrated for Medtronic surfaces, color/shape/typography/motion/elevation consistency locks, hard layout fit-and-finish rules, interactive-state coverage, and a pre-flight checklist. Motion durations/easing are sourced from Carbon (third-party) — Medtronic's own docs don't specify these |
| `references/ux-accessibility-checklist.md` | Third-party, brand-agnostic UX/WCAG 2.2 hygiene: motion cleanup, layout-shift prevention, touch-target platform table, forms/error-summary rules, current WCAG 2.2 items (Focus Not Obscured, Dragging Movements, Redundant Entry, Accessible Authentication), compact-label (badge/chip) semantics, AI-interaction disclosure, mobile-app specifics, chart-type selection (25 types), and landing-page section-order archetypes |
| `references/overlays-and-feedback.md` | Modal dialogs (+ exact shadow recipe), side/bottom sheets, focus dimmer, page-loading spinners, progress indicators, tooltips |
| `references/app-header-logo-lockup.md` | App/website header logo color correction (`#170F5F` not `#140F4B`), favicon guidance, logo+app-name lockup measurements (15px stacked logo, baseline/cap-height alignment) |
| `references/sizing-standard.md` | **§0 Logo Sizing Decision Table** (context in, exact px out) and the `[MANDATORY]` guard that a brand-asset dimension is never a spacing token, plus measured aspect ratios (from each SVG's own `viewBox`, verified in a real browser test) for every logo/lockup/Symbol/icon and a recommended pixel-size tier per UI context (header, hero, footer, favicon, inline icon) |
| `references/layout-and-spacing.md` | General spacing grid (8px), touch-target minimums (with a cross-reference to `accessibility.md`'s Medtronic-specific override), responsive breakpoints, and a Compact/Default/Spacious component-size-tier system for buttons/inputs/cards. Sourced from external UI standards (Material Design, WCAG 2.5.5, Apple/Google HIG, Nathan Curtis / EightShapes) — not Medtronic-specific |
| `references/brand-guidelines.md` | Condensed logo/tagline/symbol/typography/icon/composition/trademark rules, plus the official logo filename-key/format-selection guidance and explicit notes on what the source docs don't cover |

## What's not part of this skill

Source material that fed into this skill's condensed references but isn't bundled and can't be
retrieved by this skill: additional logo formats and print-color subsets (CMYK/spot, Pantone),
non-English (Arabic/Chinese) wordmark variants, the centered-stacked lockup orientation, the full
Illustrator icon set (every color, vector source), animated/video Symbol assets, print/video
production source files, PowerPoint and brochure templates, the 49-page editorial Style Guide, the
raw brand-guideline source documents, and the Avenir Next World vendor font-license request form.

If a task genuinely needs one of these (e.g., "give me the vertical lockup" — already bundled, see
above — or "I need the CMYK print files" — not bundled), say so explicitly and point to Global
Brand/Brand Central. Don't approximate from the bundled subset, and don't imply this skill can go
fetch the original file — it can't.
