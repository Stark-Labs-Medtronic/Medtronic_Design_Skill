# Forms and inputs

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide) — handed to this skill
directly by a user with authenticated access, pasted verbatim as data. Covers "Inputs", "Slider",
and "Search" pages.

## Text fields and areas

Two label patterns — pick one deliberately:

- **Static label:** sits above the field at all times (default and focus look identical).
- **Dynamic label:** sits inside the empty field, animates to float above it on focus (ends up in
  the same position as a static label once focused/filled).

States: inactive, active (focused), filled, filled+disabled, disabled, error.

- **Compact text field:** no label at all — only use in a context where the field's purpose is
  already obvious (inline editing in a data table/list row, tight real estate). Don't use where
  the field would be ambiguous without a label.
- **Text area:** can be user-resizable (drag handle, bottom-right corner), auto-grow to fit
  content, or stay a fixed height with an internal scrollbar — pick per use case.
- **Autocomplete / typeahead:** as the user types, a filtered suggestion list appears below.
  - Don't return server-side-filtered results until **at least 3 characters** have been typed.
  - Debounce server-side requests **200ms** between keystrokes.
  - Limit displayed results to **7 max**.
  - (A different, less authoritative mention elsewhere on the same source page said "debounce by
    300ms" for autocomplete in general — the dedicated Auto Complete section's 200ms/3-char/7-max
    guidance above is the more specific, load-bearing spec; noted here rather than silently
    resolving the discrepancy.)

### Real reference CSS (from the source page's live demo)

```css
input, textarea, select {
  width: 100%;
  background: #fff;
  caret-color: #1010EB;
  border: 1px solid rgba(0, 0, 0, 0.3); /* --mdtBorderDefaultGray */
  border-radius: 4px;
  color: rgba(0, 0, 0, 0.9);            /* --mdtTextHigh */
  padding: 0 0.8rem;
  font-size: 1rem; /* 16px */
}
input, select {
  height: 40px;
}
/* textarea is deliberately excluded from the fixed height so it can grow —
   confirmed against the real mdt-components.css, which applies `height: 40px`
   to input/select only. Set an explicit min-height/rows per the Text area
   guidance above instead. This corrects an earlier version of this snippet
   that applied height: 40px to all three; logged in SKILL.md's Contradiction
   Ledger. */
label {
  display: block;
  font-size: 0.75rem; /* 12px */
  text-transform: uppercase;
  letter-spacing: 1px;
  color: rgba(0, 0, 0, 0.55);            /* --mdtTextLow */
}
label.required::before { content: "*"; color: #c121eb; } /* Important/purple, not red/Critical */
label.optional::after  { content: "optional"; font-style: italic; color: rgba(0,0,0,0.55); float: right; }
```

The source demo's CSS used a generic Google-fonts "Nunito" family with a `/* replace with
AvenirNextWorld */` comment — that's a live-preview-sandbox substitution artifact, not a real
brand exception. Use `"Avenir Next World"` per [typography.md](./typography.md) instead. Note the
**required-field asterisk uses the Important/purple semantic color** (`#C121EB`), not
Critical/red — a specific, easy-to-get-wrong detail.

## Select dropdowns

| Variant | Size (W×H) | Notes |
| --- | --- | --- |
| Empty / Selected / Error / Empty-disabled / Selected-disabled | 328×104px | Standard size |
| Active (list open) | 328×304px | |
| Compact | 240×32px, radius 4px, fill `#F5F5F5` | For data tables/lists with inline editing, same rationale as compact text fields |
| Compact active | 240×128px | |
| Compact disabled | 240×32px | |

A custom dropdown arrow (double-triangle, drawn via layered `linear-gradient`s in `#1010EB`) is
used instead of the native OS arrow — see the bundled
[assets/code-templates/html-css-framework/](../assets/code-templates/html-css-framework/) CSS for
the general form-control patterns this pairs with.

## Multi-select

Allows multiple simultaneous selections, should support typeahead filtering. Selected options
display as dismissible **chips**; deselect either by dismissing a chip directly or reopening the
multi-select list and unchecking the option there.

## Checkboxes and radios

- **Checkboxes:** multiple options may be selected at once.
- **Radios:** selections are mutually exclusive (pick exactly one).
- Both generally require an explicit **"Save"** action to commit the change (contrast with
  toggles, below, which apply immediately).
