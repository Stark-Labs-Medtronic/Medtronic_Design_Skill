# Theme presets — Light, Dark, and Gradient Hero

Ready-to-use combinations of the exact tokens in [color-tokens.md](./color-tokens.md), the rules
in [brand-guidelines.md](./brand-guidelines.md), and the real asset files in [`../assets/`](../assets/).
Use one of these as a starting point instead of re-deriving a palette/asset selection from scratch
every time — pick the preset that matches the surface (normal app UI → Signature Light or Navy
Dark; landing/marketing hero → Gradient Hero), then layer in the specific screen's content.

Every hex value below traces back to `color-tokens.md`. Where the source guidelines describe a
rule but the exact value only exists in an uncaptioned diagram (not extractable as text — see the
"Content gaps" note in `brand-guidelines.md`), that gap is called out explicitly and **no
substitute value is invented** — the preset falls back to an exact, already-documented token
instead of guessing a new one.

## 1. Signature Light (default — most app/dashboard UI)

The standard "lead with blue and white" look the guidelines describe as the default.

| Role | Token | Value |
| --- | --- | --- |
| Page background | White | `#FFFFFF` |
| Card / section background | Atmospheric White | `#F5F5F5` |
| Primary / CTA / links | Electric Blue | `#1010EB` |
| Headline text | Navy (digital) | `#170F5F` |
| Body text | Body Dark Gray | `#3C3C3C` |
| Secondary / disclaimer text | Disclaimer Gray | `#777777` |
| Divider / border | Navy at low opacity | `rgba(20, 15, 75, 0.12)` *(structural opacity of the Navy token, not a new hue)* |

**Assets to use:** logo = `assets/logos/wordmark/medtronic-logo-navy.svg` · symbol (if used) =
`assets/symbol/symbol-full-color.svg` · icons = `assets/icons/functional/` (gray) for generic UI,
`assets/icons/thematic/` (blue) for Medtronic/health concepts.

```css
:root {
  --bg: #FFFFFF;
  --surface: #F5F5F5;
  --primary: #1010EB;
  --headline: #170F5F;
  --text: #3C3C3C;
  --text-muted: #777777;
  --border: rgba(20, 15, 75, 0.12);
}
```

Buttons: pill-shaped, `--primary` fill + white text for the primary action; `--primary` 1.5px
outline + transparent fill for secondary actions (see [react-integration.md](./react-integration.md) /
[streamlit-integration.md](./streamlit-integration.md) for framework-specific button CSS).

## 2. Navy Dark (brand/marketing contexts)

The guidelines explicitly sanction Navy (and Electric Blue) as dark, simple backgrounds for
**marketing/brand surfaces** — a hero section, an end-title moment, a promotional page. For
product/app UI dark mode, use **App Dark Mode** (section 3 below) instead — they're two separate,
both-valid conventions for two different contexts, not interchangeable.

| Role | Token | Value |
| --- | --- | --- |
| Page background | Navy | `#140F4B` |
| Card / elevated surface | Navy + white overlay | `rgba(255, 255, 255, 0.06)` over `#140F4B` *(same Navy token, an opacity overlay on top of it — not a new color)* |
| Primary / CTA / links | Electric Blue | `#1010EB` — the exact, documented brand blue, unchanged |
| Headline / primary text | White | `#FFFFFF` |
| Secondary text | Atmospheric White | `#F5F5F5` |
| Border | White at low opacity | `rgba(255, 255, 255, 0.10)` |

**A gap that's now resolved for product UI, still open for marketing:** the guidelines say *"For
dark mode, we use less saturated Electric Blue to improve legibility and reduce visual
vibration"* but never gave an exact hex for this Navy/marketing context. The product UI Design
System (section 3 below) *does* have an official dark-mode-safe blue (`#4A7DFF`) — but that's a
different token set scoped to app UI, not confirmed as the intended marketing-context color. For
a marketing/hero surface specifically, keep using the exact, unmodified Electric Blue `#1010EB`
until Global Brand confirms whether `#4A7DFF` (or something else) is the intended value there too
— don't assume the two contexts share one answer without confirming.

