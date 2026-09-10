# Code snippet – Carbon Design System

Source: https://www.carbondesignsystem.com/components/code-snippet/style/

# Code snippet

## Color

### Single line

| Element | Property | Color token |

| --- | --- | --- |

| Container | background | $layer * |

| Code | text color | $text-primary |

| Copy button | See ghost button - icon only |  |

| Container:focus | border | $focus |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

Enabled, focus, hover, and active states

### Multi-line

| Element | Property | Color token |

| --- | --- | --- |

| Container | background | $layer * |

| Code | text color | $text-primary |

| Icon | svg | $icon-primary |

| Copy button Snippet button | See ghost button - icon only |  |

| Container:focus | border | $focus |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

States for copy button: active, enabled, hover, focus, disabled

States for show toggle: enabled, hover, focus

### Inline snippet

| Element | Property | Color token |

| --- | --- | --- |

| Container | background-color | $layer * |

| Code | text color | $text-primary |

| Container:hover | background-color | $layer-hover * |

| Container:focus | focus | $focus |

| Container:active | background-color | $layer-active * |

* Denotes a contextual color token that will change values based on the layer
it is placed on.

States for inline codesnippet: enabled, hover, active, focus

### Syntax colors

Carbon has defined a set of accessible syntax colors. View an incontext
[example](https://codepen.io/team/carbon/full/eKMBLw/) on CodePen.

## Typography

| Element | Font-size (px/rem) | Font-weight | Type token |

| --- | --- | --- | --- |

| Code text | 12 / 0.75 | Regular / 400 | $code-01 |

## Structure

### Single line

| Element | Property | px / rem | Spacing token |

| --- | --- | --- | --- |

| Container | height | 40 / 3 | – |

|  | max-width | 768 / 48 | – |

|  | padding-right | 48 / 3 | $spacing-09 |

|  | padding-left | 16 / 1 | $spacing-05 |

Structure and spacing measurements for code snippet | px / rem

### Multi-line code snippet

| Element | Property | px / rem | Spacing token |

| --- | --- | --- | --- |

| Container | min-height | 288 / 18 | – |

|  | max-height | Varies based on content | – |

|  | max-width | 768 / 48 | – |

|  | padding | 16 / 1 | $spacing-05 |

|  | padding-right | 40 / 2.5 | $spacing-08 |

| Icon | height, width | 16px | – |

| Snippet button | height, width | 40 / 2.5 | – |

| Copy button | height, width | 32 / 2 | – |

Structure and spacing measurements for multi-line snippet | px / rem

### Inline code snippet

| Element | Property | px / rem | Spacing token |

| --- | --- | --- | --- |

| Container | height | 16 / 1 | – |

|  | width | Varies based on content | – |

|  | border-radius | 2 | - |

| Code | padding-right, padding-left | 8 / 0.5 | $spacing-03 |

Structure and spacing measurements for inline code snippet | px / rem