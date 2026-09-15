# Sizing standard — logo, symbol, lockups, icons, buttons

A concrete, numeric sizing spec so every **brand asset** in this skill is used at a **consistent,
legible, correctly-proportioned** size across a design/dev team, instead of everyone picking an
arbitrary height/width per screen. For the general spacing grid, breakpoints, touch-target
minimums, and component size tiers (buttons, inputs, cards) that apply beyond just brand assets,
see [layout-and-spacing.md](./layout-and-spacing.md) — this file only covers the logo/Symbol/
lockup/icon files themselves.

**Two different kinds of numbers appear in this file — don't confuse them:**

1. **Aspect ratios** — measured directly from each asset's own SVG `viewBox`. These are facts,
   not estimates. Always preserve them (set only width **or** height in CSS and let the browser
   compute the other axis via `width: auto` / `height: auto`) — never force both dimensions on a
   non-square asset, that stretches/distorts official artwork, which the guidelines explicitly
   prohibit ("do not recreate, modify, or otherwise alter the artwork").
2. **Recommended pixel tiers per context** (header, hero, footer, etc.) — these are an engineering
   sizing standard for this skill, informed by the real aspect ratios above plus common UI
   conventions (WCAG/platform touch-target minimums, typical header heights) and validated by
   rendering the actual assets in a real browser at these sizes (see the temp test app note at the
   bottom). They are **not** a rule copied from Medtronic's brand guidelines — the guidelines
   don't specify exact pixel sizes (see the "Content gaps" note in [brand-guidelines.md](./brand-guidelines.md)). Treat
   these as this skill's own recommended defaults, adjustable per layout, not brand law.

**Pick the context tier by visual isolation, not just DOM location.** A logo sitting alone in a
mostly-empty header/title area — no crowding nav items, no adjacent content competing for
attention — reads as undersized at the Compact tier even though it's technically "in the header."
Treat that as a Hero/standalone placement instead. Real example: a "Medtronic Sites" header with
just the wordmark and a large empty white area below it looked thin/lost at a ~24px Compact
height; bumping to 60px (Hero tier) is the right call there, not staying at Compact just because
the element happens to sit at the top of the page.

## 0. Logo Sizing Decision Table `[MANDATORY]` — read this before writing any logo markup

Context in, exact pixel value out. **No lookup, no interpolation, no arithmetic.** If your context
is in this table, use the value and stop reading.

| Context | Value | CSS |
| --- | --- | --- |
| Header / nav bar, logo shares the row with nav items | **28px height** | `height: 28px; width: auto;` |
| Header / title area, logo is visually alone (empty space around it) | **60px height** | `height: 60px; width: auto;` |
| Hero / standalone / "celebrate the identity" moment | **60px height** | `height: 60px; width: auto;` |
| Splash screen / large-format | **96–120px height** | `height: 96px; width: auto;` |
| Footer, horizontal tagline lockup | **28–32px height** | `height: 28px; width: auto;` |
| Hero, horizontal tagline lockup (tagline must be readable) | **56–80px height** | `height: 64px; width: auto;` |
| Sidebar / mobile / square tile, vertical stacked lockup | **64–80px height** | `height: 72px; width: auto;` |
| Standalone Full-life Symbol, footer / end-of-flow | **80–120px height** | `height: 96px; width: auto;` |
| Mobile stacked logo-above-app-name lockup **only** | **15px height** | `height: 15px; width: auto;` |
| Favicon / app icon | platform sizes — see §6 | — |
| Streamlit `st.logo()` | fixed ~32px internally, not settable | use `st.image` for other tiers |

**Set exactly one axis. Always `width: auto` (or `height: auto`) on the other.** Setting both on a
non-square asset stretches official artwork, which the guidelines explicitly prohibit.

### Guard: a brand asset dimension is never a spacing token `[MANDATORY]`

**The minimum logo height in this entire skill is 15px, and that is one specific documented mobile
lockup — not a general small size.** There is no context in which a Medtronic logo is 4px, 8px, or
12px tall.

If you are about to write a logo height below 15px, you have picked up a **spacing** value by
mistake. The usual culprits, all of which are gaps and padding, never asset dimensions:

- [composition.md](./composition.md)'s `xxs | 4px | $spacing-xxs` — the first row of the spacing table
- [layout-and-spacing.md](./layout-and-spacing.md)'s `--space-1: 4px` — the first CSS custom property in that file
- Carbon's `$spacing-02 | 0.25rem | 4px`
- [accessibility.md](./accessibility.md)'s "4px margin on all sides" — a *margin* on small icons, not a size
- The "4px sub-grid" note for icons and type — a *grid*, not a dimension
- The leading digit of an aspect ratio (`4.289 : 1`) — a ratio, not pixels

