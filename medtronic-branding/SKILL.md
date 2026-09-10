---
name: medtronic-branding
description: 'Apply official Medtronic brand identity (logo, Full-life Symbol, tagline, exact color palette, Avenir Next World typography, iconography, composition rules) when building or restyling any UI — React, Streamlit, HTML/CSS, PowerPoint, or general design work. Use whenever the user mentions Medtronic branding, Medtronic brand guidelines, Medtronic colors/logo/symbol, "brand this app", "make this look like Medtronic", or asks to pull Medtronic assets/logos/icons/colors into a project. Bundles real logo/symbol/icon files and exact hex/RGB/CMYK color tokens extracted from the official brand guidelines — do not recreate the logo, guess brand colors, or invent a substitute palette.'
argument-hint: 'optional: target stack (react/streamlit/html) and what you are building'
compatibility: 'No network access or MCP server required — everything is bundled as local files (SVG/PNG assets + Markdown references). Works in Claude.ai, Claude Code, and GitHub Copilot Chat (VS Code). One optional enhancement: where the environment can render a page (browser/preview/screenshot tooling), the design review in references/design-review.md renders the build and inspects it, which materially improves output quality; where it cannot, that file defines a non-visual fallback so the workflow still completes — nothing here hard-requires a browser. Internal Medtronic use only — see the "Internal use only" note in the repo README.'
metadata:
  author: Medtronic Global Brand (packaged by ms68)
  version: 1.1.0
  category: design-system
  tags: [branding, design-system, react, streamlit, ui]
---

# Medtronic Branding

