# Content & copy — words as design material

**Source:** general UX-writing and content-design practice, synthesized from published design skill
sets (`frontend-design`'s writing guidance, `frontend-ui-engineering`'s realistic-content rule).
**Not** Medtronic brand rules.

**Precedence:** Medtronic's own editorial rules win outright and are **not** repeated here — see
[brand-guidelines.md](./brand-guidelines.md)'s "Voice & editorial style" and "Trademarks and
copyright" sections for sentence-case headlines, active voice, acronym handling, American English,
and the legally-binding `™` placement and copyright-endnote rules. Apply those first; this file
covers the craft layer they don't reach.

**A documented gap to respect:** `brand-guidelines.md` records that Medtronic's **Brand voice /
brand messaging** guidance was not captured in the source documents. So don't invent a "Medtronic
tone of voice." Write clearly and follow the Style Guide defaults; if a task genuinely turns on
brand tone, say so and point at Brand Central rather than filling the gap.

## Why this file exists

Copy is the one part of a UI that AI output gives itself away on fastest, and the skill was silent
on it. Two distinct failures:

1. **Placeholder content hides real layout problems.** Lorem ipsum has uniform word lengths and no
   long strings, so it never wraps badly, never overflows a badge, never pushes a button to two
   lines. A layout validated on lorem ipsum is validated on a fiction.
2. **Generic copy makes a good layout read as a template.** "Welcome to your dashboard", "Manage
   your data efficiently", "Get Started" — these appear regardless of subject, which is exactly what
   makes them feel machine-made.

Words are design material. Bring the same intent to them as to spacing and color.

## 1. Never ship placeholder content

- **No lorem ipsum, ever** — not in a draft, not "temporarily." Write plausible real content for the
  actual subject: real metric names, real clinical or operational terms, real product names (spelled
  and trademarked per `brand-guidelines.md`).
- **Use realistic lengths, including the awkward ones.** Deliberately include at least one long
  string in every list, table, card grid, and nav — the longest realistic patient name, department,
  device model, or alert message. This is a *layout test*, and it belongs in the first build, not a
  later QA pass.
- **Use realistic quantities.** A table with 3 rows proves nothing. Check zero, one, many, and
  too-many for every collection — the Gate B states checklist in
  [design-review.md](./design-review.md) depends on it.
- **Realistic numbers too.** If a figure can be negative, four digits, or a percentage over 100,
  render one and see what it does to the column
  ([craft-details.md §5](./craft-details.md) — `tabular-nums`).

## 2. Name things from the user's side of the screen

Label by what the person controls and recognizes, never by how the system is built. Someone manages
*alerts*, not *notification webhook config*; they review *patients*, not *records in the patient
entity table*. Describe what something does in plain terms rather than selling it. Specific always
beats clever.

For a clinical or regulated surface this matters more than anywhere else: the vocabulary on screen
should be the vocabulary the clinician already uses in the ward, not internal engineering names and
not marketing language.

## 3. One label per action, held consistent through the flow

A control says exactly what happens when it's used: "Save changes", not "Submit". And the name
persists — the button that says "Publish" produces a toast that says "Published", and the history
entry says "Published", not "Content update succeeded".

This is the copy-level version of the rule already in
[design-intuition.md](./design-intuition.md) ("one CTA label per intent, per page"): don't mix
"Get started" / "Try it now" / "Sign up free" as if they were different actions. The interface's
vocabulary is its signposting; consistency is how people learn their way around it.

Buttons carry Demi-weight button styles (`.txt02-button` / `.txt03-button`,
[typography.md](./typography.md)), and **button text never wraps**. If a label needs two lines,
shorten the label — never shrink the documented padding to force the fit.

## 4. Empty, error, and loading states are copy problems as much as layout problems

[design-intuition.md](./design-intuition.md) requires these states exist. What they *say* decides
whether they're useful:

- **Empty state — an invitation to act.** Say what would be here, and give one clear next action.
  "No alerts in the last 24 hours" plus a primary action beats a bare "No data". Never leave an
  empty state as a lone string.
- **Error state — what happened and how to fix it.** Errors don't apologize, don't blame the user,
  and are never vague. "We couldn't reach the device. Check the connection and try again." not
  "An error occurred." Field-level errors sit directly below their field and are programmatically
  associated with it ([ux-accessibility-checklist.md](./ux-accessibility-checklist.md)).
- **Loading state — say what's loading** if it will take more than a moment. For streaming or
  agentic output, show partial results rather than a frozen spinner (already in
  `ux-accessibility-checklist.md`'s AI-interaction section).
- **Destructive confirmations name the consequence**, not just the verb: "Delete 3 saved reports?
  This can't be undone."

Write these in the interface's voice — steady and factual — not a person's.

## 5. Let each element do one job

A label labels; an example demonstrates; helper text helps. Nothing quietly does double duty. The
most common violation is using placeholder text as the label — which
[forms-and-inputs.md](./forms-and-inputs.md) already forbids on its own terms, and which also loses
the example the placeholder should have been carrying.

Keep the register plain: real verbs, sentence case (per `brand-guidelines.md`), no filler, no
exclamation marks in product UI. Cut any sentence that only exists to fill a space — if a section
needs a paragraph it doesn't have, the section may not need to exist.

## 6. Self-check

- [ ] No lorem ipsum or filler anywhere; all content is plausible for the real subject
- [ ] At least one deliberately long string per list/table/card grid/nav, and it doesn't break layout
- [ ] Zero / one / many / too-many cases exercised for every collection
- [ ] Labels name what the user controls, not how the system is built
- [ ] One label per action, identical across button, toast, and history
- [ ] No button label wraps to a second line
- [ ] Empty states offer a next action; errors state cause and fix; destructive confirmations name
      the consequence
- [ ] No placeholder-as-label anywhere
- [ ] Sentence case, active voice, acronyms expanded on first use (per `brand-guidelines.md`)
- [ ] Any Medtronic product name checked against the official trademark list, with `™` placed per
      `brand-guidelines.md`; copyright/trademark text sits in the footer endnote and was not invented
