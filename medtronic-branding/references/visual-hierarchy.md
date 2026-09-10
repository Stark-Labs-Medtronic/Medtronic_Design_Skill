# Visual hierarchy — composing the type scale and the spacing scale

**Source:** the *values* here are all Medtronic's own, from
[typography.md](./typography.md) (the real `mdt-variables.css` type scale),
[composition.md](./composition.md) (the official 8px scale and breakpoints), and
[layout-and-spacing.md](./layout-and-spacing.md) (component size tiers). The *composition method* —
how many steps to use, how far apart, how spacing encodes grouping — is general typographic and
design-systems practice, **not** a Medtronic brand rule. Nothing here introduces a size, weight,
color, or spacing value that isn't already documented elsewhere in this skill.

## Why this file exists

The skill documents a rich type scale (four headings plus twenty named `txt01`–`txt09` styles) and a
precise spacing scale — and then says nothing about how to *use* them together. That gap produces
the two most common failure modes of brand-compliant-but-mediocre output:

- **Flat pages**, where everything is `h2` and `.txt03-body` with uniform 24px padding. Every token is
  legal; nothing has rank; the eye has nowhere to land.
- **Noisy pages**, where eight of the twenty text styles appear on one screen because each felt right
  in isolation. Every token is legal; nothing has rank *because everything claims it*.

Hierarchy is not a token you apply. It is the *relationships between* tokens — and relationships are
what nothing in this skill described until now.

## 1. Budget your type steps

Decide the number of distinct text sizes on a screen **before** writing markup, and hold the line.
Sizes are a budget; every additional step spends hierarchy rather than adding it.

| Surface | Distinct size steps | Typical composition |
| --- | --- | --- |
| Product dashboard / clinical tool | **3–4** | one page title, one section/card title, body, caption |
| Marketing / landing page | **5–6** | display, section headline, subhead, body, eyebrow, caption |
| Mobile app screen | **3–4** | screen title, row title, body, caption |
| A single card or panel in isolation | **2–3** | title, body, optional caption/metric label |

A dashboard reaching for six sizes is almost always compensating for weak *spacing* and *weight*
hierarchy with size. Fix the spacing first — you'll usually find you needed one fewer size.

Note that the type scale itself already encodes surface intent:
`.txt08-headline` (56px) and `.txt09-display` (72px) are display sizes and have essentially no place
on a dense product dashboard; `h1` (44px) is normally the largest thing on an app page.

## 2. Make each step a real step

This is about **which sizes you select for one screen**, not a criticism of the scale. The documented
scale — 12 / 14 / 16 / 20 / 24 / 32 / 44 / 56 / 72 — is deliberately fine-grained so that different
surfaces can each find their own set. Your job is to pick a subset whose members are clearly distinct
from one another.

- **Ranks you use together should be ~1.4× apart or more.** 16 → 24 (1.5×) reads as a step;
  20 → 24 (1.2×) reads as a wobble. So a screen that needs three ranks is usually better served by
  44 → 20 → 14 than by 44 → 32 → 24.
- **Adjacent scale entries are usually not adjacent *ranks*.** `h1` (44) and `h2` (32) are 1.375×
  apart — that's a deliberate, well-judged relationship for a document with many heading levels, and
  it's exactly right when both are genuinely present in a long content page. It is *not* the right
  pair for "page title plus card title" on a dashboard, where the two are doing very different jobs
  and want a visible category break. Pick for the job, not by walking down the scale.
- **Don't use two sizes for the same rank.** If cards on a dashboard use `.txt04-headline` (20px) for
  their titles, every card title on that page is 20px — not 20px in one column and 24px in another
  because one column had more room.

Where you need a distinction *without* a new size, reach for weight or color first — both are free
and both are already documented:

| Mechanism | Documented options |
| --- | --- |
| Weight | Bold (headlines) · Regular (body) · Demi (bold, buttons, eyebrows) — separate font files, never `font-weight` ([typography.md](./typography.md)) |
| Color | `#170F5F` headline navy · `rgba(0,0,0,0.77)` body · `--mdtTextLow` reduced/secondary |
| Case + tracking | `.txt01-eyebrow` / `.txt02-eyebrow`: uppercase Demi with 1.3px / 1.5px tracking |

A 16px Demi label in reduced-color above a 16px Regular body value is a clear two-rank relationship
at one size. That is usually the right answer for a key-value pair
([ui-components.md](./ui-components.md)), not a new size.

## 3. The eyebrow → headline → body triad

The scale ships a ready-made three-part unit that most Medtronic sections should use and that
generic output almost never reaches for:

```
.txt01-eyebrow / .txt02-eyebrow   →  uppercase Demi, tracked, reduced color   (category)
h2 / .txt06-headline_bold         →  Bold, #170F5F                            (the claim)
.txt03-body                       →  Regular, 77% black                       (the detail)
```

Three ranks, three different mechanisms (case+tracking, size+weight, plain body) — which is why it
reads as composed rather than merely large-then-small. Spacing inside the triad should be tight
(4–8px eyebrow→headline, 8–16px headline→body) so it reads as *one object*; see §4.

Don't repeat the eyebrow's words in the headline, and don't use an eyebrow as decoration on a section
that has no category to name — that's the "structural device as ornament" failure.

## 4. Spacing encodes grouping — this is the highest-leverage rule here

The 8px scale ([composition.md](./composition.md): 4 / 8 / 16 / 24 / 32 / 40) tells you which values
are legal. It does not tell you which to pick, and picking uniformly is the mistake.

