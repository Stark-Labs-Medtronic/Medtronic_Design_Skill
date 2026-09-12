# Using this skill in a React project

## 1. Copy design tokens into the project

Don't hand-roll colors — copy the exact values from
[color-tokens.md](../references/color-tokens.md) into whatever token system the project uses.

**Plain CSS variables** (`src/styles/tokens.css`):

Self-host the real typeface instead of relying on the system-font fallback — copy
`assets/fonts/avenir-next-world/*.ttf` into the project and declare it once. **In React, prefer the
single-family + `font-weight`-descriptor approach below** — it maps each weight to its real file, so
`font-weight: 700` resolves to `AvenirNextWorld-Bold.ttf` rather than being synthesised:

```css
@font-face { font-family: "Avenir Next World"; font-weight: 400; src: url("/fonts/AvenirNextWorld-Regular.ttf") format("truetype"); }
@font-face { font-family: "Avenir Next World"; font-weight: 600; src: url("/fonts/AvenirNextWorld-Demi.ttf") format("truetype"); }
@font-face { font-family: "Avenir Next World"; font-weight: 700; src: url("/fonts/AvenirNextWorld-Bold.ttf") format("truetype"); }
@font-face { font-family: "Avenir Next World"; font-style: italic; src: url("/fonts/AvenirNextWorld-Italic.ttf") format("truetype"); }
```

> **Reconciling this with [typography.md](./typography.md)'s "never use `font-weight`" rule.** There are two valid
> strategies, and the rule is about not mixing them:
>
> | Strategy | Weight expressed as | `font-weight` |
> | --- | --- | --- |
> | **Family-per-weight** — what `mdt-variables.css` does | a distinct family name (`AvenirNextWorld-Bold`) | must stay `normal` |
> | **Single family + descriptors** — recommended for React | `font-weight: 700` | correct and required |
>
> The prohibition in `typography.md` applies to the first strategy, where a numeric `font-weight`
> would synthesise a fake weight on top of an already-weighted file. With the `@font-face` block
> above, `font-weight: 700` is the correct way to reach Bold. **Pick one strategy per project.**

**Headings are Bold** (`font-weight: 700` under this strategy) — see the headline-weight resolution in
[typography.md](./typography.md), which also has the full type scale (exact sizes/weights for
headings, body, buttons, captions) to build matching React text components from.

```css
h1, h2, h3 {
  font-family: var(--mdt-font);
  font-weight: 700;              /* AvenirNextWorld-Bold */
  color: var(--mdt-navy-digital); /* #170F5F */
}
h1 { font-size: 2.75rem; line-height: 3.25rem; }
h2 { font-size: 2rem;    line-height: 2.5rem; }
h3 { font-size: 1.5rem;  line-height: 2rem; }
h4 { font-weight: 400; font-size: 1.25rem; line-height: 1.75rem; color: var(--mdt-navy-digital); }

@media (max-width: 480px) {
  h3 { font-weight: 400; line-height: 1.75rem; }          /* de-escalates to Regular */
  h4 { font-weight: 600; line-height: 1.5rem; color: var(--mdt-text); } /* Demi */
}
```

