# Pictograms – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/pictograms/code/

# Pictograms

Carbon pictograms are provided through a set of packages allowing the use of
pictograms in multiple frameworks. Pictograms are supported in vanilla, React,
Angular, and Vue.

- [Get started](https://carbondesignsystem.com/elements/pictograms/code/#get-started)

- [Usage](https://carbondesignsystem.com/elements/pictograms/code/#usage)

- [Resources](https://carbondesignsystem.com/elements/pictograms/code/#resources)

## Get started

To install `@carbon/pictograms-react` in your project, you will need to run the
following command using [npm](https://www.npmjs.com/):

```

npm install -S @carbon/pictograms-reactCopy to clipboard

```

If you prefer [Yarn](https://yarnpkg.com/en/), use the following command
instead:

```

yarn add @carbon/pictograms-reactCopy to clipboard

```

## Usage

You can import a pictogram component into your project by referring to its name:

```

import { Airplane } from '@carbon/pictograms-react';Copy to clipboard

```

We also provide CommonJS and UMD files in the `lib` and `umd` directories,
respectively.

To import using CommonJS, you can do the following:

```

const { Airplane } = require('@carbon/pictograms-react');Copy to clipboard

```

_Note: if you would like to find the import path for a pictogram, you can
reference our
[Pictogram Library](https://www.carbondesignsystem.com/elements/pictograms/library)_

### Icon fill

All icons from the library support being styled by the `fill` property. You can
change the color of an icon by passing in a custom class name that sets this
property (preferred), or by passing in an inline style. For example:

```

// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}Copy to clipboard

```

```

import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" className="my-custom-class" />    </button>  );}Copy to clipboard

```

### Focus and aria-label

By default, the icon components from `@carbon/pictograms-react` are treated as
decorative content. This means that we set `aria-hidden="true"` unless certain
props are passed to the component.

If you would like the icon to be announced by a screen reader, you can supply an
`aria-label` or `aria-labelledby`. For example:

```

import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" />    </button>  );}Copy to clipboard

```

Doing this will add the appropriate `role` to the `<svg>` node, as well.

If you would like the `<svg>` to receive focus, you will need to pass in a
`tabIndex` value. For example:

```

import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return <Airplane aria-label="Add" tabIndex="0" />;}Copy to clipboard

```

Including `tabIndex` and `aria-label` (or `aria-labelledby`) will set the
corresponding `tabindex` on the underlying `<svg>` and verify support in older
browsers like Internet Explorer 11 by setting `focusable` to `true`.

## Resources

## Code samples

```
npm install -S @carbon/pictograms-reactCopy to clipboard
```

```bash
npm install -S @carbon/pictograms-react
```

```
yarn add @carbon/pictograms-reactCopy to clipboard
```

```bash
yarn add @carbon/pictograms-react
```

```
import { Airplane } from '@carbon/pictograms-react';Copy to clipboard
```

```jsx
import { Airplane } from '@carbon/pictograms-react';
```

```
const { Airplane } = require('@carbon/pictograms-react');Copy to clipboard
```

```js
const { Airplane } = require('@carbon/pictograms-react');
```

```
// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}Copy to clipboard
```

```css
// CSS custom class name to set the fill of the icon to `rebeccapurple`svg.my-custom-class {  fill: rebeccapurple;}
```

```
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" className="my-custom-class" />    </button>  );}Copy to clipboard
```

```jsx
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" className="my-custom-class" />    </button>  );}
```

```
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" />    </button>  );}Copy to clipboard
```

```jsx
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return (    <button>      <Airplane aria-label="Add" />    </button>  );}
```

```
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return <Airplane aria-label="Add" tabIndex="0" />;}Copy to clipboard
```

```jsx
import { Airplane } from '@carbon/pictograms-react';
function MyComponent() {  return <Airplane aria-label="Add" tabIndex="0" />;}
```
