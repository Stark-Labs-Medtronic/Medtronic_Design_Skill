# Typography – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/typography/code/

# Typography

Type is a core part of any offering and critical to how brands express and
communicate throughout any experience. Use the Carbon type package to leverage
IBM Plex and create effective typography across your products more easily.

If you’re using `@carbon/react`, you probably don’t need need to install the
type package separately. See our [Carbon React](https://carbondesignsystem.com/developing/frameworks/react/)
guide to start building.

## Usage

The `@carbon/type` package enables you to use typography from the IBM Design
Language, including the type scale and fonts, along with typography design
tokens from the Carbon Design System. It also comes with opinionated defaults
for type styles on common elements like `h1`, `h2`, `p`, etc.

You can use this package by writing the following:

```

@use '@carbon/type';// Include type reset@include type.reset();
// Include default type styles, targets h1, h2, h3, etc@include type.default-type();
// Include utility classes for type-related properties@include type.type-classes();Copy to clipboard

```

### Type-styles

Unless there are specific exceptions, always use Carbon helpers to style your
fonts. This ensures your code stays consistent and maintainable. Avoid directly
setting individual CSS properties like font-weight or font-size; instead, rely
on Carbon to handle all typography styling.

```

.selector {  // Include a type style  @include type.style('productive-heading-01');}Copy to clipboard

```

### Type classes

The `type-classes` mixin will output a collection of utility CSS that you can
use to style a given HTML element with type-related styles.

```

@mixin type-classes;Copy to clipboard

```

In particular, you can use the following classes:

| Class | Description |

| --- | --- |

| .cds--type-{font-family} | Set the font-family property for the given font. This can include mono, sans, sans-condensed, sans-arabic, sans-devanagari, sans-hebrew, sans-jp, sans-kr, sans-thai-looped, sans-thai, serif |

| .cds--type-{font-weight} | Set the font-weight property |

| .cds--type-italic | Set the font-style property to italic |

| .cds--type-{token} | Style the HTML element with the given type token |

### Type styles

Instead of using a type scale, `@carbon/type` provides tokens that represent
what we call type styles. These tokens have a variety of properties for styling
how text is rendered on a page.

You can find a full reference of the type styles that are available on the
[Carbon Design System website](https://carbondesignsystem.com/elements/typography/type-sets)
.

You can include a type token in your Sass file by using the type-style mixin
from the Carbon type package.

#### Standard type tokens

Standard type tokens apply fixed font sizes that remain constant across all
viewport sizes.

```

@use '@carbon/type';
@include type.type-style('productive-heading-01');Copy to clipboard

```

#### Fluid type tokens

Fluid type tokens scale responsively between minimum and maximum font sizes
based on the viewport width. The second parameter (`true`) is required to enable
fluid behavior for these tokens.

```

@use '@carbon/type';
@include type.type-style('fluid-heading-01', true);Copy to clipboard

```

### Reset

An optional type reset is provided under the `type.reset()` mixin. You can
include this mixin by writing the following in your Sass file:

```

@use '@carbon/type';
@include type.reset();Copy to clipboard

```

This reset sets some top-level properties on `html` and `body`, namely
`font-size`, `font-family`, and some `text-rendering` options. We also map the
`strong` tag to the semibold font weight.

### Type scale

A type scale is provided through the `$type-scale` variable and corresponding
`type-scale` function and mixin. However, for specifying type styles, the
recommendation is to use [type styles](https://carbondesignsystem.com/elements/typography/code/#type-styles) .

If you are looking to use the type scale, you can include all the scale-related
utilities and variables by writing the following in your Sass file:

```

@use '@carbon/type';Copy to clipboard

```

You can access a specific step in the type scale by using the `type-scale`
function:

```

@use '@carbon/type';
.my-selector {  font-size: type.type-scale(1);}Copy to clipboard

```

## Resources

## Code samples

```
@use '@carbon/type';// Include type reset@include type.reset();
// Include default type styles, targets h1, h2, h3, etc@include type.default-type();
// Include utility classes for type-related properties@include type.type-classes();Copy to clipboard
```

```css
@use '@carbon/type';// Include type reset@include type.reset();
// Include default type styles, targets h1, h2, h3, etc@include type.default-type();
// Include utility classes for type-related properties@include type.type-classes();
```

```
.selector {  // Include a type style  @include type.style('productive-heading-01');}Copy to clipboard
```

```scss
.selector {  // Include a type style  @include type.style('productive-heading-01');}
```

```
@mixin type-classes;Copy to clipboard
```

```css
@mixin type-classes;
```

```
@use '@carbon/type';
@include type.type-style('productive-heading-01');Copy to clipboard
```

```css
@use '@carbon/type';
@include type.type-style('productive-heading-01');
```

```
@use '@carbon/type';
@include type.type-style('fluid-heading-01', true);Copy to clipboard
```

```css
@use '@carbon/type';
@include type.type-style('fluid-heading-01', true);
```

```
@use '@carbon/type';
@include type.reset();Copy to clipboard
```

```css
@use '@carbon/type';
@include type.reset();
```

```
@use '@carbon/type';Copy to clipboard
```

```css
@use '@carbon/type';
```

```
@use '@carbon/type';
.my-selector {  font-size: type.type-scale(1);}Copy to clipboard
```

```css
@use '@carbon/type';
.my-selector {  font-size: type.type-scale(1);}
```
