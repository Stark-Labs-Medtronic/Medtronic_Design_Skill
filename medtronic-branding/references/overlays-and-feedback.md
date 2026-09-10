# Overlays and feedback

**Source:** Medtronic's internal UI Design System (Zeroheight styleguide) — handed to this skill
directly by a user with authenticated access, pasted verbatim as data. Covers "Modals and Sheets",
"Page Loading", "Progress Indicators", and "Tooltips" pages.

## Modals and sheets

Let users focus on something specific within the context of the current page — may require an
action before the user can proceed further.

### Modal dialogs

All three share: fill `#FFFFFF` (`General.Surface.level 0 elevated`), 1px inside border, **8px**
border radius, and this exact 3-layer drop shadow (distinct from the popover-menu shadow in
`navigation.md` — modals get a stronger, more pronounced elevation):

```css
box-shadow:
  0 1px 18px rgba(0, 0, 0, 0.12),
  0 6px 10px rgba(0, 0, 0, 0.14),
  0 3px 5px rgba(0, 0, 0, 0.2);
```

| Variant | Size (W×H) | Use for |
| --- | --- | --- |
| Simple | 420×204px | Important info the user must acknowledge/confirm/deny — 1–2 sentences max, optional simple imagery only |
| Standard | 600×590px | More complex, optionally-scrolling content; typically has multiple action buttons (e.g. Confirm + Cancel) |
| Critical | 484×336px | **Sparingly**, only for critical, non-undoable destructive actions — never for warnings or informational alerts. Prefer giving users an **undo** path over a critical destructive dialog wherever possible |

### Focus dimmer

`rgba(16, 16, 32, 0.6)` fill (`General.Overlay.Modal dimmer` token), sized to the full page
(1440×1024px reference). Applied on top of the entire page behind a modal or sheet to dim the
background and remove visual distractions — always pair a modal/sheet with this dimmer.

### Side and bottom sheets

| Variant | Size (W×H) | Border radius | Slides in from |
| --- | --- | --- | --- |
| Side sheet | 512×1024px (full viewport height) | 8px top-left/bottom-left only (flush on the right) | Right edge |
| Side sheet – transactional | 512×1024px | Same as above | Right edge |
| Bottom sheet | 1440×510px (full viewport width) | 8px top-left/top-right only (flush on the bottom) | Bottom edge |

Both use the same 3-layer drop shadow as modal dialogs above.

- **Side sheet** width is flexible by need — generally **30–90%** of viewport width; on mobile it
  can cover **100%** of the width.
- **Bottom sheet** should always take **100%** of viewport width.
- **On mobile, prefer bottom sheet over side sheet.**
- Both require a focus dimmer behind them, same as modal dialogs.

## Page loading

Show a page-loading indicator whenever a page takes **longer than 1 second** to load.

| Loader type | Size (W×H) | States |
| --- | --- | --- |
| Circular | 40×40px | In progress, Paused, Complete, Error |
| Linear (bar) | 300×25px | In progress, Complete, Paused, Error |

Reference CSS recipe for the circular spinner (simplified, unprefixed):

```css
.loader {
  width: 40px; height: 40px; border-radius: 50%;
  background: linear-gradient(to right, #1010EB 10%, rgba(16,16,235,0) 42%);
  animation: mdt-spin 1.4s infinite linear;
}
.loader::before {
  content: ""; position: absolute; top: 0; left: 0; width: 50%; height: 50%;
  background: #1010EB; border-radius: 100% 0 0 0;
}
.loader::after {
  content: ""; position: absolute; inset: 0; margin: auto;
  width: 75%; height: 75%; border-radius: 50%; background: #F5F5F5; /* matches page bg */
}
@keyframes mdt-spin { to { transform: rotate(360deg); } }
```

## Progress indicators

Communicate loading status or remaining time/actions for a specific **task** (as distinct from
page loading above, which is about the page itself). Only a single overview screenshot was given
in the source with no exact size/token data — treat this as effectively the same visual language
as the linear "Page loading" bar, applied to task-level progress instead of page-level.

## Tooltips

Anchored relative to the UI element that triggers them (hover or long-press) — can be positioned
above, below, or to either side of that anchor element.

- Reference tooltip bubble size: 99×40px, `border-radius: 4px`, fill `#FFFFFF`
  (`General.Surface.level 0`), 1px inside border.
- Multiple positional variants exist (top/bottom/left/right-pointing) at the same reference size —
  the source didn't distinguish them beyond the anchor-side positioning rule above.
