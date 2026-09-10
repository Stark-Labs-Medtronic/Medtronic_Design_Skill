# Using this skill in a React project

## 1. Copy design tokens into the project

Don't hand-roll colors — copy the exact values from
[color-tokens.md](../references/color-tokens.md) into whatever token system the project uses.

**Plain CSS variables** (`src/styles/tokens.css`):

Self-host the real typeface instead of relying on the system-font fallback — copy
`assets/fonts/avenir-next-world/*.ttf` into the project and declare it once:

```css
@font-face { font-family: "Avenir Next World"; src: url("/fonts/AvenirNextWorld-Regular.ttf") format("truetype"); }
@font-face { font-family: "Avenir Next World"; font-weight: 600; src: url("/fonts/AvenirNextWorld-Demi.ttf") format("truetype"); }
@font-face { font-family: "Avenir Next World"; font-style: italic; src: url("/fonts/AvenirNextWorld-Italic.ttf") format("truetype"); }
```

See [typography.md](./typography.md) for the full official type scale (exact sizes/weights for
headings, body, buttons, captions) to build matching React text components from.

```css
:root {
  --mdt-electric-blue: #1010EB;
  --mdt-navy: #140F4B;
  --mdt-navy-digital: #170F5F; /* headline/text use on screen */
  --mdt-white: #FFFFFF;
  --mdt-atmospheric-white: #F5F5F5;
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
  'mdt-body': '#3C3C3C',
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
the plain `navy` variant for print/marketing contexts, per `app-header-logo-lockup.md`.

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
height for a hero (per `sizing-standard.md`) — smaller than that and the tagline text stops being
comfortably readable.

For an actual `favicon.ico` / `apple-touch-icon`, use
[`assets/favicon/favicon.ico`](../assets/favicon/favicon.ico) — Medtronic's own live production
favicon (white "M" on Electric Blue). For social share images / social profile pictures
specifically, use `assets/logos/social-favicon-mark/` instead (the integrated Symbol+logo mark) —
these two now have distinct recommended uses, see `app-header-logo-lockup.md`.

## 3. Buttons — pill-shaped, brand colors, tiered sizing

Use the Compact/Default/Spacious tiers from
[layout-and-spacing.md §4](./layout-and-spacing.md) rather than inventing a size per screen —
`--default` matches this skill's other examples and lands at the ~44–48px touch-target minimum:

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

Import SVGs directly from `assets/icons/functional/` (gray) / `assets/icons/thematic/` (blue) on
**light** backgrounds, or `assets/icons/functional-white/` / `assets/icons/thematic-white/` on
**dark or color** backgrounds (Navy Dark preset, a colored banner, the electric-blue-to-blue
gradient) — the guidelines require white icons on any color/dark background, so swap the whole
folder rather than trying to recolor the gray/blue SVGs with CSS. They're single-color SVGs —
recolor via a wrapper `currentColor` swap only if the SVG's fill uses `currentColor` (check the
file first; if it hardcodes a hex fill, don't fight it — use the closest color/background variant

Sizing (see `sizing-standard.md` for the measured data behind this): functional icons are on a
real, fixed 24×24 grid — safe to set `width` and `height` equally. Thematic icons do **not**
share one fixed ratio between icons — set only `height` (`width: auto`) or you'll stretch some
icons more than others.

```css
.icon-functional { width: 24px; height: 24px; }
.icon-thematic { height: 24px; width: auto; }
```

that already exists, or the Carbon Design System / Health Icons libraries per the guidelines if
you need a color/style these files don't have).

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
third-party source as `ux-accessibility-checklist.md`:

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
  dark-mode-specific shade) genuinely isn't in `color-tokens.md` or `theme-presets.md`, say so and
  use the closest exact existing token rather than guessing a new one.
- Don't center the logo in a dense layout, recolor it, or place it on a low-contrast background.
- Don't use the Full-life Symbol as the only brand mark on a screen — pair it with the wordmark.
- Don't mix light-surface assets (navy logo, gray/blue icons) onto a dark surface, or vice versa —
  each theme preset in `theme-presets.md` specifies its own matching asset set.
