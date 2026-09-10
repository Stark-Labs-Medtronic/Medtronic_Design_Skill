# UI Design System colors (light / primary interface)

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Colors" page) — handed
to this skill directly by a user with authenticated access, pasted verbatim as data. This is the
**light-mode counterpart** to [dark-mode-ui-colors.md](./dark-mode-ui-colors.md), and a more
detailed, product/app-UI-specific token set than the Brand Central marketing colors in
[color-tokens.md](./color-tokens.md). Use this file for the actual token values behind any
`General.*` / `Text & Icon.*` / `Standard colors.*` name you see referenced elsewhere in this
skill (including the still-unresolved-looking aliases in `dark-mode-ui-colors.md` — most of those
are now resolved below).

## Action / interactive

| Token | Value | Notes |
| --- | --- | --- |
| `General.Interface.Action` | `#1010EB` | Electric Blue — controls/components users can interact with |
| `General.Interface.Action hover` | `#0C0CA5` | Button hover state |
| `General.Interface.Action active` | `#140F4B` | |
| `General.Interface.Action: secondary` | `#1010EB` | Non-primary (secondary/outline) buttons in **light mode**: Electric Blue text/icon/border on a transparent fill — see `sizing-standard.md` §8's `.btn-secondary` variant. For the dark-mode equivalent (white text/icon/border), see `dark-mode-ui-colors.md`'s own Action:secondary entry |
| `General.Interface.Focus` | `#ED7008` | Focus ring/outline — note this differs from the dark-mode Focus color (`#FFAD00`) |

## Surface (backgrounds)

| Token | Value |
| --- | --- |
| `General.Surface.level 0` | `#FFFFFF` |
| `General.Surface.level 1` | `#F5F5F5` |
| `General.Surface.level 2` | `#DCDCDC` |
| `General.Surface.level 0 elevated` | `#FFFFFF` |
| `General.Surface.level 1 elevated` | `#F5F5F5` |
| `General.Surface.level 2 elevated` | `#DCDCDC` |
| `General.Surface.contrast` | `#1E1E1E` |
| `General.Surface.contrast brand` | `#140F4B` |

## Borders

| Token | Value |
| --- | --- |
| `General.Borders & Lines.light` | `rgba(0, 0, 0, 0.1)` |
| `General.Borders & Lines.medium` | `rgba(0, 0, 0, 0.3)` |
| `General.Borders & Lines.dark` | `rgba(0, 0, 0, 0.55)` |
| `General.Borders & Lines.inverse light` | `rgba(255, 255, 255, 0.15)` |
| `General.Borders & Lines.inverse medium` | `rgba(255, 255, 255, 0.35)` |
| `General.Borders & Lines.inverse dark` | `rgba(255, 255, 255, 0.55)` |

## Text & icons

Never use these as background fills. Prefer the black-opacity values over solid hex — they hold
contrast better on non-white backgrounds.

### On light backgrounds

| Token | Value |
| --- | --- |
| `Text & Icon.Normal.Emphasis` | `rgba(0, 0, 0, 0.9)` |
| `Text & Icon.Normal.Standard` | `rgba(0, 0, 0, 0.77)` |
| `Text & Icon.Normal.Reduced` | `rgba(0, 0, 0, 0.55)` |
| `Text & Icon.Normal.Disabled` | `rgba(0, 0, 0, 0.3)` |
| `Text & Icon.Normal.Accent` | `#100D78` |
| `Text & Icon.Normal.Link` | `#1010EB` |

### On dark backgrounds

| Token | Value |
| --- | --- |
| `Text & Icon.Inverse.Emphasis` | `#FFFFFF` |
| `Text & Icon.Inverse.Standard` | `rgba(255, 255, 255, 0.9)` |
| `Text & Icon.Inverse.Reduced` | `rgba(255, 255, 255, 0.7)` |
| `Text & Icon.Inverse.Disabled` | `rgba(255, 255, 255, 0.45)` |
| `Text & Icon.Inverse.Accent` | `#DDE7FF` |
| `Text & Icon.Inverse.Link` | `#86A9FF` |

These "Inverse" values are byte-for-byte identical to the `Normal.*` tokens documented in
`dark-mode-ui-colors.md` — good cross-validation that the two source pages agree.

### Semantic text

