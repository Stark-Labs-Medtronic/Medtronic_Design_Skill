# Theme presets — Light, Dark, and Gradient Hero

Ready-to-use combinations of the exact tokens in [color-tokens.md](./color-tokens.md), the rules
in [brand-guidelines.md](./brand-guidelines.md), and the real asset files in [`../assets/`](../assets/).
**Offer these to the user as the Step 0.5 color-combination menu** ([SKILL.md](../SKILL.md)) rather than picking
one silently, then layer in the specific screen's content.

Every hex value below traces back to [color-tokens.md](./color-tokens.md). Where the source guidelines describe a
rule but the exact value only exists in an uncaptioned diagram (not extractable as text — see the
"Content gaps" note in [brand-guidelines.md](./brand-guidelines.md)), that gap is called out explicitly and **no
substitute value is invented** — the preset falls back to an exact, already-documented token
instead of guessing a new one.

## `[MANDATORY]` Anti-pattern: the blue-sidebar default

**A navy or blue left sidebar next to a white main content area is not a default.** It is one
combination among several, and it is only produced when:

1. The user explicitly chose it in the Step 0.5 question, **or**
2. The app being restyled already uses that structure.

Producing it by reflex on every request is the single most recognizable generic-AI output this skill
has generated, and it is a failure of the skill rather than a neutral choice. Other tells to avoid in
the same breath:

- A colored sidebar added purely as decoration, with no navigation in it
- An accent color used as sidebar chrome (this also breaks the one-accent lock — Light Blue
  `#0FC9F7` is a **data-visualization** color, never UI chrome)
- Every screen using the same shell regardless of what it does
- A full-width `layout="wide"` container holding a single narrow form
- Equal-weight cards in a uniform grid where the content isn't equally important

**Pick the shell archetype from [design-intuition.md](./design-intuition.md) and the color combination from this file as two
separate, deliberate decisions.** Note that the combinations below are *page-level* themes — none of
them prescribes a sidebar treatment, and picking one does not imply a colored sidebar.

## Preset index

| # | Preset | Best for | Mode |
| --- | --- | --- | --- |
| 1 | **Signature Light** | Most app/dashboard UI, general default | Light |
| 2 | **Navy Dark** | Marketing/brand surfaces, promotional moments | Dark |
| 3 | **App Dark Mode** | Product UI dark mode (official tokens) | Dark |
| 4 | **Gradient Hero** | Landing pages, promotional sections only | Light |
| 5 | **Atmospheric Light** | Data-dense dashboards, clinical tools | Light |
| 6 | **Navy Header Light** | Web-app shells wanting brand presence without a colored sidebar | Light |

## 1. Signature Light (general default — most app/dashboard UI)

The standard "lead with blue and white" look the guidelines describe as the default.

| Role | Token | Value |
| --- | --- | --- |
| Page background | White | `#FFFFFF` |
| Card / section background | Atmospheric White | `#F5F5F5` |
| Primary / CTA / links | Electric Blue | `#1010EB` |
| Headline text | Navy (digital) | `#170F5F` |
| Body text | Text.Normal (`--mdtText`) | `rgba(0, 0, 0, 0.77)` |
| Secondary / disclaimer text | Text.Normal.low (`--mdtTextLow`) | `rgba(0, 0, 0, 0.55)` |
| Divider / border | Navy at low opacity | `rgba(20, 15, 75, 0.12)` *(structural opacity of the Navy token, not a new hue)* |

**Assets to use:** logo = `assets/logos/wordmark/medtronic-logo-navy-digital.svg` (`#170F5F`, the
on-screen variant) · symbol (if used) = `assets/symbol/symbol-full-color.svg` · icons = **Carbon**,
colored via `color: var(--text)`; `assets/icons/thematic/` (blue) for brand/editorial moments.

```css
:root {
  --bg: #FFFFFF;
  --surface: #F5F5F5;
  --primary: #1010EB;
  --headline: #170F5F;
  --text: rgba(0, 0, 0, 0.77);
  --text-muted: rgba(0, 0, 0, 0.55);
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

## 5. Atmospheric Light (data-dense dashboards, clinical tools)

Inverts Signature Light's surface relationship: the **page** is Atmospheric White and **cards** are
pure white, so cards lift off the canvas instead of sinking into it. Better than Signature Light when
a screen is mostly cards — a white-on-white dashboard needs borders to do all the work, which reads as
flat and washed out at high density.

Every value is an existing token; nothing new is introduced.

| Role | Token | Value |
| --- | --- | --- |
| Page background | Atmospheric White | `#F5F5F5` |
| Card / raised surface | White | `#FFFFFF` |
| Primary / CTA / links | Electric Blue | `#1010EB` |
| Headline text | Navy (digital) | `#170F5F` |
| Body text | `--mdtText` | `rgba(0, 0, 0, 0.77)` |
| Secondary text | `--mdtTextLow` | `rgba(0, 0, 0, 0.55)` |
| Divider / border | Navy at low opacity | `rgba(20, 15, 75, 0.12)` |
| Row hover | `--mdtBkgdHover` | `rgba(20, 15, 75, 0.08)` |
| Row selected | `--mdtBkgdSelected` | `rgba(20, 15, 75, 0.12)` |

