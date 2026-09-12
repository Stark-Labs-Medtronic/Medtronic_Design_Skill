# Using this skill in a Streamlit project

Prefer native Streamlit theming (`.streamlit/config.toml`) over custom CSS wherever possible —
only reach for `unsafe_allow_html`/injected CSS for the handful of things native theming can't do
(pill-shaped buttons, the logo image, icon SVGs). This mirrors Streamlit's own guidance: don't
hand-roll what a theme key or built-in widget parameter already covers.

> **This file covers theming. For page structure, columns, alignment, and spacing, read
> [streamlit-layout.md](./streamlit-layout.md) `[MANDATORY]`** — it is authoritative for Streamlit
> layout and carries the alignment pre-flight checklist. Theming a misaligned layout still produces a
> misaligned app.

## 1. `.streamlit/config.toml`

**`[MANDATORY]` Pick the block matching the preset the user chose in Step 0.5.** There is no default
sidebar treatment — see the anti-pattern rule in [theme-presets.md](./theme-presets.md).

**Signature Light (preset 1) — general default:**

```toml
[theme]
primaryColor = "#1010EB"              # Electric Blue - buttons, active widgets, links
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"  # Atmospheric White - cards, widget bg
textColor = "rgba(0,0,0,0.77)"        # --mdtText, the real 77% black body token
font = "sans-serif"                   # see the font note below
```

**Atmospheric Light (preset 5) — data-dense dashboards, cards lift off the canvas:**

```toml
[theme]
primaryColor = "#1010EB"
backgroundColor = "#F5F5F5"           # page is Atmospheric White
secondaryBackgroundColor = "#FFFFFF"  # cards are white
textColor = "rgba(0,0,0,0.77)"
font = "sans-serif"
```

> **No `[theme.sidebar]` block by default.** A colored sidebar is a *chosen* combination, never a
> default — an earlier revision of this file shipped a navy sidebar as the default config, which is
> the direct source of the generic blue-sidebar-plus-white-content output this skill is meant to
> avoid. It also set the sidebar `primaryColor` to Light Blue `#0FC9F7`, which breaks the
> one-accent-per-screen lock: Light Blue is a **data-visualization** color, never UI chrome.
>
> If the user explicitly chose a navy sidebar, add it deliberately and keep the accent Electric Blue:
>
> ```toml
> [theme.sidebar]
> primaryColor = "#1010EB"              # Electric Blue - the one accent, not Light Blue
> backgroundColor = "#140F4B"           # Navy
> secondaryBackgroundColor = "#170F5F"
> textColor = "#FFFFFF"
> ```
>
> For brand presence in a shell **without** a colored sidebar, use the **Navy Header Light** preset
> instead — it puts the navy in the 64px header and leaves nav and content light.

> **The `font = "sans-serif"` above is the fallback, not the target.** Streamlit's `font` key accepts
> a generic family name or CSS font stack, not a font file. This skill bundles the real licensed
> webfont files at `assets/fonts/avenir-next-world/*.ttf`, so the correct sequence is:
>
> 1. Copy the `.ttf` files into the project's `static/` folder and set
>    `[server] enableStaticServing = true`.
> 2. Load `@font-face` declarations for `AvenirNextWorld`, `-Bold`, `-Demi`, and `-Italic` via a
>    single `st.markdown(..., unsafe_allow_html=True)` at the top of the entrypoint page — mirror the
>    real declarations in `mdt-variables.css` (it includes `-Bold`). Headings use
>    `AvenirNextWorld-Bold`.
> 3. **Then change `font` to `"Avenir Next World"`** in every `config.toml` block above.
>
> Only leave `font = "sans-serif"` if the project genuinely can't self-host — and in that case tell
> the user the real brand font isn't available in-browser. Bold survives a fallback face well, so
> `font-weight: 700` on headings **is** acceptable when the real font is missing — see the
> fallback caveat in [typography.md](./typography.md).

### Full dark mode instead (see `theme-presets.md`)

If the whole app (not just the sidebar) should be dark, use one of these instead of the light one
above — don't mix light `[theme]` with a dark sidebar and call it "dark mode".

**App Dark Mode (product UI, official tokens — use this for a normal app dark-mode toggle):**

```toml
[theme]
primaryColor = "#4A7DFF"          # General.Interface.Action - official dark-mode token
backgroundColor = "#121212"        # General.Surface.level 0
secondaryBackgroundColor = "#1E1E1E"  # General.Surface.level 1
textColor = "rgba(255,255,255,0.9)"
font = "sans-serif"
```