```css
:root {
  --mdt-electric-blue: #1010EB;
  --mdt-navy: #140F4B;
  --mdt-navy-digital: #170F5F; /* headline/text use on screen */
  --mdt-white: #FFFFFF;
  --mdt-atmospheric-white: #F5F5F5;

  /* Product UI text tokens - use THESE for app/dashboard body copy.
     Exact values from mdt-variables.css (--mdtText etc.). */
  --mdt-text: rgba(0, 0, 0, 0.77);          /* body copy - the 77% black rule */
  --mdt-text-high: rgba(0, 0, 0, 0.90);     /* emphasis */
  --mdt-text-low: rgba(0, 0, 0, 0.55);      /* secondary / eyebrow */
  --mdt-text-disabled: rgba(0, 0, 0, 0.30);

  /* Solid grays - marketing/print surfaces and anywhere an opaque fill is required
     (alpha text over a photo or gradient renders inconsistently). Not the default
     for product UI body copy. */
  --mdt-body-gray: #3C3C3C;
  --mdt-disclaimer-gray: #777777;

  --mdt-accent-light-blue: #0FC9F7;
  --mdt-accent-teal: #00DCB9;
  --mdt-accent-green: #7ECA2A;
  --mdt-accent-orange: #FFAD00;
  --mdt-accent-pink: #E5057F;
  --mdt-accent-purple: #C529BB;
  --mdt-accent-lavender: #654BDD;
  --mdt-accent-red: #ED002A;

  --mdt-gradient-blue: linear-gradient(90deg, var(--mdt-electric-blue), var(--mdt-navy));
  --mdt-gradient-teal: linear-gradient(90deg, var(--mdt-accent-light-blue), var(--mdt-accent-teal));

  --mdt-font: "Avenir Next World", "Avenir Next", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  --mdt-radius-pill: 999px;
}

/* App Dark Mode preset (product UI) — see references/theme-presets.md #3. Toggle with a
   `data-theme="dark"` attribute on <html> or a root wrapper. Official UI Design System tokens,
   not an approximation — see references/dark-mode-ui-colors.md for the full set. */
[data-theme="dark"] {
  --mdt-bg: #121212;
  --mdt-surface: #1E1E1E;
  --mdt-primary: #4A7DFF;
  --mdt-primary-hover: #285EFF;
  --mdt-primary-active: #86A9FF;
  --mdt-headline: #FFFFFF;
  --mdt-text: rgba(255, 255, 255, 0.9);
  --mdt-text-muted: rgba(255, 255, 255, 0.7);
  --mdt-border: rgba(255, 255, 255, 0.15);
}

/* Navy Dark preset (marketing/brand surfaces only — not general app dark mode) — see
   references/theme-presets.md #2. */
[data-theme="navy-dark"] {
  --mdt-bg: #140F4B;
  --mdt-surface: rgba(255, 255, 255, 0.06);
  --mdt-primary: #1010EB; /* exact Electric Blue token, unmodified - marketing-context gap still open, see theme-presets.md */
  --mdt-headline: #FFFFFF;
  --mdt-text: #FFFFFF;
  --mdt-text-muted: #F5F5F5;
  --mdt-border: rgba(255, 255, 255, 0.10);
}
```

**Tailwind** (`tailwind.config.js` — merge into `theme.extend`):

```js
colors: {
  'mdt-blue': '#1010EB',
  'mdt-navy': '#140F4B',
  'mdt-navy-digital': '#170F5F',
  'mdt-atmospheric': '#F5F5F5',
  'mdt-text': 'rgba(0,0,0,0.77)',   // product UI body copy - use this by default
  'mdt-text-low': 'rgba(0,0,0,0.55)',
  'mdt-body': '#3C3C3C',            // solid gray: marketing/print, or text over imagery
  'mdt-disclaimer': '#777777',
  'mdt-teal': '#00DCB9',
  'mdt-green': '#7ECA2A',
  'mdt-orange': '#FFAD00',
  'mdt-pink': '#E5057F',
  'mdt-purple': '#C529BB',
  'mdt-lavender': '#654BDD',
  'mdt-red': '#ED002A',
  'mdt-light-blue': '#0FC9F7',
},
fontFamily: {
  brand: ['"Avenir Next World"', '"Avenir Next"', '"Segoe UI"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
},
borderRadius: {
  pill: '999px',
},
```

## 2. Logo component

Always render the logo as an `<img>`/inline SVG pointed at the bundled asset — never recreate the
wordmark with text. Pick the color variant by the surface it sits on (never recolor via CSS
filters):

```tsx
// components/MedtronicLogo.tsx
import navyDigital from '../assets/brand/logos/wordmark/medtronic-logo-navy-digital.svg'; // #170F5F - use for app/website headers
import navy from '../assets/brand/logos/wordmark/medtronic-logo-navy.svg'; // #140F4B - print/marketing only, don't use in a UI header
import white from '../assets/brand/logos/wordmark/medtronic-logo-white.svg';

type Variant = 'navy-digital' | 'navy' | 'white';

// height default (28px) = the "compact header/nav" tier in sizing-standard.md; pass 60 for a hero.
// Only `height` is set — never add a `width` too, or you'll stretch the artwork off its real ratio.
export function MedtronicLogo({ variant = 'navy-digital', height = 28 }: { variant?: Variant; height?: number }) {
  const src = variant === 'white' ? white : variant === 'navy' ? navy : navyDigital;
  return <img src={src} alt="Medtronic" height={height} />;
}
```

