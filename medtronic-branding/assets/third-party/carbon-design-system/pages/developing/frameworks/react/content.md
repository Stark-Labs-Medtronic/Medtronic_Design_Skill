# Frameworks – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/frameworks/react/

# Frameworks

The Carbon React library provides front-end developers and engineers a
collection of reusable React components to build websites and user interfaces.
Adopting the library enables developers to use consistent markup, styles, and
behavior in prototype and production work.

- [Install](https://carbondesignsystem.com/developing/frameworks/react/#install)

- [Getting started](https://carbondesignsystem.com/developing/frameworks/react/#getting-started)

- [Development](https://carbondesignsystem.com/developing/frameworks/react/#development)

- [Troubleshooting](https://carbondesignsystem.com/developing/frameworks/react/#troubleshooting)

## Resources

## Install

```

npm install --save @carbon/reactCopy to clipboard

```

If you prefer [Yarn](https://yarnpkg.com/):

```

yarn add @carbon/reactCopy to clipboard

```

> **Note:**

Please ensure the
[peerDependencies](https://github.com/search?q=repo%3Acarbon-design-system%2Fcarbon+peerDependencies+language%3AJSON+path%3Apackages%2Freact&type=code)
for `@carbon/react` are installed in your project to avoid errors.

## Getting started

The `@carbon/react` package provides components, styles and icons for the Carbon
Design System.

Components require the use of a build pipeline in your project. This could be in
the form of a bundler, framework, or other build tool. Some examples include
Next.js, Vite, Parcel, and Webpack. A comprehensive list is available in the
[react documentation](https://react.dev/learn/start-a-new-react-project).

To use a component, you can import it directly from the package:

```

import { Button } from '@carbon/react';
function MyComponent() {  return <Button>Example usage</Button>;}Copy to clipboard

```

To include the styles for a specific component, you can either import all the
styles from the project or include the styles for a specific component:

```

// Bring in all the styles for Carbon in your root/global stylesheet@use '@carbon/react';
// Or bring in the styles for one component@use '@carbon/react/scss/components/button';Copy to clipboard

```

### Icons

The @carbon/react package also provides icon components that you can include in
your project. You can import these icon components from the
`@carbon/react/icons` entrypoint:

```

import { Add } from '@carbon/react/icons';
function MyComponent() {  return <Add />;}Copy to clipboard

```

A full list of available icons is provided in the
[icon library](https://carbondesignsystem.com/elements/icons/library/).

For a more in depth introduction to using `@carbon/react` in a webpack-based
app, [check out our React tutorial](https://carbondesignsystem.com/developing/react-tutorial/overview/).

## Development

Please refer to the
[Contribution Guidelines](https://github.com/carbon-design-system/carbon/blob/main/.github/CONTRIBUTING.md)
before starting any work.

### Using the server

We use [Storybook](https://github.com/storybookjs/storybook) for developing
components.

```

yarn storybookCopy to clipboard

```

1. Open browser to `http://localhost:9000/`.

2. Develop components in their respective folders (`/components` or
`/internal`).

3. Author stories within the `*.stories.js*` files.

### List of available components

View available React Components in
[the `@carbon/react` storybook](http://react.carbondesignsystem.com/). Usage
information is available under the “docs” tab.

## Troubleshooting

If you experience any issues while getting set up with Carbon Components React,
please head over to the
[GitHub repo](https://github.com/carbon-design-system/carbon/tree/main/packages/react)
for more guidelines and support. Please
[create an issue](https://github.com/carbon-design-system/carbon/issues) if your
issue does not already exist.

## Code samples

```
npm install --save @carbon/reactCopy to clipboard
```

```bash
npm install --save @carbon/react
```

```
yarn add @carbon/reactCopy to clipboard
```

```bash
yarn add @carbon/react
```

```
import { Button } from '@carbon/react';
function MyComponent() {  return <Button>Example usage</Button>;}Copy to clipboard
```

```js
import { Button } from '@carbon/react';
function MyComponent() {  return <Button>Example usage</Button>;}
```

```
// Bring in all the styles for Carbon in your root/global stylesheet@use '@carbon/react';
// Or bring in the styles for one component@use '@carbon/react/scss/components/button';Copy to clipboard
```

```js
// Bring in all the styles for Carbon in your root/global stylesheet@use '@carbon/react';
// Or bring in the styles for one component@use '@carbon/react/scss/components/button';
```

```
import { Add } from '@carbon/react/icons';
function MyComponent() {  return <Add />;}Copy to clipboard
```

```js
import { Add } from '@carbon/react/icons';
function MyComponent() {  return <Add />;}
```

```
yarn storybookCopy to clipboard
```

```bash
yarn storybook
```