**Navy Dark (marketing/brand surfaces only, e.g. a promotional landing page — not general app
dark mode):**

```toml
[theme]
primaryColor = "#1010EB"          # exact Electric Blue token, unmodified - see theme-presets.md
backgroundColor = "#140F4B"       # Navy
secondaryBackgroundColor = "rgba(255,255,255,0.06)"
textColor = "#FFFFFF"
font = "sans-serif"
```

**Caveat:** `config.toml` is read once at startup — Streamlit can't hot-swap between the light and
dark config at runtime from within the app. For a genuine in-app light/dark **toggle** (not just a
fixed dark deployment), keep the light `config.toml` as the base and inject an override stylesheet
conditioned on `st.session_state` when the user flips the toggle, e.g. wrap the dark CSS variables
from `theme-presets.md` in a `st.markdown(..., unsafe_allow_html=True)` block that only renders
when `st.session_state.dark_mode` is `True`. Don't try to rewrite `config.toml` from Python at
runtime.

## 2. Logo

Use `st.logo()` (native, appears top-left of the sidebar/header — matches the brand's preferred
top-left logo placement) rather than hand-positioning an `st.image` with CSS. Use the
`navy-digital` (`#170F5F`) variant, not the standard `medtronic-logo-navy.svg` (`#140F4B`) — the
UI Design System warns the standard fill reads as near-black on some screens:

```python
st.set_page_config(page_icon="assets/brand/favicon.ico")  # real browser-tab favicon

st.logo(
    "assets/brand/logos/wordmark/medtronic-logo-navy-digital.svg",
    icon_image="assets/brand/symbol/symbol-electric-blue.svg",  # collapsed-sidebar mark
)
```

