# Color – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/color/code/

# Color

The Carbon color package helps teams build engaging digital experiences through
consistent application of color.

If you’re using `@carbon/react`, you probably don’t need need to install the
color package separately. See our [Carbon React](https://carbondesignsystem.com/developing/frameworks/react/)
guide to start building.

## Usage

### Sass

The `@carbon/colors` package enables you to access colors from the IBM Design
Language in Sass. You can access a color directly from the package by writing
the following:

```

@use '@carbon/colors';
.selector {  background: colors.$blue-50;}Copy to clipboard

```

For a full list of colors exported, refer to the
[API](https://github.com/carbon-design-system/carbon/blob/main/packages/colors/docs/sass.md#api)
section in the package’s Sass Documentation.

In addition to individual colors, you can access all colors in a `Map` using the
`$colors` variable.

```

@use '@carbon/colors';@each $swatch, $grades in colors.$colors {  @each $grade in $grades {    //  }}Copy to clipboard

```

Each key in the `$colors` map is the name of a group of colors, also known as a
swatch. The value of each entry is a `Map` where the keys are the color grade
and the values are the hex codes for the color at that grade. For example:

```

$colors: (  blue: (    10: #edf5ff,    20: #d0e2ff,    30: #a6c8ff,    40: #78a9ff,    50: #4589ff,    60: #0f62fe,    70: #0043ce,Copy to clipboardShow more

```

### JavaScript

For JavaScript, you can import and use this module by doing the following in
your code:

```

// ESMimport { black, blue, warmGray } from '@carbon/colors';
// CommonJSconst { black, blue, warmGray } = require('@carbon/colors');Copy to clipboard

```

Each color swatch is exported as a variable, and each color name is also
exported as an object that can be called by specifying grade, for example:

```

black;blue[50]; // Using the `blue` object.warmGray100; // Using the `warmGray100` variable.Copy to clipboard

```

## Resources

## Code samples

```
@use '@carbon/colors';
.selector {  background: colors.$blue-50;}Copy to clipboard
```

```scss
@use '@carbon/colors';
.selector {  background: colors.$blue-50;}
```

```
@use '@carbon/colors';@each $swatch, $grades in colors.$colors {  @each $grade in $grades {    //  }}Copy to clipboard
```

```scss
@use '@carbon/colors';@each $swatch, $grades in colors.$colors {  @each $grade in $grades {    //  }}
```

```
$colors: (  blue: (    10: #edf5ff,    20: #d0e2ff,    30: #a6c8ff,    40: #78a9ff,    50: #4589ff,    60: #0f62fe,    70: #0043ce,Copy to clipboardShow more
```

```scss
$colors: (  blue: (    10: #edf5ff,    20: #d0e2ff,    30: #a6c8ff,    40: #78a9ff,    50: #4589ff,    60: #0f62fe,    70: #0043ce,
```

```
// ESMimport { black, blue, warmGray } from '@carbon/colors';
// CommonJSconst { black, blue, warmGray } = require('@carbon/colors');Copy to clipboard
```

```js
// ESMimport { black, blue, warmGray } from '@carbon/colors';
// CommonJSconst { black, blue, warmGray } = require('@carbon/colors');
```

```
black;blue[50]; // Using the `blue` object.warmGray100; // Using the `warmGray100` variable.Copy to clipboard
```

```js
black;blue[50]; // Using the `blue` object.warmGray100; // Using the `warmGray100` variable.
```
