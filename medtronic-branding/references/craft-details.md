# Craft details — the micro-layer between "correct token" and "looks considered"

**Source:** third-party, general frontend craft knowledge, synthesized from published design-
engineering skill sets (`better-ui`, `baseline-ui`, `frontend-ui-engineering`) plus the mechanics
already visible in Medtronic's own bundled production CSS
([assets/code-templates/html-css-framework/css/](../assets/code-templates/html-css-framework/css/)).
**Not** Medtronic brand rules — don't attribute anything here to "the guidelines."

**Precedence rule (same as [carbon-design-system.md](./carbon-design-system.md) and
[ux-accessibility-checklist.md](./ux-accessibility-checklist.md)): Medtronic's own documented specs
always win where they overlap.** Where a rule below is *derived from* a Medtronic source, that
source is cited inline and the rule is binding rather than supplementary.

## Why this file exists

[design-intuition.md](./design-intuition.md) covers macro composition (which hero, which shell,
which tile rhythm). The token/spec files cover exact values (which hex, which pixel height). Neither
covers the layer in between: the sub-pixel decisions that separate a UI that is *technically correct*
from one that reads as *made by someone who cared*. A screen can use every right token and still look
amateur because the radii don't nest, the icon sits 1px off its label's baseline, the numbers in a
table jitter as they update, and the card shadow is invisible in dark mode.

**Read this before writing component CSS, not after.** These are cheap while you're writing the rule
and expensive to retrofit across a finished page.

## 1. Concentric radius — inner = outer − padding

When a rounded element sits inside another rounded container, the two curves are concentric only if
`outer = inner + padding`. Break that relationship and the gap between the curves visibly pinches at
the corners — the most common reason a nested element "feels off" with no obvious cause.

**In this system the relationship is solved in one direction only: inner = outer − padding.**
Medtronic fixes the container radii, and [design-intuition.md](./design-intuition.md)'s Shape
Consistency Lock is binding: 4px for inputs/flags/tooltips, 8px for modals/sheets, pill for buttons,
and **never 16px+ on a content container.** So you may never inflate a card to 20px or 28px to
satisfy the formula — that would trade a subtle corner artifact for an outright brand violation.
Derive inward instead:

```css
/* Modal at its documented 8px, 8px of padding → an inner surface reads correctly at 0 */
.modal       { border-radius: 8px; padding: 8px; }
.modal__body { border-radius: 0; }

/* Card at 8px with 24px padding → the inner element is well clear of the corner;
   its own documented radius governs and concentricity is irrelevant at that distance */
.card  { border-radius: 8px; padding: 24px; }
.input { border-radius: 4px; }
```

Three practical consequences:

- **When padding ≥ the outer radius, the corner relationship stops mattering** — the inner element is
  far enough from the curve that the eye never compares them. This is the common case at Medtronic's
  16–24px card padding, and it's why the fixed radii and the 8px spacing scale coexist comfortably.
- **The relationship only bites when padding is small** (≤8px) — a tightly-inset thumbnail, an inner
  surface in a modal, a nested panel. There, set the inner radius to `outer − padding`, flooring at 0.
- **Never inflate the outer radius to fix an inner one.** If the math wants a 20px card, the padding
  or the inner radius is wrong, not the card. The documented value wins.

For a pill-shaped button inside a container, don't compute anything: the pill is fully round, the
container keeps its documented radius, and the padding between them does the work.

## 2. Optical alignment beats geometric alignment

Geometric centring is what the box model does; optical centring is what the eye reads. When they
disagree, the eye wins — nudge it.

- **Icons in pill buttons.** A leading icon centred by `justify-content` usually reads as sitting too
  far right, because the pill's left curve eats visual space the icon doesn't. Add 1–2px of extra
  left padding.
- **Asymmetric glyphs.** Play triangles, chevrons, send arrows, and the Full-life Symbol have their
  visual mass off-centre from their bounding box. A play triangle centred in a round button always
  needs ~1–2px of leftward offset applied as a nudge on the glyph, never by resizing the button.
