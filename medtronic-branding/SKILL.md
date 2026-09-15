---
name: medtronic-branding

description: >-
  Apply official Medtronic brand identity (logo, Full-life Symbol, tagline, exact
  color palette, Avenir Next World typography, iconography, composition rules)
  when building or restyling any UI — React, Streamlit, HTML/CSS, PowerPoint, or
  general design work. Use whenever the user mentions Medtronic branding,
  Medtronic brand guidelines, Medtronic colors/logo/symbol, "brand this app",
  "make this look like Medtronic", or asks to pull Medtronic assets/logos/icons/
  colors into a project. Bundles real logo/symbol/icon files and exact
  hex/RGB/CMYK color tokens extracted from the official brand guidelines — do not
  recreate the logo, guess brand colors, or invent a substitute palette.

argument-hint: 'optional: target stack (react/streamlit/html) and what you are building'

compatibility: >-
  No network access or MCP server required — everything is bundled as local files
  (SVG/PNG assets + Markdown references). Works identically in Claude.ai, Claude
  Code, and GitHub Copilot Chat (VS Code). Internal Medtronic use only — see the
  "Internal use only" note in the repo README.

metadata:
  author: Medtronic Global Brand (packaged by kothal1 and ms68)
  version: 1.3.0
  category: design-system
  tags: [branding, design-system, react, streamlit, ui]
---

# Medtronic Branding

Turns Medtronic's raw brand-kit zips and guideline docs into a ready-to-use design system: real
logo/symbol/icon files plus exact color tokens, ready-made light/dark/hero theme presets, and
condensed usage rules, so a UI can be branded correctly without re-deriving anything from scratch
or guessing at colors.

## Why this matters

Medtronic's brand guidelines are strict about a few things that are easy to get wrong by
"eyeballing" a brand: the logo is custom artwork that must never be retyped or recolored, the
color palette is exact (no approximated hex values), and the Full-life Symbol has specific rules
about when it can and can't stand in for the logo. Treat the bundled assets and
[references](./references/) as source of truth, not inspiration.

## Hard rule: never fabricate a brand fact

If a color, measurement, asset variant, or rule isn't in `assets/` or `references/`, **it does
not exist for the purposes of this skill** — don't invent a plausible-looking hex code, don't
guess a clear-space measurement, don't recreate a logo/Symbol variant that isn't bundled, and
don't attribute a made-up rule to "the guidelines." This applies even when the gap is small and a
close guess feels harmless (e.g., a slightly-desaturated version of Electric Blue for dark mode).

When something is genuinely missing:
1. Say so explicitly to the user — name the specific gap.
2. Fall back to the closest **exact, already-documented** token/asset instead of a fabricated one.
3. Point at where the real answer would come from (Global Brand or Brand Central directly) rather
   than filling the gap yourself.

`references/brand-guidelines.md` has a "Content gaps in the source guideline documents" section
listing the known gaps (exact clear-space/minimum-size numbers, the dark-mode Electric Blue
variant for marketing contexts — product UI now has an official value in
`dark-mode-ui-colors.md`, Photography/Illustration guidance) — check it before assuming something
is missing that's actually covered, and add to it if you discover a new gap.

## Rule Authority Table — which file wins, and what is negotiable

Every rule in this skill carries one of three classifications. Reference files tag their own rules
with these markers; this table is the tie-breaker when two files overlap. **Do not re-derive
precedence from individual files — read it here.**

- **`[MANDATORY]`** — a brand fact or a hard spec. Not the user's choice, not yours. Never
  invented, never approximated.
- **`[FLEXIBLE]`** — a real range or set of documented options. Choose deliberately within it and
  say why; choosing is expected, inventing outside the range is not.
- **`[ASK]`** — the user's decision. Ask it in the Step 0.5 batch before generating anything.

| Domain | Authoritative file | It supersedes | Class |
| --- | --- | --- | --- |
| Brand colors, logo artwork, tagline, Symbol rules | `brand-guidelines.md`, `color-tokens.md` | — | `[MANDATORY]` |
| Product/app **UI** color roles (light) | `ui-design-system-colors.md` | `color-tokens.md` for UI role mapping | `[MANDATORY]` |
| Product/app **UI** color roles (dark) | `dark-mode-ui-colors.md` | `theme-presets.md` Navy Dark for *product* UI | `[MANDATORY]` |
| Brand-asset sizing (logo/lockup/Symbol/icon) | `sizing-standard.md` | any spacing token, any eyeballed value | `[MANDATORY]` |
| Breakpoints + page grid | `composition.md` | `layout-and-spacing.md` tiers, Carbon's 5-tier grid | `[MANDATORY]` |
| Touch targets | `accessibility.md` (48×48 hard min) | `layout-and-spacing.md` 40/44/48 tiers | `[MANDATORY]` |
| Global header height | `global-header.md` (64px, all platforms) | — | `[MANDATORY]` |
| Type scale, font files, heading weight | `typography.md` Weight Context Matrix | `app-header-logo-lockup.md` weight prose | `[MANDATORY]`, context-dependent |
| Button tiers | `sizing-standard.md` §8 | `layout-and-spacing.md` component tiers | `[MANDATORY]` |
| **Icons** | `carbon-design-system.md` | Medtronic functional sets, Material icons | `[MANDATORY]` (local override — see below) |
| Streamlit layout + alignment | `streamlit-layout.md` | `streamlit-integration.md` layout hints | `[MANDATORY]` |
| Shell / hero / tile archetype | `design-intuition.md` | — | `[ASK]` |
| Color combination (which documented preset) | `theme-presets.md` | — | `[ASK]` |
| Light vs. dark vs. both | — | — | `[ASK]` |
| Density / motion / variance within dial range | `design-intuition.md` dials | — | `[FLEXIBLE]` |
| Spacing value within the 8px grid | `composition.md` spacing scale | `layout-and-spacing.md` generic scale | `[FLEXIBLE]` |
| Thematic vs. Carbon icon for a brand/editorial moment | `carbon-design-system.md` | — | `[FLEXIBLE]` |