**Related elements must be markedly closer than unrelated ones — aim for a 3–4× ratio.** If the gap
inside a group and the gap between groups are both 24px, there are no groups, only a list.

```
eyebrow                 ← 4px  (xxs)  tight: same object
HEADLINE                ← 8px  (xs)
body copy               ← 32px (l)    loose: next object begins
NEXT HEADLINE
```

Concretely, for a typical page:

| Relationship | Scale token | Value |
| --- | --- | --- |
| Label → its own value (key-value pair, form label → field) | `$spacing-xxs`/`xs` | 4–8px |
| Items within one group (list rows, form fields in a fieldset) | `$spacing-s` | 16px |
| Card internal padding | `$spacing-s`/`m` | 16–24px |
| Between sibling cards in a grid | `$spacing-m` | 24px |
| Between distinct page sections | `$spacing-l`/`xl` and above | 32–40px+ |

For section rhythm larger than the official 40px `xl`, the documented options are the responsive
container padding in [composition.md](./composition.md) (64 / 48 / 32 / 16px per breakpoint) and
Carbon's fixed-size unit scale (8/16/24/32/48/64/80px), already adopted as supplementary in
[carbon-design-system.md](./carbon-design-system.md) and cited by
[design-intuition.md](./design-intuition.md)'s tile-rhythm section. **Don't invent a 96px or 120px
section gap** — step through the documented values.

### Two spacing anti-patterns to name explicitly

- **Uniform padding everywhere.** Applying 24px to every gap on the page obeys the grid perfectly and
  destroys hierarchy. It is one of the loudest generic-output tells, and it passes every existing
  brand check.
- **Oversized padding as a substitute for composition.** Very large uniform whitespace reads as
  "airy" on a marketing page and as "empty and unfinished" on a dashboard. Density is set by the
  Design Read (see §6), not by defaulting to generous.

## 5. Alignment: fewer edges, shared down the page

- **Establish a small number of vertical edges and align everything to them.** A page where the
  header logo, the section headlines, the card grid, and the footer all begin on the same left edge
  reads as engineered. Introducing a fourth or fifth arbitrary indent is what makes a layout feel
  loose even when every element is individually fine.
- **The container padding *is* the page edge** — 64px desktop / 48px laptop / 32px tablet / 16px
  mobile, giving content areas of 1312 / 1104 / 704 / 343px
  ([composition.md](./composition.md)). Content starts there; nothing hangs outside it except a
  deliberate full-bleed hero.
- **Align to optical edges, not just boxes.** A card with a leading icon and a card without one
  should have their *text* aligned, not their box padding — otherwise the text in one card sits 24px
  further right than the other and the column looks broken.
- **Right-align numeric columns** in tables (with `tabular-nums`, per
  [craft-details.md](./craft-details.md)) so digits of different magnitudes stack; left-align text
  columns. A center-aligned data column is almost always wrong.
- **Cap the measure at 65–75 characters** for reading copy
  ([ux-accessibility-checklist.md](./ux-accessibility-checklist.md)) — the 1312px desktop content
  area is far too wide for full-width body text.

## 6. Density calibration — turning the DENSITY dial into numbers

[design-intuition.md](./design-intuition.md) assigns a DENSITY value per surface. Translate it into
the documented tiers rather than eyeballing:

| DENSITY | Component tier ([layout-and-spacing.md §4](./layout-and-spacing.md)) | Button size ([sizing-standard.md §8](./sizing-standard.md)) | Row/list height | Section rhythm |
| --- | --- | --- | --- | --- |
| 3 (marketing) | Spacious (~56–64px) | Large 48px / XL 56px | n/a | 40px+ |
| 4–5 (mobile app, light dashboard) | Default (~44–48px) | Default 40px | 44–48px | 32–40px |
| 5–6 (product dashboard) | Default, Compact in data areas | Default 40px / Small 32px | 40–44px | 24–32px |
| 6–8 (clinical / data tables) | Compact (~36–40px) | Small 32px | 32–40px | 16–24px |

**One tier per page, with a deliberate exception.** A dashboard that is Compact in its data table and
Default everywhere else is a considered decision; a dashboard where each component landed on whatever
tier looked right in isolation is drift. `layout-and-spacing.md §7` already makes this point — this
table is how to act on it.

Note that raising density does **not** mean shrinking touch targets:
[accessibility.md](./accessibility.md)'s 48×48px essential-element minimum and the 32×32px unshared
spacing rule for non-essential elements hold at every density. Increase density by tightening
*spacing and type*, not by making controls too small to hit.

## 7. Self-check

- [ ] The number of distinct text sizes on this screen matches the budget in §1
- [ ] Adjacent type ranks are ~1.4× apart or more; no two sizes serve the same rank
- [ ] Where a distinction didn't need a new size, weight/color/case was used instead
- [ ] Gaps within a group are 3–4× tighter than gaps between groups — spacing is *not* uniform
- [ ] Every spacing value is on the documented scale (4/8/16/24/32/40, then container padding /
      Carbon units above that); nothing invented
- [ ] The page resolves to a small set of shared vertical edges, starting at the container padding
- [ ] Numeric columns are right-aligned with `tabular-nums`; reading copy is capped at 65–75ch
- [ ] One component density tier governs the page, with any exception being deliberate and stated
- [ ] Touch targets still meet 48×48px essential / 32×32px unshared spacing at the chosen density
