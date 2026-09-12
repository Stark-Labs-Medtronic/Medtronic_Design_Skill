# Streamlit layout, alignment, and page structure

`streamlit-integration.md` covers **theming** (colors, fonts, logo, buttons, icons). This file covers
**structure** — page shell, columns, alignment, spacing, and the rules that keep a Streamlit app from
looking like stacked widgets with no layout.

**This file is authoritative for Streamlit layout `[MANDATORY]`.** Where `streamlit-integration.md`
gestures at layout, defer here.

## Why this file exists

Streamlit renders top-to-bottom in a single flow. Nothing enforces alignment, so the default outcome
is a vertical stack of full-width widgets with inconsistent gaps and labels that don't share a
baseline. Medtronic's own `composition.md` grid assumes CSS you don't control here. The rules below
translate that grid into Streamlit primitives.

## 1. Page shell `[MANDATORY]`

Every app starts with `st.set_page_config` as the **first Streamlit call in the entrypoint**, before
any other `st.*` call, or Streamlit raises `StreamlitAPIException`.

```python
import streamlit as st

st.set_page_config(
    page_title="App Name | Medtronic",   # brand last, matches title-bar convention
    page_icon="assets/brand/favicon.ico",
    layout="wide",                        # see the decision rule below
    initial_sidebar_state="expanded",
)
```

### `layout` — choose deliberately `[ASK]` via the archetype question

| Archetype (from `design-intuition.md`) | `layout` | Sidebar |
| --- | --- | --- |
| Product dashboard / tile-bento | `"wide"` | Optional — only if there is real navigation |
| Clinical / data-dense tool | `"wide"` | `"expanded"` |
| Marketing / hero-led landing page | `"centered"` | None — `st.set_page_config(initial_sidebar_state="collapsed")` |
| Form-led tool, single task | `"centered"` | None |
| Reading/report surface | `"centered"` | None |

**`layout="wide"` is not a default.** A form or a landing page in wide mode produces a 1400px-wide
text column that nothing anchors — that is one of the specific generic-AI tells. Centered mode gives
a ~730px content column, which is close to a comfortable reading measure.

### Sidebar `[MANDATORY]`

**A sidebar requires a reason.** Add one only when there is genuine persistent navigation, global
filters, or a mode switch. An app with three pages does not need a sidebar; `st.tabs` or
`st.navigation` is the better fit.

**Never add a colored sidebar as decoration.** See the anti-pattern rule in `theme-presets.md` — a
navy sidebar next to a white content area is a *chosen* combination, never a default.

### The 64px header

`global-header.md` mandates a 64px header on every platform. Streamlit has no native header slot, so
build it as the first element and size the logo per `sizing-standard.md` §0:

```python
def brand_header(app_name: str):
    with st.container(border=False):
        left, right = st.columns([3, 1], vertical_alignment="center")
        with left:
            # 28px logo: shares the row with other content -> Compact tier
            st.markdown(
                '<div style="display:flex;align-items:center;gap:16px;height:64px">'
                '<img src="app/static/medtronic-logo-navy-digital.svg" style="height:28px">'
                '<span style="color:rgba(0,0,0,0.30)">|</span>'
                f'<span style="font-size:20px;color:rgba(0,0,0,0.9)">{app_name}</span>'
                "</div>",
                unsafe_allow_html=True,
            )
        with right:
            st.markdown('<div style="height:64px"></div>', unsafe_allow_html=True)
    st.divider()
```

Note the app name is **standard near-black, not navy and not thin** — that is the inline desktop
lockup rule from `app-header-logo-lockup.md`. Serve static files from `static/` with
`[server] enableStaticServing = true` in `config.toml`.

## 2. Columns `[MANDATORY]`

### `vertical_alignment` is required on any mixed-height row

This is the single largest source of misaligned Streamlit UI. Widgets have different intrinsic
heights — a `st.text_input` carries a label above it, `st.button` does not — so an unaligned row
puts a button's top edge against an input's label.

