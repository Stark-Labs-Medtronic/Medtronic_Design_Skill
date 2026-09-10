# Using this skill in a Streamlit project

Prefer native Streamlit theming (`.streamlit/config.toml`) over custom CSS wherever possible —
only reach for `unsafe_allow_html`/injected CSS for the handful of things native theming can't do
(pill-shaped buttons, the logo image, icon SVGs). This mirrors Streamlit's own guidance: don't
hand-roll what a theme key or built-in widget parameter already covers.

## 1. `.streamlit/config.toml`

```toml
[theme]
primaryColor = "#1010EB"          # Electric Blue - buttons, active widgets, links
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"  # Atmospheric White - cards, sidebar, widget bg
textColor = "#3C3C3C"             # Body Dark Gray
font = "sans-serif"               # Avenir Next World isn't web-safe; see note below

[theme.sidebar]
primaryColor = "#0FC9F7"
backgroundColor = "#140F4B"       # Navy - dark sidebar is an explicitly supported native combo
secondaryBackgroundColor = "#170F5F"
textColor = "#FFFFFF"
```

> Streamlit's `font` key only accepts a generic family name/CSS font stack, not arbitrary custom
> font files. This skill now bundles the real licensed webfont files at
> `assets/fonts/avenir-next-world/*.ttf` — copy them into the project's `static/` folder and load
> a single `@font-face` (pointing at the actual `.ttf` files, base64-encoded or served as a static
> asset) via `st.markdown(..., unsafe_allow_html=True)` at the top of the entrypoint page, then
> reference `"Avenir Next World"` in `font`. See [typography.md](./typography.md) for the exact
> type scale to replicate. If a project truly can't self-host the font, fall back to
> `font = "sans-serif"` and tell the user the real brand font isn't available in-browser.

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
`st.image(..., width=...)` instead and compute the width from the logo's real 2.741:1 ratio
rather than guessing a width that stretches it.

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

Streamlit's built-in `:material/icon_name:` shortcodes do **not** match the Medtronic icon set —
for a brand-accurate UI, render the bundled SVGs directly instead of Material icons. Pass the
right color family for the surface — `functional`/`thematic` (gray/blue) on light backgrounds,
`functional-white`/`thematic-white` on the Navy Dark preset or any colored background:

```python
from pathlib import Path
import streamlit as st

def brand_icon(name: str, family: str = "functional", size: int = 20):
    svg = Path(f"assets/brand/icons/{family}/{name}.svg").read_text()
    # functional icons are on a real fixed 24x24 grid (safe to force width+height equal).
    # thematic icons do NOT share one fixed ratio between icons - only constrain height,
    # or some icons will stretch more than others. See sizing-standard.md.
    if family.startswith("functional"):
        dims = f'width="{size}" height="{size}"'
    else:
        dims = f'height="{size}" width="auto"'
    st.markdown(
        svg.replace("<svg", f'<svg {dims}', 1),
        unsafe_allow_html=True,
    )

# light background
brand_icon("alarm_rgb", family="functional")
# dark / Navy background
brand_icon("alarm_rgb", family="functional-white")
```

For simple cases (e.g., inside `st.metric(icon=...)`, `st.button(icon=...)`) Streamlit only
accepts an emoji or `:material/...:` shortcode, not an arbitrary SVG — in those specific
widget-icon slots, pick the closest Material icon rather than fighting the API, and reserve the
real bundled SVGs for places you render freely with `st.markdown`.

## 5. Data viz colors

For `st.bar_chart` / `st.line_chart` / Altair/Plotly charts, pass an explicit brand color
sequence instead of the default palette — per the guidelines, lead with blues+gray, add one
accent family before mixing multiple accents:

```python
BRAND_CHART_COLORS = ["#1010EB", "#777777", "#0FC9F7", "#00DCB9", "#7ECA2A"]
```

## 6. Building beyond tokens/logo/buttons/icons

Streamlit's native widgets already cover most of the components documented elsewhere in this
skill — map the reference to the native widget rather than hand-rolling HTML/CSS:

| Need | Reference | Native Streamlit widget |
| --- | --- | --- |
| Page grid, breakpoints, shell choice | [composition.md](./composition.md) | `st.columns`, `st.container(horizontal=True)` |
| Nav, breadcrumbs, tabs | [navigation.md](./navigation.md) | `st.tabs`, `st.sidebar` + `st.button` nav |
| Badges, flags, key-value pairs, avatars | [ui-components.md](./ui-components.md) | `st.badge`, inline `:color-badge[]`, `st.metric` |
| Text fields, selects, checkboxes, toggles, sliders | [forms-and-inputs.md](./forms-and-inputs.md) | `st.text_input`, `st.selectbox`, `st.checkbox`, `st.toggle`, `st.slider` |
| Modals, spinners, tooltips | [overlays-and-feedback.md](./overlays-and-feedback.md) | `st.dialog`, `st.spinner`, `help=` param on most widgets |

Only reach for custom CSS/HTML when a native widget genuinely can't do it — see the
developing-with-streamlit skill's own "native theming first" principle, cited in `theme-presets.md`.

## 7. What NOT to do

- Don't use `:rainbow[...]` or default Streamlit theme colors for a Medtronic-branded app.
- Don't build a custom card/KPI component when `st.metric(..., border=True)` + brand colors will
  do — see the general Streamlit theming principle above.
- Don't skip `st.logo()` in favor of manually placed `st.image` + CSS unless there's a concrete
  reason native placement doesn't work.
