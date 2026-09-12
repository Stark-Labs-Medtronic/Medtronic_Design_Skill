# Design review — critique the plan, then critique the build

**Source:** the *method* here is general design-engineering practice, synthesized from published
skill sets (`frontend-design`'s two-pass plan/critique loop, `better-ui`'s slowdown verification,
`frontend-ui-engineering`'s viewport matrix, `improve-ui`/`react-doctor`'s evidence-first,
leverage-ordered findings). The *criteria* it checks are Medtronic's own, from the reference files
cited inline. Third-party status, same precedence rule as
[carbon-design-system.md](./carbon-design-system.md): Medtronic's specs win wherever they overlap.

**What this file is not:** the read-only boundary those audit skills impose ("never modify source,
only write plans") does **not** apply here. This skill builds UI. Take the rigor, not the boundary.

## Why this file exists

The skill's pre-flight check has always run **once, at the end, from memory, in prose**. That is a
compliance audit, not a design process. Two consequences:

1. Nothing ever *looks at* the result. A model that has never seen its own output cannot tell that
   the hero is 40px too tall, that two cards are misaligned by 4px, or that the dark-mode card is
   invisible against its background.
2. Passing a checklist at the end can't change the design — by then the composition is fixed. The
   cheapest critique happens **before** the code exists.

So: critique the plan, build, then critique the build — and where the environment can render, look
at it.

## Pass 1 — critique the plan, before writing code

After the Design Read and archetype selection in [design-intuition.md](./design-intuition.md), and
before writing markup, state the plan compactly:

- **Design Read** — surface type, audience, VARIANCE/MOTION/DENSITY values
- **Archetypes chosen** — hero treatment, shell, tile rhythm
- **Signature** — the one memorable moment (see `design-intuition.md`), and what stays quiet to let it land
- **Hierarchy** — the type step budget and what occupies each rank ([visual-hierarchy.md](./visual-hierarchy.md))
- **Density** — the component tier and section rhythm
- **Theme** — which preset ([theme-presets.md](./theme-presets.md)) and therefore which asset variants

Then interrogate it with one question: **would this plan be materially different for a different
brief?** If swapping the subject matter wouldn't change the layout, the archetype was defaulted, not
chosen. Name what you're changing and why before proceeding.

Specific things to catch at this stage, because they are near-impossible to fix later:

- Every hero defaulting to Transparent Large Light; every dashboard defaulting to the same 3-column
  card grid; every tile the same 1:1 aspect ratio
- A section order that is the generic default rather than one of the named archetypes in
  [ux-accessibility-checklist.md](./ux-accessibility-checklist.md)
- A "signature" that is really just a bigger version of an ordinary element
- A type budget that has no rank for the most important thing on the screen

## Pass 2 — critique the build

### Visual path (use whenever the environment can render)

If a browser, preview, or screenshot capability is available, **use it — this is the highest-value
step in the whole skill.** Looking at the output finds in seconds what a checklist misses entirely.

1. **Render the page and take a screenshot.** Actually view it. Do not reason about what the CSS
   probably produces.
2. **Check the four viewports** — 320 / 768 / 1024 / 1440px. These map onto the official breakpoints
   in [composition.md](./composition.md) (mobile 375 / tablet 768 / laptop 1200 / desktop 1440), and
   320px is the narrow-edge stress test. Confirm at each: nav on one line or correctly collapsed, no
   wrapped button text, no horizontal overflow, hero fits the first viewport, tables scroll rather
   than blow out the layout.
3. **Squint at it / view it small.** Shrink the screenshot until text is illegible. What's left is
   pure hierarchy. If nothing dominates, the page has no focal point — a size or spacing problem, not
   a color one.
4. **Check both themes.** Render light and App Dark Mode. The dark pass specifically catches surfaces
   that vanish because a light-mode shadow was carried over instead of stepping to the `elevated`
   surface token ([craft-details.md §3a](./craft-details.md)).
5. **Review motion at 10% speed** in the browser's Animation panel. Problems invisible at full speed
   are obvious slowed down: a transition that restarts instead of retargeting, a stagger applied to a
   high-frequency control, a property animating that shouldn't be, easing that overshoots.
6. **Tab through the page.** Every interactive element reachable, focus ring visible everywhere
   (including inside modals and popovers), focus never hidden behind the 64px sticky header.
7. **Fix, re-render, re-look.** One round of this is worth more than any amount of re-reading code.

### Non-visual fallback (no rendering available)

When nothing can render — plain chat contexts with no browser or preview — do **not** silently claim
a visual pass. Instead:

1. **Trace the box model by hand** for one representative component and one full section: compute
   actual rendered heights from font-size + line-height + padding + border, and check they match the
   intended tier ([layout-and-spacing.md §4](./layout-and-spacing.md)). This catches the "two
   Default-tier components render at different heights" drift.
2. **Read the CSS for cancellation.** Type-based and element-based selectors that override each other
   (`.section` vs `.cta` padding/margin) are a common and invisible source of broken rhythm. Check
   specificity conflicts explicitly, especially on section spacing.
3. **List every spacing value used on the page** and confirm the set is small, on-scale, and encodes
   grouping rather than uniform ([visual-hierarchy.md §4](./visual-hierarchy.md)).
4. **List every text size used** and confirm it matches the step budget.
5. **State plainly which items could not be verified without rendering** — and say so in the summary
   rather than reporting a clean pass. An honest "hero fit and dark-mode contrast unverified, no
   render available" is worth more than a fabricated tick.

## Gate B — Design Quality

**Gate A (Brand Compliance) and Gate B are separate, and passing A says nothing about B.** A screen
can use every correct token, asset, radius, and font file — and still be a bad design. Gate A is in
[design-intuition.md](./design-intuition.md). This is Gate B.

Every box must be *honestly* checkable. A box that can never fail is decorative; if you find yourself
ticking all of these on the first attempt every time, you are not reviewing.

**Hierarchy**
- [ ] Squinted/small, one element clearly dominates — the page has a focal point
- [ ] Distinct text sizes are within the budget for this surface ([visual-hierarchy.md §1](./visual-hierarchy.md))
- [ ] Adjacent type ranks are a real step apart (~1.4×+); no two sizes serve the same rank
- [ ] The most important element on the screen occupies the top rank — not a label above it

**Space and rhythm**
- [ ] Spacing is *not* uniform: within-group gaps are 3–4× tighter than between-group gaps
- [ ] Every spacing value is on the documented scale; the set of distinct values is small
- [ ] Section rhythm is consistent down the page, not per-section improvisation

**Alignment and proportion**
- [ ] The page resolves to a small number of shared vertical edges, starting at container padding
- [ ] Text aligns with text across cards (not box-padding-to-box-padding)
- [ ] Numeric columns right-aligned with `tabular-nums`; reading copy capped at 65–75ch
- [ ] Tile/card aspect ratios vary deliberately where a grid exists — not N identical squares

**Density**
- [ ] Rendered density matches the DENSITY value in the stated Design Read
- [ ] One component tier governs the page; any exception is deliberate and stated
- [ ] Density was raised by tightening type and space, never by shrinking touch targets

**Idea**
- [ ] A signature element exists, is genuinely the one bold thing, and everything else is quiet
- [ ] Structural devices (eyebrows, numbering, dividers, rules) encode something true — no ornament
- [ ] The layout would be materially different for a different brief
- [ ] The shell and color combination came from Step 0.5 (or an already-specified brief), not a
      silent default — a blue/navy left sidebar beside white content, defaulted to rather than
      chosen, is exactly the generic-SaaS tell this pass exists to catch, even though its
      mechanical check lives in Gate A's pre-flight (`design-intuition.md`)

**Craft**
- [ ] [craft-details.md §10](./craft-details.md) self-check passes
- [ ] Dark mode reviewed on its own terms — elevation via surface tokens, not carried-over shadows

**Content**
- [ ] Real content at realistic lengths; no lorem ipsum, no filler
  ([content-and-copy.md](./content-and-copy.md))
- [ ] A deliberately long string was tested for wrapping/overflow

**States**
- [ ] Loading, empty, and error states are designed and implemented, not just the happy path
- [ ] Hover, focus, active, disabled, and selected states exist for every interactive element
- [ ] Zero / one / many / too-many data cases considered for every list, table, and chart

**Review actually happened**
- [ ] The build was rendered and looked at — or the non-visual fallback ran and its unverified items
      were stated explicitly

## Reporting findings

When reviewing an existing UI (audit-first mode in `design-intuition.md`, or a "make this better"
request), report findings **ordered by leverage — impact ÷ effort — not by rule severity**, and keep
the list short. Three well-evidenced findings beat twelve padded ones.

For each finding give: where it is, what's wrong, which documented rule or file it violates, and the
one specific correction. If the evidence supports more than one possible correction, it isn't a
finding yet — it's a question for the user.

Two honest outcomes that are always available: *"the existing structure is sound; these are the three
things worth changing"* and *"this cannot be verified without rendering."* Prefer either over
padding a list.

## Calibration — compliant vs. good

The point of Gate B in one example. Both versions below pass **every** box in Gate A: exact palette
values, real font files, a documented radius, a documented shadow recipe, a documented Carbon
duration and productive easing curve, no invented anything.

### Passes Gate A, fails Gate B

```css
.kpi-card {
  background: #FFFFFF;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 1px 8px rgba(0,0,0,.12), 0 3px 4px rgba(0,0,0,.14), 0 3px 3px rgba(0,0,0,.2);
  transition: all 240ms cubic-bezier(0.2, 0, 0.38, 0.9);
}
.kpi-title { font-family: "AvenirNextWorld-Bold"; font-size: 24px; color: #170F5F;            margin-bottom: 24px; }
.kpi-value { font-family: "AvenirNextWorld";      font-size: 24px; color: rgba(0,0,0,0.77);   margin-bottom: 24px; }
.kpi-delta { font-family: "AvenirNextWorld";      font-size: 16px; color: rgba(0,0,0,0.77); }
```

What's wrong, none of which Gate A can see:

| Problem | Rule |
| --- | --- |
| The number — the entire point of the card — is the same size as its own label. No rank. | [visual-hierarchy.md §1–2](./visual-hierarchy.md) |
| Uniform 24px gaps: label, value, and delta read as three unrelated items, not one object | [visual-hierarchy.md §4](./visual-hierarchy.md) |
| Shadow on a card that never lifts — elevation should be a background step | [craft-details.md §3](./craft-details.md) |
| No `tabular-nums`: the figure jitters every refresh | [craft-details.md §5](./craft-details.md) |
| `transition: all` animates layout properties on a hover | [craft-details.md §8](./craft-details.md) |
| The delta carries no semantic meaning — just body-colored text | [ui-design-system-colors.md](./ui-design-system-colors.md) |

### Passes both

```css
.kpi-card {
  background: #F5F5F5;                    /* General.Surface.level 1 — background step, no shadow */
  border-radius: 8px;
  padding: 24px;
  transition-property: background-color;  /* named, not `all` */
  transition-duration: 110ms;             /* duration-fast-02 */
  transition-timing-function: cubic-bezier(0.2, 0, 0.38, 0.9);
}
.kpi-label {                              /* rank 3 — category */
  font-family: "AvenirNextWorld-Demi";
  font-size: 12px; letter-spacing: 1.3px; text-transform: uppercase;
  color: #777777;
  margin-bottom: 4px;                     /* tight: same object */
}
.kpi-value {                              /* rank 1 — the number */
  font-family: "AvenirNextWorld-Bold";
  font-size: 44px; line-height: 52px;
  color: #170F5F;
  font-variant-numeric: tabular-nums;
  margin-bottom: 8px;
}
.kpi-delta {                              /* rank 2 — supporting, semantic */
  font-family: "AvenirNextWorld";
  font-size: 14px;
  color: #3F6E03;                         /* General.Semantic.Confirm; sign carries meaning too */
  font-variant-numeric: tabular-nums;
}
```

Same palette, same fonts, same radius, same scale — 12 / 44 / 14 instead of 24 / 24 / 16, and
4 / 8 / 24 instead of 24 / 24 / 24. Nothing was invented; the difference is entirely composition.
That difference is what Gate B exists to force.
