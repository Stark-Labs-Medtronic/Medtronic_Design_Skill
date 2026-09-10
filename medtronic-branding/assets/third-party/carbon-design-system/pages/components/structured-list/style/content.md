# Structured list – Carbon Design System

Source: https://www.carbondesignsystem.com/components/structured-list/style/

# Structured list

The following page documents visual specifications such as color, typography,
structure, and size.

- [Color](https://carbondesignsystem.com/components/structured-list/style/#color)

- [Typography](https://carbondesignsystem.com/components/structured-list/style/#typography)

- [Structure](https://carbondesignsystem.com/components/structured-list/style/#structure)

- [Size](https://carbondesignsystem.com/components/structured-list/style/#size)

- [Feedback](https://carbondesignsystem.com/components/structured-list/style/#feedback)

## Color

Structured lists have a transparent background layer. Optionally, you can apply
a background color to a structured list. Structured lists with a background
color are only available in the hang alignment.

### Default color

| Element | Property | Color token |

| --- | --- | --- |

| Header | background-color | transparent |

| Header: text | text color | $text-primary |

| Row | background-color | transparent |

| Row: text | text color | $text-secondary |

| Divider | border-bottom | $border-subtle * |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

Default structured list color

### Selectable color

Selectable structured list has an available
[feature flag](https://carbondesignsystem.com/components/overview/feature-flags/).

| Element | Property | Color token |

| --- | --- | --- |

| Header | background-color | transparent |

| Header: text | text color | $text-primary |

| Row | background-color | transparent |

| Row: text | text color | $text-secondary |

| Divider | border-bottom | $border-subtle * |

| Icon | svg | $icon-primary |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

- Flag enabled

- Flag disabled

| State | Element | Property | Color token |

| --- | --- | --- | --- |

| Enabled (selected) | Row | background-color | $layer-selected * |

|  | Row: text | text color | $text-primary |

| Hover | Row | background-color | $layer-hover * |

|  | Row: text | text color | $text-primary |

| Hover (selected) | Row | background-color | $layer-selected-hover * |

|  | Row: text | text color | $text-primary |

| Focus | Row | border | $focus |

| Focus (selected) | Row | background-color | $layer-selected * |

|  | Row: text | text color | $text-primary |

|  | Border | border | $focus |

| Disabled |  |  |  |

|  | Row: text | text color | $text-disabled |

|  | Icon | svg | $icon-disabled |

| Disabled (selected) | Row | background-color | $layer-selected * |

|  | Row: text | text color | $text-disabled |

|  | Icon | svg | $icon-disabled |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

- Flag enabled

- Flag disabled

### With background color

| Element | Property | Color token |

| --- | --- | --- |

| Header | background-color | $layer * |

| Row | background-color | $layer * |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

- Flag enabled

- Flag disabled

- Flag enabled

- Flag disabled

## Typography

Structured list header and row text should use sentence-case capitalization. All
typography is left aligned.

| Element | Font-size (px/rem) | Font-weight | Type token |

| --- | --- | --- | --- |

| Header text | 14 / 0.875 | SemiBold / 600 | $heading-compact-01 |

| Row text | 14 / 0.875 | Regular / 400 | $body-01 |

## Structure

### Default structure

| Element | Property | px / rem | Spacing token |

| --- | --- | --- | --- |

| Container | min-width | 500 / 31.25 | – |

| Header: text | padding-top | 16 / 1 | $spacing-05 |

|  | padding-bottom | 8 / 0.5 | $spacing-03 |

|  | padding-right | 16 / 1 | $spacing-05 |

|  | padding-left (hang) | 16 / 1 | $spacing-05 |

|  | padding-left (flush) | 0px | – |

| Row: text | padding-top | 16 / 1 | $spacing-05 |

|  | padding-bottom | 24 / 1.5 | $spacing-06 |

|  | padding-right | 16 / 1 | $spacing-05 |

|  | padding-left (hang) | 16 / 1 | $spacing-05 |

|  | padding-left (flush) | 0px | – |

Spacing and measurements for default structured list with hang and flush
alignment | px / rem.

### Selectable structure

| Element | Property | px / rem | Spacing token |

| --- | --- | --- | --- |

| Container | min-width | 500 / 31.25 | – |

| Header: text | padding-top | 16 / 1 | $spacing-05 |

|  | padding-bottom | 8 / 0.5 | $spacing-03 |

|  | padding-right | 16 / 1 | $spacing-05 |

|  | padding-left, padding-right | 16 / 1 | $spacing-05 |

| Row: text | padding-top | 16 / 1 | $spacing-05 |

|  | padding-bottom | 24 / 1.5 | $spacing-06 |

|  | padding-left, padding-right | 16 / 1 | $spacing-05 |

| Icon | height, width | 16px | – |

|  | padding-left, padding-right | 16 / 1 | $spacing-05 |

Structure and spacing measurements for selectable structured list with a
feature flag | px / rem.

## Size

There are two structured list height sizes: **default** and **condensed**.

| Element | Size | Height (px/rem) |

| --- | --- | --- |

| Row | Default | 60 / 3.75 |

|  | Condensed | 36 / 2.25 |

Structured list sizes | px / rem

## Feedback

Help us improve this component by providing feedback, asking questions, and
leaving any other comments on
[GitHub](https://github.com/carbon-design-system/carbon-website/issues/new?assignees=&labels=feedback&template=feedback.md).