Stop, return to the decision table above, and take the value for your actual context.

## 1. Wordmark (plain logo, no tagline)

Real aspect ratio (measured): **2.741 : 1** (width ÷ height) — e.g. `medtronic-logo-navy.svg`.

| Context | Height | Resulting width | Notes |
| --- | --- | --- | --- |
| Compact header / nav bar | 24–32px | ~66–88px | Default: **28px** height. Matches typical product header logo scale. Only use this tier when the logo shares the row with nav items/other content — not when it's the lone element in an otherwise empty header. |
| Hero / standalone / print-style placement | 48–64px | ~132–175px | Default: **60px** height. For a "celebrate our identity" hero moment per the guidelines. |
| Large-format (splash screen, print collateral) | 96–120px | ~263–329px | |

> **Exception, not a contradiction:** Medtronic's own UI Design System specifies the logo at
> exactly **15px tall** for one *specific* documented pattern — a mobile stacked logo+app-name
> lockup (logo above the app name). That's a precise spec for that one pattern, not a general
> "mobile" tier — don't apply 15px outside that exact context, and don't round it into the
> Compact range above. See [app-header-logo-lockup.md](./app-header-logo-lockup.md).
>
> **`[MANDATORY]` The on-screen header asset has a different, wider ratio than the plain wordmark
> above — don't use the 2.741:1 figure to size it.** `medtronic-logo-navy.svg` (2.741:1, the ratio
> the table above is built from) is the print/Brand-Central wordmark. For app/website headers,
> [app-header-logo-lockup.md](./app-header-logo-lockup.md) and `brand-guidelines.md` both mandate
> `medtronic-logo-navy-digital.svg` instead — and that file's real, measured aspect ratio is
> **6.091 : 1** (viewBox `438.5736084 × 72.0010681`), more than double the plain wordmark's ratio.
> Using 2.741:1 to compute a header logo's width silently produces an asset less than half as wide
> as it should be. Logged in [SKILL.md](../SKILL.md)'s Contradiction Ledger.
>
> | Context | Height | Resulting width (`-digital`, 6.091:1) |
> | --- | --- | --- |
> | Compact header / nav bar | 28px | ~171px |
> | Hero / standalone | 60px | ~365px |

```css
.logo--header { height: 28px; width: auto; } /* medtronic-logo-navy-digital.svg on-screen */
.logo--hero   { height: 60px; width: auto; }
```

## 2. Logo + tagline lockup — horizontal

Real aspect ratio: **4.289 : 1**. The tagline text is small relative to the logo mark inside this
artwork — verified by rendering it at 40px height, where "engineering the extraordinary" was
legible but felt undersized for a hero moment (see testing note at the bottom).

| Context | Height | Resulting width | Notes |
| --- | --- | --- | --- |
| Compact header/footer (tagline is decorative, not meant to be read closely) | 28–32px | ~120–137px | |
| **Hero (tagline should be comfortably readable)** | **56–80px** | **~240–343px** | Don't go below 56px if the tagline needs to be read, not just recognized. |

## 3. Logo + tagline lockup — vertical (stacked)

Real aspect ratio: **2.401 : 1**.

| Context | Height | Resulting width | Notes |
| --- | --- | --- | --- |
| Sidebar / mobile / square tile | 64–80px | ~154–192px | |

## 4. Full-life Symbol (standalone)

Real aspect ratio: **0.863 : 1** (taller than wide — it's a standing/rising figure, not a square
icon). Verified by rendering it in a footer at 56px height, where it looked visually lost in the
surrounding space; 96px read as an intentional focal element instead.

| Context | Height | Resulting width | Notes |
| --- | --- | --- | --- |
| Small, paired inline with the wordmark in a lockup | 24–32px | ~21–28px | Use the pre-built combo assets (below) instead of hand-pairing these two at this size where possible. |
| **Standalone footer / end-of-flow moment** | **80–120px** | **~69–104px** | **Don't use less than 80px** for a standalone Symbol — below that it reads as an accidental leftover graphic rather than a deliberate brand moment. |
| Hero / promotional centerpiece | 140–200px | ~121–173px | |

## 5. Pre-built combo lockups

| Asset | Real ratio | Recommended height | Resulting width |
| --- | --- | --- | --- |
| Logo + Symbol combo (horizontal) | 3.4 : 1 | 40–56px | ~136–190px |
| Logo + tagline + Symbol combo (horizontal) | 3.271 : 1 | 56–80px | ~183–262px |

