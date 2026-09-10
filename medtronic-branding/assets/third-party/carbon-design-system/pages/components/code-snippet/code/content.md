# Code snippet – Carbon Design System

Source: https://www.carbondesignsystem.com/components/code-snippet/code/

# Code snippet

Preview the code snippet component with the React live demo. For detailed code
usage documentation, see the Storybooks for each framework below.

## Documentation

## Live demo

This live demo contains only a preview of functionality and styles available for this component. View the [full demo](https://react.carbondesignsystem.com/?path=/story/components-codesnippet--inline&globals=theme:white) on Storybook for additional information such as its version, controls, and API documentation.

## Sample data

```

const codeSnippet = `"scripts": {  "build": "lerna run build --stream --prefix --npm-client yarn",  "ci-check": "carbon-cli ci-check",  "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",  "doctoc": "doctoc --title '## Table of Contents'",  "format": "prettier --write '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**'",  "format:diff": "prettier --list-different '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**' '!packages/components/**'",  "lint": "eslint actions config codemods packages",  "lint:styles": "stylelint '**/*.{css,scss}' --report-needless-disables --report-invalid-scope-disables",Copy to clipboardShow more

```

## Code samples

```
const codeSnippet = `"scripts": {  "build": "lerna run build --stream --prefix --npm-client yarn",  "ci-check": "carbon-cli ci-check",  "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",  "doctoc": "doctoc --title '## Table of Contents'",  "format": "prettier --write '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**'",  "format:diff": "prettier --list-different '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**' '!packages/components/**'",  "lint": "eslint actions config codemods packages",  "lint:styles": "stylelint '**/*.{css,scss}' --report-needless-disables --report-invalid-scope-disables",Copy to clipboardShow more
```

```javascript
const codeSnippet = `"scripts": {  "build": "lerna run build --stream --prefix --npm-client yarn",  "ci-check": "carbon-cli ci-check",  "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",  "doctoc": "doctoc --title '## Table of Contents'",  "format": "prettier --write '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**'",  "format:diff": "prettier --list-different '**/*.{js,md,scss,ts}' '!**/{build,es,lib,storybook,ts,umd}/**' '!packages/components/**'",  "lint": "eslint actions config codemods packages",  "lint:styles": "stylelint '**/*.{css,scss}' --report-needless-disables --report-invalid-scope-disables",
```