Copy the specific files you need from this skill's `assets/` into the app's own `assets/brand/`
folder first. Use the white wordmark variant instead if the header/sidebar background is dark
navy (per [brand-guidelines.md](../references/brand-guidelines.md) contrast rules). `st.logo()`
sizes the image itself (fixed internal height, ~32px) — if you need the "hero" scale from
[sizing-standard.md](./sizing-standard.md) (e.g. 60px+ for a landing page), render it with
`st.image(..., width=...)` instead and compute the width from `medtronic-logo-navy-digital.svg`'s
real **6.091:1** ratio (not the plain wordmark's 2.741:1) rather than guessing a width that
stretches it.

## 3. Buttons

Native `st.button` is rectangular with soft corners; the brand's pill-shaped button is one of the
few things worth a small global CSS override:

```python
st.markdown("""
<style>
.stButton > button, .stFormSubmitButton > button {
    border-radius: 999px !important;
}
button[kind="primary"] {
    background-color: #1010EB !important;
    border-color: #1010EB !important;
}
</style>
""", unsafe_allow_html=True)
```

Use `type="primary"` for the main call-to-action button on a page/form, `type="secondary"` (or
`type="tertiary"` for a ghost/borderless look) for everything else — don't hand-style every button
individually.

## 4. Icons

**`[MANDATORY]` Carbon is the default icon system — use it without being asked.** See
[carbon-design-system.md](./carbon-design-system.md). Carbon SVGs use `fill="currentColor"`, so a
single file works on light and dark backgrounds — no `-white` variant to pair, no background-mismatch
bug. Resolve names via `catalog/icons-manifest.json`; never guess a filename.

Streamlit's built-in `:material/icon_name:` shortcodes do **not** match the Medtronic/Carbon visual
language — for a brand-accurate UI, render SVGs directly wherever you control the markup:

```python
from pathlib import Path
import streamlit as st

CARBON = Path("assets/brand/icons/carbon")  # copied from assets/third-party/.../assets/icons/

def icon(name: str, size: int = 20, color: str = "rgba(0,0,0,0.77)"):
    """Carbon icons are square on a 32x32 viewBox - width and height are both safe."""
    svg = (CARBON / f"{name}.svg").read_text()
    svg = svg.replace("<svg", f'<svg width="{size}" height="{size}"', 1)
    st.markdown(
        f'<span style="color:{color};display:inline-flex;vertical-align:middle">{svg}</span>',
        unsafe_allow_html=True,
    )

icon("dashboard")                          # inherits body text color
icon("arrow--right", color="#1010EB")      # interactive only - one accent per screen
icon("warning--alt", color="#B56409")      # semantic token, light mode
```

`color` is the only thing that changes between light and dark mode — pass the active mode's text
token. Do not maintain two icon folders.

**Medtronic thematic icons `[FLEXIBLE]`** remain the better choice for brand/editorial moments
(marketing feature rows, value-prop blocks). Those have **varying aspect ratios** — set height only:

```python
def thematic_icon(name: str, size: int = 24, dark_bg: bool = False):
    family = "thematic-white" if dark_bg else "thematic"
    svg = Path(f"assets/brand/icons/{family}/{name}.svg").read_text()
    # height only - thematic ratios vary per icon, forcing width stretches them
    st.markdown(svg.replace("<svg", f'<svg height="{size}" width="auto"', 1),
                unsafe_allow_html=True)
```

Don't mix Carbon and Medtronic functional icons in the same UI region.

For widget-icon slots that only accept an emoji or `:material/...:` shortcode (`st.metric(icon=)`,
`st.button(icon=)`), pick the closest Material icon rather than fighting the API, and reserve real
SVGs for places you render freely with `st.markdown`.

## 5. Data viz colors

For `st.bar_chart` / `st.line_chart` / Altair/Plotly charts, pass an explicit brand color
sequence instead of the default palette — per `ui-design-system-colors.md`'s Do's/Don'ts, a
**multi-series chart leads with Navy Blue, not Electric Blue** (Electric Blue is reserved for
single-data-point charts), then continues in the documented preferred order:

```python
BRAND_CHART_COLORS = ["#140F4B", "#1010EB", "#0FC9F7", "#E5057F", "#FFAD00"]
# Navy, Electric Blue, Light Blue, Pink, Orange - leads with Navy per the
# corrected multi-series rule (was previously #1010EB-first; logged in
# SKILL.md's Contradiction Ledger).
```

## 6. Building beyond tokens/logo/buttons/icons

Streamlit's native widgets already cover most of the components documented elsewhere in this
skill — map the reference to the native widget rather than hand-rolling HTML/CSS:

| Need | Reference | Native Streamlit widget |
| --- | --- | --- |
| **Page shell, grid, alignment, spacing** | **[streamlit-layout.md](./streamlit-layout.md)** | `st.set_page_config`, `st.columns(gap=, vertical_alignment=)`, `st.container(border=, height=)` |
| Breakpoints, archetype choice | [composition.md](./composition.md), [design-intuition.md](./design-intuition.md) | `layout="wide"` vs `"centered"` |
| Nav, breadcrumbs, tabs | [navigation.md](./navigation.md) | `st.navigation` + `st.Page`, `st.tabs` |
| Badges, flags, key-value pairs, avatars | [ui-components.md](./ui-components.md) | `st.badge`, inline `:color-badge[]`, `st.metric` |
| Text fields, selects, checkboxes, toggles, sliders | [forms-and-inputs.md](./forms-and-inputs.md) | `st.text_input`, `st.selectbox`, `st.checkbox`, `st.toggle`, `st.slider` |
| Modals, spinners, tooltips | [overlays-and-feedback.md](./overlays-and-feedback.md) | `st.dialog`, `st.spinner`, `help=` param on most widgets |

**Where the native widget genuinely can't match the spec** — be honest about the gap rather than
claiming coverage:

| Spec | Gap |
| --- | --- |
| `ui-components.md` badge: 99+ overflow, 24×24, 2px top-right offset | `st.badge` has no overflow or offset control |
| `overlays-and-feedback.md` modal: size tiers + 3-layer shadow | `st.dialog` offers `width` only, no shadow control |
| `navigation.md` tabs: filled-vs-outline 56px variants | `st.tabs` has one visual style |
| `composition.md` exact 8px padding | Container padding is fixed — see the spacing table in `streamlit-layout.md` |

For these, use the native widget and accept the approximation, or state plainly that exact fidelity
needs React. **Don't inject CSS against Streamlit's internal class names** — they aren't a public API
and break on upgrade.

Only reach for custom CSS/HTML when a native widget genuinely can't do it — see the
developing-with-streamlit skill's own "native theming first" principle, cited in `theme-presets.md`.

## 7. What NOT to do

- Don't use `:rainbow[...]` or default Streamlit theme colors for a Medtronic-branded app.
- Don't build a custom card/KPI component when `st.metric(..., border=True)` + brand colors will
  do — see the general Streamlit theming principle above.
- Don't skip `st.logo()` in favor of manually placed `st.image` + CSS unless there's a concrete
  reason native placement doesn't work.