| Token | Value |
| --- | --- |
| `Text & Icon.Semantic.Critical` | `#A3001E` |
| `Text & Icon.Semantic.Caution` | `#B56409` |
| `Text & Icon.Semantic.Confirm` | `#3F6E03` |
| `Text & Icon.Semantic.Informative` | `#0A5694` |
| `Text & Icon.Semantic.Important` | `#871C80` |

This resolves the alias noted in `dark-mode-ui-colors.md` ("Semantic text colors alias to the
light-mode semantic tokens") — dark mode uses these exact same values for semantic text.

### Typography color Do's and Don'ts

- Do use large fonts and navy blue text color for headlines. **Weight: use `AvenirNextWorld-Bold`.**
  (The original styleguide wording here was "large *thin* fonts". That half is **superseded** —
  Brand Central says "Use Regular, Demi, or Bold weight for headlines; avoid Thin weight if it hurts
  legibility." See the resolution in [typography.md](./typography.md) and the Contradiction Ledger in
  `SKILL.md`. The navy-color half of the rule still stands: `#170F5F`.)
- Do use 77% black (`rgba(0,0,0,0.77)` — `Text & Icon.Normal.Standard`) for body text.
- Do use Electric Blue (`#1010EB`) for links only.
- Do use low-emphasis text for eyebrow text.
- Don't use accent colors for headlines or links — most accent colors fail accessibility contrast
  requirements for typography.
- Don't use Electric Blue for body text, or for eyebrow text (unless the eyebrow itself is a
  link — and in general, avoid making eyebrow text a clickable link; keep one clear CTA per text
  group).
- Don't use bold/demi-weight fonts, or small font sizes, for headlines or links.

## Semantic colors (flags, color bars, backgrounds)

For semantic *text* color, use the Semantic text table above instead — these are for flags,
color bars, and background fills.

| Token | Value |
| --- | --- |
| `General.Semantic.Critical primary` | `#E40A1A` |
| `General.Semantic.Critical surface` | `#FFEFEE` |
| `General.Semantic.Caution primary` | `#F7A800` |
| `General.Semantic.Caution surface` | `#FFF9DB` |
| `General.Semantic.Confirm primary` | `#59A719` |
| `General.Semantic.Confirm surface` | `#EFF9E3` |
| `General.Semantic.Informative primary` | `#008EFF` |
| `General.Semantic.Informative surface` | `#E9FAFF` |
| `General.Semantic.Important primary` | `#C121EB` |
| `General.Semantic.Important surface` | `#F8ECFF` |

**Note:** these light-mode values are *not* all identical to the dark-mode Semantic table in
`dark-mode-ui-colors.md` (e.g. Caution primary is `#F7A800` here vs `#F7AD00` in dark mode,
Confirm primary is `#59A719` here vs `#7ECA2A` in dark mode) — both are official, as pasted
directly from their respective source pages. Use the light table for light-theme UI and the dark
table for dark-theme UI; don't average or "fix" the discrepancy without confirming with Global
Brand.

## Accent & data visualization

Reserved for charts/graphics only — **never** for body copy, links, buttons, or large background
fills (Navy Blue is the one exception for large fills).

| Token | Value | Tint-stack equivalent |
| --- | --- | --- |
| `General.Accents.Brown` | `#7B4D35` | `Standard colors.Brown.60` |
| `General.Accents.Green` | `#7ECA2A` | `Standard colors.Green.50` |
| `General.Accents.Lavender` | `#654BDD` | `Standard colors.Lavender.50` |
| `General.Accents.Light blue` | `#0FC9F7` | `Standard colors.Light blue.50` |
| `General.Accents.Orange` | `#FFAD00` | `Standard colors.Orange.50` |
| `General.Accents.Pink` | `#E5057F` | `Standard colors.Pink.50` |
| `General.Accents.Purple` | `#C529BB` | `Standard colors.Purple.50` |
| `General.Accents.Red` | `#ED002A` | `Standard colors.Red.50` |
| `General.Accents.Teal` | `#00DCB9` | `Standard colors.Teal.50` |

**Preferred order** (chosen for accessibility/color-blindness, holds up in grayscale too):
Electric Blue, Navy Blue, Light Blue, Pink, Orange, Lavender, Green, Purple, Teal, Red, Brown.

- Do use Electric Blue as the sole accent for a **single-data-point chart** (one number — a gauge,
  a donut showing one %, a single KPI visualization).
- Don't use any accent color when a chart has **only one data series across multiple points**
  (e.g. a single-line trend chart) — use Navy Blue or a neutral gray instead; an accent implies
  "one of several," which isn't true here.