- **Icon-to-label baseline.** An icon beside text aligns to the text's *optical* centre (roughly the
  x-height midpoint), not the line-box centre. With Medtronic's `line-height: 30px` on a 16px body
  ([typography.md](./typography.md)), naive `align-items: center` leaves the icon reading slightly
  low — check it and nudge.
- **Text inside a circular avatar.** Initials in the 40×40px avatar
  ([ui-components.md](./ui-components.md)) sit optically high when centred geometrically, because
  most initials have no descender.

Where the 8px grid and optical alignment disagree, **optical alignment wins** — a 1px nudge for the
eye is not a grid violation, it's the reason the grid looks right.

## 3. Elevation: pick one mechanism per surface

Three ways to separate a surface from what's behind it. They are not interchangeable and they should
not be stacked:

| Mechanism | Means | Use for |
| --- | --- | --- |
| **Shadow** | "floating above the page" | Popovers, dropdowns, menus, modals, sheets — things temporarily on top |
| **Border** | "structurally distinct / stateful" | Dividers, table rules, input outlines, focus, selected state |
| **Background step** | "grouped, part of the page" | Cards, sections, panels that live in the layout permanently |

A resting card that carries a shadow *and* a border *and* a background step is the classic
over-specified surface — it reads as noise. Pick the one that matches what the surface actually is.
Most Medtronic dashboard cards are **background step** (`General.Surface.level 0` → `level 1`),
not shadowed — shadow is for things that *lift*, and a card that never lifts shouldn't cast.

When you do use shadow, it must be one of the three documented recipes in
[design-intuition.md](./design-intuition.md)'s Elevation Discipline. Never an ad hoc single-layer
`box-shadow`.

### 3a. Dark mode uses a different elevation mechanism — this is a real, documented rule

[dark-mode-ui-colors.md](./dark-mode-ui-colors.md) states it directly: *"Elevation in dark mode is
conveyed with progressively lighter grays, not drop shadows alone."* The token tables prove why —
compare the two modes' `elevated` surfaces:

| Level | Light mode | Light "elevated" | Dark mode | Dark "elevated" |
| --- | --- | --- | --- | --- |
| 0 | `#FFFFFF` | `#FFFFFF` (unchanged) | `#121212` | `#1E1E1E` (steps up) |
| 1 | `#F5F5F5` | `#F5F5F5` (unchanged) | `#1E1E1E` | `#2C2C2C` (steps up) |
| 2 | `#DCDCDC` | `#DCDCDC` (unchanged) | `#2C2C2C` | `#3C3C3C` (steps up) |

Light mode's elevated surfaces are **identical** to their resting surfaces — because light mode
expresses elevation with the shadow recipes. Dark mode's elevated surfaces **step one level lighter**
— because a black-based shadow is effectively invisible on `#121212`.

**So:** in App Dark Mode, raise a surface by moving it to its `elevated` token, optionally with
`General.Borders & Lines.light` (`rgba(255, 255, 255, 0.15)`) — **not** by applying the light-mode
shadow recipes. Porting a light-mode card's shadow into dark mode produces a surface that looks flat
and muddy while technically passing every brand check. This is exactly the class of failure Gate B
in `design-intuition.md` exists to catch.

## 4. Focus rings are a documented token, not a default

Both modes have an official focus color, and they differ:

| Mode | Token | Value |
| --- | --- | --- |
| Light | `General.Interface.Focus` | `#ED7008` ([ui-design-system-colors.md](./ui-design-system-colors.md)) |
| Dark | `General.Interface.Focus` | `#FFAD00` ([dark-mode-ui-colors.md](./dark-mode-ui-colors.md)) |

Medtronic's own production CSS
([mdt-components.css](../assets/code-templates/html-css-framework/css/mdt-components.css)) implements
the light-mode ring as:

```css
*:focus:not(:focus-visible) { outline: 2px solid transparent; }
*:focus-visible             { outline: 2px solid #ED7008; border-radius: 2px; }
```

Note the `:focus-visible` split — the ring shows for keyboard users, not on every mouse click. Use
this pattern rather than a browser default or a removed outline. It also satisfies the WCAG 2.2
Focus Appearance minimum already noted in
[ux-accessibility-checklist.md](./ux-accessibility-checklist.md) (~2 CSS px perimeter at 3:1).

