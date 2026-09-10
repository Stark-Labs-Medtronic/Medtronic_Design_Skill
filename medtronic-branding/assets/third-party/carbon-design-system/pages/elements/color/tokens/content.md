# Color – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/color/tokens/

# Color

Tokens are a method of applying color in a consistent, reusable, and scalable
way. They are used in place of hard coded values, like hex codes.

- [Core Tokens](https://carbondesignsystem.com/elements/color/tokens/#core-tokens)

- [Component Tokens](https://carbondesignsystem.com/elements/color/tokens/#component-tokens)

- [AI Tokens](https://carbondesignsystem.com/elements/color/tokens/#ai-tokens)

## Core Tokens

Core tokens are global colors that are used across components. They are named
and grouped by the common UI element that they are applied to.

- [Background](https://carbondesignsystem.com/elements/color/tokens/#background)

- [Layer](https://carbondesignsystem.com/elements/color/tokens/#layer)

- [Layer accent](https://carbondesignsystem.com/elements/color/tokens/#layer-accent)

- [Field](https://carbondesignsystem.com/elements/color/tokens/#field)

- [Border](https://carbondesignsystem.com/elements/color/tokens/#border)

- [Text](https://carbondesignsystem.com/elements/color/tokens/#text)

- [Link](https://carbondesignsystem.com/elements/color/tokens/#link)

- [Syntax](https://carbondesignsystem.com/elements/color/tokens/#syntax)

- [Icon](https://carbondesignsystem.com/elements/color/tokens/#icon)

- [Support](https://carbondesignsystem.com/elements/color/tokens/#support)

- [Focus](https://carbondesignsystem.com/elements/color/tokens/#focus)

- [Miscellaneous](https://carbondesignsystem.com/elements/color/tokens/#miscellaneous)

### Background

| Token | Role | Value |

| --- | --- | --- |

| $background | Default page background;UI Shell base color | White—#ffffffOptions |

| $layer-background-01 | Default page background;Automatically matches contextual layer background | White—#ffffffOptions |

| $background-hover | Hover color for $background;Hover color for transparent backgrounds | Gray 50, 12%—#8d8d8d @ 12%Options |

| $background-active | Active color for $background | Gray 50, 50%—#8d8d8d @ 50%Options |

| $background-selected | Selected color for $background | Gray 50, 20%—#8d8d8d @ 20%Options |

| $background-selected-hover | Hover color for $background-selected | Gray 50, 32%—#8d8d8d @ 32%Options |

| $background-inverse | High contrast backgrounds;High contrast elements | Gray 80—#393939Options |

| $background-inverse-hover | Hover color for $background-inverse | Gray 80 hover—#4c4c4cOptions |

| $background-brand | Feature background color | Blue 60—#0f62feOptions |

### Layer

| Token | Role | Value |

| --- | --- | --- |

| $layer-01 | Container color on $background;Secondary page background | Gray 10—#f4f4f4Options |

| $layer-02 | Container color on $layer-01 | White—#ffffffOptions |

| $layer-03 | Container color on $layer-02 | Gray 10—#f4f4f4Options |

| $layer-background-02 | Container color on $layer-background-01;Automatically matches contextual layer background | Gray 10—#f4f4f4Options |

| $layer-background-03 | Container color on $layer-background-02;Automatically matches contextual layer background | White—#ffffffOptions |

| $layer-hover-01 | Hover color for $layer-01 | Gray 10 hover—#e8e8e8Options |

| $layer-hover-02 | Hover color for $layer-02 | Gray 10 hover—#e8e8e8Options |

| $layer-hover-03 | Hover color for $layer-03 | Gray 10 hover—#e8e8e8Options |

| $layer-active-01 | Active color for $layer-01 | Gray 30—#c6c6c6Options |

| $layer-active-02 | Active color for $layer-02 | Gray 30—#c6c6c6Options |

| $layer-active-03 | Active color for $layer-03 | Gray 30—#c6c6c6Options |

| $layer-selected-01 | Selected color for $layer-01 | Gray 20—#e0e0e0Options |

| $layer-selected-02 | Selected color for $layer-02 | Gray 20—#e0e0e0Options |

| $layer-selected-03 | Selected color for $layer-03 | Gray 20—#e0e0e0Options |

| $layer-selected-hover-01 | Hover color for $layer-selected-01 | Gray 20 hover—#d1d1d1Options |

| $layer-selected-hover-02 | Hover color for $layer-selected-02 | Gray 20 hover—#d1d1d1Options |

| $layer-selected-hover-03 | Hover color for $layer-selected-03 | Gray 20 hover—#d1d1d1Options |

| $layer-selected-inverse | High contrast elements;4.5:1 AA element contrast | Gray 100—#161616Options |

| $layer-selected-disabled | Disabled color for selected layers | Gray 50—#8d8d8dOptions |

### Layer accent

| Token | Role | Value |

| --- | --- | --- |

| $layer-accent-01 | Tertiary background paired with $layer-01 | Gray 20—#e0e0e0Options |

| $layer-accent-02 | Tertiary background paired with $layer-02 | Gray 20—#e0e0e0Options |

| $layer-accent-03 | Tertiary background paired with $layer-03 | Gray 20—#e0e0e0Options |

| $layer-accent-hover-01 | Hover color for $layer-accent-01 | Gray 20 hover—#cacacaOptions |

| $layer-accent-hover-02 | Hover color for $layer-accent-02 | Gray 20 hover—#cacacaOptions |

| $layer-accent-hover-03 | Hover color for $layer-accent-03 | Gray 20 hover—#cacacaOptions |

| $layer-accent-active-01 | Active color for $layer-accent-01 | Gray 40—#a8a8a8Options |

| $layer-accent-active-02 | Active color for $layer-accent-02 | Gray 40—#a8a8a8Options |

| $layer-accent-active-03 | Active color for $layer-accent-03 | Gray 40—#a8a8a8Options |

### Field

| Token | Role | Value |

| --- | --- | --- |

| $field-01 | Default input fields;Fields on $background | Gray 10—#f4f4f4Options |

| $field-02 | Secondary input fields;Fields on $layer-01 | White—#ffffffOptions |

| $field-03 | Tertiary input fields;Fields on $layer-02 | Gray 10—#f4f4f4Options |

| $field-hover-01 | Hover color for $field-01 | Gray 10 hover—#e8e8e8Options |

| $field-hover-02 | Hover color for $field-02 | Gray 10 hover—#e8e8e8Options |

| $field-hover-03 | Hover color for $field-03 | Gray 10 hover—#e8e8e8Options |

### Border

| Token | Role | Value |

| --- | --- | --- |

| $border-interactive | 3:1 AA contrast;Selected borders;Active borders | Blue 60—#0f62feOptions |

| $border-subtle-00 | Subtle borders paired with $background | Gray 20—#e0e0e0Options |

| $border-subtle-01 | Subtle borders paired with $layer-01 | Gray 30—#c6c6c6Options |

| $border-subtle-02 | Subtle borders paired with $layer-02 | Gray 20—#e0e0e0Options |

| $border-subtle-03 | Subtle borders paired with $layer-03 | Gray 30—#c6c6c6Options |

| $border-subtle-selected-01 | Selected color for $border-subtle-01 | Gray 30—#c6c6c6Options |

| $border-subtle-selected-02 | Selected color for $border-subtle-02 | Gray 30—#c6c6c6Options |

| $border-subtle-selected-03 | Selected color for $border-subtle-03 | Gray 30—#c6c6c6Options |

| $border-strong-01 | Medium contrast border;Border-bottom paired with $field-01;3:1 AA non-text contrast | Gray 50—#8d8d8dOptions |

| $border-strong-02 | Medium contrast border;Border-bottom paired with $field-02;3:1 AA non-text contrast | Gray 50—#8d8d8dOptions |

| $border-strong-03 | Medium contrast border;Border-bottom paired with $field-03;3:1 AA non-text contrast | Gray 50—#8d8d8dOptions |

| $border-tile-01 | Operable tile indicator paired with $layer-01 | Gray 30—#c6c6c6Options |

| $border-tile-02 | Operable tile indicator paired with $layer-02 | Gray 40—#a8a8a8Options |

| $border-tile-03 | Operable tile indicator paired with $layer-03 | Gray 30—#c6c6c6Options |

| $border-inverse | High contrast border;4.5:1 AA non-text contrast | Gray 100—#161616Options |

| $border-disabled | Disabled border color (excluding border-subtles) | Gray 30—#c6c6c6Options |

### Text

| Token | Role | Value |

| --- | --- | --- |

| $text-primary | Primary text;Body copy;Headers;Hover text color for $text-secondary | Gray 100—#161616Options |

| $text-secondary | Secondary text;Input labels | Gray 70—#525252Options |

| $text-placeholder | Placeholder text | Gray 40—#a8a8a8Options |

| $text-on-color | Text on interactive colors;Text on button colors | White—#ffffffOptions |

| $text-on-color-disabled | Disabled color for $text-on-color | Gray 50—#8d8d8dOptions |

| $text-helper | Tertiary text;Help text | Gray 60—#6f6f6fOptions |

| $text-error | Error message text | Red 60—#da1e28Options |

| $text-inverse | Inverse text color | White—#ffffffOptions |

| $text-disabled | Disabled text color | Gray 100 – 25%—#161616 – 25%Options |

### Link

| Token | Role | Value |

| --- | --- | --- |

| $link-primary | Primary links | Blue 60—#0f62feOptions |

| $link-primary-hover | Hover color for $link-primary | Blue 70—#0043ceOptions |

| $link-secondary | Secondary link color for lower contrast backgrounds | Blue 70—#0043ceOptions |

| $link-inverse | Links on $background-inverse backgrounds | Blue 40—#78a9ffOptions |

| $link-inverse-hover | Hover color for links on $background-inverse backgrounds | Blue 30—#a6c8ffOptions |

| $link-inverse-active | Active color for links on $background-inverse backgrounds | Gray 10—#f4f4f4Options |

| $link-inverse-visited | Color for visited links on $background-inverse backgrounds | Purple 40—#be95ffOptions |

| $link-visited | Color for visited links | Purple 60—#8a3ffcOptions |

### Syntax

| Token | Role | Value |

| --- | --- | --- |

| $syntax-comment | Default comment text | Green 60—#198038Options |

| $syntax-line-comment | Single-line comment | Green 60—#198038Options |

| $syntax-block-comment | Block comment | Green 60—#198038Options |

| $syntax-doc-comment | Documentation comment | Green 60—#198038Options |

| $syntax-doc-string | Docstring | Gray 100—#161616Options |

| $syntax-keyword | Keywords | Blue 60—#0f62feOptions |

| $syntax-operator-keyword | Operator keywords | Blue 60—#0f62feOptions |

| $syntax-control-keyword | Control-flow keywords | Purple 70—#8a3ffcOptions |

| $syntax-definition-keyword | Definition keywords | Cyan 70—#00bcd4Options |

| $syntax-module-keyword | Module/import keywords | Purple 70—#8a3ffcOptions |

| $syntax-variable | Variable | Blue 60—#0f62feOptions |

| $syntax-name | Name | Blue 60—#0f62feOptions |

| $syntax-variable-name | Variable name | Blue 60—#0f62feOptions |

| $syntax-label-name | Label name | Blue 60—#0f62feOptions |

| $syntax-attribute | Attribute | Cyan 70—#00bcd4Options |

| $syntax-attribute-name | Attribute name | Cyan 70—#00bcd4Options |

| $syntax-property-name | Property name | Cyan 70—#00bcd4Options |

| $syntax-tag | Tag delimiters | Teal 60—#009d9aOptions |

| $syntax-tag-name | Tag name | Teal 60—#009d9aOptions |

| $syntax-type | Type | Teal 60—#009d9aOptions |

| $syntax-type-name | Type name | Teal 60—#009d9aOptions |

| $syntax-class-name | Class name | Teal 60—#009d9aOptions |

| $syntax-namespace | Namespace | Teal 60—#009d9aOptions |

| $syntax-macro-name | Macro name | Gray 100—#161616Options |

| $syntax-atom | Atom literal | Gray 100—#161616Options |

| $syntax-literal | Literal | Gray 100—#161616Options |

| $syntax-bool | Boolean | Gray 100—#161616Options |

| $syntax-null | Null/undefined | Gray 100—#161616Options |

| $syntax-self | Self/this | Teal 60—#009d9aOptions |

| $syntax-number | Number | Green 60—#198038Options |

| $syntax-integer | Integer | Green 60—#198038Options |

| $syntax-float | Float | Green 60—#198038Options |

| $syntax-unit | Unit | Green 60—#198038Options |

| $syntax-string | String | Gray 100—#161616Options |

| $syntax-character | Character | Gray 100—#161616Options |

| $syntax-attribute-value | Attribute value | Gray 100—#161616Options |

| $syntax-special-string | Special string | Purple 60—#a56effOptions |

| $syntax-regexp | RegExp | Purple 70—#8a3ffcOptions |

| $syntax-escape | Escape sequence | Cool Gray 80—#8d8d8dOptions |

| $syntax-url | URL literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-color | Color literal | Gray 100—#161616Options |

| $syntax-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-deref-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-arithmetic-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-logic-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-bitwise-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-compare-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-update-operator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-definition-operator | Color literal | Cyan 70—#0072c3Options |

| $syntax-type-operator | Color literal | Teal 60—#009d9aOptions |

| $syntax-control-operator | Color literal | Purple 60—#8a3ffcOptions |

| $syntax-modifier | Color literal | Magenta 60—#d02670Options |

| $syntax-punctuation | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-separator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-bracket | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-angle-bracket | Color literal | Cool Gray 60—#6f6f6fOptions |

| $syntax-square-bracket | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-paren | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-brace | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-content | Color literal | Gray 100—#161616Options |

| $syntax-list | Color literal | Gray 100—#161616Options |

| $syntax-emphasis | Color literal | Gray 100—#161616Options |

| $syntax-strong | Color literal | Gray 100—#161616Options |

| $syntax-monospace | Color literal | Gray 100—#161616Options |

| $syntax-strikethrough | Color literal | Gray 100—#161616Options |

| $syntax-heading | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-1 | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-2 | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-3 | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-4 | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-5 | Color literal | Cyan 70—#0072c3Options |

| $syntax-heading-6 | Color literal | Cyan 70—#0072c3Options |

| $syntax-content-separator | Color literal | Cool Gray 80—#8d8d8dOptions |

| $syntax-quote | Color literal | Gray 60—#6f6f6fOptions |

| $syntax-link | Color literal | Blue 60—#0f62feOptions |

| $syntax-invalid | Color literal | Red 60—#da1e28Options |

| $syntax-meta | Color literal | Green 60—#24a148Options |

| $syntax-document-meta | Color literal | Green 60—#24a148Options |

| $syntax-annotation | Color literal | Teal 60—#009d9aOptions |

| $syntax-processing-instruction | Color literal | Purple 60—#8a3ffcOptions |

| $syntax-definition | Color literal | Cyan 70—#0072c3Options |

| $syntax-constant | Color literal | Blue 60—#0f62feOptions |

| $syntax-function | Color literal | Yellow 60—#f1c21bOptions |

| $syntax-standard | Color literal | Blue 60—#0f62feOptions |

| $syntax-local | Color literal | Blue 60—#0f62feOptions |

| $syntax-special | Color literal | Blue 60—#0f62feOptions |

| $syntax-deleted | Color literal | Red 20—#ffd7d9Options |

| $syntax-inserted | Color literal | Green 20—#a7f0baOptions |

### Icon

| Token | Role | Value |

| --- | --- | --- |

| $icon-primary | Primary icons | Gray 100—#161616Options |

| $icon-secondary | Secondary icons | Gray 70—#525252Options |

| $icon-on-color | Icons on interactive colors;Icons on non-layer colors | White—#ffffffOptions |

| $icon-on-color-disabled | Disabled color for $icon-on-color | Gray 50—#8d8d8dOptions |

| $icon-interactive | Icons that indicate operability | Blue 60—#0f62feOptions |

| $icon-inverse | Inverse icon color | White—#ffffffOptions |

| $icon-disabled | Disabled icon color | Gray 100 – 25%—#161616 – 25%Options |

### Support

| Token | Role | Value |

| --- | --- | --- |

| $support-error | Error;Invalid state | Red 60—#da1e28Options |

| $support-success | Success;On | Green 50—#24a148Options |

| $support-warning | Warning | Yellow 30—#f1c21bOptions |

| $support-info | Information | Blue 70—#0043ceOptions |

| $support-error-inverse | Error in high contrast moments | Red 50—#fa4d56Options |

| $support-success-inverse | Success in high contrast moments | Green 40—#42be65Options |

| $support-warning-inverse | Warning in high contrast moments | Yellow 30—#f1c21bOptions |

| $support-info-inverse | Information in high contrast moments | Blue 50—#4589ffOptions |

| $support-caution-minor | Minor caution status | Yellow 30—#f1c21bOptions |

| $support-caution-major | Major caution status | Orange 40—#ff832bOptions |

| $support-caution-undefined | Undefined status | Purple 60—#8a3ffcOptions |

### Focus

| Token | Role | Value |

| --- | --- | --- |

| $focus | Focus border;Focus underline | Blue 60—#0f62feOptions |

| $focus-inset | Contrast border paired with $focus | White—#ffffffOptions |

| $focus-inverse | Focus on high contrast moments | White—#ffffffOptions |

### Miscellaneous

| Token | Role | Value |

| --- | --- | --- |

| $interactive | 3:1 AA contrast;Selected elements;Active elements;Accent icons | Blue 60—#0f62feOptions |

| $highlight | Highlight color | Blue 20—#d0e2ffOptions |

| $toggle-off | Off background;3:1 AA contrast | Gray 50—#8d8d8dOptions |

| $overlay | Background overlay | Black—#000000 @ 60%Options |

| $skeleton-element | Skeleton color for text and UI elements | Gray 30—#c6c6c6Options |

| $skeleton-background | Skeleton color for containers | Gray 10 hover—#e5e5e5Options |

## Component Tokens

Some components have their own specific color tokens, known as component tokens.
They represent the properties associated with a particular component. They are
not global tokens like the core tokens and should never be used for anything
other than their own component. For more information on how to use component
tokens, see the
[developer documentation](https://github.com/carbon-design-system/carbon/blob/main/packages/styles/docs/sass.md#component-tokens).

- [Button](https://carbondesignsystem.com/elements/color/tokens/#button)

- [Content switcher](https://carbondesignsystem.com/elements/color/tokens/#content-switcher)

- [Tag](https://carbondesignsystem.com/elements/color/tokens/#tag)

- [Notification](https://carbondesignsystem.com/elements/color/tokens/#notification)

### Button

| Token | Role | Value |

| --- | --- | --- |

| $button-primary | Primary button color | Blue 60—#0f62feOptions |

| $button-primary-hover | Hover color for $button-primary | Blue 60 hover—#0353e9Options |

| $button-primary-active | Active color for $button-primary | Blue 80—#002d9cOptions |

| $button-secondary | Secondary button color | Gray 80—#393939Options |

| $button-secondary-hover | Hover color for $button-secondary | Gray 80 hover—#4c4c4cOptions |

| $button-secondary-active | Active color for $button-secondary | Gray 60—#6f6f6fOptions |

| $button-tertiary | Tertiary button color;4.5:1 AA text contrast | Blue 60—#0f62feOptions |

| $button-tertiary-hover | Hover color for $button-tertiary | Blue 60 hover—#0353e9Options |

| $button-tertiary-active | Active color for $button-tertiary | Blue 80—#002d9cOptions |

| $button-danger-primary | Primary danger button color;3:1 AA non-text contrast | Red 60—#da1e28Options |

| $button-danger-secondary | Tertiary danger button color;Ghost danger button color;4.5:1 AA text contrast | Red 60—#da1e28Options |

| $button-danger-hover | Hover color for $danger-primary;Hover color for $danger-secondary | Red 60 hover—#ba1b23Options |

| $button-danger-active | Active color for $danger-primary;Active color for $danger-secondary | Red 80—#750e13Options |

| $button-separator | Fluid button separator;3:1 AA non-text contrast | Gray 20—#e0e0e0Options |

| $button-disabled | Disabled color for button elements | Gray 30—#c6c6c6Options |

### Content Switcher

| Token | Role | Value |

| --- | --- | --- |

| $content-switcher-background | Low contrast background color | Gray 20—#e0e0e0Options |

| $content-switcher-background-hover | Low contrast hover color for $content-switcher-background | Gray 20 hover—#d1d1d1Options |

| $content-switcher-selected | Low contrast selected color | White—#ffffffOptions |

### Tag

| Token | Role | Value |

| --- | --- | --- |

| $tag-background-gray | Gray tag background | Gray 20—#e0e0e0Options |

| $tag-color-gray | Gray tag text;Gray tag icon | Gray 100—#161616Options |

| $tag-hover-gray | Gray tag hover for $tag-background-gray | Gray 20 hover—#d1d1d1Options |

| $tag-border-gray | Gray tag border for operational tag | Gray 40—#a8a8a8Options |

| $tag-background-cool-gray | Cool gray tag background | Cool gray 20—#dde1e6Options |

| $tag-color-cool-gray | Cool gray tag text;Cool gray tag icon | Cool gray 100—#121619Options |

| $tag-hover-cool-gray | Cool gray tag hover for $tag-background-cool-gray | Cool gray 20 hover—#cdd3daOptions |

| $tag-border-cool-gray | Cool gray tag border for operational tag | Cool gray 40—#a2a9b0Options |

| $tag-background-warm-gray | Warm gray tag background | Warm gray 20—#e5e0dfOptions |

| $tag-color-warm-gray | Warm gray tag text;Warm gray tag icon | Warm gray 100—#171414Options |

| $tag-hover-warm-gray | Warm gray tag hover for $tag-background-warm-gray | Warm gray 20 hover—#d8d0cfOptions |

| $tag-border-warm-gray | Warm gray tag border for operational tag | Warm gray 40—#ada8a8Options |

| $tag-background-red | Red tag background | Red 20—#ffd7d9Options |

| $tag-color-red | Red tag text;Red tag icon | Red 70—#a2191fOptions |

| $tag-hover-red | Red tag hover for $tag-background-red | Red 20 hover—#ffc2c5Options |

| $tag-border-red | Red tag border for operational tag | Red 40—#ff8389Options |

| $tag-background-magenta | Magenta tag background | Magenta 20—#ffd6e8Options |

| $tag-color-magenta | Magenta tag text;Magenta tag icon | Magenta 70—#9f1853Options |

| $tag-hover-magenta | Magenta tag hover for $tag-background-magenta | Magenta 20 hover—#ffbddaOptions |

| $tag-border-magenta | Magenta tag border for operational tag | Magenta 40—#ff7eb6Options |

| $tag-background-purple | Purple tag background | Purple 20—#e8daffOptions |

| $tag-color-purple | Purple tag text;Purple tag icon | Purple 70—#6929c4Options |

| $tag-hover-purple | Purple tag hover for $tag-background-purple | Purple 20 hover—#dcc7ffOptions |

| $tag-border-purple | Purple tag border for operational tag | Purple 40—#be95ffOptions |

| $tag-background-blue | Blue tag background | Blue 20—#d0e2ffOptions |

| $tag-color-blue | Blue tag text;Blue tag icon | Blue 70—#0043ceOptions |

| $tag-hover-blue | Blue tag hover for $tag-background-blue | Blue 20 hover—#b8d3ffOptions |

| $tag-border-blue | Blue tag border for operational tag | Blue 40—#78a9ffOptions |

| $tag-background-cyan | Cyan tag background | Cyan 20—#bae6ffOptions |

| $tag-color-cyan | Cyan tag text;Cyan tag icon | Cyan 70—#00539aOptions |

| $tag-hover-cyan | Cyan tag hover for $tag-background-cyan | Cyan 20 hover—#99daffOptions |

| $tag-border-cyan | Cyan tag border for operational tag | Cyan 40—#33b1ffOptions |

| $tag-background-teal | Teal tag background | Teal 20—#9ef0f0Options |

| $tag-color-teal | Teal tag text;Teal tag icon | Teal 70—#005d5dOptions |

| $tag-hover-teal | Teal tag hover for $tag-background-teal | Teal 20 hover—#57e5e5Options |

| $tag-border-teal | Teal tag border for operational tag | Teal 40—#08bdbaOptions |

| $tag-background-green | Green tag background | Green 20—#a7f0baOptions |

| $tag-color-green | Green tag text;Green tag icon | Green 70—#0e6027Options |

| $tag-hover-green | Green tag hover for $tag-background-green | Green 20 hover—#74e792Options |

| $tag-border-green | Green tag border for operational tag | Green 40—#42be65Options |

### Notification

| Token | Role | Value |

| --- | --- | --- |

| $notification-background-error | Error low contrast notification background | Red 10—#fff1f1Options |

| $notification-background-success | Success low contrast notification background | Green 10—#defbe6Options |

| $notification-background-info | Informational low contrast notification background | Blue 10—#edf5ffOptions |

| $notification-background-warning | Warning low contrast notification background | Yellow 10—#fcf4d6Options |

| $notification-action-hover | Hover for notification ghost button | White—#ffffffOptions |

| $notification-action-tertiary-inverse | Tertiary button color for notification | White—#ffffffOptions |

| $notification-action-tertiary-inverse-active | Active color for tertiary button in notification | White—#ffffffOptions |

| $notification-action-tertiary-inverse-hover | Hover color for tertiary button in notification | Gray 30—#c6c6c6Options |

| $notification-action-tertiary-inverse-text | Text color for tertiary button in notification | Gray 100—#161616Options |

| $notification-action-tertiary-inverse-text-on-color-disabled | Disabled color for tertiary button in notification | White—#ffffffOptions |

## AI Tokens

To accommodate for the new AI styles, we have introduced a new suite of color
tokens that can be found within the main Carbon themes. These tokens should only
be used when building custom AI components, variants, or instances in your UI.
For more information on how to use the AI tokens, see the
[Carbon for AI](https://carbondesignsystem.com/guidelines/carbon-for-ai/)
documentation.

- [General AI](https://carbondesignsystem.com/elements/color/tokens/#general-ai)

- [Chat](https://carbondesignsystem.com/elements/color/tokens/#chat)

- [Chat button](https://carbondesignsystem.com/elements/color/tokens/#chat-button)

### General AI

| Token | Role | Value |

| --- | --- | --- |

| $ai-aura-start | Linear gradient start value for large AI layers | Blue 50, 10%—#4589ff @ 10%Options |

| $ai-aura-start-sm | Linear gradient start value for small AI layers | Blue 50, 16%—#4589ff @ 16%Options |

| $ai-aura-end | Linear gradient start value for all AI layers | White, 0%—#ffffff @ 0%Options |

| $ai-aura-hover-start | Linear gradient start value for the AI aura hover | Blue 50, 32%—#4589ffOptions |

| $ai-aura-hover-end | Linear gradient end value for the AI aura hover | White, 0%—#ffffff @ 0%Options |

| $ai-aura-hover-background | Hover background color for AI layers | Blue 10—#edf5ffOptions |

| $ai-border-start | Linear gradient start value for AI borders | Blue 30, 64%—#a6c8ff @ 64%Options |

| $ai-border-end | Linear gradient end value for AI borders | Blue 40—#78a9ffOptions |

| $ai-border-strong | Medium contrast border for AI elements;Border-bottom paired with AI fields;3:1 AA non-text contrast | Blue 50—#4589ffOptions |

| $ai-drop-shadow | Drop shadow for the AI layer | Blue 60, 10%—#0f62fe @ 10%Options |

| $ai-inner-shadow | Inner shadow for the AI layer | Blue 50, 10%—#4589ff @ 10%Options |

| $ai-popover-background | Background color for the AI explainability popover | White—#ffffffOptions |

| $ai-popover-shadow-outer-01 | 1 of 2 shadow colors for the AI explainability popover | Blue 70, 6%—#0043ce @ 6%Options |

| $ai-popover-shadow-outer-02 | 2 of 2 shadow colors for the AI explainability popover | Black, 4%—#000000 @ 4%Options |

| $ai-skeleton-element | Skeleton color for AI text and UI elements | Blue 50—#4589ffOptions |

| $ai-skeleton-background | Skeleton color for AI containers | Blue 20—#d0e2ffOptions |

| $ai-overlay | Background overlay for AI components | Blue 100, 50%—#001141 @ 50%Options |

### Chat

| Token | Role | Value |

| --- | --- | --- |

| $chat-avatar-bot | Chat avatar background color for bots | Gray 60—#6f6f6fOptions |

| $chat-avatar-agent | Chat avatar background color for agents | Gray 80—#393939Options |

| $chat-avatar-user | Chat avatar background color for users | Blue 60—#0f62feOptions |

| $chat-bubble-user | Chat bubble background color for users | Gray 20—#e0e0e0Options |

| $chat-bubble-agent | Chat bubble background color for agents | White—#ffffffOptions |

| $chat-bubble-agent-text | Chat bubble text color for agents | Gray 100—#161616Options |

| $chat-bubble-border | Chat bubble border color for agents | Gray 20—#e0e0e0Options |

| $chat-bubble-user-text | Chat bubble text color for users | Gray 100—#161616Options |

| $chat-prompt-background | Background color for chat prompt input | White—#ffffffOptions |

| $chat-prompt-border-start | Linear gradient start value for chat prompts border | Gray 10—#f4f4f4Options |

| $chat-prompt-border-end | Linear gradient end value for chat prompts border | Gray 10, 0%—#f4f4f4 @ 0%Options |

| $chat-prompt-text | Text for chat prompt | Gray 100—#161616Options |

| $chat-shell-background | Chat shell background color | White—#ffffffOptions |

| $chat-header-background | Chat header background color | White—#ffffffOptions |

| $chat-header-text | Text / fill for header | Gray 100—#161616Options |

### Chat button

| Token | Role | Value |

| --- | --- | --- |

| $chat-button | Chat quick action button color | $link-primary—#0f62feOptions |

| $chat-button-hover | Hover color for $chat-button | $background-hover—#8d8d8d @ 12%Options |

| $chat-button-text-hover | Text color for hovered chat button | $link-primary-hover—#0043ceOptions |

| $chat-button-active | Active color for $chat-button | $background-active—#8d8d8d @ 50%Options |

| $chat-button-selected | Selected color for $chat-button | $background-selected—#8d8d8d @ 20%Options |

| $chat-button-text-selected | Text color for selected chat-button | $text-secondary—#525252Options |