Default to `navy-digital` (`#170F5F`) for any on-screen app/website header — the UI Design System
explicitly warns the standard Navy fill (`#140F4B`) reads as near-black on some screens. Only use
the plain `navy` variant for print/marketing contexts, per [app-header-logo-lockup.md](./app-header-logo-lockup.md).

Every logo/lockup/Symbol/icon has a real measured aspect ratio and a recommended size per context
in [sizing-standard.md](./sizing-standard.md) — check it before picking a height/width, especially
for the Symbol (it's taller than wide, not a square icon) and thematic icons (ratio varies per
icon, so they need height-only or width-only sizing, never both).

Copy the actual files from this skill's `assets/logos/` into the app's own asset folder (e.g.
`src/assets/brand/`) rather than importing across the skill directory, then use them per the
placement rules in [brand-guidelines.md](../references/brand-guidelines.md) (top-left preferred,
never centered/trapped mid-layout on a busy background).

If the app has a dark mode (Navy Dark preset), swap `variant` to `'white'` whenever
`data-theme="dark"` is active — don't leave the navy logo sitting on a dark background, and don't
recolor the navy SVG with a CSS filter to fake white.

Use the logo+tagline lockup (`assets/logos/tagline-lockup-horizontal/`, or
`tagline-lockup-vertical/` for narrow/mobile layouts) for hero/landing sections or page footers —
not for a compact app header/nav bar (use the plain wordmark there instead). Size it at 56–80px
height for a hero (per [sizing-standard.md](./sizing-standard.md)) — smaller than that and the tagline text stops being
comfortably readable.

For an actual `favicon.ico` / `apple-touch-icon`, use
[`assets/favicon/favicon.ico`](../assets/favicon/favicon.ico) — Medtronic's own live production
favicon (white "M" on Electric Blue). For social share images / social profile pictures
specifically, use `assets/logos/social-favicon-mark/` instead (the integrated Symbol+logo mark) —
these two now have distinct recommended uses, see `app-header-logo-lockup.md`.

## 3. Buttons — pill-shaped, brand colors, tiered sizing

**For an actual Medtronic app, use the real button spec in
[sizing-standard.md §8](./sizing-standard.md) instead** — `.btn`/`.btn-small`/`.btn-large`/`.btn-xl`,
fixed 40/32/48/56px heights with horizontal-only padding, from the bundled `mdt-components.css`.
The Compact/Default/Spacious tiers below are this skill's own generic fallback for non-Medtronic-
shaped custom buttons only — don't cite `--default`'s `12px 28px` padding as if it were the
Medtronic spec, and note it lands at ~44–48px, not the 40px the real `.btn` class uses (that real
default sits at the accessibility floor tier, not the recommended tier — see
[layout-and-spacing.md §2](./layout-and-spacing.md)):

```css
.btn-primary, .btn-outline {
  font-family: var(--mdt-font);
  border-radius: var(--mdt-radius-pill);
  border: 1.5px solid transparent;
  font-weight: 600;
}
.btn-primary {
  background: var(--mdt-electric-blue);
  color: var(--mdt-white);
}
.btn-outline {
  background: transparent;
  color: var(--mdt-electric-blue);
  border-color: var(--mdt-electric-blue);
}

/* size tiers - pick one, don't invent a fourth */
.btn--compact  { font-size: 14px; padding: 8px 20px; }
.btn--default  { font-size: 15px; padding: 12px 28px; } /* default */
.btn--spacious { font-size: 17px; padding: 16px 36px; }
```

## 4. Icons

**`[MANDATORY]` Carbon is the default icon system — use it by default, without being asked.** See
[carbon-design-system.md](./carbon-design-system.md) for the rationale and the manifest lookup
procedure. Copy from `assets/third-party/carbon-design-system/assets/icons/`; resolve names via
`catalog/icons-manifest.json` rather than guessing a filename.

Carbon SVGs are square on a **32×32 `viewBox`** and use **`fill="currentColor"`**, which means one
file serves light and dark mode — set `color`, not `fill`, and never maintain paired variants:

