# Design intuition — composition, consistency, and anti-generic discipline

**You are not a token-filling script.** Getting hex codes and pixel sizes technically right while
producing a generic, templated layout is a failure of this skill, not a partial success. Act like
a senior Medtronic product designer who happens to have perfect recall of the brand system — not
like an intern pattern-matching "blue button, navy heading, done." Tokens and component specs
elsewhere in this skill tell you *what* Medtronic's assets are. This file tells you *how to
compose them* — the layer most brand-token skills skip, and the reason AI-generated brand UI so
often looks templated even when every hex code is correct.

**This file is mandatory reading before writing any UI code, not optional polish.** The
[pre-flight check](#pre-flight--two-gates-and-passing-the-first-proves-nothing-about-the-second) at
the end is a **gate**: if you can't honestly check every box, the work isn't done — go back and fix
it, don't ship it and mention the gaps in prose afterward.

**This file is the macro layer. Three companions carry the rest, and they are not optional:**

| File | Covers | Read it |
| --- | --- | --- |
| [visual-hierarchy.md](./visual-hierarchy.md) | How to *compose* the type and spacing scales — step budgets, real steps, spacing that encodes grouping, alignment, density calibration | While planning the layout |
| [craft-details.md](./craft-details.md) | The micro-layer: concentric radii, optical alignment, elevation mechanism, focus rings, `text-wrap`/`tabular-nums`, motion mechanics | While writing component CSS |
| [design-review.md](./design-review.md) | Critique the plan before building, critique the build after — and **Gate B, the design-quality gate** that this file's Gate A deliberately does not cover | Before and after building |

Copy is design material too — [content-and-copy.md](./content-and-copy.md) covers it, and no
placeholder text is ever acceptable (it hides real layout failures).

## Step 0: Read the brief before touching code

Medtronic's brand identity is fixed — you're never choosing a palette or typeface. What you *are*
choosing, every time, is composition: density, motion, hierarchy, and restraint. Get this from
context before generating anything:

1. **Surface type** — marketing/website, product/app dashboard, clinical or regulated internal
   tool, mobile app. This is the single biggest driver of the dials below.
2. **Audience** — clinician under time pressure, patient/caregiver, internal enterprise employee,
   prospective customer browsing marketing. Regulated/clinical audiences override aesthetic
   preference every time (see the Density/Motion table).
3. **Existing product context** — is this a new page in an existing app (match its density/shell
   choice — see `composition.md`), or a greenfield build (you get to choose the shell)?

State a one-line **Design Read** before generating code, e.g.:
*"Reading this as: an internal clinical dashboard for time-pressured staff — high density, low
motion, App Dark Mode available, web-app-style shell with side nav."*
*"Reading this as: a public marketing landing page — moderate density, restrained-but-present
motion, website-style shell, Signature Light theme, hero-scale logo."*

If genuinely ambiguous, ask — don't guess and rebuild later. See `SKILL.md`'s "Step 0" for the full
rule on when to ask vs. when the prompt is already structured enough to skip straight to work: use
the interactive questions tool for **up to 2–3 batched, targeted questions** about *context only*
(surface type, stack, new-build vs. restyle) — never about brand facts (color/font/logo/shape),
those are fixed and not the user's choice.

## The three dials, calibrated for Medtronic

Unlike a generic agency brief, Medtronic's brand is conservative-professional by design — even the
"high variance" end here is far more restrained than a consumer/agency site. Never reach for
agency-tier chaos (rotated cards, mesh gradients, oversized display type) — that's off-brand, not
"bold."

| Dial | 1 (low) | Medtronic baseline | 10 (high — rarely appropriate) |
| --- | --- | --- | --- |
| **VARIANCE** (layout boldness) | Single-column, perfectly symmetric, dense forms | **4–5**: asymmetric hero (logo/content split), varied card sizes in a bento using real aspect ratios | Never go past ~6 — Medtronic has no precedent for "artsy chaos" layouts |
| **MOTION** (animation presence) | Static, instant state changes | **3–4**: productive easing on micro-interactions only (see Motion section below) | Never go past ~5 — expressive motion is reserved for rare, meaningful moments (a critical alert appearing), not everyday chrome |
| **DENSITY** (information per screen) | Airy marketing page | **4–6** depending on surface type (see table) | Dense clinical data tables can push to 7–8 — Medtronic's Data Tables/Compact tiers exist exactly for this |

### Surface → dial presets

| Surface | VARIANCE | MOTION | DENSITY | Notes |
| --- | --- | --- | --- | --- |
| Marketing/website | 5–6 | 4 | 3 | Hero banners, website-style shell, more whitespace is appropriate here than anywhere else in the system |
| Product dashboard (internal, non-clinical) | 4 | 3 | 5–6 | Web app-style shell, side nav, Compact component tier for data-dense areas |
| Clinical / regulated tool | 2–3 | 1–2 | 6–8 | Motion should be nearly invisible — a clinician mid-task should never wonder if something is still loading or already changed. Favor instant, obvious state changes over animated ones. |
| Mobile app | 3–4 | 3 | 4–5 | 64px header rule still applies; bottom sheet preferred over side sheet per `overlays-and-feedback.md` |

## Composition archetypes — pick one deliberately, don't default to the first idea

Every documented Medtronic layout pattern already has multiple real, named variants. "Bland
generic AI layout" usually isn't a brand-accuracy failure — it's picking the single most obvious
variant every time instead of choosing deliberately from what's actually available. Before laying
out a page, explicitly pick from these real (not invented) options:

### Hero archetypes (`ui-components.md` → Hero banners)

| Archetype | When to use |
| --- | --- |
| **Transparent, Large** | Desktop/tablet marketing pages with strong photography/illustration — header overlays the hero image |
| **Transparent, Medium** | Marketing pages where the hero needs less dominance than a full Large treatment |
| **Below Nav, Medium/Large** | Product pages, any page with breadcrumbs, and the *only* pattern used on mobile — header stays opaque, hero sits cleanly below it |
| **Light vs Dark background** | Pick based on surrounding content and which gives the logo/CTA the most contrast — don't default to Light every time just because it's listed first |

Don't build every hero as "Transparent Large Light" by reflex — that's the equivalent of the
generic centered-hero-on-gradient AI default, just wearing Medtronic colors. A results/dashboard
landing page reads more truthfully as **Below Nav Medium**; a campaign/launch page earns
**Transparent Large**.

For a full marketing/landing page, the hero is one section among several — see
[ux-accessibility-checklist.md](./ux-accessibility-checklist.md)'s "Landing-page section-order
archetypes" table for named, structural full-page patterns (Hero+Features+CTA, Funnel,
Comparison table, Pricing page, etc.) to pick from instead of defaulting to the same section order
every time. Same rule applies to charts: that file's "Chart type selection" table picks the right
chart *shape* for a data question — fill it with Medtronic's own accent colors/order, never the
source dataset's example hex values.

