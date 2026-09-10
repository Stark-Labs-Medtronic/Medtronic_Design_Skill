# UX & accessibility hygiene checklist (third-party, supplementary)

**Source:** Synthesized from two downloaded design-skill collections (`ui-ux-pro-max-skill`,
MIT-licensed design-intelligence dataset; `taste-skill` collection) — third-party, general web/app
UX and accessibility knowledge, **not** Medtronic-specific. Covers interaction/motion/layout/forms
hygiene, current WCAG 2.2 specifics, chart-type selection, and landing-page section-order
archetypes. Bundled here because it's genuinely high-value and largely orthogonal to brand
identity: these are fit-and-finish/accessibility/structure rules that apply regardless of which
company's colors are on screen.

**Precedence rule (same as `carbon-design-system.md`): Medtronic's own documented specs always
win where they overlap.** Notably: Medtronic's own [accessibility.md](./accessibility.md) already
specifies **48×48px for essential interactive elements** and **32×32px minimum spacing for
non-essential ones** — that is stricter than (and takes precedence over) the general WCAG 24×24px
floor cited below, which applies to the *general web minimum with exceptions*, not to Medtronic's
essential-element rule specifically.

## Motion hygiene (tool-agnostic — complements `design-intuition.md`'s Motion section)

- **Always honor `prefers-reduced-motion`.** When it matches, skip non-essential motion entirely
  and render the final state immediately — don't just slow the animation down.
- Hover feedback should read as *feedback*, not motion: keep displacement under ~2-4px and/or a
  subtle opacity/scale change — animate only `transform`/`opacity`, never layout-affecting
  properties (`width`/`height`/`top`/`left`/`margin`).
- Cap decorative/loading-loop animations at ~1.2–1.5s per cycle; longer reads as the UI being
  stuck, not "loading."
- Auto-rotating content (carousels, notifications) must have visible previous/next and play/pause
  controls, and must **pause on hover, keyboard focus, when scrolled offscreen, and when the
  browser tab is hidden** — never a timer-only auto-advance with no stop control.
- Clean up every animation/timer/observer on unmount — a `repeat: -1`/`setInterval` loop that
  isn't explicitly killed leaks across route changes in an SPA.
- Don't rely on an animation-end event for state correctness that matters (e.g. "the item is now
  selected") — set the real state directly and let the animation be purely cosmetic on top of it;
  rapid input should cancel/replace an in-flight transition rather than queue behind it.

## Layout & responsive hygiene

- **Content layout shift ("jumping"):** reserve space for async content (images, badges,
  validation text, skeleton-to-content swaps) with `aspect-ratio` or a stable-sized container —
  don't let a badge or async label insertion push nearby controls around.
- **Z-index:** define a small numeric scale (e.g. 10/20/30/50 for nav/dropdown/modal/toast) —
  never reach for an arbitrary `z-[9999]`.
- Use `dvh` (dynamic viewport height) instead of `vh` for full-height mobile layouts — `100vh` is
  unreliable with mobile browser chrome (address bar) showing/hiding.
- Limit text-content width to ~65–75 characters per line for readability — don't let body copy
  span the full viewport on wide screens.
- Long unbroken tokens (URLs, IDs, user-generated content) must not force horizontal overflow —
  use `overflow-wrap: anywhere` on the specific token, not a blanket `word-break: break-all` on
  all prose (that breaks normal words too).
- Tables should get a horizontal-scroll wrapper or convert to a card layout on narrow viewports —
  never let a wide table blow out the page layout.

## Touch and pointer targets

| Context | Minimum | Source |
| --- | --- | --- |
| Medtronic essential interactive elements | **48×48px** | `accessibility.md` (wins over the below) |
| Medtronic non-essential elements | May be smaller, but **32×32px** unshared spacing | `accessibility.md` |
| Native iOS | 44pt | Apple HIG |
| Native Android | 48dp | Material Design |
| General web (WCAG 2.2 §2.5.8) | 24×24 CSS px, with documented exceptions (inline text links, essential-appearance controls, controls whose spacing already provides an equivalent 24px target) | WCAG 2.2 AA |

Don't collapse these three different platform numbers into one universal constant when building
cross-platform (React Native etc.) — select per-platform at runtime instead.

- Minimum 8px gap between adjacent touch targets, even when each target individually meets its
  minimum size.
- Hover-only interactions don't work on touch devices — any interaction that matters must also
  work on tap/click, not rely on `:hover`/`onMouseEnter` alone.

## Interaction feedback

- Every interactive control needs a **visible keyboard focus indicator** — including controls
  *inside* a modal/popover. Never remove `outline` without a replacement.
- Disabled buttons must prevent double-submission during async actions (disable + show a loading
  state) — never leave a submit button clickable while the request is in flight.
