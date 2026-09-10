# Accordion – Carbon Design System

Source: https://www.carbondesignsystem.com/components/accordion/style/

# Accordion

## Color

| Element | Property | Color token |

| --- | --- | --- |

| Title | color | $text-primary |

| Content | color | $text-primary |

| Icon | fill | $icon-primary |

| Header | border-top | $border-subtle |

|  | background | Transparent |

| Panel | border-bottom | $border-subtle |

|  | background | Transparent |

### Interactive states

| Element | State | Property | Color token |

| --- | --- | --- | --- |

| Header | Hover | background | $layer-hover |

|  | Focus | border | $focus |

|  | Disabled | border-top | $border-subtle |

| Title | Disabled | background | $text-disabled |

| Icon | Disabled | fill | $icon-disabled |

- Default

- Flush

## Typography

All accordion titles are set in sentence case. See the accordion
[content guidelines](https://carbondesignsystem.com/components/accordion/usage#content) for more details.

| Element | Font-size (px/rem) | Font-weight | Type token |

| --- | --- | --- | --- |

| Title | 14 / 0.875 | Regular / 400 | $body-01 |

| Content | 14 / 0.875 | Regular / 400 | $body-01 |

## Structure

There is no max-height for an open panel but an accordion may
[scroll](https://carbondesignsystem.com/components/accordion/usage#scrolling-content) if constrained by
vertical space. The width of an accordion varies based on the content, layout,
and page design. The icon used in the header is a `chevron`. The accordion has
an indented default alignment but can also be set to have a flush alignment.

### Default alignment

| Element | Property | px/rem | Spacing token |

| --- | --- | --- | --- |

| Header | height | 40 / 2.5 | – |

| Item | border-top | 1 | – |

| Title | margin-left | 16 / 1 | $spacing-05 |

| Panel | padding-top | 8 / 0.5 | $spacing-03 |

|  | padding-bottom | 24 / 1.5 | $spacing-06 |

|  | padding-right | 25% | – |

|  | padding-left | 16 / 1 | $spacing-05 |

| Icon | size | 16 / 1 | – |

|  | padding-right | 16 / 1 | $spacing-05 |

Structure measurements for default accordion alignment. | px / rem

Spacing measurements for default accordion alignment. | px / rem

### Flush alignment

| Element | Property | px/rem | Spacing token |

| --- | --- | --- | --- |

| Header | height | 40 / 2.5 | – |

| Item | border-top | 1 | – |

| Title | margin-left | 0 | – |

| Panel | padding-top | 8 / 0.5 | $spacing-03 |

|  | padding-bottom | 24 / 1.5 | $spacing-06 |

|  | padding-right | 25% | – |

|  | padding-left | 0 | – |

| Icon | size | 16 / 1 | – |

|  | padding-right | 0 | – |

Structure measurements for flush accordion alignment. | px / rem

Spacing measurements for flush accordion alignment. | px / rem

### Margin right

Accordions have a variable right margin that changes based on its width.
Accordions that are 640px and wider have a `margin-right: 25%` with the
percentage being based off the width of the container it is placed in. At
smaller widths, the `margin-right` is a fixed size.

Body copy, including titles, in an accordion always follows the margin-right
rules. However, inputs and other components may still expand to the full width
of the accordion panel.

| Accordion width | Margin-right | Spacing token |

| --- | --- | --- |

| > 640 | 25% | – |

| 420-640px | 64px / 4rem | $spacing-10 |

| < 420 | 16px / 1rem | $spacing-05 |

## Sizes

| Element | Size | Height (px/rem) |

| --- | --- | --- |

| Header | Small (sm) | 32 / 2 |

|  | Medium (md) | 40 / 2.5 |

|  | Large (lg) | 48 / 3 |