### Shell archetypes (`composition.md` → UI shell selection)

| Archetype | When to use |
| --- | --- |
| **Website-style shell** (sticky top nav, no side nav) | Content-driven: marketing, docs, informational pages |
| **Web app-style shell** (static top nav + collapsible side nav + floating content card) | Actionable/interactive: dashboards, admin tools, anything with persistent navigation between many views |
| Background variant: gray header + white body | Default, most general-purpose |
| Background variant: white header + gray body | When the body content itself needs to read as "the canvas" (data tables, forms) |
| Background variant: transparent header + full link-farm footer | `.com`-style marketing/informational sites specifically |

Never mix shell archetypes on one page (e.g. a floating-card app shell with a `.com`-style footer)
— pick one shell family and stay in it end to end.

### Tile/bento rhythm (`carbon-design-system.md` → 2x Grid aspect ratios)

When a page needs a card/tile grid (feature grid, dashboard summary tiles, a bento layout), don't
repeat one tile size and shape down the page — that's the specific "one-sided repetition" tell.
Instead:

- **Cell count matches content count.** 3 items → 3 cells, not 3 cells plus an empty filler tile.
- **Vary aspect ratio deliberately** using the real documented set (1:1, 2:1, 2:3, 3:2, 4:3, 16:9)
  — e.g. one 2:1 "hero" tile plus several 1:1 supporting tiles reads as intentional; six identical
  1:1 tiles in a row reads as a template.