Turns the raw Medtronic brand-kit zips and guideline docs (archived in `Archive/` alongside this
skill's own working folder) into a ready-to-use design system: real logo/symbol/icon files plus
exact color tokens, ready-made light/dark/hero theme presets, and condensed usage rules, so a UI
can be branded correctly without re-deriving anything from scratch or guessing at colors.

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
3. Point at where the real answer would come from (Global Brand, `Archive/` source docs, or
   Brand Central directly) rather than filling the gap yourself.

`references/brand-guidelines.md` has a "Content gaps in the source guideline documents" section
listing the known gaps (exact clear-space/minimum-size numbers, the dark-mode Electric Blue
variant for marketing contexts — product UI now has an official value in
`dark-mode-ui-colors.md`, Photography/Illustration guidance) — check it before assuming something
is missing that's actually covered, and add to it if you discover a new gap.

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

Read [references/design-intuition.md](./references/design-intuition.md) before generating any UI —
it's the macro layer, and it covers:

- A **Design Read** step: state the surface type (marketing / product dashboard / clinical
  internal tool / mobile app) and audience before writing code — this drives density and motion
  far more than "what color is the button."
- **Composition archetypes** for hero/shell/tile-grid layout, drawn from Medtronic's own real
  documented variants — pick deliberately instead of defaulting to the same layout every time.
- An **audit-first mode** for redesign/restyle tasks on an existing UI: inventory what's there,
  name the specific generic-AI patterns present, then fix them as a targeted diff.
- **Consistency locks** (color/shape/typography/motion/elevation) that catch the specific ways
  Medtronic UI ends up looking like generic templated AI output even when the tokens are
  technically correct — one accent color per screen, pill buttons only, Thin-weight navy
  headlines, the two real documented shadow recipes (never an invented third), and a motion
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
  `text-wrap: balance`/`pretty` and `tabular-nums`, and motion mechanics (interruptible transitions,
  named `transition-property`, scoped `will-change`, `scale(0.96)` press).
- [references/content-and-copy.md](./references/content-and-copy.md) — words are design material.
  No lorem ipsum ever (it hides real wrapping/overflow failures), one label per action held
  consistent across the flow, and empty/error states written to be useful. Medtronic's own editorial
  and trademark rules in `brand-guidelines.md` take precedence.

And [references/design-review.md](./references/design-review.md) — **the loop**: critique the plan
before building, critique the build after, and Gate B. Where the environment can render a page, it
says to actually look at the result; where it can't, it defines the non-visual fallback.

## Step 0: Read the brief — ask questions only when genuinely ambiguous

This skill works from both a one-line request ("brand this app") and a fully-specified one
("React app, web app-style shell, App Dark Mode, KPI dashboard with an agent bar") — and both
should produce a top-tier result. The difference is whether you need to ask anything first.

**A prompt is already "structured" — skip straight to the Workflow below, no questions — when it
already tells you:** the target stack/surface (step 1), and enough about what's being built that
a composition archetype (per `design-intuition.md`) is obvious. Don't ask questions just to be
thorough when the brief already answers them — that's friction, not diligence.

**A prompt is "simple/vague" — ask before generating anything** when one or more of these is
genuinely unclear and would change the output: target stack (React/Streamlit/HTML/other), surface
type (marketing page / product dashboard / clinical-regulated tool / mobile app — this drives the
VARIANCE/MOTION/DENSITY dials in `design-intuition.md`), light vs. dark mode, and whether this is
a new build vs. restyling/matching an existing app (which triggers Audit-First Mode). Use the
interactive questions tool to ask **up to 2–3 targeted questions in one batch** (not one-at-a-time,
not an open-ended interview) covering only what's actually ambiguous — for example:

- "What are we building this for — a marketing page, an internal dashboard, or a clinical/
  regulated tool?" (drives density/motion)
- "What stack — React, Streamlit, plain HTML, something else?"
- "Is this a new page, or restyling something that already exists?" (if restyling, triggers
  audit-first mode in `design-intuition.md`)

**Never ask about anything that's already fixed by the brand** — colors, fonts, logo variant,
button shape, spacing scale, etc. are not the user's choice to make; asking "what color scheme
would you like?" is a hard miss for a skill whose entire point is that the palette is exact and
non-negotiable. Only ask about *context*, never about *brand facts*.

After the (optional) questions, state the one-line **Design Read** from `design-intuition.md`
Step 0 before generating anything, then proceed through the Workflow below.

## Workflow

1. **Figure out the target stack and surface.** React app, Streamlit app, static HTML, a
   PowerPoint deck, a Word doc? This determines which integration reference to read (step 3) and
   whether assets need copying into an app-specific folder at all.

2. **Read the references your task actually needs — route, don't read everything.** There are 20+
   reference files; loading all of them before a small task crowds out the attention the design
   itself needs, and an overloaded context is one of the reasons output drifts generic. Read the
   core, then only the rows that apply.

   **Core — always, but read each at the moment it's used, not all at once:**

   | Read | When |
   | --- | --- |
   | [design-intuition.md](./references/design-intuition.md) — composition, consistency locks, signature element, Gate A | Now, before anything else |
   | [visual-hierarchy.md](./references/visual-hierarchy.md) — type/space composition | While planning the layout (step 6) |
   | [color-tokens.md](./references/color-tokens.md) *or* the active preset in [theme-presets.md](./references/theme-presets.md) | At step 3, once you know the surface |
   | [craft-details.md](./references/craft-details.md) — the micro-layer | While writing component CSS (step 8) |
   | [design-review.md](./references/design-review.md) — the critique loop and Gate B | Pass 1 at step 6, Pass 2 at step 10 |

   **Then route by what you're building:**

   | Building… | Also read |
   | --- | --- |
   | Page shell, grid, breakpoints | `composition.md`, `layout-and-spacing.md` |
   | Header, top/side nav, breadcrumbs, tabs, footer | `global-header.md`, `navigation.md`, `app-header-logo-lockup.md` |
   | Buttons, badges, cards, accordions, carousels, avatars, hero banners | `ui-components.md`, `sizing-standard.md` |
   | Any form control | `forms-and-inputs.md`, `accessibility.md` |
   | Modals, sheets, tooltips, spinners, progress | `overlays-and-feedback.md` |
   | Dark mode | `dark-mode-ui-colors.md`, `theme-presets.md` |
   | Light-mode product UI colors, semantic/status colors | `ui-design-system-colors.md` |
   | Charts / data visualization | `ux-accessibility-checklist.md` (chart-type table), `ui-design-system-colors.md` (accent order) |
   | Type scale, headings, text styles | `typography.md` |
   | Placing/sizing logo, Symbol, lockups, icons | `brand-guidelines.md`, `sizing-standard.md`, `asset-manifest.md` |
   | Marketing / landing page | `ux-accessibility-checklist.md` (section-order archetypes), `theme-presets.md` (Gradient Hero) |
   | Static HTML / no framework | `assets/code-templates/html-css-framework/` (see step 5) |
   | An app-icon deliverable | `application-icons.md` |
   | Restyling an existing UI | `design-intuition.md` audit-first mode, `design-review.md` |
   | Any UI copy at all | `content-and-copy.md` |
   | Accessibility sign-off | `accessibility.md`, `ux-accessibility-checklist.md` |

   **Three precedence rules that hold regardless of which rows you read:**
   - For **digital product UI specifically**, `ui-design-system-colors.md`,
     `dark-mode-ui-colors.md`, and `app-header-logo-lockup.md` supplement *and correct* the Brand
     Central guidelines in `brand-guidelines.md` — including the `#170F5F` vs `#140F4B` logo color
     correction for on-screen headers.
   - `carbon-design-system.md` is **third-party** (IBM, not Medtronic) — supplementary outer-layout
     structure only, when Medtronic's own `composition.md`/`layout-and-spacing.md` don't cover
     something. Read the precedence rule in that file before using anything from it. Same status for
     `ux-accessibility-checklist.md` and `craft-details.md`.
   - Read `brand-guidelines.md` before any task that places the logo, tagline, or Symbol — those
     have real "don't do this" constraints a naive brand application will violate.

3. **Pick a theme preset instead of inventing a palette combination.**
   [references/theme-presets.md](./references/theme-presets.md) defines three ready-made,
   asset-linked combinations: **Signature Light** (default), **Navy Dark** (dark mode/dark
   sidebar), and **Gradient Hero** (landing-page headlines only, tightly scoped to the
   guidelines' gradient rule). Each preset already specifies which exact logo/Symbol/icon file
   variant to pair with it — use that pairing rather than mixing, e.g., a white logo on a light
   background or gray icons on a dark background.

4. **Size every asset from [references/sizing-standard.md](./references/sizing-standard.md),
   don't eyeball it.** Every logo/lockup/Symbol/icon has a real, measured aspect ratio (not a
   guess) and a recommended pixel tier per context (header, hero, footer, favicon, inline icon,
   etc.). Two hard rules from that file: (1) never set both width and height on a non-square
   asset — set one and let the other auto-compute, or you'll stretch official artwork; (2)
   thematic icons don't share one fixed aspect ratio the way functional icons (24×24) do, so they
   specifically need height-only (or width-only) sizing, never both.

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
   - [references/streamlit-integration.md](./references/streamlit-integration.md) — native
     `config.toml` theme mapping, `st.logo()`, pill-button CSS override, icon rendering, chart
     color sequences. Follow the "native theming first" principle — don't hand-roll CSS for
     things Streamlit's theme keys or widget params already do natively.
   - **Static HTML/CSS — start from Medtronic's own production starter code, don't hand-roll it.**
     [assets/code-templates/html-css-framework/](./assets/code-templates/html-css-framework/) is the
     real shipped UI Design System kit: `page-template.html` (CSS Grid shell with correct responsive
     margins/content areas), three working header variants (`header-no-nav.html`,
     `header-simple-nav.html`, `header-dropdown-nav.html`), two footers
     (`footer-standard.html`, `footer-minimal.html`), and `css/mdt-variables.css` (tokens + the full
     type scale), `css/mdt-components.css` (buttons, inputs, focus rings), `css/mdt-app-template.css`
     (grid/breakpoints/nav), `css/mdt-app-footer.css`. This is the source `typography.md`,
     `composition.md`, and `sizing-standard.md` were derived *from* — building an HTML page from
     scratch when this exists produces strictly worse output. Copy it in and extend it.
   - Building a PowerPoint deck or Word doc? Apply the tokens and rules directly — those are
     stack-agnostic and there's no separate reference file.

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
   - Icons: [assets/icons/functional/](./assets/icons/functional/) (gray) and
     [assets/icons/thematic/](./assets/icons/thematic/) (blue) on **light** backgrounds;
     [assets/icons/functional-white/](./assets/icons/functional-white/) and
     [assets/icons/thematic-white/](./assets/icons/thematic-white/) on **dark/color**
     backgrounds (Navy Dark preset, colored gradient sections, etc.) — per the icon color rule,
     never leave gray/blue icons sitting on a dark or colored background.
   - Starter code (HTML/CSS builds): [assets/code-templates/html-css-framework/](./assets/code-templates/html-css-framework/)
     — Medtronic's own shipped page shell, header/footer variants, and four production CSS files.
     Copy these in rather than writing an equivalent from scratch (see step 5). Even on React or
     Streamlit, `css/mdt-variables.css` and `css/mdt-components.css` are worth reading as the
     authoritative source for the type scale, button tiers, and focus-ring implementation.
   - Full manifest of everything bundled vs. what's still only in the original zips (video,
     print/CMYK, vector source, PPT templates, full icon set, the 49-page style guide, font
     license form) is in [references/asset-manifest.md](./references/asset-manifest.md) — check
     it before telling the user something "isn't available."