- Checkbox states: default, selected, hover, **partial/indeterminate** (use only when this is a
  parent checkbox and some—but not all—of its children are selected), disabled, selected-disabled,
  partial-disabled. Reference size: 116×40px (checkbox + label row).
- Radio states: default, selected, hover, disabled, selected-disabled. Reference size: 115×40px.
- **Do** use radios/checkboxes for in-form selections; **don't** use them for navigation or for
  changing overall system state (that's what toggles or buttons are for).
- **Do** show child options in a disabled state by default when their parent isn't selected.
- Reference HTML checkbox input is sized 24×24px with a 12px right margin before its label.

## Toggle switches

Enable/disable a feature or setting — applies **immediately**, no "Save" action needed (this is
the key behavioral difference from checkboxes/radios above). States: off, on, off-hover, on-hover,
off-disabled, on-disabled. Reference size: 126×40px.

- **Do** use toggles to turn a feature/functionality on or off within an app.
- **Don't** use a toggle as a substitute for a binary-choice radio button inside a form.

## Date picker

| Element | Size (W×H) | Notes |
| --- | --- | --- |
| Datepicker input (closed) | 318×104px | A separate general "Inputs sizes" mention gave 328×104px (Standard/Large) and 328×96px (Small) for what appears to be the same control — both values preserved as given, not reconciled |
| Datepicker active (calendar open) | 318×466px | Border radius 4px |
| Month picker view | 318×466px | Radius 4px |
| Year picker view | 318×466px | Radius 4px |
| Standalone calendar (no input wrapper) | 294×328px | For displaying a calendar directly on a page, not inside a datepicker field |
| Day-of-week header row | 394×32px | |

Calendar text styles: Month/Year label = Eyebrow text size (`.txt0N-eyebrow`, see
[typography.md](./typography.md)); days header = Text-3 Demi, low emphasis; calendar dates =
Text-3 Regular, black; chevron carats = reference icon size 24×24px.

## Number picker

For inputting a small numeric quantity (e.g. items in a cart) with increment/decrement controls
plus direct keyboard entry. Requires a default value. Reference size: 130×104px (inactive, active,
error, disabled states all the same footprint).

- **Do** use for values a user increments/decrements in small steps.
- **Don't** use when the acceptable range is large or users are likely to deviate far from the
  default.
- **Don't** use for numeric fields where incrementing has no real value (zip codes, IDs, order
  numbers) — those are plain text/number inputs, not number pickers.

## Slider

| Variant | Size (W×H) | Notes |
| --- | --- | --- |
| Standard (0%/50%/100% fill) | 354×44px | Same footprint at every fill level and for the handle overlay |
| Disabled (0%/50%/100%) | 354×44px | |
| Centered slider (bidirectional, e.g. -100..100) | 354×44px | Plus handle and disabled variants at the same size |
| Range-selection slider (two handles) | 354×44px | Plus handle and disabled variants (two separate disabled examples given, same size) |

354×44px is a reference-example width — sliders should stretch to fill their container, not be
hardcoded to that exact width.

## Search field

A specialized text input for search/filtering. Pill-shaped (`border-radius: 9999px`).

| State | Size (W×H) | Fill | Border |
| --- | --- | --- | --- |
| Default | 328×40px | `#FFFFFF` | `rgba(0,0,0,0.3)` |
| Active (typing) | 328×40px | `#F5F5F5` (Surface level 1) | `#1010EB` (Electric Blue) |
| Collapsed (icon-only) | 48×40px | `#FFFFFF` | `rgba(0,0,0,0.3)` |

- When active with typed text, a small **X** appears on the right to clear the term.
- **Collapsed** variant is a condensed icon-button form, common on mobile — tapping it expands the
  field (covering or pushing aside nearby components), matching the responsive search behavior
  already noted in [global-header.md](./global-header.md).
- **Three sizes exist** by context: Large (standalone on-page search — the 328×40px spec above),
  Medium (global headers / smaller screens), Small (toolbars for data-table/list search) — exact
  pixel sizes for Medium/Small weren't given in the source text.
- Used extensively inside the Global Header, Website header, and Application Shell components —
  confirms the search field's home is the header, per [global-header.md](./global-header.md).