- **Base every tile on the same fixed-size unit** (8/16/24/32/48/64/80px from Carbon's sizing
  scale) multiplied consistently — mixing an arbitrarily-sized tile into an otherwise consistent
  grid is the visible "didn't plan the grid" tell.

## The signature element — one deliberate moment per screen

Picking an archetype from the tables above stops you producing the *worst* default. It does not, on
its own, produce something memorable — a page assembled entirely from correct menu selections is
competent and anonymous. The missing question is positive rather than defensive: **what is the one
thing someone remembers about this screen?**

Pick exactly one, name it in the Design Read, and then **keep everything else quiet so it lands.**
Boldness spent in two places cancels out; boldness spent in five is noise.

**Within Medtronic's brand this is a composition decision, never a decoration decision.** The
VARIANCE ≤6 cap above still binds, and the consistency locks below are not negotiable. A signature
is *never* a new color, font, radius, shadow, gradient, or motion curve — those are all fixed, and
reaching for one is a brand failure, not a bold choice. What's actually available:

| Signature | What it looks like in this system |
| --- | --- |
| **A data moment** | The primary metric treated as the hero — `.txt08-headline`/`.txt09-display` scale on the number itself, with the chart as quiet support. Or one genuinely well-chosen chart type (per `ux-accessibility-checklist.md`) instead of three generic ones. |
| **A typographic moment** | One Thin-weight 56px/72px headline given real space, against otherwise compact type. The documented display scale exists and is almost never used. |
| **A composed empty/first-run state** | The state most products neglect, done properly — Symbol or thematic icon, one clear sentence, one action. Memorable precisely because nobody expects care here. |
| **A structural asymmetry** | A deliberate hero split or a 2:1 tile anchoring an otherwise 1:1 grid — using the documented aspect ratios, not an invented layout. |
| **A meaningful Symbol placement** | The Full-life Symbol at an end-of-flow or completion moment, per its documented complementary-mark role — never as the only brand mark on the screen. |

**Surface calibration.** The higher the stakes, the quieter the signature:

- Marketing / website — a signature is expected; use the fuller end of the range.
- Product dashboard — usually the data moment or a composed empty state. Restrained.
- Clinical / regulated tool — the signature is *clarity itself*: the most important reading being
  unmistakably the most prominent thing on screen. Nothing expressive. A clinician mid-task is not
  an audience for a design flourish.

If you can't name the signature in one sentence, the page doesn't have one yet — and it will read as
generic no matter how correct its tokens are.

## Audit-first mode (redesigning or restyling an existing UI)

When the task is "brand this existing app/page" or "redesign X to match Medtronic," **don't start
editing immediately.** Audit first, then act:

1. **Inventory what's already there** before touching it: what shell pattern is it using, what
   component tiers, what's the existing spacing rhythm. Don't discard working structure just to
   rebuild it from scratch — brand it in place where the underlying structure is already sound.
2. **Name the specific generic-AI patterns present**, out loud, before fixing them — e.g. "this
   uses `Inter` with a system-default blue, three symmetric feature cards, and a single flat
   `box-shadow` everywhere." Fixing without naming the problem first tends to fix the colors and
   miss the structural issues (shape/shadow/motion consistency, hero fit, nav wrapping).
3. **Apply the consistency locks below as a diff, not a rewrite** — swap the font/color/shadow/
   radius values for the documented Medtronic ones, keep working layout structure, and only
   restructure composition (hero archetype, shell, tile rhythm) where the existing choice was
   actively generic (e.g. a centered hero with no real reason to be centered).
4. **Re-run the pre-flight check against the *whole* page**, not just the parts you touched — a
   rebrand that fixes the header but leaves an old system-font modal is a visible inconsistency,
   not a partial win.

## Anti-generic consistency locks

These are hard rules, not suggestions. Each one exists because it's a specific way AI-generated
Medtronic UI ends up looking like generic Bootstrap/Tailwind-default slop wearing a blue logo.

### Color Consistency Lock