8. **Apply the color tokens and typography exactly as documented** — copy hex values verbatim
   from `color-tokens.md` (or the relevant theme preset), use the sentence-case headline
   convention, and use the documented Avenir Next World fallback stack (the real font is
   licensed/proprietary and not bundled — see the typography section of `brand-guidelines.md`
   for what to tell the user about that gap).

9. **Brand sanity-check**: logo not recolored/centered-in-clutter, Symbol not used
   alone as the only brand mark, favicon uses the dedicated social-favicon-mark (not the plain
   Symbol or wordmark), icon color variant matches the background (white icons on dark/color,
   gray/blue on light — never mismatched), every logo/lockup/Symbol/icon sized per
   `sizing-standard.md` with only one axis set explicitly (no stretched artwork), only exact
   palette colors used (including tints — never an invented hex, not even a "reasonable-looking"
   one — if a value genuinely isn't in the bundled tokens/assets, say so explicitly and fall back
   to the closest exact existing token instead of guessing), buttons pill-shaped if the surface
   calls for the brand button style, and any visible product name/trademark text follows the
   `™`-placement rule in `brand-guidelines.md` rather than being guessed.

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
2. Copy `assets/logos/wordmark/medtronic-logo-navy.svg` into the app's asset folder.
3. Build the header per `react-integration.md`'s `MedtronicLogo` pattern — top-left, 28px height
   (Compact tier from `sizing-standard.md`), only `height` set (no `width`).