```tsx
// vite-plugin-svgr / SVGR: currentColor flows through from CSS
import Dashboard from "@/assets/icons/carbon/dashboard.svg?react";
import ArrowRight from "@/assets/icons/carbon/arrow--right.svg?react";

<Dashboard className="icon" />                       {/* inherits text color */}
<ArrowRight className="icon icon--action" />         {/* interactive only */}
```

```css
.icon           { width: 20px; height: 20px; color: var(--mdt-text); }
.icon--action   { color: var(--mdt-electric-blue); }  /* one accent per screen */
[data-theme="dark"] .icon { color: rgba(255, 255, 255, 0.9); }
```

| Context | Size |
| --- | --- |
| Inline with body text, dense table row | 16px |
| Default UI icon (buttons, nav, form affordances) | 20px |
| Standalone in a card, toolbar, icon button | 24px |
| Large feature / empty-state icon | 32px |

**Medtronic thematic icons `[FLEXIBLE]`** are still the better choice for brand/editorial moments
(marketing feature rows, value-prop blocks) — Carbon has no equivalent of the blue brand-illustrative
set. Those hardcode their fills, so pair the variant to the background (`thematic/` on light,
`thematic-white/` on dark or color), and note their **aspect ratios vary per icon** — set `height`
only, never both axes:

```css
.icon-thematic { height: 24px; width: auto; } /* required: ratio varies per icon */
```

Don't mix Carbon and Medtronic functional icons in the same UI region — a toolbar containing both
reads as two design systems collided. If you need an icon Carbon genuinely lacks, Health Icons (CC0)
is the other library the guidelines approve.

## 5. Building beyond tokens/logo/buttons/icons

For page shells, navigation, forms, and overlays, don't hand-invent a layout — check the matching
reference first and translate its measurements/rules into components:

- Page grid, breakpoints, UI shell choice → [composition.md](./composition.md)
- Header (64px rule), top/side nav, breadcrumbs, tabs, popovers, footer →
  [global-header.md](./global-header.md), [navigation.md](./navigation.md)
- Badges, segmented buttons, carousels, accordions, flags, hero banners, avatars →
  [ui-components.md](./ui-components.md)
- Text fields, selects, checkboxes/radios, toggles, date/number pickers, slider, search →
  [forms-and-inputs.md](./forms-and-inputs.md)
- Modals, side/bottom sheets, loading spinners, tooltips → [overlays-and-feedback.md](./overlays-and-feedback.md)
- General page-grid/spacing structure not covered by the above →
  [carbon-design-system.md](./carbon-design-system.md) (third-party supplementary reference —
  Medtronic's own specs above always take precedence)

## 6. Performance quick-reference (third-party, general React/Next.js practice)

Not brand-specific, but worth checking on any data-driven Medtronic app — condensed from the same
third-party source as [ux-accessibility-checklist.md](./ux-accessibility-checklist.md):

- Run independent async calls with `Promise.all()` instead of sequential `await`s; in API routes,
  start promises immediately and `await` them as late as possible instead of awaiting one at a
  time.
- Import icons/utilities directly from their source path (`lucide-react/dist/esm/icons/check`),
  not from a package's barrel/`index` export — barrel imports pull in every icon in the library.
- Lazy-load heavy, non-initial-render components (`next/dynamic`, `React.lazy`) instead of
  importing them at the top level; preload on hover/focus intent rather than waiting for the click.
- Wrap slow-loading sections in `<Suspense>` with a skeleton fallback instead of `await`-blocking
  the whole page on one slow data source.
- Across a React Server Components boundary, pass only the specific fields a client component
  actually uses, not the entire object — full-object props serialize everything to the client.

## 7. What NOT to do

- Don't generate a new "Medtronic-style" logo/wordmark with an LLM or font — always use the
  bundled artwork.
- Don't invent hex colors "close to" brand blue — use the exact tokens. If a needed value (like a
  dark-mode-specific shade) genuinely isn't in [color-tokens.md](./color-tokens.md) or [theme-presets.md](./theme-presets.md), say so and
  use the closest exact existing token rather than guessing a new one.
- Don't center the logo in a dense layout, recolor it, or place it on a low-contrast background.
- Don't use the Full-life Symbol as the only brand mark on a screen — pair it with the wordmark.
- Don't mix light-surface assets (navy logo, gray/blue icons) onto a dark surface, or vice versa —
  each theme preset in `theme-presets.md` specifies its own matching asset set.
