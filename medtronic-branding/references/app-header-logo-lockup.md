# App header logo lockup (Digital Design System)

**Source:** Medtronic's internal UI Design System (Zeroheight, "Logo" page) — handed to this
skill directly by a user with authenticated access. This is the **product/app UI-specific**
logo guidance (header bars, favicons, app-name lockups), complementing — and in one important
place, correcting — the Brand Central identity rules in `brand-guidelines.md`.

## Critical correction: logo color for on-screen headers

**Use Navy Blue Text color `#170F5F`** for the Medtronic logo in an app/website header —
**not** `#140F4B` (the standard Navy fill used elsewhere in this skill's bundled
`medtronic-logo-navy.svg`). Per the UI Design System's own Do/Don't guidance:

- **Do**: use `#170F5F` for the on-screen logo.
- **Don't**: use `#140F4B` fill for the logo — "it comes across some screens as black, or
  near-black."
- **Don't**: ever use Electric Blue `#1010EB` for the logo itself.

A new asset matching this exact requirement is bundled at
[`assets/logos/wordmark/medtronic-logo-navy-digital.svg`](../assets/logos/wordmark/medtronic-logo-navy-digital.svg)
(confirmed `fill:#170F5F` in the file itself) — **use this one for app/website header logos**,
not `medtronic-logo-navy.svg` (`#140F4B`, still correct for print/marketing/Brand-Central
contexts per the original guidelines).

## Logo placement

- **Primary/header logo**: top header bar, navy digital text color `#170F5F` — the SVG above.
- **Optional footer logo**: on a navy-blue footer background, use the logo **+ tagline**
  lockup, white text. A reference preview image was provided for this
  (`assets/logos/wordmark/uidesignsystem-footer-logo-reference.png`), but its actual pixel
  content shows navy text, not white — **this looks like a caption/asset mismatch on the source
  page**, not a confirmed white-on-navy asset. Don't treat that PNG as verified white-text
  artwork; use the already-bundled, confirmed `assets/logos/tagline-lockup-horizontal/medtronic-logo-tagline-white.svg`
  for an actual white-on-navy footer lockup instead, and flag the mismatch if the source page is
  ever revisited.

## Favicon

Medtronic's live public favicon (fetched directly from `medtronic.com`, not a Zeroheight upload)
is bundled at [`assets/favicon/favicon.ico`](../assets/favicon/favicon.ico) — a white "M" mark on
an Electric Blue `#1010EB` square, simpler than the Symbol-based `social-favicon-mark` bundled
elsewhere in this skill. **Prefer this one for real app favicons** — it's what Medtronic's own
production site currently uses. The Symbol-based `social-favicon-mark` remains the documented
choice specifically for social-media profile images per Brand Central (see
`brand-guidelines.md`); use `favicon.ico` for actual `<link rel="icon">` / browser-tab favicons.

## Logo + application name lockup

Two documented layout patterns for pairing the Medtronic logo with an app's own name in a header:

**Inline (desktop):** Medtronic logo, then a divider pipe `|`, then the application name.

- The application name sits on the same text baseline as the Medtronic logo.
- The application name's cap height is sized to match the height of the lowercase "c" in the
  Medtronic wordmark (not the full logo height) — a specific, exact alignment rule, not a rough
  visual match.
- Application name: standard black text.
- Divider pipe: low-emphasis black (light gray), not full-strength black.
- **Don't** use navy-blue-colored or thin-weight fonts for the application name. `[MANDATORY]`
  **Scope: this rule governs the inline horizontal desktop lockup only** (logo | App Name on one
  baseline). It does **not** govern page headings — `h1`–`h3` are **Bold** per `typography.md`, and
  that is not a conflict. It also does not govern the mobile stacked lockup below, which has its own
  explicit spec.
- **Don't** pair the logo+tagline lockup together with an application name in the same header —
  pick one or the other, not both (avoids two competing brand statements in one header).

**Mobile stacked:** Medtronic logo stacked above the application name.

- Medtronic logo: **15px tall** in this stacked/mobile arrangement — an exact, documented pixel
  value (contrast with `sizing-standard.md`'s own Compact-tier range of 24–32px, which is this
  skill's own engineering recommendation for a *generic* header logo; 15px is Medtronic's own
  specific spec for this *particular* stacked mobile lockup pattern — don't average the two or
  treat them as interchangeable).
- Application name: set in "Text 5-Heading Thin" (a named type style from Medtronic's UI
  typography scale — resolved: this is `.txt05-headline` in `typography.md`, 24px/27.6px,
  `--mdtTextPrimary` `#170F5F`. **Note the weight is now Bold, not Thin** — see the headline-weight
  resolution in `typography.md`; the Medtronic style *name* still contains "Thin" but the style
  renders Bold).

> **`[MANDATORY]` Resolving the apparent conflict between the two arrangements above.** The inline
> desktop rule forbids thin + navy app names; the mobile stacked rule specifies a style that is both
> thin *and* navy. Both are correct — they are **different, non-interchangeable arrangements**, and
> Medtronic specifies them differently on purpose:
>
> | Arrangement | App name style |
> | --- | --- |
> | Inline horizontal (desktop): `logo \| App Name` | Standard black, **not** bold-headline styled, **not** navy |
> | Stacked (mobile): logo above app name | `.txt05-headline` — Bold, 24px, navy `#170F5F` |
>
> Pick the arrangement first, then take that row's style. Never blend them, and never apply the
> desktop prohibition to the stacked lockup or vice versa. Logged in `SKILL.md`'s Contradiction
> Ledger.

## Logo combination hierarchy

The UI Design System reiterates Brand Central's three-level brand hierarchy (wordmark; tagline
and/or Symbol; product/initiative/department/region names) and the same general composition
principles already covered in `brand-guidelines.md` (clear space, relative sizing to avoid
competing elements, legibility) — no new numeric specs beyond what's captured above were
extractable from the diagrams provided. For the full visual reference, Brand Central's
downloadable logo assets remain the canonical source (see `brand-guidelines.md` and
`asset-manifest.md`).