```python
# WRONG - button floats to the top, input sits below its label
c1, c2 = st.columns([3, 1])
c1.text_input("Search")
c2.button("Go")

# CORRECT - bottom-aligns the control with the input it belongs to
c1, c2 = st.columns([3, 1], vertical_alignment="bottom")
c1.text_input("Search")
c2.button("Go")
```

| Row content | `vertical_alignment` |
| --- | --- |
| Labeled input + button/submit | `"bottom"` |
| Metrics, KPI cards, equal-height tiles | `"center"` |
| Icon + text label pairs | `"center"` |
| Text blocks of differing length | `"top"` |
| Chart beside a caption or legend | `"center"` |

Default is `"top"`; state it explicitly anyway so the intent is visible.

### `gap` maps onto the 8px grid

Streamlit exposes named gaps, not pixel values. Use this mapping and don't fight it with CSS:

| `gap` | Approx. | Medtronic token | Use |
| --- | --- | --- | --- |
| `"small"` | 16px | `$spacing-s` | Tightly related cells — icon + label, metric clusters |
| `"medium"` | 24px | `$spacing-m` | Default for tile grids and card rows |
| `"large"` | 32px | `$spacing-l` | Major section separation, hero blocks |
| `None` | 0 | `$spacing-none` | Segmented controls, joined cells only |

```python
cols = st.columns(3, gap="medium", vertical_alignment="center")
```

### Ratio discipline

- **Use whole-number ratios** that read as intentional: `[1, 1, 1]`, `[2, 1]`, `[3, 1]`, `[1, 2, 1]`.
  Avoid `[0.7, 1.3, 1.1]` — arbitrary fractions are a generic-AI tell.
- **A single-column row is not a row.** `st.columns(1)` adds nothing; write the content directly.
- **Never nest columns more than one level deep.** Streamlit's nesting is fragile and produces
  unpredictable widths. If you need a third level, the layout is wrong — use a container or a tab.
- **Keep column counts consistent down the page.** A 3-col row followed by a 4-col row followed by a
  2-col row reads as arbitrary. Pick a base count and subdivide it: 4 → 2+2, 4 → 1+3.
- **Reserve the ratio for the content**, not the widget. A chart beside a filter panel is `[3, 1]`
  because the chart deserves the space, not because 3 and 1 look nice.

### Orphan cells

If content count doesn't divide evenly by column count, do **not** leave a trailing empty column —
it reads as a rendering bug. Either change the column count to divide evenly, or fill the remainder
deliberately (a summary tile, a call-to-action, an empty-state message). This mirrors
`design-intuition.md`'s tile-rhythm rule that cell count matches content count.

## 3. Containers `[MANDATORY]`

`st.container(border=True)` is **the** card primitive. Don't hand-roll a card div.

```python
with st.container(border=True):
    st.markdown("##### Section title")
    st.caption("Supporting context")
    st.line_chart(df)
```

- `border=True` renders a 1px border matching the theme's border token — this is the
  `theme-presets.md` card surface. Don't inject CSS to restyle it.
- **Fixed `height=` for tile-grid rhythm.** Cards in the same row must share a height, or the row
  ragged-bottoms. `design-intuition.md` requires every tile in a grid to derive from the same
  base unit.

```python
KPI_H = 160  # every tile in this grid shares one base height
for col, kpi in zip(st.columns(4, gap="medium"), kpis):
    with col.container(border=True, height=KPI_H):
        st.metric(kpi.label, kpi.value, kpi.delta)
```

- `st.container(horizontal=True)` lays children out in a row — good for button groups and chip rows,
  and it respects `gap`. Prefer it over `st.columns` when cells should size to content rather than
  to a ratio.
- **Don't use `st.expander` to hide primary content.** It's for genuinely secondary detail.

## 4. Spacing translation table

