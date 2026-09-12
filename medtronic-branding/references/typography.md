# Typography (Digital Design System type scale)

**Source:** Medtronic's official `mdt-variables.css` — part of the "HTML/CSS Framework" starter
code kit (Zeroheight UI Design System, "HTML/CSS Framework" page, `02-Header-Variations.zip`).
This is the actual production CSS Medtronic ships, not a page description — treat it as the most
authoritative source for exact type-scale numbers, more precise than any prose description could
be. Bundled at
[assets/code-templates/html-css-framework/css/mdt-variables.css](../assets/code-templates/html-css-framework/css/mdt-variables.css).

## Typeface

Weights are used **by family name, never via `font-weight`** — Avenir Next World's weights are
separate font files, and the CSS pairs every one of them with an explicit `font-weight: normal`:

| CSS `font-family` name | Font file | Use |
| --- | --- | --- |
| `AvenirNextWorld` | `AvenirNextWorld-Regular.ttf` | Body copy (default), `h4` |
| `AvenirNextWorld-Bold` | `AvenirNextWorld-Bold.ttf` | **Headlines `h1`–`h3` and all headline/display styles** |
| `AvenirNextWorld-Demi` | `AvenirNextWorld-Demi.ttf` | Bold/strong text, buttons, eyebrow labels |
| `AvenirNextWorld-Italic` | `AvenirNextWorld-Italic.ttf` | Italic/emphasis text |
| `AvenirNextWorld-Thin` | `AvenirNextWorld-Thin.ttf` | Not used for headlines — see the note below |

All 8 static weights (Regular, Italic, Thin, ThinIt, Demi, DemiIt, **Bold**, BoldIt) are bundled at
`assets/fonts/avenir-next-world/*.ttf` — self-host these rather than relying on a system-font
fallback, per the existing font-license note in [brand-guidelines.md](./brand-guidelines.md).

Base document: `html { font-size: 16px; line-height: 30px; }`, `body` uses `AvenirNextWorld` with
color `var(--mdtText)` (`rgba(0,0,0,0.77)` — the "77% black" body-text rule already documented in
[ui-design-system-colors.md](./ui-design-system-colors.md), confirmed byte-for-byte from source code).

## `[MANDATORY]` Headlines are Bold

Brand Central: "Use **Regular, Demi, or Bold** weight for headlines; **avoid Thin** weight if it
hurts legibility." Thin at 44–72px is the weight most prone to legibility failure — thin strokes at
display size are exactly the case that warning is about, and it fails hardest for the low-vision
and time-pressured clinical users much of this skill's output serves.

Medtronic's HTML/CSS Framework starter kit originally shipped Thin for `h1`–`h3` and the named
headline/display classes. This skill uses `AvenirNextWorld-Bold` there instead — a documented
**Local Override** (see the table in [SKILL.md](../SKILL.md)), baked directly into the bundled
`mdt-variables.css` rather than layered on top of it, so there's one file to read instead of two.
If you're writing fresh CSS rather than using the starter kit, just follow the matrix below.

## `[MANDATORY]` Never express weight with `font-weight`

```css
/* CORRECT - weight lives in the family name */
h1 { font-family: "AvenirNextWorld-Bold"; font-weight: normal; }

/* WRONG - synthesises a weight and ignores the real font file */
h1 { font-weight: 700; }
h1 { font-weight: bold; }
h1 { font-weight: 100; }
```

Setting a numeric or keyword `font-weight` is a defect in either direction. The weight is the
**font family name**; `font-weight` stays `normal` throughout.

> **Exception — the single-family strategy.** The rule above applies when each weight is a **distinct
> family name**, as `mdt-variables.css` does. There is a second valid strategy, recommended for React
> in [react-integration.md](./react-integration.md): declare **one** family (`"Avenir Next World"`)
> with `font-weight` descriptors in each `@font-face`, so `font-weight: 700` resolves to
> `AvenirNextWorld-Bold.ttf`. Under that strategy `font-weight: 700` is correct and required.
>
> | Strategy | Weight expressed as | `font-weight` |
> | --- | --- | --- |
> | Family-per-weight (`mdt-variables.css`, HTML starter kit) | family name | `normal` |
> | Single family + descriptors (React) | `font-weight: 700` | required |
>
> **Pick one per project and don't mix them** — a numeric `font-weight` on top of an
> already-weighted family file synthesises a fake weight, which is the actual defect the rule guards
> against.

**Fallback-stack caveat `[MANDATORY]`.** Bold survives a fallback far better than Thin did — if the
licensed font is unavailable, a system sans-serif at `font-weight: 700` is a reasonable
approximation of Bold, whereas a synthesised thin renders as washed-out hairline text. So in a
fallback scenario, `font-weight: bold` **is** acceptable — but only on the fallback face, never
alongside the real `AvenirNextWorld-Bold` family:

```css
h1 {
  font-family: "AvenirNextWorld-Bold", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  font-weight: normal;         /* real font: weight is in the family name */
}
@supports not (font-family: "AvenirNextWorld-Bold") {
  h1 { font-weight: 700; }     /* fallback only */
}
```