- **One accent per screen: Electric Blue (`#1010EB`).** Never let a second accent color
  (Pink/Orange/Teal/etc. from the accent palette) creep in as a "second brand color" for buttons
  or links just because it's technically in `ui-design-system-colors.md` — those accents are for
  **data visualization only**, never UI chrome. A screen with an Electric Blue primary button and
  a Teal secondary button is a Do NOT documented explicitly in `ui-design-system-colors.md`.
- If multiple data series need color, use the documented preferred order (Electric Blue → Navy →
  Light Blue → Pink → Orange → Lavender → Green → Purple → Teal → Red → Brown) — never invent a
  different order or skip straight to a "nice looking" color out of sequence.
- Light and dark mode use **different exact tokens** (see `dark-mode-ui-colors.md` vs
  `ui-design-system-colors.md`) — never algorithmically darken/lighten a light-mode hex to fake a
  dark-mode color.

### Shape Consistency Lock

- **Buttons are always pill-shaped** (`border-radius` = the button's own height — 32/40/48/56px
  per tier). Never a slightly-rounded rectangle button anywhere in a Medtronic UI.
- **Cards, inputs, flags, tooltips use small fixed radii** — 4px (inputs, flags, tooltips) or 8px
  (modals, sheets). Never mix a 2xl/"squircle" radius (16px+) onto these — that's a different
  design language, not a Medtronic one.
- Don't let one screen mix "pill everything" (a generic AI default) with Medtronic's actual rule
  (pills for buttons/search only, small radii for content containers).

### Typography Discipline

- Headlines (`h1`–`h3`, `.txt06`+) are **always** the Thin weight file, **always** colored
  `#170F5F` (on-screen navy) — never the Regular/Demi weight, never plain black, never a random
  accent color, per `typography.md`.
- Body copy is **77% black** (`rgba(0,0,0,0.75)` / `--mdtText`), not pure black — pure-black body
  text is a generic-AI tell in this system specifically because Medtronic's own guidelines call
  out 77% black by name.
- **Never substitute a system font** (Inter, Roboto, Arial, "sans-serif" left un-overridden) when
  Avenir Next World is available and bundled at `assets/fonts/avenir-next-world/` — self-host it
  per `react-integration.md`/`streamlit-integration.md`. A Medtronic UI in Inter is an immediate,
  visible brand miss.
- One emphasis mechanism: **bold/strong text uses the Demi font file**, *never* `font-weight:
  bold` on the Regular file (Avenir Next World's weights are separate font files, not a single
  variable font) — this is a specific, easy-to-get-wrong detail from the real bundled CSS.

### Motion (a genuine gap in Medtronic's own docs — filled from Carbon, clearly marked as such)

Medtronic's own UI Design System doesn't publish motion/animation tokens. Rather than inventing
arbitrary durations, borrow IBM Carbon's motion system (same third-party/supplementary status as
`carbon-design-system.md`'s grid) — it's well-reasoned and pairs naturally with Carbon's
already-adopted grid:

| Duration token | Value | Use for |
| --- | --- | --- |
| `duration-fast-01` | 70ms | Micro-interactions: button/toggle state changes |
| `duration-fast-02` | 110ms | Micro-interactions: fades |
| `duration-moderate-01` | 150ms | Small expansions, short-distance movement |
| `duration-moderate-02` | 240ms | Larger expansion, toasts, system communication |
| `duration-slow-01` | 400ms | Large expansions, important system notifications |
| `duration-slow-02` | 700ms | Background dimming (the modal focus-dimmer fade) |

Two easing families — **use "productive" everywhere by default**; "expressive" only for rare,
meaningful moments (a critical alert, opening a brand-new page), never for everyday chrome:

| Curve | Productive (default) | Expressive (rare, meaningful moments only) |
| --- | --- | --- |
| Standard (visible start → end) | `cubic-bezier(0.2, 0, 0.38, 0.9)` | `cubic-bezier(0.4, 0.14, 0.3, 1)` |
| Entrance (element appearing) | `cubic-bezier(0, 0, 0.38, 0.9)` | `cubic-bezier(0, 0, 0.3, 1)` |
| Exit (element leaving) | `cubic-bezier(0.2, 0, 1, 0.9)` | `cubic-bezier(0.4, 0.14, 1, 1)` |