Medtronic's 8px grid has no direct Streamlit expression. This is the honest mapping — where no
mechanism exists, that is stated rather than papered over:

| Intent | Medtronic token | Streamlit mechanism |
| --- | --- | --- |
| Gap between columns | `$spacing-s`/`-m`/`-l` | `gap="small"/"medium"/"large"` |
| Gap between stacked blocks | `$spacing-m` (24px) | Implicit — Streamlit's own block margin, ~1rem. Not settable |
| Section separation | `$spacing-l` (32px) | `st.divider()`, or a spacer container |
| Card inner padding | 24–40px | Fixed by `st.container(border=True)`. **Not settable** without CSS |
| Explicit vertical space | any | `st.container(height=N, border=False)` as a spacer |
| Page L/R margin | 64px desktop (`composition.md`) | Fixed by `layout`. **Not settable** natively |

**Where the mechanism is "not settable", accept it.** Injecting CSS to force exact padding onto
Streamlit's internal classes breaks on every Streamlit upgrade, because those class names are not a
public API. The theme's own spacing is close enough to the 8px grid to be brand-acceptable.

If a project genuinely requires exact `composition.md` spacing, say so explicitly and recommend
React (`react-integration.md`) rather than fighting Streamlit's DOM.

## 5. Multi-page structure

Use `st.navigation` + `st.Page` (not the legacy `pages/` directory) so the nav is declared in code
and can carry Carbon icons:

```python
pages = [
    st.Page("views/overview.py", title="Overview", icon=":material/dashboard:", default=True),
    st.Page("views/patients.py", title="Patients", icon=":material/groups:"),
    st.Page("views/reports.py", title="Reports", icon=":material/description:"),
]
nav = st.navigation(pages, position="sidebar")  # or position="top"
nav.run()
```

`st.Page(icon=)` accepts only emoji or `:material/...:` shortcodes — a documented Streamlit API
limit, so Material is the correct fallback here. Use Carbon SVGs everywhere you control the markup.
`position="top"` matches the website-style shell archetype; `"sidebar"` matches web-app-style.

## 6. Charts

- Always pass the brand color sequence — see `streamlit-integration.md` §5.
- **`use_container_width=True`** on every chart, or charts in a column row render at different
  widths and break the grid.
- Set an explicit `height` on charts sharing a row, for the same reason cards need fixed heights.

## 7. Alignment pre-flight `[MANDATORY]`

Check every box before calling a Streamlit layout done. A failed box means fixing the layout, not
shipping with a caveat.

- [ ] `st.set_page_config` is the first Streamlit call, with `layout` chosen per archetype — not
      `"wide"` by reflex.
- [ ] The sidebar exists only if it holds real navigation, filters, or a mode switch.
- [ ] A colored sidebar, if present, was **chosen by the user**, not defaulted to.
- [ ] Every `st.columns` call passes an explicit `vertical_alignment`.
- [ ] Every row mixing labeled inputs with buttons uses `vertical_alignment="bottom"`.
- [ ] Every `st.columns` call passes an explicit `gap` from the 8px mapping.
- [ ] Column ratios are whole numbers and reflect content priority.
- [ ] No `st.columns(1)`, and no columns nested more than one level.
- [ ] No trailing empty column; content count divides evenly or the remainder is filled on purpose.
- [ ] Column counts down the page derive from one base count.
- [ ] Cards in the same row share an explicit `height`.
- [ ] Cards use `st.container(border=True)`, not hand-rolled HTML.
- [ ] Every chart sets `use_container_width=True`, plus explicit `height` when sharing a row.
- [ ] The header is 64px, with the logo at the `sizing-standard.md` §0 value for its context —
      **never a value taken from a spacing token.**
- [ ] The app name in an inline header lockup is near-black, not navy and not thin.
- [ ] No injected CSS targeting Streamlit's internal class names for spacing.
- [ ] Icons are Carbon, colored via `color`/`currentColor`, with Material only in widget-icon slots.