- Don't lead with Electric Blue in a **multi-series/multi-color chart** — lead with Navy Blue,
  then continue in the preferred order above (Light Blue → Pink → Orange → Lavender → Green →
  Purple → Teal → Red → Brown). See the Contradiction Ledger in `SKILL.md` — this bullet used to
  read as self-contradictory (Electric Blue for "single-data-point" vs. "only one data source" in
  the same breath); split into three unambiguous cases above.
- Don't use Navy Blue alone in a chart — it reads as near-black.
- Don't use tint-stack colors for charts, and don't mix Electric Blue with other accent colors.

### Resolves the dark-mode accent aliases

`dark-mode-ui-colors.md` documents its Accent & data visualization tokens only as aliases (e.g.
`{Standard colors.Green.30}`) because the dark-mode source page didn't spell out hex values. Now
that the full tint stacks are available (below), those aliases resolve to:

| Token | Dark-mode alias | Resolved value |
| --- | --- | --- |
| `General.Accents.Brown` (dark) | `Standard colors.Brown.40` | `#BC8162` |
| `General.Accents.Green` (dark) | `Standard colors.Green.30` | `#BEE891` |
| `General.Accents.Lavender` (dark) | `Standard colors.Lavender.30` | `#B2A5EE` |
| `General.Accents.Light blue` (dark) | `Standard colors.Light blue.30` | `#86E4FB` |
| `General.Accents.Orange` (dark) | `Standard colors.Orange.30` | `#FFD780` |
| `General.Accents.Pink` (dark) | `Standard colors.Pink.30` | `#FC78C1` |
| `General.Accents.Purple` (dark) | `Standard colors.Purple.30` | `#E88FE2` |
| `General.Accents.Red` (dark) | `Standard colors.Red.30` | `#FF758F` |
| `General.Accents.Teal` (dark) | `Standard colors.Teal.30` | `#66FFE2` |

## Neutrals

Standard tint stack of neutrals for use throughout a digital application.

| Step | Value |
| --- | --- |
| 00 | `#FFFFFF` |
| 10 | `#F5F5F5` |
| 20 | `#DCDCDC` |
| 30 | `#BFBFBF` |
| 40 | `#999999` |
| 50 | `#777777` |
| 60 | `#555555` |
| 70 | `#3C3C3C` |
| 80 | `#2C2C2C` |
| 90 | `#1E1E1E` |
| 100 | `#121212` |
| 110 | `#000000` |

## Full tint stacks

**Reserved for data visualization, illustrations, and graphics only** — never for body copy,
links, buttons, or icons (use the Action/Text-Icon/Semantic tables above for those).

| Step | Brown | Green | Lavender | Light blue | Medtronic Blues | Orange | Pink | Purple | Red | Teal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | `#FCECE1` | `#EFF9E3` | `#ECE9FB` | `#E1F8FE` | `#DDE7FF` | `#FFF5DF` | `#FEDDEF` | `#F9E3F8` | `#FFDDE3` | `#D6FFF8` |
| 20 | `#E3C7B8` | `#DFF4C8` | `#D9D2F6` | `#C2F1FD` | `#C2D5FF` | `#FFEBBF` | `#FEBCE0` | `#F4C7F1` | `#FFBAC7` | `#AAFAF0` |
| 30 | `#CEA48D` | `#BEE891` | `#B2A5EE` | `#86E4FB` | `#86A9FF` | `#FFD780` | `#FC78C1` | `#E88FE2` | `#FF758F` | `#66FFE2` |
| 40 | `#BC8162` | `#9EDD5A` | `#8C78E5` | `#48D6F9` | `#4A7DFF` | `#FFC240` | `#FB35A2` | `#DD57D4` | `#FF3056` | `#00F5CC` |
| 50 | `#9D6343` | `#7ECA2A` | `#654BDD` | `#0FC9F7` | `#285EFF` | `#FFAD00` | `#E5057F` | `#C529BB` | `#ED002A` | `#00DCB9` |
| 60 | `#7B4D35` | `#64AD28` | `#5727D4` | `#009BDA` | `#252AFF` | `#F59300` | `#C9056C` | `#A923A0` | `#CD0025` | `#00B899` |
| 70 | `#563625` | `#599518` | `#4121AB` | `#0073B4` | `#1010EB` | `#CC7A00` | `#AC0460` | `#871C80` | `#A3001E` | `#008F77` |
| 80 | `#412816` | `#376415` | `#291778` | `#0A5694` | `#0C0CA5` | `#8C5300` | `#730240` | `#63145E` | `#7A0016` | `#006655` |
| 90 | `#2B1B13` | `#26460F` | `#1D1056` | `#083C71` | `#100D78` | `#4A2D00` | `#46112F` | `#3F173D` | `#52000F` | `#003D33` |
| 100 | `#24140A` | `#1C2A0A` | `#150C3E` | `#082542` | `#140F4B` | `#331D05` | `#390120` | `#320A2F` | `#3B000B` | `#002922` |

