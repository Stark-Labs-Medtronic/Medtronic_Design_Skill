# Community frameworks – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/community-frameworks/angular/

# Community frameworks

The library provides front-end developers & engineers a collection of reusable
Angular components to build websites and user interfaces. Adopting the library
enables developers to use consistent markup, styles, and behavior in prototype
and production work.

The Angular library is maintained by members of the Carbon community. For
support, contact the
[Carbon Angular team](https://github.com/IBM/carbon-components-angular/issues/new).

v11 upgrade for Carbon Angular is coming soon.

## Resources

## Install

Assuming we’re starting with a new @angular/cli project:

```

npx @angular/cli new my-project --style=scsscd my-projectnpm i --save carbon-components-angular carbon-componentsCopy to clipboard

```

Then we need to include carbon-components in `src/styles.scss`:

```

@import '~carbon-components/scss/globals/scss/styles.scss';Copy to clipboard

```

That’s it! Now start the server and start building.

```

npm startCopy to clipboard

```

_Note: This isn’t the only way to bootstrap a_ `carbon-components-angular`
_application, but the combination of_ `@angular/cli` _and the_
`carbon-components` _scss is our recommended setup._

### Using our starter app

We recommend using the
[carbon-angular-starter](https://github.com/carbon-design-system/carbon-angular-starter)
for bootstrapping applications with Carbon components. Within five minutes your
app will be running with the following already configured:

- Angular-cli

- Build process

- Code styles and editor configs

- Folder structure

- Lazy loading

- Routing

- Service workers

- Test framework

Check out the
[readme](https://github.com/carbon-design-system/carbon-angular-starter) for
installation instructions.

## Development

Please refer to the
[contributing guidelines](https://github.com/IBM/carbon-components-angular/blob/master/README.md#contributing)
before starting any work.

## Code samples

```
npx @angular/cli new my-project --style=scsscd my-projectnpm i --save carbon-components-angular carbon-componentsCopy to clipboard
```

```bash
npx @angular/cli new my-project --style=scsscd my-projectnpm i --save carbon-components-angular carbon-components
```

```
@import '~carbon-components/scss/globals/scss/styles.scss';Copy to clipboard
```

```scss
@import '~carbon-components/scss/globals/scss/styles.scss';
```

```
npm startCopy to clipboard
```

```bash
npm start
```
