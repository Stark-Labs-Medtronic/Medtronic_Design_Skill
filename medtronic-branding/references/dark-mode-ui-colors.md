# Dark mode UI colors (Digital Design System)

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Dark Mode Colors"
page) — handed to this skill directly by a user with authenticated access, pasted verbatim as
data. This is a **different, more specific source** than [color-tokens.md](./color-tokens.md) /
[brand-guidelines.md](./brand-guidelines.md) (which come from the Brand Central marketing/identity guidelines): this one
is the actual **product/app UI token set**, scoped specifically to dark-mode interface design —
use it for React/Streamlit/app dark themes, not for marketing collateral.

**Important distinction from [theme-presets.md](./theme-presets.md)'s old guidance:** Brand Central says Navy
(`#140F4B`) and Electric Blue are approved **dark backgrounds for marketing/print** (logo and
Symbol placement). The actual **product UI dark-mode background is a neutral dark gray scale**
(`#121212` at its darkest), not Navy — these are two different, both-valid conventions for two
different contexts. Don't conflate them.

## Action / interactive

| Token | Value | Notes |
| --- | --- | --- |
| `General.Interface.Action` | `#4A7DFF` | Default interactive control color — this is the official dark-mode-safe blue (fills the "no official desaturated Electric Blue" gap noted elsewhere in this skill) |
| `General.Interface.Action hover` | `#285EFF` | Button hover state |
| `General.Interface.Action active` | `#86A9FF` | |
| `General.Interface.Action: secondary` | `#86A9FF` | Non-primary buttons use white text/icons/borders in dark mode |
| `General.Interface.Focus` | `#FFAD00` | Focus ring/outline color |

## Surface (backgrounds)

Elevation in dark mode is conveyed with progressively lighter grays, not drop shadows alone.

| Token | Value |
| --- | --- |
| `General.Surface.level 0` | `#121212` |
| `General.Surface.level 1` | `#1E1E1E` |
| `General.Surface.level 2` | `#2C2C2C` |
| `General.Surface.level 0 elevated` | `#1E1E1E` |
| `General.Surface.level 1 elevated` | `#2C2C2C` |
| `General.Surface.level 2 elevated` | `#3C3C3C` |
| `General.Surface.contrast` | `#F5F5F5` |
| `General.Surface.contrast brand` | `#DDE7FF` |

## Borders

| Token | Value |
| --- | --- |
| `General.Borders & Lines.light` | `rgba(255, 255, 255, 0.15)` |
| `General.Borders & Lines.medium` | `rgba(255, 255, 255, 0.35)` |
| `General.Borders & Lines.dark` | `rgba(255, 255, 255, 0.55)` |
| `General.Borders & Lines.inverse light` | `rgba(0, 0, 0, 0.1)` |
| `General.Borders & Lines.inverse medium` | `rgba(0, 0, 0, 0.3)` |
| `General.Borders & Lines.inverse dark` | `rgba(0, 0, 0, 0.55)` |

## Text & icons

Use these **only** for text/icon color, never as a background fill. White-with-opacity is
preferred over solid hex for contrast consistency across varied dark backgrounds.

| Token | Value |
| --- | --- |
| `Text & Icon.Normal.Emphasis` | `#FFFFFF` |
| `Text & Icon.Normal.Standard` | `rgba(255, 255, 255, 0.9)` |
| `Text & Icon.Normal.Reduced` | `rgba(255, 255, 255, 0.7)` |
| `Text & Icon.Normal.Disabled` | `rgba(255, 255, 255, 0.45)` |
| `Text & Icon.Inverse.Emphasis` | `rgba(0, 0, 0, 0.9)` |
| `Text & Icon.Inverse.Standard` | `rgba(0, 0, 0, 0.77)` |
| `Text & Icon.Inverse.Reduced` | `rgba(0, 0, 0, 0.55)` |
| `Text & Icon.Inverse.Disabled` | `rgba(0, 0, 0, 0.3)` |
| `Text & Icon.Normal.Accent` | `#DDE7FF` |
| `Text & Icon.Inverse.Accent` | `#100D78` |
| `Text & Icon.Normal.Link` | `#86A9FF` |
| `Text & Icon.Inverse.Link` | `#1010EB` |

Semantic text colors alias to the *light-mode* semantic tokens, now resolved via
[ui-design-system-colors.md](./ui-design-system-colors.md) — dark mode uses the identical values:
`Critical` `#A3001E`, `Caution` `#B56409`, `Confirm` `#3F6E03`, `Informative` `#0A5694`,
`Important` `#871C80`.

## Semantic (flags, color bars, backgrounds)

For semantic *text*, use the Text & Icons table above instead.

| Token | Value |
| --- | --- |
| `General.Semantic.Critical primary` | `#E40A1A` |
| `General.Semantic.Critical surface` | `#640012` |
| `General.Semantic.Caution primary` | `#F7AD00` |
| `General.Semantic.Caution surface` | `#643D00` |
| `General.Semantic.Confirm primary` | `#7ECA2A` |
| `General.Semantic.Confirm surface` | `#335900` |
| `General.Semantic.Informative primary` | `#008EFF` |
| `General.Semantic.Informative surface` | `#003866` |
| `General.Semantic.Important primary` | `#D24ADF` |
| `General.Semantic.Important surface` | `#560051` |

## Accent & data visualization

Reserved for charts/graphics only — same restraint rule as the Brand Central accent palette
(lead with blues/grays first). These alias to *light-mode* base tokens at specific tint steps,
now resolved to exact hex via the full tint stacks in
[ui-design-system-colors.md](./ui-design-system-colors.md):

| Token | Aliases to | Resolved value |
| --- | --- | --- |
| `General.Accents.Brown` | `{Standard colors.Brown.40}` | `#BC8162` |
| `General.Accents.Green` | `{Standard colors.Green.30}` | `#BEE891` |
| `General.Accents.Lavender` | `{Standard colors.Lavender.30}` | `#B2A5EE` |
| `General.Accents.Light blue` | `{Standard colors.Light blue.30}` | `#86E4FB` |
| `General.Accents.Orange` | `{Standard colors.Orange.30}` | `#FFD780` |
| `General.Accents.Pink` | `{Standard colors.Pink.30}` | `#FC78C1` |
| `General.Accents.Purple` | `{Standard colors.Purple.30}` | `#E88FE2` |
| `General.Accents.Red` | `{Standard colors.Red.30}` | `#FF758F` |
| `General.Accents.Teal` | `{Standard colors.Teal.30}` | `#66FFE2` |

## CSS custom properties

```css
[data-theme="dark"] {
  /* interactive */
  --action: #4A7DFF;
  --action-hover: #285EFF;
  --action-active: #86A9FF;
  --focus: #FFAD00;

  /* surfaces */
  --surface-0: #121212;
  --surface-1: #1E1E1E;
  --surface-2: #2C2C2C;
  --surface-contrast: #F5F5F5;

  /* borders */
  --border-light: rgba(255, 255, 255, 0.15);
  --border-medium: rgba(255, 255, 255, 0.35);

  /* text/icon */
  --text-emphasis: #FFFFFF;
  --text-standard: rgba(255, 255, 255, 0.9);
  --text-reduced: rgba(255, 255, 255, 0.7);
  --text-disabled: rgba(255, 255, 255, 0.45);
  --text-link: #86A9FF;
}
```

This supersedes the "no substitute value, use exact Electric Blue" fallback previously in
`theme-presets.md`'s Navy Dark preset for **app/product UI** — see that file for the updated
guidance and how it relates to the still-valid Navy/Electric-Blue dark-background rule for
marketing contexts.