`Standard colors.Misc.navy` = `#170F5F` (the same on-screen/app-header navy documented in
`app-header-logo-lockup.md` — good cross-validation from a second, independent source page) and
`Standard colors.Misc.orange` = `#ED7008` (same as `General.Interface.Focus` above).

## Design tokens (raw JSON, tint stacks only)

Machine-readable form of the tint-stack tables above, in W3C design-tokens-community-group format
— pasted verbatim from the source page, useful for generating a `design-tokens.json` in a project.

```json
{
  "Standard colors": {
    "Brown": {
      "10": { "$type": "color", "$value": "#FCECE1" },
      "20": { "$type": "color", "$value": "#E3C7B8" },
      "30": { "$type": "color", "$value": "#CEA48D" },
      "40": { "$type": "color", "$value": "#BC8162" },
      "50": { "$type": "color", "$value": "#9D6343" },
      "60": { "$type": "color", "$value": "#7B4D35" },
      "70": { "$type": "color", "$value": "#563625" },
      "80": { "$type": "color", "$value": "#412816" },
      "90": { "$type": "color", "$value": "#2B1B13" },
      "100": { "$type": "color", "$value": "#24140A" }
    },
    "Green": {
      "10": { "$type": "color", "$value": "#EFF9E3" },
      "20": { "$type": "color", "$value": "#DFF4C8" },
      "30": { "$type": "color", "$value": "#BEE891" },
      "40": { "$type": "color", "$value": "#9EDD5A" },
      "50": { "$type": "color", "$value": "#7ECA2A" },
      "60": { "$type": "color", "$value": "#64AD28" },
      "70": { "$type": "color", "$value": "#599518" },
      "80": { "$type": "color", "$value": "#376415" },
      "90": { "$type": "color", "$value": "#26460F" },
      "100": { "$type": "color", "$value": "#1C2A0A" }
    },
    "Lavender": {
      "10": { "$type": "color", "$value": "#ECE9FB" },
      "20": { "$type": "color", "$value": "#D9D2F6" },
      "30": { "$type": "color", "$value": "#B2A5EE" },
      "40": { "$type": "color", "$value": "#8C78E5" },
      "50": { "$type": "color", "$value": "#654BDD" },
      "60": { "$type": "color", "$value": "#5727D4" },
      "70": { "$type": "color", "$value": "#4121AB" },
      "80": { "$type": "color", "$value": "#291778" },
      "90": { "$type": "color", "$value": "#1D1056" },
      "100": { "$type": "color", "$value": "#150C3E" }
    },
    "Light blue": {
      "10": { "$type": "color", "$value": "#E1F8FE" },
      "20": { "$type": "color", "$value": "#C2F1FD" },
      "30": { "$type": "color", "$value": "#86E4FB" },
      "40": { "$type": "color", "$value": "#48D6F9" },
      "50": { "$type": "color", "$value": "#0FC9F7" },
      "60": { "$type": "color", "$value": "#009BDA" },
      "70": { "$type": "color", "$value": "#0073B4" },
      "80": { "$type": "color", "$value": "#0A5694" },
      "90": { "$type": "color", "$value": "#083C71" },
      "100": { "$type": "color", "$value": "#082542" }
    },
    "Medtronic Blues": {
      "10": { "$type": "color", "$value": "#DDE7FF" },
      "20": { "$type": "color", "$value": "#C2D5FF" },
      "30": { "$type": "color", "$value": "#86A9FF" },
      "40": { "$type": "color", "$value": "#4A7DFF" },
      "50": { "$type": "color", "$value": "#285EFF" },
      "60": { "$type": "color", "$value": "#252AFF" },
      "70": { "$type": "color", "$value": "#1010EB" },
      "80": { "$type": "color", "$value": "#0C0CA5" },
      "90": { "$type": "color", "$value": "#100D78" },
      "100": { "$type": "color", "$value": "#140F4B" }
    },
    "Misc": {
      "navy": { "$type": "color", "$value": "#170F5F" },
      "orange": { "$type": "color", "$value": "#ED7008" }
    },
    "Neutral": {
      "00": { "$type": "color", "$value": "#FFFFFF" },
      "10": { "$type": "color", "$value": "#F5F5F5" },
      "20": { "$type": "color", "$value": "#DCDCDC" },
      "30": { "$type": "color", "$value": "#BFBFBF" },
      "40": { "$type": "color", "$value": "#999999" },
      "50": { "$type": "color", "$value": "#777777" },
      "60": { "$type": "color", "$value": "#555555" },
      "70": { "$type": "color", "$value": "#3C3C3C" },
      "80": { "$type": "color", "$value": "#2C2C2C" },
      "90": { "$type": "color", "$value": "#1E1E1E" },
      "100": { "$type": "color", "$value": "#121212" },
      "110": { "$type": "color", "$value": "#000000" }
    },
    "Orange": {
      "10": { "$type": "color", "$value": "#FFF5DF" },
      "20": { "$type": "color", "$value": "#FFEBBF" },
      "30": { "$type": "color", "$value": "#FFD780" },
      "40": { "$type": "color", "$value": "#FFC240" },
      "50": { "$type": "color", "$value": "#FFAD00" },
      "60": { "$type": "color", "$value": "#F59300" },
      "70": { "$type": "color", "$value": "#CC7A00" },
      "80": { "$type": "color", "$value": "#8C5300" },
      "90": { "$type": "color", "$value": "#4A2D00" },
      "100": { "$type": "color", "$value": "#331D05" }
    },
    "Pink": {
      "10": { "$type": "color", "$value": "#FEDDEF" },
      "20": { "$type": "color", "$value": "#FEBCE0" },
      "30": { "$type": "color", "$value": "#FC78C1" },
      "40": { "$type": "color", "$value": "#FB35A2" },
      "50": { "$type": "color", "$value": "#E5057F" },
      "60": { "$type": "color", "$value": "#C9056C" },
      "70": { "$type": "color", "$value": "#AC0460" },
      "80": { "$type": "color", "$value": "#730240" },
      "90": { "$type": "color", "$value": "#46112F" },
      "100": { "$type": "color", "$value": "#390120" }
    },
    "Purple": {
      "10": { "$type": "color", "$value": "#F9E3F8" },
      "20": { "$type": "color", "$value": "#F4C7F1" },
      "30": { "$type": "color", "$value": "#E88FE2" },
      "40": { "$type": "color", "$value": "#DD57D4" },
      "50": { "$type": "color", "$value": "#C529BB" },
      "60": { "$type": "color", "$value": "#A923A0" },
      "70": { "$type": "color", "$value": "#871C80" },
      "80": { "$type": "color", "$value": "#63145E" },
      "90": { "$type": "color", "$value": "#3F173D" },
      "100": { "$type": "color", "$value": "#320A2F" }
    },
    "Red": {
      "10": { "$type": "color", "$value": "#FFDDE3" },
      "20": { "$type": "color", "$value": "#FFBAC7" },
      "30": { "$type": "color", "$value": "#FF758F" },
      "40": { "$type": "color", "$value": "#FF3056" },
      "50": { "$type": "color", "$value": "#ED002A" },
      "60": { "$type": "color", "$value": "#CD0025" },
      "70": { "$type": "color", "$value": "#A3001E" },
      "80": { "$type": "color", "$value": "#7A0016" },
      "90": { "$type": "color", "$value": "#52000F" },
      "100": { "$type": "color", "$value": "#3B000B" }
    },
    "Teal": {
      "10": { "$type": "color", "$value": "#D6FFF8" },
      "20": { "$type": "color", "$value": "#AAFAF0" },
      "30": { "$type": "color", "$value": "#66FFE2" },
      "40": { "$type": "color", "$value": "#00F5CC" },
      "50": { "$type": "color", "$value": "#00DCB9" },
      "60": { "$type": "color", "$value": "#00B899" },
      "70": { "$type": "color", "$value": "#008F77" },
      "80": { "$type": "color", "$value": "#006655" },
      "90": { "$type": "color", "$value": "#003D33" },
      "100": { "$type": "color", "$value": "#002922" }
    }
  }
}
```