```css
:root {
  --bg: #F5F5F5;
  --surface: #FFFFFF;
  --primary: #1010EB;
  --headline: #170F5F;
  --text: rgba(0, 0, 0, 0.77);
  --text-muted: rgba(0, 0, 0, 0.55);
  --border: rgba(20, 15, 75, 0.12);
  --row-hover: rgba(20, 15, 75, 0.08);
  --row-selected: rgba(20, 15, 75, 0.12);
}
```

Pairs naturally with the "gray header + white body" shell variant in `design-intuition.md`. At
DENSITY 6+, prefer `.txt06-headline` (Regular, 32px) over the Bold variant for *section* headings, so
the Bold `h1`/`h2` stays the dominant tier — see the Weight Context Matrix in [typography.md](./typography.md).

**Assets:** same as Signature Light. Carbon icons at `color: var(--text)`.

## 6. Navy Header Light (brand presence without a colored sidebar)

For a web-app shell that wants visible brand presence but **no colored sidebar**. The header carries
the navy; navigation and content stay light. This is the preset to reach for when the instinct says
"navy sidebar" — it satisfies the same goal without the generic-AI layout.

| Role | Token | Value |
| --- | --- | --- |
| Header surface (64px) | Navy | `#140F4B` |
| Header text / logo | White | `#FFFFFF` — use the **white** wordmark here |
| Header divider | Border.dim white | `rgba(255, 255, 255, 0.10)` |
| Page background | White | `#FFFFFF` |
| Card / section surface | Atmospheric White | `#F5F5F5` |
| Side nav surface (if present) | White | `#FFFFFF` — **not** navy |
| Side nav active item | `--mdtBkgdSelected` | `rgba(20, 15, 75, 0.12)` |
| Primary / CTA / links | Electric Blue | `#1010EB` |
| Headline text | Navy (digital) | `#170F5F` |
| Body text | `--mdtText` | `rgba(0, 0, 0, 0.77)` |

```css
:root {
  --header-bg: #140F4B;
  --header-text: #FFFFFF;
  --header-border: rgba(255, 255, 255, 0.10);
  --bg: #FFFFFF;
  --surface: #F5F5F5;
  --nav-bg: #FFFFFF;
  --nav-active: rgba(20, 15, 75, 0.12);
  --primary: #1010EB;
  --headline: #170F5F;
  --text: rgba(0, 0, 0, 0.77);
}
```

**Assets:** logo = `assets/logos/wordmark/medtronic-logo-white.svg` (white, because the header is
navy — never the navy wordmark on a navy bar). Carbon icons in the header at
`color: rgba(255,255,255,0.9)`, in the body at `color: var(--text)` — one file, two contexts, because
Carbon inherits `currentColor`.

Header is 64px per [global-header.md](./global-header.md), logo at 28px per [sizing-standard.md](./sizing-standard.md) §0.

## Picking a preset

**Offer these to the user in the Step 0.5 question rather than choosing silently** (`SKILL.md`). The
notes below are for framing the options and for the case where the brief already decided.

- **Signature Light** — the safe general default for most app/dashboard UI.
- **Atmospheric Light** — prefer over Signature Light when the screen is mostly cards or a dense
  data table; cards need to lift off the canvas.
- **App Dark Mode** — the correct choice for a real product/app dark-mode toggle. This is the one
  with official UI Design System tokens (`#121212` background, `#4A7DFF` action color), not an
  approximation.
- **Navy Dark** — marketing/brand surfaces and promotional "end-title" moments paired with the
  Symbol. **Not** a general app dark-mode theme, and **not** a license to build a navy sidebar. If
  the goal is brand presence in a product shell, use **Navy Header Light** instead.
- **Navy Header Light** — brand presence in a web-app shell without a colored sidebar.
- **Gradient Hero** — sparingly, only for a landing page's main headline or a section's accent
  shapes. Never more than one gradient per screen, never on body copy or UI chrome (buttons, nav,
  form fields).
- These presets aren't mutually exclusive within one product: a marketing site can use Gradient
  Hero for its landing page and Signature Light for the rest of the app; a data-heavy dashboard
  with a dark-mode toggle should use App Dark Mode (not Navy Dark) and lean on the
  data-visualization color-sequence guidance in `brand-guidelines.md` instead of introducing an
  ad-hoc seventh palette.

**In every preset, the one-accent lock holds:** Electric Blue `#1010EB` (or `#4A7DFF` in App Dark
Mode) is the only accent used for interactive UI chrome. Light Blue, Teal, Pink, Orange, and the rest
of the accent palette are **data-visualization colors only** — never a sidebar fill, never a
secondary button.