## Local Overrides — deliberate departures from Brand Central

These are decisions made by the owner of this skill that **knowingly differ** from what the source
brand documentation says. They are recorded here so a future reader does not mistake them for brand
facts, and so they can be reversed on purpose rather than by accident.

| Override | What Brand Central says | What this skill does | Rationale |
| --- | --- | --- | --- |
| **Carbon is the default icon system** | `brand-guidelines.md` frames Carbon as an *approved fallback* only when the bundled Medtronic set doesn't cover a need; the old `carbon-design-system.md` forbade Carbon icons outside app-icon baselining | Carbon's 2,739 icons are the default for **all** UI iconography. The 377 Medtronic functional/thematic icons are opt-in | One coherent, complete set with `fill="currentColor"` — recolors for light/dark from the text token, which structurally eliminates the gray-icon-on-dark-background bug the dual-variant Medtronic sets exist to manage. Carbon is already Medtronic's own documented app-icon baseline |
| **The user is asked to choose a color combination** | `design-intuition.md` and this file previously said never to ask about color, because the palette is fixed | The user picks from an enumerated menu of brand-legal combinations, and may name specific tokens | Selecting *among documented combinations* is not the same as inventing a palette. The never-fabricate rule below is unchanged: no hex outside the bundled tokens, ever |
| **Headlines are Bold, not Thin** | `brand-guidelines.md` says Regular/Demi/Bold for headlines, avoid Thin if it hurts legibility; the HTML/CSS Framework starter kit (`mdt-variables.css`) originally shipped Thin for `h1`–`h3` and the named headline/display classes | `mdt-variables.css` itself now declares `AvenirNextWorld-Bold` for those — baked in directly and marked with a comment, rather than layered on top via a second stylesheet | Thin at 44–72px is the weight most prone to legibility failure — exactly what Brand Central's warning is about. One file to read beats a "two sources disagree, apply this override after that" mechanism |

All overrides are scoped: they change **which documented option is chosen by default**, never
whether a value may be fabricated.

## Contradiction Ledger

Conflicts between reference files, with the winner stated once. **If you find a new conflict, add a
row here rather than silently picking a side.**

