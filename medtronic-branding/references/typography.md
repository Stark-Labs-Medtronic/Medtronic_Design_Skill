# Typography (Digital Design System type scale)

**Source:** Medtronic's official `mdt-variables.css` — part of the "HTML/CSS Framework" starter
code kit (Zeroheight UI Design System, "HTML/CSS Framework" page, `02-Header-Variations.zip`).
This is the actual production CSS Medtronic ships, not a page description — treat it as the most
authoritative source for exact type-scale numbers, more precise than any prose description could
be. Bundled at
[assets/code-templates/html-css-framework/css/mdt-variables.css](../assets/code-templates/html-css-framework/css/mdt-variables.css).

## Typeface

Four `@font-face` weights are declared and used directly (not via `font-weight`, which the CSS
never sets above `normal` — Avenir Next World's weight variants are separate font files):

| CSS `font-family` name | Font file | Use |
| --- | --- | --- |
| `AvenirNextWorld` | `AvenirNextWorld-Regular.ttf` | Body copy (default) |
| `AvenirNextWorld-Thin` | `AvenirNextWorld-Thin.ttf` | Headlines (`h1`–`h3`, `txt06-08-09` headline/display styles) |
| `AvenirNextWorld-Demi` | `AvenirNextWorld-Demi.ttf` | Bold/strong text, buttons, eyebrow labels |
| `AvenirNextWorld-Italic` | `AvenirNextWorld-Italic.ttf` | Italic/emphasis text |

All 8 static weights (including `Bold`/`BoldIt`/`DemiIt`/`ThinIt`, not individually declared as
`@font-face` in this particular file but shipped in the same kit) are bundled at
`assets/fonts/avenir-next-world/*.ttf` — self-host these rather than relying on a system-font
fallback, per the existing font-license note in `brand-guidelines.md`.

Base document: `html { font-size: 16px; line-height: 30px; }`, `body` uses `AvenirNextWorld` with
color `var(--mdtText)` (`rgba(0,0,0,0.77)` — the "77% black" body-text rule already documented in
`ui-design-system-colors.md`, now confirmed byte-for-byte from source code).

## Heading scale (`h1`–`h4`)

| Element | Font | Size | Line-height | Color |
| --- | --- | --- | --- | --- |
| `h1` | Thin | 44px (`2.75rem`) | 52px | `--mdtTextPrimary` (`#170F5F`) |
| `h2` | Thin | 32px (`2rem`) | 40px | `--mdtTextPrimary` |
| `h3` | Thin | 24px (`1.5rem`) | 32px | `--mdtTextPrimary` |
| `h4` | Regular | 20px (`1.25rem`) | 28px | `--mdtTextPrimary` |

**Mobile override (`max-width: 480px`):** `h1` line-height tightens to 48px; `h3` switches to
Regular weight (24px/28px); `h4` switches to Demi weight (20px/24px), color changes to
`--mdtText` (body gray, not navy) — headings simplify visually on small screens.

## Named utility text styles (`txt01`–`txt09`)

A parallel, more granular scale used for non-heading text (captions, eyebrows, body copy at
different densities, buttons, and large display/marketing text):

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
| `.txt04-headline` | Regular | 20px | `--mdtTextPrimary` color |
| `.txt05-body` | Regular | 24px | `--mdtText` color |
| `.txt05-headline` | Thin | 24px | `--mdtTextPrimary` color |
| `.txt06-headline` | Regular | 32px | `--mdtTextPrimary` color |
| `.txt06-headline_thin` | Thin | 32px | `--mdtTextPrimary` color |
| `.txt07-headline` | Thin | 44px | `--mdtTextPrimary` color |
| `.txt08-headline` | Thin | 56px | `--mdtTextPrimary` color |
| `.txt09-display` | Thin | 72px | `--mdtTextPrimary` color, block-level |

**Links:** no underline by default, `color: var(--mdtTextLink)` (`#1010EB`); underline + color
`var(--mdtTextPrimary)` (`#170F5F`) on hover/active. `b`/`strong` forces the Demi font file
(not `font-weight: bold`); `i`/`em` forces the Italic font file.

## Reconciles the earlier color/typography Do's and Don'ts

`ui-design-system-colors.md`'s "Do use large thin fonts and navy blue text color for headlines"
rule is now exactly quantified: headlines use the **Thin** weight file and `#170F5F`
(`--mdtTextPrimary`, matching the on-screen-header navy from `app-header-logo-lockup.md` — a third
independent source confirming that hex), not the plain `#140F4B` Navy token.