4. Apply `--mdt-electric-blue` etc. CSS variables from `react-integration.md` for nav/CTA colors.
5. Gate B pass — the part that's easy to skip: nav items on one line at desktop with no wrapped
   labels, a visible `:focus-visible` ring (`#ED7008`, per `craft-details.md`) on every nav link and
   the avatar, the logo optically aligned against the nav baseline rather than just
   `align-items: center`, and one shared left edge with the page content below it.

Result: a header with a correctly-sized, correctly-placed navy logo and brand-accurate colors —
no invented hex values, no stretched artwork — that also sits properly on the page instead of
merely containing the right assets.

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

### Example 3: User asks for a color/asset that isn't bundled

User says: *"make the icon pink to match our accent"* (no pink icon variant exists)

Actions:
1. Check `color-tokens.md` — confirm Pink (`#E5057F`) is a real, exact accent token.
2. Check `asset-manifest.md` — confirm no pink icon SVGs are bundled (only gray/blue/white).
3. Don't recolor the SVG with a CSS filter/hue-hack to fake a pink icon.

Result: tell the user directly — "there's no pink icon variant bundled; the closest options are
the gray/blue/white functional and thematic sets, or request the accent-color icon set from
`Archive/coll-icons-png-svg.zip` if a true pink variant exists there" — per the Hard Rule, don't
fabricate one.

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
contact, Brand Central, or the raw source docs in `Archive/`) — never fill the gap with a guess.

## Quick facts (so you don't need to open a reference file for the basics)

- Primary color: **Electric Blue `#1010EB`**. Secondary: **Navy `#140F4B`** (`#170F5F` for
  on-screen text/headlines specifically). Canvas: white / atmospheric white `#F5F5F5`.
- Tagline: **"engineering the extraordinary"** — sentence case, never all caps/italic, most
  common use is inside the logo lockup artwork, not standalone.
- Typeface: **Avenir Next World** (licensed, not bundled — use a sans-serif fallback, see above).
- Buttons are pill-shaped (full circular end radius, not just rounded corners).
- Full source guideline docs (`1st Half Guidelines.docx`, `2nd Half Guidelines.docx`,
  `Style Guide.pdf`, `doc-color-palette-breakdown.pdf`) live in the `Archive/` folder if something
  isn't covered by the condensed references.