Never use `linear` or a bouncy/spring/overshoot easing — Medtronic/Carbon's whole motion language
is "quick to start, smooth to stop," never playful bounce. Animate only `transform`/`opacity` for
performance, same as any modern frontend discipline.

See [ux-accessibility-checklist.md](./ux-accessibility-checklist.md)'s Motion hygiene section for
the tool-agnostic rules on top of these tokens (reduced-motion handling, carousel pause behavior,
cleanup, not relying on animation-end for state correctness).

### Elevation Discipline

Two, and only two, documented shadow recipes exist in this system — use the one that matches what
you're building, never invent a third:

- **Popover/dropdown/menu elevation** (`navigation.md`):
  `0 1px 8px rgba(0,0,0,.12), 0 3px 4px rgba(0,0,0,.14), 0 3px 3px rgba(0,0,0,.2)`
- **Modal/sheet elevation** (`overlays-and-feedback.md`, stronger):
  `0 1px 18px rgba(0,0,0,.12), 0 6px 10px rgba(0,0,0,.14), 0 3px 5px rgba(0,0,0,.2)`

Never use a generic single-layer `box-shadow: 0 4px 6px rgba(0,0,0,0.3)` default — flat single-tone
shadows are a visible generic-AI tell next to these real, layered, tuned recipes.

**Two limits on when a shadow is the right mechanism at all** — see
[craft-details.md §3](./craft-details.md):

- **Shadow means "floating above", not "is a surface".** A resting card that never lifts should be
  separated by a background step (`General.Surface.level 0` → `level 1`) or a border, not a shadow.
  The two recipes above are for popovers/menus and modals/sheets — things that are temporarily on
  top. A page of shadowed resting cards is the generic SaaS-card look wearing Medtronic colors.
- **Both recipes above are light-mode only.** They're black-based and effectively invisible on
  `#121212`. [dark-mode-ui-colors.md](./dark-mode-ui-colors.md) says so directly — *"Elevation in
  dark mode is conveyed with progressively lighter grays, not drop shadows alone"* — and ships
  `elevated` surface tokens that step one level lighter for exactly this purpose. In App Dark Mode,
  raise a surface with its `elevated` token (plus `General.Borders & Lines.light` if needed), not
  with these recipes.

### Layout Hard Rules (fit-and-finish, not just brand accuracy)

- **Header is always exactly 64px** (`global-header.md`) — never taller "for breathing room."
- **Hero must fit believably in the first viewport** on desktop — a headline that forces 4+ lines
  or pushes the CTA below the fold is a font-scale error, not a copy-length problem worth
  tolerating.
- **Nav renders on one line at desktop.** If items don't fit, condense labels or move to an
  overflow/hamburger — never let primary nav wrap to a second line.
- **Button text never wraps.** If a label wraps to 2 lines, shorten it (buttons use `.txt02-` /
  `.txt03-button` styles, not body copy) — never shrink the tier's official padding to force a fit.
