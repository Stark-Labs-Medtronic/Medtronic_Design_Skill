# Accessibility (Digital Design System)

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide, "Accessibility" page) —
handed to this skill directly by a user with authenticated access, pasted verbatim as data.
Applies to all digital product UI (React/Streamlit/web apps), not marketing/print collateral.

## Color and contrast

All text/icon-vs-background color pairings should meet **APCA** (Accessible Perceptual Contrast
Algorithm) standards, not the older WCAG 2.x contrast-ratio formula. Reference:
[github.com/Myndex/SAPC-APCA](https://github.com/Myndex/SAPC-APCA/tree/master/documentation).
When picking colors from `ui-design-system-colors.md` / `dark-mode-ui-colors.md`, use the
provided `Text & Icon.*` opacity tokens as-is rather than substituting an arbitrary similar color
— they were chosen to hold up under APCA.

## Text scaling

Components must support font-size scaling up to **200%** without breaking usability:

- Text areas scale **vertically** as type scales, pushing surrounding content down (don't clip or
  truncate).
- Spacing *between* text elements stays fixed as text scales — only the text itself grows.

## Touch targets

| Element type | Minimum size | Rule |
| --- | --- | --- |
| Essential interactive elements (primary CTAs, required-field inputs) | **48×48px** | Hard minimum — don't go smaller |
| Non-essential interactive elements | May be visually/hit-box smaller | Must still keep **32×32px** of unshared spacing between any two adjacent elements |
| Small icon buttons (e.g. 24×24px) | Visual/hit-box size can be smaller than the minimums above | Only acceptable if the element has a **4px margin on all sides**, effectively restoring a 32×32px total footprint |

This is the authoritative Medtronic spec for touch-target sizing in product UI — it supersedes
the generic WCAG/Apple/Google-sourced tiers in `layout-and-spacing.md` §2 for anything built to
this Design System (that file's 40/44/48px tiers remain valid as general industry cross-reference,
but 48×48px is the Medtronic-specific hard minimum for essential elements).