Never remove `outline` without replacing it, and never use Electric Blue for the focus ring — the
system deliberately uses an orange so focus stays distinguishable from the primary action color.

## 5. Text rendering — three properties, large payoff

Absent from this skill until now, and disproportionately visible on the data-dense screens Medtronic
builds most:

```css
h1, h2, h3, .txt06-headline, .txt07-headline,
.txt08-headline, .txt09-display { text-wrap: balance; }

p, .txt02-body, .txt03-body, .txt04-body { text-wrap: pretty; }

.kpi-value, td, th, .metric, time { font-variant-numeric: tabular-nums; }
```

- **`text-wrap: balance` on headings** evens the line lengths instead of leaving one orphaned word.
  Medtronic headlines are Bold weight at 32–72px, where a single trailing word is very visible.
- **`text-wrap: pretty` on body** prevents single-word last lines in paragraphs.
- **`tabular-nums` on anything numeric** fixes column jitter — in proportional figures a `1` is
  narrower than a `0`, so live-updating KPIs and table columns visibly shimmy. This is close to
  mandatory on a clinical dashboard, where a number that twitches on refresh undermines trust in the
  reading itself.

Do **not** touch `letter-spacing` to "improve" type — the real scale already specifies it where it
matters (1.3px on `.txt01-eyebrow`, 1.5px on `.txt02-eyebrow`, 0.6px on `.txt03-button`, per
[typography.md](./typography.md)). Those values are the spec, not a starting point.

## 6. Icons

- **Carbon icons are `fill="currentColor"` by construction** — no hardcoded-fill problem, no
  `-white` folder to swap. Set `color`, not `fill`, and the same file works on light or dark
  backgrounds; see [carbon-design-system.md](./carbon-design-system.md) for sizing/lookup. This is
  the default icon system for this skill (local override, see `SKILL.md`).
- **Stroke weight tracks adjacent text weight.** An icon beside Regular-weight body copy wants a
  ~1.5px stroke; beside Demi (buttons, eyebrows, bold) it wants ~2px. A hairline icon next to bold
  text reads as a rendering bug.
- **Size follows the parent component's tier**, per
  [layout-and-spacing.md §5](./layout-and-spacing.md) — 16px compact / 20–24px default / 24–28px
  spacious. Not one fixed size crammed into every button size.
- **Medtronic thematic icons are the opt-in case** (brand/editorial moments) and are the one place
  the old hardcoded-fill caveat still applies: [react-integration.md](./react-integration.md) warns
  most bundled Medtronic SVGs hardcode a hex fill — check the file, and if it hardcodes, swap to
  the correct color-variant folder (`thematic-white` on dark/colored backgrounds) rather than
  fighting it with CSS filters. Don't mix Carbon and Medtronic icons in the same UI region.
- **Fill vs outline as state.** Where a set offers both, outline is the resting state and fill is the
  active/selected one. Don't encode that state with color alone
  ([ux-accessibility-checklist.md](./ux-accessibility-checklist.md)).

## 7. Images and media

- Give every image a **1px achromatic outline at ~10% opacity** — `rgba(0, 0, 0, 0.1)` on light
  (this is the documented `General.Borders & Lines.inverse light` token) and
  `rgba(255, 255, 255, 0.1)` on dark. It keeps a photo with a near-white or near-black edge from
  bleeding into the surface. Use pure black/white at low alpha, never a tinted outline — a tinted
  edge reads as dirt on the image.
- Reserve space with `aspect-ratio` so a loading image doesn't shove the layout
  ([ux-accessibility-checklist.md](./ux-accessibility-checklist.md) layout-shift rule).

## 8. Motion mechanics

Durations and easing curves are already specified in
[design-intuition.md](./design-intuition.md)'s Motion section (Carbon's tokens:
70/110/150/240/400/700ms, productive easing by default, never linear, never bouncy/spring/overshoot).
**Those values stand — nothing here replaces them.** This section is about the *mechanics* of
applying them.

- **CSS transitions for interactive state; keyframes only for one-time sequences.** A transition can
  be interrupted mid-flight and retargets from where it is; a keyframe animation restarts or fights
  the new state. Anything driven by hover/focus/active/checked belongs in a transition.