## 6. Social/favicon integrated mark

Real aspect ratio: **1.076 : 1** — close to square but not exact. Favicon/app-icon pixel sizes
themselves are **platform requirements, not a Medtronic brand rule** — cite them as such:

| Use | Required size | Note |
| --- | --- | --- |
| `favicon.ico` (multi-res) | 16×16, 32×32, 48×48 | Browser/OS standard |
| `apple-touch-icon` | 180×180 | iOS standard |
| PWA manifest icons | 192×192, 512×512 | Android/PWA standard |

Because the asset's real ratio (1.076) isn't exactly square, exporting it to any of the sizes
above means a ~7% crop or letterbox — pick a crop that keeps the Symbol's rising-figure silhouette
centered, don't stretch it to force an exact square.

## 7. Icons

**`[MANDATORY]` Functional icons are documented as a 24×24 grid, but the shipped SVGs don't match
that spec — don't hardcode both dimensions.** The guidelines' own text says "Draw icons on a
24×24-unit frame," but measuring all 286 files in `assets/icons/functional/` directly: only **2**
are exactly 24×24. The dominant real size is **28×28** (119 icons, ~42%), and **156 of 286 (55%)**
are non-square (e.g. `10.07×29`, `24.08×21.59`, `25×16`, `30×29`). Setting both `width` and
`height` per the old guidance stretches or squashes the majority of the set. Logged in `SKILL.md`'s
Contradiction Ledger.

**Both functional and thematic icons need height-only sizing.** Thematic icons do NOT share one
fixed ratio either — verified by inspecting multiple files (e.g. one sampled icon measured
`24 × 16.25`, ratio 1.477, not square). **Never hardcode both width and height for either icon
set** — set only one dimension (height is usually more useful for aligning icons in a row of mixed
content) and let width auto-compute per icon, or icons will stretch by a different, inconsistent
amount. (Carbon icons are the one icon set in this skill that's genuinely square — see
[carbon-design-system.md](./carbon-design-system.md) §Sizing — don't apply this height-only rule to those.)

| Context | Size (functional, height only) | Size (thematic, height only) |
| --- | --- | --- |
| Inline with body text / list item | 16–20px height | 16–20px height |
| Standalone in a card or button | 24–28px height | 24–28px height |
| Large feature icon | 32–48px height | 32–48px height |

```css
.icon--functional { height: 24px; width: auto; } /* ratio varies per icon - see note above */
.icon--thematic   { height: 24px; width: auto; }  /* required: ratio varies per icon */
```

## 8. Buttons (now a real Medtronic spec, not just an engineering recommendation)

Pill-shaped (full circular end radius = the button's own height). Medtronic's actual official
button CSS — bundled at
[assets/code-templates/html-css-framework/css/mdt-components.css](../assets/code-templates/html-css-framework/css/mdt-components.css)
— defines **4 exact tiers**, which supersede the generic engineering-derived tiers previously here:

| Tier | Height | Font size | Horizontal padding | Class |
| --- | --- | --- | --- | --- |
| Small | 32px | 14px | 16px (`1rem`) | `.btn-small` |
| **Default** | 40px | 16px, 0.6px letter-spacing | 24px (`1.5rem`) | `.btn` |
| Large | 48px | 16px | 32px (`2rem`) | `.btn-large` |
| XL | 56px | 20px | 40px (`2.5rem`) | `.btn-xl` |

```css
.btn { font-family: "AvenirNextWorld"; font-size: 1rem; letter-spacing: 0.6px; padding: 0 1.5rem; height: 40px; border: 1px solid var(--mdtColorAction); border-radius: 40px; }
```

Default-tier buttons are full-width below 480px viewport width, `width: fit-content` above it
(mobile buttons should stretch to the container, desktop buttons should hug their label). Variants:
`.btn-primary` (filled, Action color bg), `.btn-secondary` (transparent, Action-color text/border),
`.btn-ghost` (transparent, no border until hover). Focus ring: `2px solid #ed7008` (Focus token),
`2px` border-radius, applied via `:focus-visible` only (not plain `:focus`, to avoid a ring on
mouse clicks). See [typography.md](./typography.md) for the exact `.txt02-button`/`.txt03-button`
label text styles used inside these.

## Validating changes to this file

Whenever a size tier here changes, re-render it in a real browser rather than trusting the math
alone — a temporary Vite+React test app was used to validate every tier above (logo header size,
hero tagline lockup legibility, footer Symbol prominence, dark-mode contrast). The app itself is
not part of this skill (deleted after validation) — recreate a similar throwaway app if you need
to re-validate a future change, don't just eyeball computed widths.