- **One CTA label per intent, per page.** Don't mix "Get Started" / "Try it now" / "Sign up free"
  as if they were different actions — pick one label for one intent (this compounds with the
  brand's own "one clear CTA per text group" eyebrow-link rule in `ui-design-system-colors.md`).
- **Button/text contrast is checked, not assumed.** A ghost/secondary button over a photo or
  gradient background needs a scrim or border — ghost buttons with no border floating over
  variable-contrast imagery is a real, easy-to-ship accessibility bug.
- **Form labels sit above the field, always** (per `forms-and-inputs.md`) — never
  placeholder-as-label; the required-field asterisk is `#C121EB` (Important/purple), not red.

### Interactive States (don't ship the "happy path" only)

For every list/table/card view, plan for — and actually implement — all of:

- **Loading:** the documented circular/linear spinner (`overlays-and-feedback.md`), not a generic
  browser spinner or a skeleton shape that doesn't match the final content's layout.
- **Empty state:** composed intentionally (icon/illustration + short copy + a primary action),
  never a bare "No data" string.
- **Error state:** inline for forms (per `forms-and-inputs.md`'s error state), a Critical-semantic
  banner/toast for system-level failures (`General.Semantic.Critical`, not a generic red).

## Pre-flight — two gates, and passing the first proves nothing about the second

**Brand fidelity and design quality are separate dimensions.** This file's gate checks the first.
A screen can use the exact palette, the real font files, the documented radii, the two real shadow
recipes, and a 64px header — and still be a flat, generic, badly-composed page. That result passes
Gate A completely. It is still a failure of this skill.

So there are two gates, and **both are mandatory**:

| | What it checks | Where |
| --- | --- | --- |
| **Gate A — Brand Compliance** | Tokens, assets, type, shape, shadow, sizing, no fabrication | Below |
| **Gate B — Design Quality** | Hierarchy, spacing rhythm, alignment, density, signature, craft, content, states — and whether the build was actually reviewed | [design-review.md](./design-review.md) |

Never report Gate A as "the checklist passed." Report them separately, and if Gate B has never
failed for you on a first attempt, you are not really running it.

### Gate A — Brand Compliance

Every box must be honestly checkable before the work is done — this is a gate, not a
retrospective. If a box fails, fix the work; don't ship it with a caveat in prose.

- [ ] Design Read stated (surface type, audience, dial values) before code was generated
- [ ] A composition archetype (hero/shell/tile rhythm) was consciously picked, not defaulted to
      the first/most obvious option
- [ ] Exactly one accent color (Electric Blue) used for interactive UI chrome; any other accent
      colors present are only in a chart/data-viz context, in the documented preferred order
- [ ] Buttons are pill-shaped at the correct tier height (32/40/48/56px); no other radius sneaks
      onto a button
- [ ] Cards/inputs/modals use their documented small radius (4px or 8px) — nothing squircle-shaped
- [ ] Headlines are Thin weight + `#170F5F`; body is 77% black; no system-font fallback visible
      (fonts actually self-hosted, not just named in CSS)
- [ ] Bold text uses the Demi font file, not `font-weight: bold` on Regular
- [ ] Any shadow used is one of the two documented recipes, not an ad hoc single-layer shadow, and
      is on something that actually lifts (popover/menu/modal/sheet) rather than a resting card
- [ ] In dark mode, elevation comes from the `elevated` surface tokens — the light-mode shadow
      recipes were not carried over
- [ ] Any animation uses a documented duration + productive easing curve, `transform`/`opacity`
      only, nothing linear or bouncy
- [ ] Header is 64px; nav fits on one line at desktop; hero fits the first viewport
- [ ] No wrapped button text; one CTA label per intent on the page
- [ ] Loading/empty/error states are designed, not just the happy path
- [ ] Light/dark mode each use their own exact documented tokens, not a derived/algorithmic guess
- [ ] Destructive/irreversible actions require confirmation; async submits disable their button
      and show a loading state (no double-submit)
- [ ] No layout shift from async content (badges/images/validation) popping in without reserved
      space; keyboard focus is never fully obscured by a sticky header/footer/widget
- [ ] `prefers-reduced-motion` is honored; any auto-rotating content (carousel, etc.) has visible
      pause/prev/next controls and stops on hover/focus/offscreen
- [ ] Badges vs chips markup matches their actual semantics (static vs interactive); no compact
      label was truncated if it was essential text (primary actions, errors, safety text)
- [ ] Nothing was invented — every color/size/font/shadow traces to a specific file in
      `references/`; if something genuinely isn't documented, it was flagged as a gap (per
      `brand-guidelines.md`'s no-fabrication rule), not guessed
- [ ] For anything not covered above, [ux-accessibility-checklist.md](./ux-accessibility-checklist.md)
      was checked before shipping

### Gate B — Design Quality

**Gate A above does not satisfy this.** Run
[design-review.md](./design-review.md)'s Gate B — hierarchy, spacing rhythm, alignment, density,
signature element, craft details, content, interaction states — and its build critique (render and
look at the result where the environment allows; otherwise run the stated non-visual fallback and
say which items couldn't be verified). Work isn't done until both gates pass.