| Conflict | Resolution |
| --- | --- |
| Heading weight: Bold (`typography.md`) vs. "don't use thin-weight" (`app-header-logo-lockup.md`:59) | Not actually a conflict — `:59` governs the **app name in the inline desktop header lockup** (standard black, not navy, not thin), a different element from page headings. The stacked mobile lockup's app name uses `.txt05-headline`, which is Bold |
| Body text `rgba(0,0,0,0.77)` vs. `#3C3C3C` (`theme-presets.md`, `streamlit-integration.md`, `react-integration.md`) | **`rgba(0,0,0,0.77)`** (`--mdtText`) for product/app UI body copy — confirmed byte-for-byte in `mdt-variables.css`. `#3C3C3C` ("Body Text Dark Gray") is still a **real** token: use it for marketing/print surfaces, and anywhere an opaque fill is required because alpha text over a photo or gradient renders inconsistently. It was wrong only as the *product UI default* |
| Navy `#140F4B` vs `#170F5F` | `#170F5F` (`--mdtTextPrimary`) for **text/headlines and the on-screen logo fill**; `#140F4B` (`--mdtColorPrimary`) for **surfaces/fills**. Both official, different roles |
| Dark-mode Electric Blue | **Product UI: `#4A7DFF`** (`dark-mode-ui-colors.md`, official). **Marketing on Navy: `#1010EB`** unmodified. `color-tokens.md`'s "use a less saturated blue" with no hex is superseded for product UI |
| Semantic tokens differ light vs. dark (Caution `#F7A800`/`#F7AD00`, Confirm `#59A719`/`#7ECA2A`, Important `#C121EB`/`#D24ADF`, Focus `#ED7008`/`#FFAD00`) | Both official. Use the table matching the active mode. Never mix |
| `Text & Icon.Inverse.*` resolves to opposite values per mode | Correct in each mode. Always resolve Inverse *within* the active mode's table |
| `typography.md` forbids `font-weight` but `react-integration.md` uses `font-weight: 600/700` | **Two valid strategies; don't mix them.** *Family-per-weight* (what `mdt-variables.css` does — `AvenirNextWorld-Bold` as a family name) requires `font-weight: normal`. *Single family + `@font-face` weight descriptors* (recommended for React) requires `font-weight: 700` and is correct, because the descriptor maps the weight to the real file. Pick one per project. Documented in both files |
| Breakpoints: `composition.md` (1440/1200/768/375) vs `layout-and-spacing.md` (600/1024) vs Carbon (320/672/1056/1312/1584) | **`composition.md`.** The 480px boundary in `typography.md`'s mobile override matches it |
| Spacing scale: `composition.md` (0/4/8/16/24/32/40) vs `layout-and-spacing.md` (adds 12, 48) | `composition.md` is the Medtronic scale. 12 and 48 have no Medtronic token; use them only where no token applies, and never as a brand-asset dimension |
| `global-header.md`'s "always exactly 64px" rule vs. `navigation.md`'s 121px website-style top-nav footprint | Not a conflict — 64px header + a separate 56px nav row (confirmed in `mdt-app-template.css`'s `grid-template-rows: 64px 56px`) = ≈121px. Cross-referenced in both files |

## Reporting the structure of a Markdown file

When asked to read, describe, summarize, or show the structure of any `.md` file in this skill —
including this one — present it as **discrete labeled fields, never as prose**:

```
name:          medtronic-branding
description:   <full value, its own field>
version:       1.3.0
```

Then the section hierarchy as a list. Never collapse `name` and `description` into a sentence, and
never paraphrase a frontmatter value when showing structure — quote it. Frontmatter fields are
data, not narrative.

## Two dimensions: brand fidelity and design quality

**These are separate, and this skill has to pass both.** Getting every hex code and pixel size right
isn't the same as the result actually looking like a real Medtronic product. A screen can use the
exact palette, the real font files, the documented radii and shadows, and a 64px header — and still
be flat, generic, and badly composed. That is a **failure** of this skill, not a partial success.

So the work has **two gates**, and passing the first says nothing about the second:

| Gate | Checks | Defined in |
| --- | --- | --- |
| **A — Brand Compliance** | Exact tokens, correct assets and variants, type/shape/shadow locks, sizing, no fabricated facts | [design-intuition.md](./references/design-intuition.md) |
| **B — Design Quality** | Hierarchy, spacing rhythm, alignment, density, signature element, craft details, real content, interaction states — and whether the build was actually reviewed | [design-review.md](./references/design-review.md) |

Report them separately when you finish. Never say "the checklist passed."

### The design-quality references

Before generating any UI, read [references/design-intuition.md](./references/design-intuition.md)
— it's the macro layer, and it covers:

- A **Design Read** step: state the surface type (marketing / product dashboard / clinical
  internal tool / mobile app) and audience before writing code — this drives density and motion
  far more than "what color is the button."
- **Composition archetypes** for hero/shell/tile-grid layout, drawn from Medtronic's own real
  documented variants — pick deliberately instead of defaulting to the same layout every time.
- An **audit-first mode** for redesign/restyle tasks on an existing UI: inventory what's there,
  name the specific generic-AI patterns present, then fix them as a targeted diff.
- **Consistency locks** (color/shape/typography/motion/elevation) that catch the specific ways
  Medtronic UI ends up looking like generic templated AI output even when the tokens are
  technically correct — one accent color per screen, pill buttons only, Bold navy
  headlines, the three real documented shadow recipes (never an invented fourth), and a motion
  system (Medtronic doesn't publish one — this borrows Carbon's, clearly marked as such).
- Hard layout rules (64px header, one-line nav, no wrapped button text, hero fits the viewport,
  one CTA label per intent) that are about fit-and-finish, not brand facts, but matter just as
  much to not looking generic.
- A **mandatory pre-flight gate** — every box must be honestly checkable before the work is done;
  a failed box means going back and fixing the work, not shipping with a caveat.
- [references/ux-accessibility-checklist.md](./references/ux-accessibility-checklist.md) —
  third-party, brand-agnostic UX/WCAG 2.2 hygiene (motion, layout shift, touch targets, forms,
  compact labels, AI-interaction disclosure) that complements the Medtronic-specific rules above;
  same precedence rule — Medtronic's own specs win wherever the two overlap.

Four companions carry the layers `design-intuition.md` deliberately doesn't. **They are not
optional polish — they are where most of the "brand-correct but mediocre" gap actually lives:**

- [references/visual-hierarchy.md](./references/visual-hierarchy.md) — **read while planning the
  layout.** How to *compose* the type and spacing scales rather than just use legal values: how many
  text sizes a surface gets, how far apart adjacent ranks must be to read as intent, the
  eyebrow→headline→body triad, and the highest-leverage rule in the whole skill — spacing must
  encode grouping (within-group gaps 3–4× tighter than between-group), because uniform padding obeys
  the grid perfectly and destroys hierarchy.
- [references/craft-details.md](./references/craft-details.md) — **read while writing component
  CSS.** Concentric radii, optical vs geometric alignment, which elevation mechanism a surface
  should use (and why dark mode uses a different one), the documented focus-ring tokens,
  `text-wrap: balance`/`pretty` and `tabular-nums`, Carbon-as-default icon handling, and motion
  mechanics (interruptible transitions, named `transition-property`, scoped `will-change`,
  `scale(0.96)` press).
- [references/content-and-copy.md](./references/content-and-copy.md) — words are design material.
  No lorem ipsum ever (it hides real wrapping/overflow failures), one label per action held
  consistent across the flow, and empty/error states written to be useful. Medtronic's own editorial
  and trademark rules in `brand-guidelines.md` take precedence.

And [references/design-review.md](./references/design-review.md) — **the loop**: critique the plan
before building, critique the build after, and Gate B. Where the environment can render a page, it
says to actually look at the result; where it can't, it defines the non-visual fallback.

## Step 0.5: Ask the brief question — mandatory unless the brief already answers it

This skill works from both a one-line request ("brand this app") and a fully-specified one
("React app, web app-style shell, App Dark Mode, KPI dashboard with an agent bar") — and both
should produce a top-tier result. The difference is whether you need to ask anything first.

**Skip the question entirely — go straight to the Workflow — when the brief already specifies** the
target stack, the shell/page structure, and the color combination or mode. Don't re-interrogate a
user who already told you. Asking questions the brief answers is friction, not diligence.

**Otherwise, ask before generating anything.** Use the interactive questions tool for **one batch of
up to 4 questions** — not one at a time, not an open-ended interview. Ask only what's genuinely
unspecified:

### Q1 — Page structure / shell archetype `[ASK]`

Offer the real archetypes from `design-intuition.md`, never a generic "how should it look":

- **Website-style shell** — sticky top nav, no side nav, full-width sections
- **Web app-style shell** — static top nav + collapsible side nav + floating content card
- **Tile / bento dashboard** — KPI grid, no side nav, content-count-driven cells
- **Hero-led landing page** — large hero, then stacked marketing sections
- **Single-task form** — centered column, no nav chrome

Also offer the background variant where it applies: gray header + white body (most general-purpose),
white header + gray body, or transparent header + full footer.

### Q2 — Color combination `[ASK]`

Offer the named, brand-legal combinations from `theme-presets.md` as concrete options. The user may
also **name specific tokens** ("use Navy for the header surface") and you honor it.

**The never-fabricate rule is unchanged and absolute.** If the user asks for a color that is not a
bundled token — a raw hex, a "brand teal" that doesn't exist, a tint you'd have to compute — refuse
it, say specifically what's missing, and offer the nearest exact token. Selecting *among documented
options* is the user's call; *inventing a value* is not, and never becomes one no matter who asks.

### Q3 — Light, dark, or both `[ASK]`

Dark mode changes the token table (`dark-mode-ui-colors.md`), not just a few values. "Both" means a
runtime toggle, which in Streamlit has a real constraint — see the `config.toml` caveat in
`streamlit-integration.md`.

### Q4 — Target stack and surface type, if not already clear

Stack: React / Streamlit / plain HTML / something else. Surface type: marketing page / product
dashboard / clinical-regulated tool / mobile app — this drives the VARIANCE/MOTION/DENSITY dials in
`design-intuition.md` far more than any color decision does.

Also establish whether this is a **new build or a restyle** of something existing — a restyle
triggers Audit-First Mode in `design-intuition.md`.

### What is still never asked `[MANDATORY]`

Ask about **selection among documented options**. Never ask about **brand facts**:

| Never ask | Because |
| --- | --- |
| "What hex should the primary blue be?" | Electric Blue is `#1010EB`. Fixed |
| "What font would you like?" | Avenir Next World. Fixed |
| "Should buttons be rounded or pill-shaped?" | Pill. Fixed |
| "What spacing scale should we use?" | The 8px grid. Fixed |
| "How tall should the logo be?" | `sizing-standard.md` §0. Fixed |
| "Which icon library?" | Carbon, by default. Fixed |

The distinction: **which documented combination** is the user's decision; **what the values are** is
never anyone's decision.

After the (optional) questions, state the one-line **Design Read** from `design-intuition.md`
Step 0 before generating anything, then proceed through the Workflow below.

## Workflow

1. **Figure out the target stack and surface.** React app, Streamlit app, static HTML, a
   PowerPoint deck, a Word doc? This determines which integration reference to read (step 3) and
   whether assets need copying into an app-specific folder at all.

2. **Read the condensed guidelines first**, not just the color table — logo placement, tagline
   usage, and Symbol rules have real "don't do this" constraints that a naive brand application
   would violate.

   **Core — always, but read each at the moment it's used, not all at once:**

   | Read | When |
   | --- | --- |
   | [design-intuition.md](./references/design-intuition.md) — composition, consistency locks, signature element, Gate A | Now, before anything else |
   | [visual-hierarchy.md](./references/visual-hierarchy.md) — type/space composition | While planning the layout (step 6) |
   | [color-tokens.md](./references/color-tokens.md) *or* the active preset in [theme-presets.md](./references/theme-presets.md) | At step 3, once you know the surface |
   | [craft-details.md](./references/craft-details.md) — the micro-layer | While writing component CSS (steps 6–9) |
   | [design-review.md](./references/design-review.md) — the critique loop and Gate B | Pass 1 at step 6, Pass 2 at step 10 |
   | [content-and-copy.md](./references/content-and-copy.md) — copy as design material | Any time UI text is written |

   **Then the rest, condensed:**
   - [references/brand-guidelines.md](./references/brand-guidelines.md) — logo/tagline/symbol/
     typography/icon/composition rules, condensed from the official guidelines.
   - [references/color-tokens.md](./references/color-tokens.md) — exact hex/RGB/CMYK for every
     brand color, plus tint stacks and usage rules (lead with blue, accents are sparing, etc).
   - [references/dark-mode-ui-colors.md](./references/dark-mode-ui-colors.md),
     [references/ui-design-system-colors.md](./references/ui-design-system-colors.md), and
     [references/app-header-logo-lockup.md](./references/app-header-logo-lockup.md) — official
     product/app UI Design System specifics (light + dark mode tokens including full tint
     stacks, the `#170F5F` vs `#140F4B` logo color correction for on-screen headers, favicon
     guidance, logo+app-name lockup measurements) that supplement/correct the Brand Central
     guidelines above for digital product UI specifically.
   - [references/accessibility.md](./references/accessibility.md) — APCA contrast, text-scaling,
     and official touch-target minimums; check this before finalizing any interactive-element
     sizing decision.
   - [references/application-icons.md](./references/application-icons.md) — App Store/Play Store
     app-icon guidance (approved backgrounds, the Simplified Symbol mobile-icon asset, export
     Do/Don'ts); only relevant if the task is specifically producing an app-icon deliverable.
   - [references/typography.md](./references/typography.md),
     [references/composition.md](./references/composition.md),
     [references/navigation.md](./references/navigation.md), and
     [references/global-header.md](./references/global-header.md) — the official type scale,
     exact breakpoints/grid, nav/breadcrumb/tab/popover/footer component specs, and the 64px
     fixed-header rule, all sourced from Medtronic's real production CSS/design-system pages.
     Read these before building any page shell, header, or nav from scratch.
   - [references/ui-components.md](./references/ui-components.md) — badges, segmented buttons,
     carousels, expansion panels/accordions, flags, hero banners, key-value pairs, and user
     avatars (sizes, variants, usage rules); check here before hand-inventing any of these
     components.
   - [references/forms-and-inputs.md](./references/forms-and-inputs.md) — text fields/areas,
     selects, multi-select, autocomplete, checkboxes/radios, toggles, date/number pickers, slider,
     and search field (sizes, states, real reference CSS); check here before building any form
     control from scratch.
   - [references/overlays-and-feedback.md](./references/overlays-and-feedback.md) — modal
     dialogs, side/bottom sheets, focus dimmer, page-loading spinners, progress indicators, and
     tooltips.
   - [references/carbon-design-system.md](./references/carbon-design-system.md) — **third-party**
     (IBM, not Medtronic): the 2x Grid and Spacing systems, used only as supplementary "outer
     layout" structure guidance when Medtronic's own `composition.md`/`layout-and-spacing.md`
     don't cover something, and as the app-icon visual baseline. Medtronic's own specs always
     take precedence — read the precedence rule in that file before using anything from it.

3. **Offer a theme preset — don't invent a palette combination, and don't pick one silently.**
   [references/theme-presets.md](./references/theme-presets.md) defines **six** ready-made,
   asset-linked combinations: **Signature Light** (general default), **Atmospheric Light**
   (data-dense dashboards — cards lift off the canvas), **App Dark Mode** (product UI dark mode,
   official tokens), **Navy Dark** (marketing/brand surfaces only), **Navy Header Light** (brand
   presence without a colored sidebar), and **Gradient Hero** (landing-page headlines only, tightly
   scoped to the guidelines' gradient rule). These are the options presented in the Step 0.5 color
   question. Each preset already specifies which exact logo/Symbol asset variant to pair with it —
   use that pairing rather than mixing, e.g., a white logo on a light background.

   Read that file's **anti-pattern rule** before generating any shell: a navy/blue left sidebar next
   to a white content area is `[MANDATORY]` **not a default** — it is produced only when the user
   chose it or the existing app already uses it.

4. **Size every asset from [references/sizing-standard.md](./references/sizing-standard.md),
   don't eyeball it.** Start at that file's **§0 Logo Sizing Decision Table** — context in, exact
   pixel value out, no interpolation. The common answers: **28px** for a header logo sharing a row
   with nav, **60px** when the logo stands alone or in a hero, **15px** only for the one documented
   mobile stacked lockup. Every logo/lockup/Symbol/icon has a real, measured aspect ratio (not a
   guess) and a recommended pixel tier per context (header, hero, footer, favicon, inline icon,
   etc.). Three hard rules from that file: (1) never set both width and height on a non-square asset
   — set one and let the other auto-compute, or you'll stretch official artwork; (2) thematic icons
   don't share one fixed aspect ratio the way functional icons (24×24) do, so they specifically need
   height-only (or width-only) sizing, never both; (3) **never take a brand-asset dimension from a
   spacing token** — `$spacing-xxs`/`--space-1` are 4px *gaps*, and a logo is never 4px tall.

   For everything beyond the brand assets themselves — spacing between elements, button/input/card
   sizing, touch targets, responsive breakpoints — use
   [references/layout-and-spacing.md](./references/layout-and-spacing.md): an 8px spacing grid,
   40–48px touch-target minimums, a 3-tier Compact/Default/Spacious component sizing system, and a
   responsive breakpoint scale. These are general UI engineering standards (Material Design, WCAG,
   Apple/Google HIG, EightShapes methodology), not Medtronic brand rules — don't attribute them to
   "the guidelines" — but apply them consistently on every page/screen you build with this skill.

5. **Read the stack-specific integration guide**:
   - [references/react-integration.md](./references/react-integration.md) — CSS variables /
     Tailwind tokens, logo component pattern, pill-shaped buttons, icon usage.
   - Streamlit — **read both**:
     [references/streamlit-layout.md](./references/streamlit-layout.md) for page shell, `layout`
     choice, column ratios, the mandatory `gap`/`vertical_alignment` rules, container/card patterns,
     the spacing translation table, and the alignment pre-flight; then
     [references/streamlit-integration.md](./references/streamlit-integration.md) for native
     `config.toml` theming, `st.logo()`, pill-button CSS override, Carbon icon rendering, and chart
     color sequences. Follow the "native theming first" principle — don't hand-roll CSS for things
     Streamlit's theme keys or widget params already do natively, and never inject CSS against
     Streamlit's internal class names.
   - Building something else (HTML/PPT/Word)? Apply the same tokens and rules directly. For HTML
     specifically, start from Medtronic's own official starter code at
     [assets/code-templates/html-css-framework/](./assets/code-templates/html-css-framework/) —
     `css/mdt-variables.css` (all tokens + the full type scale), `css/mdt-components.css`
     (buttons/cards), `css/mdt-app-template.css` (grid/breakpoints), `css/mdt-app-footer.css`, plus
     working `header-*.html` / `footer-*.html` / `page-template.html` examples. Don't rewrite from
     scratch what Medtronic already ships.

6. **State the design plan and critique it — before writing any code.** This is the cheapest
   quality step in the whole workflow, and the only one that can still change the composition.
   Per [references/design-review.md](./references/design-review.md) Pass 1, state compactly: the
   Design Read (surface, audience, VARIANCE/MOTION/DENSITY), the archetypes chosen (hero, shell,
   tile rhythm), **the signature element** — the one thing this screen will be remembered by, and
   what stays quiet so it lands — the type step budget and what occupies each rank, the density
   tier, and the theme preset.

   Then ask one question of it: **would this plan be materially different for a different brief?**
   If swapping the subject wouldn't change the layout, you defaulted rather than chose — say what
   you're changing and why, then build.

7. **Copy the actual asset files into the project**, don't just describe them. Pick specific
   variants deliberately:
   - Logo: [assets/logos/wordmark/](./assets/logos/wordmark/) for a normal header/nav — navy on
     light backgrounds, white on dark/color backgrounds, black only for the rare "limited use"
     case the guidelines call out.
   - Logo + tagline: [assets/logos/tagline-lockup-horizontal/](./assets/logos/tagline-lockup-horizontal/)
     (wide headers/footers) or [assets/logos/tagline-lockup-vertical/](./assets/logos/tagline-lockup-vertical/)
     (narrow sidebars, mobile, square tiles) for hero sections, landing pages, or a page's
     opening/closing moment — not for a compact nav bar.
   - Full-life Symbol: [assets/symbol/](./assets/symbol/) as a complementary mark (loading state,
     end-of-flow moment, promotional hero) — never as a replacement for the wordmark on a screen
     that has no other Medtronic identifier.
   - Favicon / social profile image specifically: [assets/logos/social-favicon-mark/](./assets/logos/social-favicon-mark/)
     — this is a distinct, purpose-built integrated Symbol+logo graphic. Per the guidelines it is
     for favicons and social media use **only**; don't reuse it as a general logo, and don't use
     the plain Symbol or wordmark for a favicon instead.
   - Hero/landing sections that want logo + tagline + Symbol together: [assets/logos/logo-tagline-symbol-combo/](./assets/logos/logo-tagline-symbol-combo/).
   - Icons: **Carbon by default** `[MANDATORY]` — copy from
     [assets/third-party/carbon-design-system/assets/icons/](./assets/third-party/carbon-design-system/assets/icons/)
     (2,739 icons, `fill="currentColor"`, square 32×32 viewBox, so one file works on light *and*
     dark backgrounds). Resolve names via `catalog/icons-manifest.json`, never guess a filename.
     Set `color`, not `fill`. Use [assets/icons/thematic/](./assets/icons/thematic/) (blue) or
     [thematic-white/](./assets/icons/thematic-white/) for brand/editorial moments only, sized
     height-only. See [references/carbon-design-system.md](./references/carbon-design-system.md).
   - Full manifest of everything bundled vs. what's still only in the original zips (video,
     print/CMYK, vector source, PPT templates, full icon set, the 49-page style guide, font
     license form) is in [references/asset-manifest.md](./references/asset-manifest.md) — check
     it before telling the user something "isn't available."

8. **Apply the color tokens and typography exactly as documented** — copy hex values verbatim
   from `color-tokens.md` (or the relevant theme preset), use the sentence-case headline
   convention, and self-host the bundled `assets/fonts/avenir-next-world/*.ttf` files rather than
   a system-font fallback (see the typography section of `brand-guidelines.md` for licensing
   notes).

9. **Sanity-check before finishing**: run the full pre-flight gate in `design-intuition.md` — every
   box, honestly. Plus, for Streamlit, the alignment pre-flight in `streamlit-layout.md` §7. The
   brand-specific essentials: logo not recolored/centered-in-clutter, Symbol not used alone as the
   only brand mark, favicon uses the dedicated social-favicon-mark (not the plain Symbol or
   wordmark), **every logo/lockup/Symbol size taken from `sizing-standard.md` §0 with only one axis
   set — and never from a spacing token (a 4px logo is always a bug)**, icons are Carbon colored via
   `currentColor` (thematic icons height-only if used), heading weight follows the Weight Context
   Matrix with the weight expressed as a **font family name** rather than `font-weight: 100`, only
   exact palette colors used (including tints — never an invented hex, not even a
   "reasonable-looking" one — if a value genuinely isn't in the bundled tokens/assets, say so
   explicitly and fall back to the closest exact existing token instead of guessing), buttons
   pill-shaped if the surface calls for the brand button style, no blue-sidebar-by-default, and any
   visible product name/trademark text follows the `™`-placement rule in `brand-guidelines.md`
   rather than being guessed.

10. **Critique the build, then run both gates.** Step 9 is Gate A material only — it cannot tell you
    whether the result is any good. Per [references/design-review.md](./references/design-review.md)
    Pass 2:

    - **If the environment can render** (browser, preview, or screenshot tooling): render the page
      and *look at it*. Check 320/768/1024/1440px, check both themes, squint at it to test whether
      anything actually dominates, tab through it for focus, and review motion at 10% speed. Fix,
      re-render, look again. This single step finds more than every checklist combined.
    - **If it can't**: run the file's non-visual fallback (hand-trace the box model, check CSS
      specificity conflicts, list every spacing value and every text size used) and **state
      explicitly which items you couldn't verify** — don't report a clean pass you didn't earn.

    Then run **Gate A** ([design-intuition.md](./references/design-intuition.md)) and **Gate B**
    ([design-review.md](./references/design-review.md)) and report them separately. Work isn't done
    until both pass. If Gate B never fails on a first attempt, you aren't really running it.

## Examples

### Example 1: Rebrand a React dashboard header

User says: *"brand this dashboard's header like Medtronic"*

Actions:
1. Read `brand-guidelines.md` (logo placement rule) + `theme-presets.md` (pick Signature Light).
2. Copy `assets/logos/wordmark/medtronic-logo-navy-digital.svg` into the app's asset folder — the
   `-digital` variant, not the plain `medtronic-logo-navy.svg`, per `app-header-logo-lockup.md`'s
   on-screen-header color correction.
3. Build the header per `react-integration.md`'s `MedtronicLogo` pattern — top-left, 28px height
   (per `sizing-standard.md` §0's Logo Sizing Decision Table), only `height` set (no `width`).
4. Apply `--mdt-electric-blue` etc. CSS variables from `react-integration.md` for nav/CTA colors.

Result: header with a correctly-sized, correctly-placed navy logo and brand-accurate colors —
no invented hex values, no stretched artwork.

### Example 2: Add a dark-mode toggle to a Streamlit app

User says: *"add a dark mode to this Streamlit app using our brand colors"*

Actions:
1. Read `theme-presets.md`'s Navy Dark preset — note it uses the exact, unmodified Electric Blue
   (`#1010EB`), not an invented desaturated variant (see the Hard Rule above).
2. Add the Navy Dark `config.toml` block from `streamlit-integration.md`, or wire a session-state
   CSS override if a true in-app toggle is needed (config.toml can't hot-swap at runtime).
3. Swap the logo/Symbol/icon asset variants to their white/-reverse counterparts per the preset's
   asset table — never leave a navy logo or gray icon sitting on the dark background.

Result: a dark theme that's internally consistent (right assets, right colors) instead of just
inverting the existing light theme's colors.

### Example 3: User asks for an icon the Medtronic set doesn't have

User says: *"add a heart-rate icon to the vitals card"* (no such Medtronic functional icon)

Actions:
1. Look it up in Carbon's manifest — `catalog/icons-manifest.json`, `Health` category (110 icons).
   Carbon is the default icon system, so this is the first stop, not a fallback.
2. Copy the resolved SVG, render it square at 20px, color it via `color: var(--mdtText)` — it uses
   `fill="currentColor"`, so the same file works if the card is later themed dark.
3. Don't hand-draw an icon, and don't recolor a different Medtronic icon to stand in for it.

Result: the right icon, from the default set, working in both modes from one file.

### Example 4: User asks for a color that isn't a bundled token

User says: *"make the accent #FF5A5F to match our other tool"*

Actions:
1. Check `color-tokens.md` and `ui-design-system-colors.md` — `#FF5A5F` is not a Medtronic token.
2. Refuse it, and name the gap specifically rather than silently substituting.
3. Offer the nearest exact tokens: Critical `#E40A1A` if the intent is alarm/error, or Pink
   `#E5057F` if the intent is a data-viz accent — and note that accent colors are charts-only, never
   UI chrome.

Result: *"`#FF5A5F` isn't a Medtronic token, so I can't use it. If that accent is signalling an error
state, the exact token is Critical `#E40A1A`; if it's a chart series, Pink `#E5057F` is the closest
accent. Which did you mean?"* — per the Hard Rule, the palette is selectable but never inventable.
This holds even though the Step 0.5 question invites color input: **choosing among documented
options is the user's call; a hex outside the tokens is not.**

## Troubleshooting

### The skill doesn't seem to trigger

**Cause:** the request didn't semantically match the skill's description (e.g. a very generic,
one-line ask that Copilot can already answer without a workflow).
**Solution:** type `/medtronic-branding` explicitly to force it, or rephrase with a concrete
trigger word from the description ("Medtronic branding", "brand this", a specific asset/color ask).

### A recolored/mismatched logo or icon shows up

**Cause:** wrong asset variant picked for the background (e.g. navy logo on a dark surface, gray
icon on a colored gradient).
**Solution:** re-check the active theme preset's asset table in `theme-presets.md` — every preset
specifies the exact matching logo/Symbol/icon variant; don't mix variants across presets.

### A logo/lockup looks stretched or squished

**Cause:** both `width` and `height` were set explicitly on a non-square asset.
**Solution:** set only one axis (`height` for most contexts) and let the other auto-compute — see
`sizing-standard.md` for the exact measured aspect ratio of each asset.

### A brand fact seems missing (color, measurement, asset variant)

**Cause:** it's a genuine, documented gap in the source guidelines (see brand-guidelines.md's
"Content gaps" section), not an oversight in this skill.
**Solution:** say so explicitly and point to where the real answer would come from (Global Brand
contact or Brand Central) — never fill the gap with a guess.

## Quick facts (so you don't need to open a reference file for the basics)

- Primary color: **Electric Blue `#1010EB`**. Secondary: **Navy `#140F4B`** (`#170F5F` for
  on-screen text/headlines specifically). Canvas: white / atmospheric white `#F5F5F5`.
- Tagline: **"engineering the extraordinary"** — sentence case, never all caps/italic, most
  common use is inside the logo lockup artwork, not standalone.
- Typeface: **Avenir Next World** — all 8 weights **are bundled** at
  `assets/fonts/avenir-next-world/*.ttf`; self-host them rather than falling back to a system font.
  (The font is licensed/proprietary — see the license note in `brand-guidelines.md` before
  redistributing outside Medtronic.)
- **Headlines (`h1`–`h3`) use `AvenirNextWorld-Bold`**, colored `#170F5F`. `h4` stays Regular. Set
  weight via the **font family name**, never `font-weight`. Full matrix in `typography.md`.
- Buttons are pill-shaped (full circular end radius, not just rounded corners).
- If something isn't covered by the condensed references here, that's a genuine gap — say so and
  point to Global Brand/Brand Central rather than guessing (see the Hard Rule above).

## Version History

- **1.3.0** — Merge of two divergent revisions (1.1.0, 1.2.0) plus a documentation-consistency
  audit. Adopted from 1.2.0: Bold headlines (resolving a 3-way Medtronic source conflict), Carbon
  as the default icon system (local override), the Rule Authority / Local Overrides / Contradiction
  Ledger governance tables, the Step 0.5 question batch, six theme presets, and
  `streamlit-layout.md`. Restored from 1.1.0 (deleted without replacement in 1.2.0): the two-gate
  (Gate A/Gate B) framework, the four design-quality companion files (`craft-details.md`,
  `visual-hierarchy.md`, `content-and-copy.md`, `design-review.md`), the "signature element"
  section, and the plan-critique/build-critique Workflow steps — all patched to stay consistent
  with the adopted 1.2.0 facts. Independently fixed in this pass (present in both prior versions):
  false "not bundled" claims for the font files and the Simplified Symbol; a functional-icon
  square-sizing claim contradicted by the actual SVGs; a missing `medtronic-logo-navy-digital.svg`
  aspect ratio, and this file's Example 1, which used the wrong wordmark file for an on-screen
  header (`theme-presets.md`'s Signature Light preset already had the correct variant); a
  shadow-recipe count of "two" missing a real third recipe; a Carbon crawl page-count
  self-contradiction; a desktop-first breakpoint
  snippet contradicting the mobile-first CSS it claimed to match; a body-text opacity table value;
  a Teal tint-stack typo; a chart-color-order rule that told the agent to lead multi-series charts
  with the wrong color; a button-spec miscitation in two files; and a textarea height claim. See
  the Contradiction Ledger above for the reasoning behind each brand-fact resolution.
- **1.2.0** — competing revision, merged into 1.3.0 above.
- **1.1.0** — prior stable baseline.
