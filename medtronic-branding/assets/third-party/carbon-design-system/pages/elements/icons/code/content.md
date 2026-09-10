# Icons – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/icons/code/

# Icons

Carbon icons are provided through a set of packages allowing the use of icons in
multiple frameworks. Icons are supported in vanilla, React, Angular, and Vue.

- [Get started](https://carbondesignsystem.com/elements/icons/code/#get-started)

- [Usage](https://carbondesignsystem.com/elements/icons/code/#usage)

- [Resources](https://carbondesignsystem.com/elements/icons/code/#resources)

## Get started

To install `@carbon/icons-react` in your project, you will need to run the
following command using [npm](https://www.npmjs.com/):

```

npm install -S @carbon/icons-reactCopy to clipboard

```

If you prefer [Yarn](https://yarnpkg.com/en/), use the following command
instead:

```

yarn add @carbon/icons-reactCopy to clipboard

```

## Usage

Icons in this package can be accessed through importing them by name.

```

import { Add } from '@carbon/icons-react';Copy to clipboard

```

Icons in this package support the following sizes: `16`, `20`, `24`, and `32`
pixels. These sizes refer to the width and height of the icon. Icons default to
size `16`. You can change the size of the icon by adding the `size` prop:

```

<Add size="24" />Copy to clipboard

```

_Note: if you would like to find the import path for an icon, you can reference
our [Icon Library](https://www.carbondesignsystem.com/elements/icons/library)_

### Icon fill

All icons from the library support being styled by the `fill` property. You can
change the color of an icon by passing in a custom class name that sets this
property (preferred), or by passing in an inline style. For example:

```

// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}Copy to clipboard

```

```

import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" className="my-custom-class" />    </button>  );}Copy to clipboard

```

#### Two-tone icons

Certain icons in the library support two distinct fill colors. You can target
the inner path by using the `[data-icon-path="inner-path"]` attribute selector.
For example:

```

// CSS custom class name to set the fill of the icon to `yellow`svg.outer-icon-fill {  fill: yellow;}
// Use the `data-icon-path` attribute selector to target the inner path// where we want to set the fill to `black`. We also set `opacity` to `1` so// that this inner-path is visible.svg.outer-icon-fill [data-icon-path='inner-path'] {Copy to clipboardShow more

```

```

import { WarningFilled } from '@carbon/icons-react';
function MyComponent() {  return <WarningFilled aria-label="Add" className="my-custom-class" />;}Copy to clipboard

```

### Focus and aria-label

By default, the icon components from `@carbon/icons-react` are treated as
decorative content. This means that we set `aria-hidden="true"` unless certain
props are passed to the component.

If you would like the icon to be announced by a screen reader, you can supply an
`aria-label` or `aria-labelledby`. For example:

```

import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" />    </button>  );}Copy to clipboard

```

Doing this will add the appropriate `role` to the `<svg>` node, as well.

If you would like the `<svg>` to receive focus, you will need to pass in a
`tabIndex` value. For example:

```

import { Add } from '@carbon/icons-react';
function MyComponent() {  return <Add aria-label="Add" tabIndex="0" />;}Copy to clipboard

```

Including `tabIndex` and `aria-label` (or `aria-labelledby`) will set the
corresponding `tabindex` on the underlying `<svg>` and verify support in older
browsers like Internet Explorer 11 by setting `focusable` to `true`.

## Resources

## Code samples

```
npm install -S @carbon/icons-reactCopy to clipboard
```

```bash
npm install -S @carbon/icons-react
```

```
yarn add @carbon/icons-reactCopy to clipboard
```

```bash
yarn add @carbon/icons-react
```

```
import { Add } from '@carbon/icons-react';Copy to clipboard
```

```jsx
import { Add } from '@carbon/icons-react';
```

```
<Add size="24" />Copy to clipboard
```

```js
<Add size="24" />
```

```
// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}Copy to clipboard
```

```css
// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}
```

```
import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" className="my-custom-class" />    </button>  );}Copy to clipboard
```

```jsx
import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" className="my-custom-class" />    </button>  );}
```

```
// CSS custom class name to set the fill of the icon to `yellow`svg.outer-icon-fill {  fill: yellow;}
// Use the `data-icon-path` attribute selector to target the inner path// where we want to set the fill to `black`. We also set `opacity` to `1` so// that this inner-path is visible.svg.outer-icon-fill [data-icon-path='inner-path'] {Copy to clipboardShow more
```

```scss
// CSS custom class name to set the fill of the icon to `yellow`svg.outer-icon-fill {  fill: yellow;}
// Use the `data-icon-path` attribute selector to target the inner path// where we want to set the fill to `black`. We also set `opacity` to `1` so// that this inner-path is visible.svg.outer-icon-fill [data-icon-path='inner-path'] {
```

```
import { WarningFilled } from '@carbon/icons-react';
function MyComponent() {  return <WarningFilled aria-label="Add" className="my-custom-class" />;}Copy to clipboard
```

```jsx
import { WarningFilled } from '@carbon/icons-react';
function MyComponent() {  return <WarningFilled aria-label="Add" className="my-custom-class" />;}
```

```
import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" />    </button>  );}Copy to clipboard
```

```jsx
import { Add } from '@carbon/icons-react';
function MyComponent() {  return (    <button>      <Add aria-label="Add" />    </button>  );}
```

```
import { Add } from '@carbon/icons-react';
function MyComponent() {  return <Add aria-label="Add" tabIndex="0" />;}Copy to clipboard
```

```jsx
import { Add } from '@carbon/icons-react';
function MyComponent() {  return <Add aria-label="Add" tabIndex="0" />;}
```
