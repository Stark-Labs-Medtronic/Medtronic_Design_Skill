# Themes – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/themes/code/

# Themes

Use the themes package to customize your product while maintaining consistency.

If you’re using `@carbon/react`, you probably don’t need need to install the
themes package separately. See our [Carbon React](https://carbondesignsystem.com/developing/frameworks/react/)
guide to start building.

## Usage

You can use `@carbon/themes` in JavaScript or Sass by including this package in
your project. By default, `@carbon/themes` provides a set of color tokens that
are pre-defined for a specific theme. Currently, we offer the following color
themes: white, gray 10, gray 90, gray 100.

You can preview all of the token values for this on the
[color guidelines](https://carbondesignsystem.com/elements/color/usage) page.

### Sass

If your project is using Sass, you can include this package and the
corresponding default theme by writing the following in your Sass file:

```

@use '@carbon/themes';
.my-component {  // Use tokens from the theme, this will map to a CSS Custom Property  color: themes.$token-01;}
:root {  // Emit CSS Custom Properties for the current themeCopy to clipboardShow more

```

By default, the white theme will be initialized. If you would like to include
another theme, you can do so by configuring the sass module using `with`. For
example:

```

@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes' with (  $theme: $g100);Copy to clipboard

```

Inline theming of theme switching can be done by using the mixin. For example:

```

@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
:root {  @include themes.theme($white);}
[data-carbon-theme='g10'] {  @include themes.theme($g10);Copy to clipboardShow more

```

Themes can also be extended with your own custom tokens:

```

@use '@carbon/themes/scss/themes';@use '@carbon/themes' with (  $fallback: themes.$g100,  $theme: (    token-01: #000000,  ));Copy to clipboard

```

#### System preferences

Modern browsers and systems have adopted the idea of dark and light themes
applied at a system level. Where no user preference has been specified their
system level theme should be matched.

For example applying `g10` or `g100` automatically based on system preferences.

```

@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
/* system preference theme by default */:root {  @include themes.theme($g10);}
@media (prefers-color-scheme: dark) {Copy to clipboardShow more

```

Some designs include a sections in the opposite theme.

```

@mixin theme-scheme($default, $compliment) {  /* apply default theme */  @include theme($default, true);
  /* apply to the compliment theme */  [data-carbon-theme--compliment] {    @include theme($compliment, true);  }
Copy to clipboardShow more

```

### JavaScript

If you’re looking to use these themes in JavaScript, we export a variety of
bindings for you to use, including:

```

import {  // An object of all themes  themes,
  // Direct theme values  white,  g10,  g90,  g100,Copy to clipboardShow more

```

## Resources

## Code samples

```
@use '@carbon/themes';
.my-component {  // Use tokens from the theme, this will map to a CSS Custom Property  color: themes.$token-01;}
:root {  // Emit CSS Custom Properties for the current themeCopy to clipboardShow more
```

```scss
@use '@carbon/themes';
.my-component {  // Use tokens from the theme, this will map to a CSS Custom Property  color: themes.$token-01;}
:root {  // Emit CSS Custom Properties for the current theme
```

```
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes' with (  $theme: $g100);Copy to clipboard
```

```scss
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes' with (  $theme: $g100);
```

```
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
:root {  @include themes.theme($white);}
[data-carbon-theme='g10'] {  @include themes.theme($g10);Copy to clipboardShow more
```

```scss
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
:root {  @include themes.theme($white);}
[data-carbon-theme='g10'] {  @include themes.theme($g10);
```

```
@use '@carbon/themes/scss/themes';@use '@carbon/themes' with (  $fallback: themes.$g100,  $theme: (    token-01: #000000,  ));Copy to clipboard
```

```scss
@use '@carbon/themes/scss/themes';@use '@carbon/themes' with (  $fallback: themes.$g100,  $theme: (    token-01: #000000,  ));
```

```
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
/* system preference theme by default */:root {  @include themes.theme($g10);}
@media (prefers-color-scheme: dark) {Copy to clipboardShow more
```

```scss
@use '@carbon/themes/scss/themes' as *;@use '@carbon/themes';
/* system preference theme by default */:root {  @include themes.theme($g10);}
@media (prefers-color-scheme: dark) {
```

```
@mixin theme-scheme($default, $compliment) {  /* apply default theme */  @include theme($default, true);
  /* apply to the compliment theme */  [data-carbon-theme--compliment] {    @include theme($compliment, true);  }
Copy to clipboardShow more
```

```scss
@mixin theme-scheme($default, $compliment) {  /* apply default theme */  @include theme($default, true);
  /* apply to the compliment theme */  [data-carbon-theme--compliment] {    @include theme($compliment, true);  }
```

```
import {  // An object of all themes  themes,
  // Direct theme values  white,  g10,  g90,  g100,Copy to clipboardShow more
```

```js
import {  // An object of all themes  themes,
  // Direct theme values  white,  g10,  g90,  g100,
```
