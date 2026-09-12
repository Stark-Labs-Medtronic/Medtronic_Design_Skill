# Layout, spacing & component size tiers

This complements [sizing-standard.md](./sizing-standard.md), which covers **brand asset**
proportions only (logo/Symbol/icon aspect ratios measured from the real SVG files). This file
covers the **general spacing/grid/breakpoint/touch-target/component-density system** every page
built with this skill should follow, so buttons, cards, and inputs stay visually consistent with
each other across an entire product — not just within one screen.

**Source of this content, stated plainly:** these are well-established external UI engineering
standards — Material Design's spacing/breakpoint system, WCAG 2.5.5 / Apple / Google touch-target
guidance, and Nathan Curtis's (EightShapes) component-sizing methodology — **not** Medtronic brand
rules. Where Medtronic's own guidelines already specify something that overlaps (e.g., "grid in
multiples of 4 units," pill-shaped buttons), that takes precedence — see
[brand-guidelines.md](./brand-guidelines.md#composition--layout). Don't attribute anything in this
file to "the Medtronic guidelines."

## 1. Spacing scale — 8px grid (4px sub-increments where needed)

All spacing (padding, margin, gap) should be a multiple of **8px**: 8, 16, 24, 32, 40, 48, 64…
For small/tight values, drop to **4px** sub-increments instead: 4, 12, 20, 28, 36 — typical for
icon padding, small badges, or tight inline gaps where 8px would feel too loose.

- Container padding: **24–40px**, so bordered cards/sections stay clearly distinguishable
  (matters most for low-vision users).
- This independently reinforces Medtronic's own composition rule already in
  `brand-guidelines.md`: "use the grid with a multiple of 4 units" — the 8px grid here is a
  (compatible) refinement of that for spacing specifically, not a contradiction of it.

```css
:root {
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 40px; --space-8: 48px;
}
```

**For an actual Medtronic app, use [composition.md](./composition.md)'s real spacing scale**
(`none/xxs/xs/s/m/l/xl` = 0/4/8/16/24/32/40px, mapped to `$spacing-*` Sass variables and
`.p-0`–`.p-6` utility classes) instead of the generic scale above wherever it applies — the table
here (which includes a 12px step and a 48px step with no Medtronic equivalent) remains a valid
generic fallback only where no official Medtronic spec covers the value.

> **`[MANDATORY]` Spacing tokens are never asset dimensions.** `--space-1: 4px` is the tightest
> *gap* in the system, not a size. Never apply any `--space-*` value as the width or height of a
> logo, lockup, Symbol, or icon — those come from `sizing-standard.md` §0. A logo height below 15px
> means a spacing token was read as a dimension.
>
> Note also that `--space-3` (12px) and `--space-8` (48px) have **no** Medtronic equivalent in
> `composition.md`'s official scale — prefer the official tiers where one applies.

## 2. Touch targets — minimum interactive size

| Tier | Size | Source |
| --- | --- | --- |
| Absolute floor | 40×40px | General accessibility best-practice minimum |
| Recommended default | 44×44px | Apple Human Interface Guidelines |
| Safest cross-platform choice | 48×48px | Google Material Design — practitioner consensus is this is the more consistent choice when a product spans iOS + Android + web |

Applies to buttons, icon buttons, tappable list items/rows, and nav links — not just literal
`<button>` elements. **`[MANDATORY]` Correction, logged in `SKILL.md`'s Contradiction Ledger:**
Medtronic's real default button (`sizing-standard.md` §8) is a **fixed 40px height** with
**horizontal-only** padding (`padding: 0 1.5rem` — there is no vertical padding value, since height
is set directly) — not the `12px 28px`/"~44–48px" figures this line previously (and wrongly)
attributed to that section. That real 40px sits at this table's **Absolute-floor** tier, not the
Recommended-default tier — it clears the general accessibility minimum but not Apple's 44px
recommendation. The `12px 28px` figure is this file's *own* generic non-Medtronic fallback tier
(§4 below), not the Medtronic spec — don't cite the two interchangeably.

**Medtronic's own Digital Design System spec** (see [accessibility.md](./accessibility.md)) is
more specific than the generic tiers above: **48×48px is a hard minimum** for essential
interactive elements (primary CTAs, required-field inputs), non-essential elements may be visually
smaller but need **32×32px** of unshared spacing between adjacent elements, and a small 24×24px
icon button is fine only with a 4px margin on all sides. Prefer that spec over the generic tiers
for anything built against this Design System.

## 3. Responsive breakpoints

Simplified 3-tier convention (matches common web practice and a simplified reading of Material
Design's system):

| Tier | Width |
| --- | --- |
| Mobile | < 600px |
| Tablet | 600–1024px |
| Desktop | ≥ 1024px |

For finer control, Material Design's full breakpoint system: `0 / 480 / 600 / 840 / 960 / 1280 /
1440 / 1600dp`, with a 4-column grid on the smallest tier scaling up to 12 columns at desktop
widths, and 16–24dp gutters. Use the simplified 3-tier version unless a layout genuinely needs the
finer stops.

**For an actual Medtronic app, use the real official breakpoints in
[composition.md](./composition.md) instead** (1440/1200/768/375px artboards with exact padding
and content-area widths, cross-validated against the bundled `mdt-app-template.css`) — the tiers
above remain a valid generic fallback only when no official Medtronic spec applies.

## 4. Component size tiers — consistent height per tier, not just font-size

Adopting Nathan Curtis's design-systems methodology: pick 2–3 discrete size tiers (not a
continuous scale — avoid XS/XL/XXL sprawl), and unify **height** — not just `font-size` — across
every component in a tier by combining font-size + line-height + padding + border consistently.
Two components both labeled "Default" should end up the same rendered height; if they don't,
that's drift to fix, not an acceptable variation.

| Tier | Font size | Vertical padding | Resulting height (approx) | Use for |
| --- | --- | --- | --- | --- |
| Compact | 13–14px | 8px | ~36–40px | Dense data tables, admin/analyst tools |
| **Default** | 15–16px | 12px | ~44–48px | Most app UI — this skill's default button/input |
| Spacious | 17–18px | 16px | ~56–64px | Marketing/landing pages, onboarding flows |

Apply this to buttons, inputs, selects, list items, and table cells. **Don't force every component
into every tier** — an alert/notification shouldn't get a "Compact" variant (it needs to stay
noticeable regardless of density), and a tag/badge doesn't need a "Spacious" variant (it's
inherently a small, subtle element). Decide per component whether a tier actually serves its
purpose rather than mechanically generating every combination.

```css
.btn--compact  { font-size: 14px; padding: 8px 20px; }
.btn--default  { font-size: 15px; padding: 12px 28px; } /* matches react-integration.md's default */
.btn--spacious { font-size: 17px; padding: 16px 36px; }
```

**For an actual Medtronic app, use the real official button spec in
[sizing-standard.md §8](./sizing-standard.md) instead** (Small 32px / Default 40px / Large 48px /
XL 56px, from the bundled `mdt-components.css`) — the tiers above remain a valid generic-UI
fallback for non-button components (inputs, list items, table cells) where no official Medtronic
spec exists.

## 5. Icon size follows its parent component's tier, not one fixed value everywhere

Match icon size to the tier of the button/component it sits inside (small button → small icon,
large button → a proportionally larger icon — not the same icon size crammed into every size of
button):

| Component tier | Icon size |
| --- | --- |
| Compact | 16px |
| Default | 20–24px |
| Spacious | 24–28px |

Cross-reference [sizing-standard.md §7](./sizing-standard.md) for the functional-vs-thematic icon
aspect-ratio rule (functional = fixed 24×24 grid, safe to force square; thematic = ratio varies
per icon, height-only sizing).

## 6. Don't use T-shirt sizing for single-dimension properties

Width-only variations (modal width, dialog width, sidebar width) shouldn't be named Small/Medium/
Large — a T-shirt scale doesn't extend cleanly once a new width is needed later (is 1000px "XL"
or "Extra-Medium"?). Name these by their actual value instead: `modal--width-480`,
`modal--width-720`, `sidebar--width-280`. Reserve Small/Medium/Large/Compact/Default/Spacious
naming for the component-height tiers in §4.

## 7. Apply this holistically across a page/product, not component-by-component

Unify sizing across a whole page or product in one pass rather than deciding it ad hoc per
component as you build each one — inconsistent per-component sizing is the most common way a UI
ends up feeling subtly "off" even when each individual piece looks fine in isolation. When editing
an existing app, audit every button/input/card currently on the page and bring them to one
consistent tier before adding anything new, rather than adding a new component at whatever size
looks right in isolation.