## Heading scale — Weight Context Matrix `[MANDATORY]`

| Element | Desktop (>480px) | Mobile (≤480px) | Size | Line-height | Color |
| --- | --- | --- | --- | --- | --- |
| `h1` | **Bold** | Bold | 44px (`2.75rem`) | 52px → **48px** mobile | `--mdtTextPrimary` (`#170F5F`) |
| `h2` | **Bold** | Bold | 32px (`2rem`) | 40px | `--mdtTextPrimary` |
| `h3` | **Bold** | **Regular** | 24px (`1.5rem`) | 32px → 28px mobile | `--mdtTextPrimary` |
| `h4` | **Regular** | **Demi** | 20px (`1.25rem`) | 28px → 24px mobile | `--mdtTextPrimary` → **`--mdtText`** mobile |

So: **h1 and h2 are always Bold. h3 is Bold on desktop and Regular on mobile. h4 is never Bold.**
Headings deliberately simplify on small screens — do not carry desktop Bold into a mobile layout for
h3/h4. The mobile de-escalation is preserved exactly as the source CSS defines it; only the top-end
weight changed from Thin to Bold.

### Where a real choice exists `[FLEXIBLE]`

At 32px the design system ships two headline variants. With Bold headlines, the pairing is:

| Class | Font | Size | When |
| --- | --- | --- | --- |
| `.txt06-headline` | Regular | 32px | Denser product UI, section headings inside a card, secondary hierarchy under a Bold `h2` |
| `.txt06-headline_bold` | **Bold** | 32px | Primary section headings, marketing, hero sub-heads |

Pick by surface type per [design-intuition.md](./design-intuition.md)'s DENSITY dial: on a dense screen, a Regular 32px
heading under a Bold `h1` reads as clearer hierarchy than two Bold sizes competing.

## Named utility text styles (`txt01`–`txt09`)

A parallel, more granular scale used for non-heading text (captions, eyebrows, body copy at
different densities, buttons, and large display/marketing text).

| Class | Font | Size | Notes |
| --- | --- | --- | --- |
| `.txt01-caption` | Regular | 12px | |
| `.txt01-caption_alt` | Italic | 12px | |
| `.txt01-eyebrow` | Demi | 12px | Uppercase, 1.3px letter-spacing, `--mdtTextLow` color |
| `.txt01-label` | Regular | 12px | Uppercase |
| `.txt02-body` | Regular | 14px | `--mdtText` color |
| `.txt02-eyebrow` | Demi | 14px | Uppercase, 1.5px letter-spacing, `--mdtTextLow` color |
| `.txt02-button` | Demi | 14px | Small-button label text |
| `.txt03-body` | Regular | 16px | `--mdtText` color |
| `.txt03-button` | Demi | 16px | Default-button label text, 0.6px letter-spacing |
| `.txt04-body` | Regular | 20px | `--mdtText` color, line-height 1.75 |
| `.txt04-headline` | Regular | 20px | `--mdtTextPrimary` color — smallest headline, stays Regular |
| `.txt05-body` | Regular | 24px | `--mdtText` color |
| `.txt05-headline` | **Bold** | 24px | `--mdtTextPrimary` color |
| `.txt06-headline` | Regular | 32px | `--mdtTextPrimary` color |
| `.txt06-headline_bold` | **Bold** | 32px | `--mdtTextPrimary` color |
| `.txt07-headline` | **Bold** | 44px | `--mdtTextPrimary` color |
| `.txt08-headline` | **Bold** | 56px | `--mdtTextPrimary` color |
| `.txt09-display` | **Bold** | 72px | `--mdtTextPrimary` color, block-level |

> `.txt06-headline_thin` is **renamed to `.txt06-headline_bold`** so the class name doesn't lie about
> its weight. If a project already ships markup using `_thin`, keep an alias rather than silently
> changing what that class renders — a class named `_thin` rendering Bold is worse than either.

**Links:** no underline by default, `color: var(--mdtTextLink)` (`#1010EB`); underline + color
`var(--mdtTextPrimary)` (`#170F5F`) on hover/active. `b`/`strong` forces the Demi font file
(not `font-weight: bold`); `i`/`em` forces the Italic font file.

**Note on `strong` vs. headlines:** `b`/`strong` stays **Demi**, not Bold. With Bold headlines, Demi
emphasis inside body copy keeps a visible step between "emphasised body text" and "heading" — using
Bold for both would flatten that distinction.

## Reconciles the earlier color/typography Do's and Don'ts

The headline **color** rule is settled and unchanged: headlines are `#170F5F`
(`--mdtTextPrimary`, matching the on-screen-header navy from [app-header-logo-lockup.md](./app-header-logo-lockup.md) — a third
independent source confirming that hex), not the plain `#140F4B` Navy token.

The headline **weight** is `AvenirNextWorld-Bold`, per Brand Central's explicit "Use Regular, Demi,
or Bold weight for headlines; avoid Thin weight if it hurts legibility." See the resolution section
at the top of this file.