- **Name the properties.** `transition-property: transform, opacity` — never `transition: all`,
  which quietly animates properties you didn't intend (and often can't afford). Note that
  `transition: transform` covers `transform`, `translate`, `scale`, and `rotate`.
- **Animate only `transform` and `opacity`.** Never `width`/`height`/`top`/`left`/`margin`/`padding`
  — they force layout every frame. Avoid animating large `blur()`/`backdrop-filter` surfaces at all.
- **`will-change` only on `transform`/`opacity`/`filter`, and only while an animation is actually
  running.** Add it in response to observed first-frame stutter, remove it after; a permanent
  `will-change` holds GPU memory for nothing. Never `will-change: all`.
- **Press feedback: `transform: scale(0.96)` on `:active`.** Nothing below 0.95 — deeper reads as a
  toy. Pair it with the 70ms `duration-fast-01` token.
- **Stagger staged entrances by ~100ms per semantic chunk** — and only for infrequent, one-time
  reveals (a page or panel opening). Never stagger a high-frequency interaction; a dropdown the user
  opens fifty times a day should appear as one unit.
- **Suppress transitions during a theme switch.** Toggling light/dark fires color, background, border
  and shadow transitions simultaneously across the whole page, which smears. Inject
  `*, *::before, *::after { transition: none !important; }`, force a reflow, then remove it on the
  next frame.
- **Never gate real state on an animation-end event** — set the state, let the motion be cosmetic on
  top (already in [ux-accessibility-checklist.md](./ux-accessibility-checklist.md)).

Under `prefers-reduced-motion`, skip non-essential motion entirely and render the final state
immediately — don't merely shorten the duration.

## 9. Viewport and stacking mechanics

- **`dvh`, not `vh`**, for any full-height layout. `100vh` is wrong while mobile browser chrome is
  showing (also in `ux-accessibility-checklist.md`; repeated here because it belongs with the other
  mechanics).
- **Respect `safe-area-inset-*`** on anything fixed — bottom bars, sticky CTAs, the mobile nav drawer
  — or it lands under the home indicator / notch.
- **One fixed z-index scale**, e.g. 10 nav / 20 dropdown / 30 modal / 40 toast. Never an ad hoc
  `z-index: 9999`. The 64px fixed header ([global-header.md](./global-header.md)) is the base layer
  everything else stacks against, and it's also what `scroll-padding-top` must offset so keyboard
  focus never lands behind it.
- **Square sizing from one property.** For genuinely square elements (Carbon icons — real 32×32
  `viewBox`) set a single size rather than a `width` + `height` pair that can drift apart. This does
  **not** override [sizing-standard.md](./sizing-standard.md)'s rule for brand artwork: non-square
  logos, lockups, the Symbol, and Medtronic's own functional and thematic icons (most of which are
  not actually square despite the 24×24 grid they're documented against) still get exactly one axis
  set, never both.

## 10. Quick self-check

Run this while writing CSS, not at the end:

- [ ] Tightly-inset nested elements derive their radius inward (inner = outer − padding); no
      container was inflated past its documented 4px/8px to satisfy the math
- [ ] Icons/glyphs beside text are optically aligned, not just `align-items: center`
- [ ] Each surface uses exactly one elevation mechanism (shadow OR border OR background step)
- [ ] Dark-mode elevation uses the `elevated` surface tokens, not the light-mode shadow recipes
- [ ] `:focus-visible` ring present, 2px, `#ED7008` light / `#FFAD00` dark — never removed, never blue
- [ ] `text-wrap: balance` on headings, `pretty` on body, `tabular-nums` on every number
- [ ] `letter-spacing` untouched except where the real type scale specifies it
- [ ] Icon stroke weight matches the weight of the text beside it
- [ ] Images carry a 1px achromatic 10% outline and a reserved `aspect-ratio`
- [ ] Transitions name their properties; nothing uses `transition: all`
- [ ] Only `transform`/`opacity` animate; `will-change` is scoped and temporary
- [ ] `scale(0.96)` press feedback on interactive controls
- [ ] Theme switch suppresses transitions for one frame
- [ ] `dvh` not `vh`; `safe-area-inset` respected; z-index comes from the scale