**Assets to use:** logo = `assets/logos/wordmark/medtronic-logo-white.svg` · symbol =
`assets/symbol/symbol-full-color-reverse.svg` (preferred on Navy/Electric Blue per the guidelines'
"suitable for electric blue, navy blue and other dark, simple backgrounds" rule) or
`assets/symbol/symbol-white.svg` for busier/small contexts · icons =
`assets/icons/functional-white/` and `assets/icons/thematic-white/` — **use the white icon
folders here, not the default gray/blue ones**, per the icon color rule ("set icons in white when
they appear on a color background").

```css
[data-theme="navy-dark"] {
  --bg: #140F4B;
  --surface: rgba(255, 255, 255, 0.06);
  --primary: #1010EB; /* exact token, unmodified - see note above on the marketing-vs-product-UI gap */
  --headline: #FFFFFF;
  --text: #FFFFFF;
  --text-muted: #F5F5F5;
  --border: rgba(255, 255, 255, 0.10);
}
```

## 3. App Dark Mode (product UI — official tokens)

Use this for a React/Streamlit/app dark-mode toggle — a real dark theme for interactive product
UI, as opposed to Navy Dark's marketing/brand-surface use case above. Every value below is an
official token from Medtronic's UI Design System (not derived/approximated) — full table in
[dark-mode-ui-colors.md](./dark-mode-ui-colors.md).

| Role | Token | Value |
| --- | --- | --- |
| Page background | `General.Surface.level 0` | `#121212` |
| Card / elevated surface | `General.Surface.level 1` | `#1E1E1E` |
| Primary / CTA / links | `General.Interface.Action` | `#4A7DFF` |
| Primary hover | `General.Interface.Action hover` | `#285EFF` |
| Primary active | `General.Interface.Action active` | `#86A9FF` |
| Headline / primary text | `Text & Icon.Normal.Emphasis` | `#FFFFFF` |
| Body text | `Text & Icon.Normal.Standard` | `rgba(255,255,255,0.9)` |
| Secondary/muted text | `Text & Icon.Normal.Reduced` | `rgba(255,255,255,0.7)` |
| Border | `General.Borders & Lines.light` | `rgba(255,255,255,0.15)` |

```css
[data-theme="dark"] {
  --bg: #121212;
  --surface: #1E1E1E;
  --primary: #4A7DFF;
  --primary-hover: #285EFF;
  --primary-active: #86A9FF;
  --headline: #FFFFFF;
  --text: rgba(255, 255, 255, 0.9);
  --text-muted: rgba(255, 255, 255, 0.7);
  --border: rgba(255, 255, 255, 0.15);
}
```

**Assets to use:** logo = `assets/logos/wordmark/medtronic-logo-white.svg` · symbol =
`assets/symbol/symbol-full-color-reverse.svg` (preferred on Navy/Electric Blue per the guidelines'
"suitable for electric blue, navy blue and other dark, simple backgrounds" rule) or
`assets/symbol/symbol-white.svg` for busier/small contexts · icons =
`assets/icons/functional-white/` and `assets/icons/thematic-white/` — **use the white icon
folders here, not the default gray/blue ones**, per the icon color rule ("set icons in white when
they appear on a color background"). The near-black `#121212` background is dark/simple enough to
satisfy the same Symbol-on-dark-background rule as Navy.

## 4. Gradient Hero (landing pages / promotional sections only)

Builds on the guidelines' explicit, narrowly-scoped gradient rule — **don't** use this for body
text, buttons in a normal app, or anything other than a bold hero headline/graphic accents.

| Role | Value | Rule it follows |
| --- | --- | --- |
| Headline gradient | `linear-gradient(90deg, #1010EB, #140F4B)` | electric-blue-to-blue gradient, **bold weight, ≥18pt, light background only** |
| Decorative fill/stroke gradient | `linear-gradient(90deg, #0FC9F7, #00DCB9)` | light-blue-to-teal, for graphic shapes/strokes — not headline text |
| Background | White `#FFFFFF` | gradient headlines are only approved on light backgrounds |

```css
.hero-headline {
  font-weight: 700; /* bold */
  font-size: 2rem;  /* well over 18pt/24px */
  background: linear-gradient(90deg, #1010EB, #140F4B);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

**Assets to use:** the horizontal logo+tagline lockup
(`assets/logos/tagline-lockup-horizontal/medtronic-logo-tagline-navy.svg`) or the triple
logo+tagline+Symbol combo (`assets/logos/logo-tagline-symbol-combo/logo-tagline-symbol-combo-full-color.svg`)
for the hero itself — treat the lockup as a single unit, generous clear space, don't also repeat
the standalone tagline as a headline on the same screen (avoids the repetition the guidelines
warn against).

## Picking a preset

- Default to **Signature Light** unless the user asks for dark mode or the existing app is
  already dark-themed.
- Use **App Dark Mode** for a real product/app dark-mode toggle — this is the one with official
  UI Design System tokens (`#121212` background, `#4A7DFF` action color), not an approximation.
- Use **Navy Dark** specifically for marketing/brand surfaces — a dark sidebar, an "end-title"/
  promotional moment paired with the Symbol — not as a general app dark-mode theme.
- Use **Gradient Hero** treatments sparingly, only for a landing page's main headline or a
  section's accent shapes — never mix more than one gradient into the same screen, and never
  apply it to body copy or UI chrome (buttons, nav, form fields).
- These presets aren't mutually exclusive within one product: a marketing site can use Gradient
  Hero for its landing page and Signature Light for the rest of the app; a data-heavy dashboard
  with a dark-mode toggle should use App Dark Mode (not Navy Dark) and lean on the
  data-visualization color-sequence guidance in `brand-guidelines.md` instead of introducing a
  fifth ad-hoc palette.
