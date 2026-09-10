# Asset manifest — what's bundled vs. what's only in the source zips

This skill bundles a **curated subset** (~151 MB, most of which is the third-party Carbon Design
System reference below) of the full Medtronic brand kit plus supplementary layout/icon reference
material for day-to-day UI work. The full source zips (some are 100s of MB — video, animated, and
AI vector source files) live in the sibling `Archive/` folder (one level above `.github/`) and are
**not** duplicated into the skill. Every file in `Archive/` is accounted for below — bundled, or
explicitly pointed at.

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

| Path | Contents | Extracted from |
| --- | --- | --- |
| `assets/logos/wordmark/` | Plain Medtronic wordmark, no tagline: `medtronic-logo-{navy,white,black}.{svg,png}`, plus `medtronic-logo-navy-digital.svg` (`#170F5F`, for app/website headers specifically) and `uidesignsystem-footer-logo-reference.png` (unverified reference image, caption/asset mismatch noted in `app-header-logo-lockup.md`) | `coll-art-logo-png-only.zip` + UI Design System (Zeroheight) |
| `assets/logos/tagline-lockup-horizontal/` | Logo + "engineering the extraordinary" tagline, horizontal lockup: `medtronic-logo-tagline-{navy,white,black}.{svg,png}` | `art-logo-tag-all.zip` |
| `assets/logos/tagline-lockup-vertical/` | Same lockup, vertical/stacked (logo on top, tagline below, left-aligned) — for narrow sidebars, mobile, or square tiles | `art-logo-tag-all.zip` |
| `assets/logos/logo-symbol-combo/` | Logo + Full-life Symbol horizontal lockup, full color + reverse (general-purpose "combining the logo + Symbol" lockup from the guidelines) | `coll-art-logo-symbol-combo.zip` |
| `assets/logos/logo-tagline-symbol-combo/` | Logo + tagline + Full-life Symbol triple lockup, horizontal, full color + reverse | `coll-art-logo-tag-symbol-combo.zip` |
| `assets/logos/social-favicon-mark/` | The **integrated** Symbol+logo mark — a single fused graphic. Per the guidelines this is for **social media profile images**, not general logo use. Full color, full-color-reverse, white. | `coll-symbol-logo-rgb-all.zip` |
| `assets/favicon/favicon.ico` | Medtronic's actual live production favicon (white "M" on Electric Blue) — prefer this for real browser-tab favicons over the social-favicon-mark | Public `medtronic.com` (fetched directly, not from the UI Design System page itself) |
| `assets/symbol/` | Full-life Symbol: `symbol-full-color`, `symbol-full-color-reverse`, `symbol-white`, `symbol-black`, `symbol-electric-blue`, `symbol-light-blue`, `symbol-pink` — each as `.svg` + `.png` | `all-versions-symbol.zip` |
| `assets/symbol/mobile-app-icon/` | Simplified Symbol variant, **mobile app icon canvases only** (not general logo/lockup use): `simplified-symbol-{electric-blue,navy,white}.svg` — navy fill is `#140E4B`, one character off the standard `#140F4B` token, flagged in `application-icons.md` | Medtronic UI Design System (Zeroheight, "Application Icons" page), `Simplified_Symbol.zip` |
| `assets/icons/functional/` | 286 generic UI SVG icons (gray, for light backgrounds) — search, close, calendar, alerts, devices, etc. | `coll-icons-png-svg.zip` |
| `assets/icons/functional-white/` | The same 286 functional icons in white, for dark/color backgrounds (Navy Dark preset, gradients) | `coll-icons-png-svg.zip` |
| `assets/icons/thematic/` | 91 Medtronic/health-themed SVG icons (blue, for light backgrounds) — clinical, treatment, and industry concepts | `coll-icons-png-svg.zip` |
| `assets/fonts/avenir-next-world/` | All 8 real Avenir Next World `.ttf` weights (Regular, Italic, Thin, ThinIt, Demi, DemiIt, Bold, BoldIt) — self-host these, don't rely on a system-font fallback | Medtronic UI Design System (Zeroheight, "HTML/CSS Framework" page), `02-Header-Variations.zip` |
| `assets/code-templates/html-css-framework/` | Medtronic's own official starter code: `css/mdt-variables.css` (tokens + full type scale), `css/mdt-components.css` (buttons/cards), `css/mdt-app-template.css` (grid/breakpoints), `css/mdt-app-footer.css`, plus working `header-*.html`/`footer-*.html`/`page-template.html` examples. **Plus `css/mdt-typography-override.css`** — this skill's own addition, loaded after `mdt-variables.css` to make headlines Bold; the vendored files are otherwise kept byte-accurate | Same UI Design System source, `01-Page-Shell.zip` + `02-Header-Variations.zip` + `03-Footer-Variations.zip` |
| `assets/icons/thematic-white/` | The same 91 thematic icons in white, for dark/color backgrounds | `coll-icons-png-svg.zip` |
| `assets/colors/` | Adobe `.ase` swatch files: RGB, CMYK, Pantone — for design-tool import | `coll-color-ase.zip` |
| `assets/third-party/carbon-design-system/` | IBM Carbon Design System crawl (third-party, Apache-2.0): `pages/**/content.md`+`meta.json` (356 pages per the crawl manifest — see `carbon-design-system.md` for a residual on-disk-count caveat), `assets/icons/` (2739 SVGs), `assets/pictograms/` (1565 SVGs), `assets/images/`, `assets/documents/`, `assets/data/` (`llms.txt` etc.), `catalog/` (manifests + REPORT.md). Raw `page.html` (~997MB, redundant with `content.md`) and a handful of malformed broken-link folders were deliberately excluded — see `carbon-design-system.md` for the full rationale | `carbon-design-system-crawl.zip` (user-run crawl of `carbondesignsystem.com`) |
| `references/color-tokens.md` | Exact hex/RGB/CMYK for every brand color + tint stacks | `doc-color-palette-breakdown.pdf` |
| `references/theme-presets.md` | Six ready-made combinations — Signature Light / Atmospheric Light / App Dark Mode / Navy Dark / Navy Header Light / Gradient Hero — tying tokens + rules + the correct asset variant together, plus the `[MANDATORY]` blue-sidebar anti-pattern rule | Derived from `color-tokens.md` + `brand-guidelines.md` + `dark-mode-ui-colors.md`, no separate source file |
| `references/dark-mode-ui-colors.md` | Official dark-mode UI tokens (surfaces, interactive/action colors, borders, text/icon opacity system, semantic, accent/data-viz) for product/app dark mode specifically | Medtronic's internal UI Design System (Zeroheight styleguide) — pasted directly by an authenticated user, see note below |
| `references/ui-design-system-colors.md` | Official **light-mode** UI tokens: same categories as `dark-mode-ui-colors.md` plus the full Neutral/Brown/Green/Lavender/Light-blue/Medtronic-Blues/Orange/Pink/Purple/Red/Teal tint stacks and raw JSON design tokens — resolves the dark-mode file's previously-unresolved accent/semantic aliases | Same UI Design System source, "Colors" page |
| `references/accessibility.md` | APCA contrast standard, 200% text-scaling requirement, official Medtronic touch-target minimums (48×48px essential, 32×32px non-essential spacing, 24×24px+4px-margin icon exception) | Same UI Design System source, "Accessibility" page |
| `references/application-icons.md` | App Store/Play Store icon guidance: Carbon-baselined template, approved backgrounds (Gradient/Electric Blue/Navy/White), Simplified Symbol usage rule, Do/Don't for stroke weight/margins/platform-crop testing/export | Same UI Design System source, "Application Icons" page |
| `references/typography.md` | Full official type scale (h1–h4, `.txt01`–`.txt09` utility classes) extracted directly from the real `mdt-variables.css`, the `@font-face` declarations, the **headline-weight resolution (Bold, not Thin — Brand Central over framework CSS)**, the Weight Context Matrix, and the `[MANDATORY]` never-use-`font-weight` rule | Same UI Design System source, "HTML/CSS Framework" page code kit |
| `references/composition.md` | Exact breakpoints (1440/1200/768/375px with padding + content-area widths), 8px grid + spacing scale, 12-column responsive grid, UI shell selection guide (website-style vs web app-style) | Same UI Design System source, "Composition" page |
| `references/navigation.md` | Top nav (121px, floating-header shadow recipe), side nav shell dims, breadcrumb rules + sizes, tabs, popover-menu shadow recipe, anchor links, footer (dark/white-text confirmed via real CSS) | Same UI Design System source, "Navigation" and "Footer" pages |
| `references/global-header.md` | The 64px-fixed-height header rule, application-style vs website-style header behavior, mobile responsive stacking | Same UI Design System source, "Global Header" page |
| `references/ui-components.md` | Badges, segmented buttons, carousels, expansion panels/accordions, flags, hero banners, key-value pairs, user avatars — sizes, variants, and usage rules | Same UI Design System source, "Alerts - Badges"/"Segmented buttons"/"Carousels"/"Expansion Panels"/"Flags"/"Hero Banners"/"Key value pairs"/"User avatars" pages |
| `references/forms-and-inputs.md` | Text fields/areas, select dropdowns, multi-select, autocomplete, checkboxes/radios, toggles, date picker, number picker, slider, search field — sizes, states, and real reference CSS | Same UI Design System source, "Inputs"/"Slider"/"Search" pages |
| `references/carbon-design-system.md` | **The default icon system** (2,739 `currentColor` icons + manifest lookup procedure + sizing/coloring rules), plus IBM Carbon's 2x Grid (mini units, fluid/fixed/hybrid boxes, breakpoints, sizing scale, aspect ratios) and Spacing scale (`$spacing-01`–`13`) as supplementary "outer layout" guidance, a full breakdown of what was/wasn't bundled, and precedence rules vs Medtronic's own specs | Third-party: IBM Carbon Design System crawl |
| `references/streamlit-layout.md` | Streamlit **structure** (authoritative): page shell + `layout` choice per archetype, the 64px header recipe, `[MANDATORY]` `gap`/`vertical_alignment` rules, column-ratio discipline, container/card patterns with fixed heights, the 8px-grid→Streamlit spacing translation table (including where no mechanism exists), multi-page `st.navigation`, and a 17-point alignment pre-flight | Synthesized from Streamlit's own API + `composition.md`/`design-intuition.md`; fills a genuine gap — `streamlit-integration.md` covered theming only |
| `references/design-intuition.md` | Composition/consistency layer: brief-read step, VARIANCE/MOTION/DENSITY dials calibrated for Medtronic surfaces, color/shape/typography/motion/elevation consistency locks, hard layout fit-and-finish rules, interactive-state coverage, and a pre-flight checklist | Synthesized from this skill's own documented tokens/specs, plus Carbon's motion durations/easing (clearly marked third-party) for the one genuine gap in Medtronic's own docs |
| `references/ux-accessibility-checklist.md` | Third-party, brand-agnostic UX/WCAG 2.2 hygiene: motion cleanup, layout-shift prevention, touch-target platform table, forms/error-summary rules, current WCAG 2.2 items (Focus Not Obscured, Dragging Movements, Redundant Entry, Accessible Authentication), compact-label (badge/chip) semantics, AI-interaction disclosure, mobile-app specifics, chart-type selection (25 types), and landing-page section-order archetypes | Synthesized/condensed from two downloaded design-skill collections (`ui-ux-pro-max-skill`, MIT-licensed; `taste-skill` collection) |
| `references/overlays-and-feedback.md` | Modal dialogs (+ exact shadow recipe), side/bottom sheets, focus dimmer, page-loading spinners, progress indicators, tooltips | Same UI Design System source, "Modals and Sheets"/"Page Loading"/"Progress Indicators"/"Tooltips" pages |
| `references/app-header-logo-lockup.md` | App/website header logo color correction (`#170F5F` not `#140F4B`), favicon guidance, logo+app-name lockup measurements (15px stacked logo, baseline/cap-height alignment) | Same UI Design System source, "Logo" page |
| `references/sizing-standard.md` | **§0 Logo Sizing Decision Table** (context in, exact px out) and the `[MANDATORY]` guard that a brand-asset dimension is never a spacing token, plus measured aspect ratios (from each SVG's own `viewBox`) for every logo/lockup/Symbol/icon and a recommended pixel-size tier per UI context (header, hero, footer, favicon, inline icon) | Measured directly from the bundled `assets/` SVGs, cross-checked in a real browser test |
| `references/layout-and-spacing.md` | General spacing grid (8px), touch-target minimums (with a cross-reference to `accessibility.md`'s Medtronic-specific override), responsive breakpoints, and a Compact/Default/Spacious component-size-tier system for buttons/inputs/cards | External UI standards (Material Design, WCAG 2.5.5, Apple/Google HIG, Nathan Curtis / EightShapes sizing methodology) — not Medtronic-specific, cited explicitly |
| `references/brand-guidelines.md` | Condensed logo/tagline/symbol/typography/icon/composition/trademark rules, plus the official logo filename-key/format-selection guidance and explicit notes on what the source docs don't cover | `1st Half Guidelines.docx`, `2nd Half Guidelines.docx`, `Style Guide.pdf`, `doc-avenir-next-world-agreement.docx`, the `READ ME - Logo Selection Guide.pdf` inside `coll-art-medtronic-logos.zip` |

## Every other file in `Archive/` — not duplicated into the skill

| File | What it is | When you'd need it |
| --- | --- | --- |
| `art-logo-tag-en-bl.zip` | Navy-only subset of `art-logo-tag-all.zip` (all formats: ai/eps/jpg/png/svg, all orientations including the centered `c`/`c1` stacked variants) | Only if you need a format not in the bundled SVG/PNG (print CMYK/spot) or the centered-stacked lockup variant specifically |
| `art-logo-tag-en-k.zip` | Black-only subset of the same, all formats/orientations | Same as above, black variant |
| `art-logo-tag-en-w.zip` | White-only subset of the same, all formats/orientations | Same as above, white variant |
| `coll-art-medtronic-logos.zip` | Plain wordmark reorganized by "print vs. digital screens" folders, plus the `READ ME - Logo Selection Guide.pdf` (its content is now folded into `brand-guidelines.md`) | Alternate source for the same navy/black/white wordmark; the PDF itself is only needed if you want Medtronic's exact original wording |
| `black-symbol.zip`, `white-symbol.zip`, `full-color-reverse.zip` | Single-variant symbol zips (already covered by the bundled `assets/symbol/`, which was pulled from the more complete `all-versions-symbol.zip`) | Rarely — bundled versions are equivalent |
| `coll-icons-ai.zip` (266 MB) | Full icon set as Adobe Illustrator vector source, every color | Editing an icon's actual vector paths in Illustrator |
| `coll-symbol-animated-HDVideo-MOVs.zip` (524 MB), `coll-symbol-animated-GIFs.zip`, `coll-symbol-logo-tagline-animated-hd-video.zip` | Motion versions of the Symbol (video/GIF) | Video/motion work, not static UI |
| `coll-rendered-transitions+endtitles-HD+4K.zip` (+ duplicate `(1)` copy) | Pre-rendered video transition/end-title elements | Video production only |
| `coll-production-graphics-toolkit.zip` (160 MB) | Full layered production source files (print/video design toolkit) | Professional print/video design work, not typical app UI work |
| `doc-temp-all-slides.potx` | PowerPoint master template (includes an icon library near the end of the deck) | Building a Medtronic-branded PowerPoint deck |
| `coll-temp-brochure.zip` | Print brochure template | Print collateral, not app UI |
| `Style Guide.pdf` | Full 49-page A–Z editorial/writing style guide (grammar, terminology, trademark handling in depth) | Any task producing significant marketing/UI copy — check this before finalizing product-name text or legal/trademark copy beyond the summary in `brand-guidelines.md` |
| `doc-avenir-next-world-agreement.docx` | The actual vendor/3rd-party font-license request form for Avenir Next World | Tell the user to fill this out and return it to their Medtronic Global Brand contact if they need the real licensed font |
| `doc-color-palette-breakdown.pdf` | Source of truth for every hex/RGB/CMYK value and tint stack | If a color value in `color-tokens.md` ever looks stale or a needed tint isn't listed there |
| `1st Half Guidelines.docx`, `2nd Half Guidelines.docx` | Source of truth for `brand-guidelines.md` — covers Visual brand ID system through Motion & video | Anything not covered by the condensed reference, or to verify exact original wording |

If a user's task genuinely needs one of the "not bundled" items (e.g., "give me the vertical
lockup" or "I need the CMYK print files"), open the relevant zip with a zip-listing/extraction
step rather than approximating from the bundled subset — don't recreate or guess at artwork that
already exists in these files.