- Show a clear, near-the-problem error message for failures — never a silent failure with no
  visible feedback.
- **Confirm before any destructive/irreversible action** (delete, discard, etc.) — never wire a
  destructive action directly to a single click with no confirmation step.
- Toasts/transient success messages auto-dismiss after ~3–5 seconds; persistent-until-dismissed
  toasts are a UX bug, not a feature.

## Forms

- Every input needs a real, visible `<label>` — placeholder text is never a substitute for a
  label (this matches Medtronic's own `forms-and-inputs.md` static/dynamic label rule).
- Field-level errors go directly below their field and are programmatically associated with it
  (`aria-describedby`) — a top-level error summary alone, with no per-field indication, fails
  accessibility.
- For a **multi-field validation failure**, also place a focusable error summary at the top of the
  form, move focus to it after a failed submit, and link each summary item to its invalid field —
  this is a current WCAG 2.2 item (§3.3.7-adjacent guidance), not yet common practice.
- Never require the same information twice in one flow (WCAG 2.2 §3.3.7 "Redundant Entry") — reuse
  previously entered/confirmed values (e.g. shipping address) instead of asking again.
- Never block password managers, paste, or autofill on auth fields (WCAG 2.2 §3.3.8 "Accessible
  Authentication") — `onpaste preventDefault` on a password field is a hard accessibility failure.

## WCAG 2.2 specifics worth knowing (current as of the 2023 update — genuinely new, not common knowledge)

- **Focus Not Obscured:** a sticky header/footer/chat-widget must not fully cover the element that
  currently has keyboard focus. Offset scroll position for sticky UI (`scroll-padding-top`) rather
  than letting focus land behind a fixed element.
- **Dragging Movements:** any drag-to-reorder/resize/select interaction needs a non-drag
  alternative (e.g. explicit "Move up"/"Move down" buttons) that still works via keyboard —
  drag-only interaction fails this criterion.
- **Consistent Help:** if a help/contact mechanism appears on multiple pages, it must stay in the
  same relative location across all of them.
- **Focus Appearance:** a focus indicator needs a real minimum visible area/contrast (roughly a 2
  CSS px perimeter at 3:1 contrast against the adjacent color) — a faint 1px outline technically
  present but hard to see doesn't satisfy this.

## Compact labels — badges, chips, and pills (directly relevant to `ui-components.md`)

- **Badges communicate state; chips/tags represent values or actions** — pick static (`<span>`)
  vs interactive (`<button>`) markup based on which one a given label actually is. Don't make every
  pill clickable "just in case," and don't encode status by color alone (pair color with an icon
  or text, matching the semantic-color + text rule already in `ui-design-system-colors.md`).
- A compact label should stay on one line where practical; if truncation is unavoidable, expose
  the full value to keyboard/pointer/touch users (not a hover-only tooltip, which touch users
  can't reach) — never let a fixed-width badge silently wrap to a second line.
- **Never truncate essential text** (primary action labels, error/safety text, distinguishing
  names) purely to keep a card's height uniform — wrap, resize the container, or provide a visible
  "see full detail" path instead.
- Async badge/count updates (e.g. a cart count) should announce one meaningful status message
  (`role="status"`, e.g. "3 items in cart"), not a bare changing number in a separate live region.

## AI interaction (directly relevant to an agentic/agent-bar UI)

- **Disclose that content/interaction is AI-generated** — never present an AI agent as a human
  with no indication otherwise.
- Prefer streaming a response token-by-token over a long blocking spinner — for anything likely to
  take more than a couple seconds, showing partial output beats a frozen "thinking" state.
- Provide a feedback mechanism (thumbs up/down, "regenerate") rather than read-only output with no
  way to signal a bad response.

## Mobile app specifics (React Native / native — supplements `design-intuition.md`'s Mobile app row)

- Icon-only buttons need an accessible name (`accessibilityLabel`/equivalent) — this is the same
  rule as the web `aria-label` requirement, just under a different API name per platform.
- Bottom tab bars: **3–5 primary items max** — move anything beyond that into a "More"/Settings
  destination rather than cramming a 6th+ tab icon in.
- Modals/sheets need an unambiguous close action (button, and swipe-down where the platform
  expects it) — never trap the user with no visible way out.
- Returning to a previously visited screen should restore its scroll position and form state, not
  reset it — don't unmount/remount a screen's state on every tab switch by default.

## Sustainability (lower priority, still real)

- Prefer click-to-play over autoplaying high-resolution video loops; always provide pause and
  captions, and stop offscreen video rather than letting it run unseen.
- Compress/lazy-load heavy media (3D assets, large images) rather than shipping raw, oversized
  source files to production.

## Chart type selection (data visualization)

Which chart shape fits a given data question — **use Medtronic's own accent colors/order from
`ui-design-system-colors.md` for the actual fill colors**, never the example hex values a
generic source might suggest. This table is about *shape selection and accessibility*, not color.

| Data question | Best chart | Avoid when | Accessibility must-have |
| --- | --- | --- | --- |
| Trend over time | Line / area chart | Fewer than 4 points (use a stat card instead); more than ~6 series (visual noise) | Distinguish series by line style (solid/dashed/dotted) + direct labels, never hue alone |
| Compare discrete categories | Bar chart (sort descending) | More than 15 categories (use a table instead) | Direct value labels; never encode category by color alone |
| Part-to-whole | Pie/donut (≤5 slices) or 100% stacked bar (>5) | Slice differences under ~5% (use a table — differences won't be visually readable) | Label every slice with its %; provide a table fallback |
| Correlation between 2 variables | Scatter/bubble plot | Fewer than ~20 points (a pattern isn't meaningful yet) | Combine marker shape with group labels, not color alone |
| Intensity across a 2D grid | Heat map | Fewer than 20 cells (use a bar chart instead) | Print values/symbols in cells in addition to the color scale |
| Sequential funnel/conversion | Funnel or Sankey | Stages aren't sequential, or fewer than 3 stages | Keep stage names/values visible; show conversion % between stages |
| Single KPI vs a target | Gauge or bullet chart | No defined target exists; comparing 3+ KPIs at once (use a bullet-chart grid instead) | Place the number and target as text beside the chart, not color-zone-only |
| Cumulative additive changes | Waterfall chart | Changes aren't additive; more than ~12 bars (aggregate the rest into "Other") | Pair increase/decrease bars with signed values and directional icons, not red/green alone |
| Multi-attribute comparison (2-3 entities) | Radar/spider chart | More than ~8 axes (unreadable); precise comparison needed (use grouped bar instead) | Use distinct line styles/point shapes + direct labels, not color alone |
| Distribution/spread across groups | Box plot | Fewer than ~20 points per group | Label median/quartiles/whiskers/outliers directly |
| Live/streaming monitoring | Streaming area/line chart | Update frequency under ~1/min (use a periodic-refresh line chart instead) | Show the current value as text; provide a pause control; never flash without a `prefers-reduced-motion` fallback |

General rule across every chart type above: **color is never the only carrier of meaning** — pair
it with direct labels, line/marker style, or icons, and always provide a visible data table as the
accessible source of truth alongside the visualization.

## Landing-page section-order archetypes (marketing surfaces)

Named, common section-order patterns for a marketing/landing page — pick deliberately per
`design-intuition.md`'s composition-archetype discipline, using **Medtronic's own colors/type**
for the actual styling (the color/effect specifics from the source dataset are stripped out below
on purpose — only the structural pattern and accessibility notes are kept):

| Pattern | Section order | Primary CTA placement | Accessibility note |
| --- | --- | --- | --- |
| Hero + Features + CTA | Hero → value prop → 3–5 key features → CTA → footer | Hero (sticky) + bottom | Verify CTA label contrast at 4.5:1 minimum against its fill; disable any hero parallax under `prefers-reduced-motion` |
| Hero + Testimonials + CTA | Hero → problem → solution → testimonial carousel → CTA | Hero (sticky) + post-testimonials | Testimonial carousel needs visible prev/next + pause, stops on focus/hover/reduced-motion |
| Product Demo + Features | Hero → product video/mockup → feature breakdown → optional comparison → CTA | Video-adjacent + CTA | Captions, transcript, visible play/pause, non-video fallback; don't autoplay under reduced motion |
| Minimal Single Column | Hero headline → short description → ≤3 benefit bullets → CTA → footer | Centered, single large CTA | Single CTA focus, no nav clutter — matches Medtronic's own "one CTA per intent" rule already in `design-intuition.md` |
| Funnel (3-step conversion) | Hero → step 1 (problem) → step 2 (solution) → step 3 (action) | Mini-CTA per step + final main CTA | Progress indicators required; each step shows only essential info |
| Comparison table + CTA | Hero → problem intro → comparison table → optional pricing → CTA | Below the table | Table needs a sortable/accessible fallback, not just visual row highlighting |
| Lead magnet + form | Hero (benefit headline) → lead-magnet preview → minimal-field form → CTA submit | Form submit button | Ask only for information necessary to deliver the lead magnet; show submission progress |
| Pricing page + CTA | Hero → pricing cards → feature comparison table → FAQ → final CTA | Per-card CTA + sticky nav CTA | Show real annual savings transparently, not just a bigger discount-looking number |
| Video-first hero | Video-background hero → key features overlay → benefits → CTA | Overlay center/bottom + bottom section | Overlay must guarantee text contrast; captions + visible pause control; static poster + preserved CTA under reduced motion |
