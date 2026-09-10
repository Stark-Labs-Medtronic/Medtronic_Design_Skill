# 4. Creating components – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/react-tutorial/step-4/

# 4. Creating components

With two pages comprised entirely of Carbon components, let’s revisit the
landing page and build a couple components of our own by using Carbon pictograms
and tokens.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/react-tutorial/step-4/#fork-clone-and-branch)

- [Review design](https://carbondesignsystem.com/developing/react-tutorial/step-4/#review-design)

- [Create components](https://carbondesignsystem.com/developing/react-tutorial/step-4/#create-components)

- [Use components](https://carbondesignsystem.com/developing/react-tutorial/step-4/#use-components)

- [Add styling](https://carbondesignsystem.com/developing/react-tutorial/step-4/#add-styling)

- [Check accessibility](https://carbondesignsystem.com/developing/react-tutorial/step-4/#check-accessibility)

- [Submit pull request](https://carbondesignsystem.com/developing/react-tutorial/step-4/#submit-pull-request)

## Preview

Carbon provides a solid foundation for building web applications through its
color palette, layout, spacing, type, as well as common building blocks in the
form of components. So far, we’ve only used Carbon components to build out two
pages.

Next, we’re going to use Carbon assets to build application-specific components.
We’ll do so by including accessibility and responsive considerations all
throughout.

A
[preview](https://carbon-tutorial-nextjs-git-v11-next-step-5-carbon-design-system.vercel.app/)
of what you’ll build (see bottom of page):

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-nextjs](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
that we’ll use as a starting point for each step. If you haven’t forked and
cloned that repository yet, and haven’t added the upstream remote, go ahead and
do so by following the
[step 1 instructions](https://carbondesignsystem.com/developing/react-tutorial/step-1#fork-clone-and-branch).

### Branch

With your repository all set up, let’s check out the branch for this tutorial
step’s starting point.

```

git fetch upstreamgit checkout -b v11-next-step-4 upstream/v11-next-step-4Copy to clipboard

```

**Note:** This builds on top of step 3, but be sure to check out the upstream
step 4 branch because it includes the static assets required to get through this
step.

### Build and start app

Install the app’s dependencies (in case you’re starting fresh in your current
directory and not continuing from the previous step):

```

yarnCopy to clipboard

```

Then, start the app:

```

yarn devCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/react-tutorial/step-3) left off.

## Review design

Here’s what we’re building – an informational section that has a heading and
three subheadings. Each subheading has accompanying copy and a pictogram. We’ll
assume that this informational section is used elsewhere on the site, meaning
it’s a great opportunity to build it as a reusable component. As for naming,
we’ll call it an `InfoSection` with three `InfoCard`s as children.

Info section layout

## Create components

First we need files for the components, so create an `Info` folder in
`src/components`. Even though we’re building multiple components, their names
all start with `Info`, so it makes sense to have them share one folder in
components. Create these files:

### Add files

```

src/components/Info├──_info.scss└──Info.jsCopy to clipboard

```

Import `_info.scss` in `app.scss` after all of the `tutorial-header.scss`
import.

```

src/app/globals.scssCopy to clipboard@use '@/components/Info/info';

```

### InfoSection component

Let’s create the parent component that includes the “The Principles” heading.
That markup currently looks like this in `LandingPage`:

```

src/app/home/page.jsCopy to clipboard<Column lg={16} md={8} sm={4} className="landing-page__r3">  <Grid>    <Column lg={4} md={2} sm={4}>      <h3 className="landing-page__label">The Principles</h3>    </Column>    <Column      lg={{ start: 5, span: 3 }}      md={{ start: 3, span: 6 }}      sm={4}Show more

```

We want to do a few things when abstracting it to a component. First, we only
want this component’s class names; we don’t want to include `landing-page__r3`
as that’s specific to the landing page. For that we’ll use React `props` so we
can pass in and use `props.className`.

We’ll also:

- Add component class names like `info-section`, `info-card`, and
`info-section__heading`

- We will be using the `Grid` and `Column` components

- Replace `The Principles` with `{props.heading}`

- Replace columns 2 - 4 with `{props.children}`

Using `props` we can render any heading and any number of children components
(`InfoCard` that we’ll build soon.)

```

src/components/Info/Info.jsCopy to clipboardimport { Grid, Column } from '@carbon/react';
const InfoSection = (props) => (  <Grid className={`${props.className} info-section`}>    <Column md={8} lg={16} xlg={3}>      <h3 className="info-section__heading">{props.heading}</h3>    </Column>    {props.children}  </Grid>Show more

```

At this point let’s import our needed styles and add styling for the new class
names that we just added.

```

src/components/Info/_info.scssCopy to clipboard@use '@carbon/react/scss/type' as *;
.info-section__heading {  @include type-style('heading-01');  padding-bottom: $spacing-08;}

```

### InfoCard component

Next up we’re going to build a component for columns 2 - 4, which currently
looks like `<Column md={4} lg={4}>Carbon is Open</Column>`. At the bottom of
`Info.js`, add:

```

src/components/Info/Info.jsCopy to clipboardconst InfoCard = (props) => {  return (    <Column sm={4} md={8} lg={5} xlg={4} className="info-card">      <div>        <h4 className="info-card__heading">          {`${splitHeading[0]} `}          <strong>{splitHeading[1]}</strong>        </h4>        <p className="info-card__body">{props.body}</p>Show more

```

**Note:** Make sure to export the two components!

In doing so, we:

- Added `info-card` classes

- Used `props` to render the heading, body copy, and icon

- Set columns to match the grid

## Use components

Nothing is styled yet, but with our components built let’s put them to use. In
`LandingPage`, import the components towards the top of the file.

```

src/app/home/page.jsCopy to clipboardimport { InfoSection, InfoCard } from '@/components/Info/Info';

```

Next, we will install the pictograms we will use in the header.

```

yarn add @carbon/pictograms-reactCopy to clipboard

```

While we’re at the top of `LandingPage`, import the pictograms that we’ll need
as well.

```

src/app/home/page.jsCopy to clipboardimport {  Advocate,  Globe,  AcceleratingTransformation,} from '@carbon/pictograms-react';

```

With everything imported, replace the current:

```

src/app/home/page.jsCopy to clipboard<Grid>  <Column lg={16} md={8} sm={4} className="landing-page__r3">    <Grid>      <Column lg={4} md={2} sm={4}>        <h3 className="landing-page__label">The Principles</h3>      </Column>      <Column        lg={{ start: 5, span: 3 }}        md={{ start: 3, span: 6 }}Show more

```

With the new components:

```

src/app/home/page.jsCopy to clipboard<InfoSection heading="The Principles">  <InfoCard    heading="Carbon is Open"    body="It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    icon={() => <Advocate size={32} />}  />  <InfoCard    heading="Carbon is Modular"    body="Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user."Show more

```

**Note:** Now is a good time to resize your browser from phone to large viewport
widths to see how the responsive grid is working before we add further styling.

## Add styling

Here’s our design showing the spacing tokens that we need to add. We also need
to set type style and borders.

### Layout

Starting with layout, import the following carbon styles to
`src/components/Info/_info.scss`. Make sure to import the needed carbon styles.

```

src/components/Info/_info.scssCopy to clipboard@use '@carbon/react/scss/spacing' as *;@use '@carbon/react/scss/breakpoint' as *;@use '@carbon/react/scss/theme' as *;

```

We will then add the following styles to the same file to style our info cards.

```

src/components/Info/_info.scssCopy to clipboard.info-card {  margin-top: $spacing-09;  display: flex;  flex-direction: column;  padding-left: 1rem;
  svg {    margin-top: $spacing-09;  }Show more

```

Once you save, go ahead and resize your browser to see the responsive layout at
the different breakpoints. Make sure to review these color and spacing tokens.
There are also a few breakpoint mixins that may be new to you.

### Type

Our `InfoCard` headings look to be too small. We need to increase their font
sizes according to the design spec. Lets update the heading with the following
type style:

```

src/components/Info/_info.scssCopy to clipboard.info-card__heading {  @include type-style('productive-heading-03');}

```

Also, the design has the last word in each subheading as bold. To accomplish
that, add this helper function after the import in `Info.js`.

```

src/components/Info/Info.jsCopy to clipboard// Take in a phrase and separate the third word in an arrayfunction createArrayFromPhrase(phrase) {  const splitPhrase = phrase.split(' ');  const thirdWord = splitPhrase.pop();  return [splitPhrase.join(' '), thirdWord];}

```

Then, update `InfoCard` to use `createArrayFromPhrase`.

```

src/components/Info/Info.jsCopy to clipboardconst InfoCard = (props) => {  const splitHeading = createArrayFromPhrase(props.heading);
  return (    <Column sm={4} md={8} lg={4} className="info-card">      <h4 className="info-card__heading">        {`${splitHeading[0]} `}        <strong>{splitHeading[1]}</strong>      </h4>Show more

```

Finally, add the declaration block in `_info.scss` to set `InfoCard` body copy
styles and to bottom-align the pictograms.

```

src/components/Info/_info.scssCopy to clipboard.info-card__body {  margin-top: $spacing-06;  flex-grow: 1; // fill space so pictograms are bottom aligned  @include type-style('body-long-01');
  // prevent large line lengths between small and medium viewports  @include breakpoint-between(321px, md) {    max-width: 75%;  }Show more

```

## Check accessibility

We’ve added new markup and styles, so it’s a good practice to check
[Equal Access Checker](https://www.ibm.com/able/toolkit/tools/) and make sure
our rendered markup is on the right track for accessibility.

With the browser extension installed, Chrome in this example, open Dev Tools and
run Accessibility Assessment.

## Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step.

### Continuous integration (CI) check

Run the CI check to make sure we’re all set to submit a pull request.

```

yarn ci-checkCopy to clipboard

```

**Note:** Having issues running the CI check?
[Step 1](https://carbondesignsystem.com/developing/react-tutorial/step-1#continuous-integration-(ci)-check)
has troubleshooting notes that may help.

### Git commit and push

Before we can create a pull request, format your code, then stage and commit all
of your changes:

```

yarn formatgit add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard

```

Then, push to your repository:

```

git push origin v11-next-step-4Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/react-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-nextjs](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`v11-next-step-4` into `base: v11-next-step-4`.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

**Note:** If your PR fails the CircleCI test with the error
`Can't make a request in offline mode`, try running the following command:
`rm -rf .yarn-offline-mirror node_modules && yarn cache clean && yarn install`.
Add and commit the changes once this completes, and try pushing again.

## Code samples

```
git fetch upstreamgit checkout -b v11-next-step-4 upstream/v11-next-step-4Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b v11-next-step-4 upstream/v11-next-step-4
```

```
yarnCopy to clipboard
```

```bash
yarn
```

```
yarn devCopy to clipboard
```

```bash
yarn dev
```

```
src/components/Info├──_info.scss└──Info.jsCopy to clipboard
```

```bash
src/components/Info├──_info.scss└──Info.js
```

```
src/app/globals.scssCopy to clipboard@use '@/components/Info/info';
```

```scss
@use '@/components/Info/info';
```

```
src/app/home/page.jsCopy to clipboard<Column lg={16} md={8} sm={4} className="landing-page__r3">  <Grid>    <Column lg={4} md={2} sm={4}>      <h3 className="landing-page__label">The Principles</h3>    </Column>    <Column      lg={{ start: 5, span: 3 }}      md={{ start: 3, span: 6 }}      sm={4}Show more
```

```jsx
<Column lg={16} md={8} sm={4} className="landing-page__r3">  <Grid>    <Column lg={4} md={2} sm={4}>      <h3 className="landing-page__label">The Principles</h3>    </Column>    <Column      lg={{ start: 5, span: 3 }}      md={{ start: 3, span: 6 }}      sm={4}
```

```
src/components/Info/Info.jsCopy to clipboardimport { Grid, Column } from '@carbon/react';
const InfoSection = (props) => (  <Grid className={`${props.className} info-section`}>    <Column md={8} lg={16} xlg={3}>      <h3 className="info-section__heading">{props.heading}</h3>    </Column>    {props.children}  </Grid>Show more
```

```javascript
import { Grid, Column } from '@carbon/react';
const InfoSection = (props) => (  <Grid className={`${props.className} info-section`}>    <Column md={8} lg={16} xlg={3}>      <h3 className="info-section__heading">{props.heading}</h3>    </Column>    {props.children}  </Grid>
```

```
src/components/Info/_info.scssCopy to clipboard@use '@carbon/react/scss/type' as *;
.info-section__heading {  @include type-style('heading-01');  padding-bottom: $spacing-08;}
```

```scss
@use '@carbon/react/scss/type' as *;
.info-section__heading {  @include type-style('heading-01');  padding-bottom: $spacing-08;}
```

```
src/components/Info/Info.jsCopy to clipboardconst InfoCard = (props) => {  return (    <Column sm={4} md={8} lg={5} xlg={4} className="info-card">      <div>        <h4 className="info-card__heading">          {`${splitHeading[0]} `}          <strong>{splitHeading[1]}</strong>        </h4>        <p className="info-card__body">{props.body}</p>Show more
```

```javascript
const InfoCard = (props) => {  return (    <Column sm={4} md={8} lg={5} xlg={4} className="info-card">      <div>        <h4 className="info-card__heading">          {`${splitHeading[0]} `}          <strong>{splitHeading[1]}</strong>        </h4>        <p className="info-card__body">{props.body}</p>
```

```
src/app/home/page.jsCopy to clipboardimport { InfoSection, InfoCard } from '@/components/Info/Info';
```

```javascript
import { InfoSection, InfoCard } from '@/components/Info/Info';
```

```
yarn add @carbon/pictograms-reactCopy to clipboard
```

```bash
yarn add @carbon/pictograms-react
```

```
src/app/home/page.jsCopy to clipboardimport {  Advocate,  Globe,  AcceleratingTransformation,} from '@carbon/pictograms-react';
```

```javascript
import {  Advocate,  Globe,  AcceleratingTransformation,} from '@carbon/pictograms-react';
```

```
src/app/home/page.jsCopy to clipboard<Grid>  <Column lg={16} md={8} sm={4} className="landing-page__r3">    <Grid>      <Column lg={4} md={2} sm={4}>        <h3 className="landing-page__label">The Principles</h3>      </Column>      <Column        lg={{ start: 5, span: 3 }}        md={{ start: 3, span: 6 }}Show more
```

```jsx
<Grid>  <Column lg={16} md={8} sm={4} className="landing-page__r3">    <Grid>      <Column lg={4} md={2} sm={4}>        <h3 className="landing-page__label">The Principles</h3>      </Column>      <Column        lg={{ start: 5, span: 3 }}        md={{ start: 3, span: 6 }}
```

```
src/app/home/page.jsCopy to clipboard<InfoSection heading="The Principles">  <InfoCard    heading="Carbon is Open"    body="It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    icon={() => <Advocate size={32} />}  />  <InfoCard    heading="Carbon is Modular"    body="Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user."Show more
```

```javascript
<InfoSection heading="The Principles">  <InfoCard    heading="Carbon is Open"    body="It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    icon={() => <Advocate size={32} />}  />  <InfoCard    heading="Carbon is Modular"    body="Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user."
```

```
src/components/Info/_info.scssCopy to clipboard@use '@carbon/react/scss/spacing' as *;@use '@carbon/react/scss/breakpoint' as *;@use '@carbon/react/scss/theme' as *;
```

```scss
@use '@carbon/react/scss/spacing' as *;@use '@carbon/react/scss/breakpoint' as *;@use '@carbon/react/scss/theme' as *;
```

```
src/components/Info/_info.scssCopy to clipboard.info-card {  margin-top: $spacing-09;  display: flex;  flex-direction: column;  padding-left: 1rem;
  svg {    margin-top: $spacing-09;  }Show more
```

```scss
.info-card {  margin-top: $spacing-09;  display: flex;  flex-direction: column;  padding-left: 1rem;
  svg {    margin-top: $spacing-09;  }
```

```
src/components/Info/_info.scssCopy to clipboard.info-card__heading {  @include type-style('productive-heading-03');}
```

```scss
.info-card__heading {  @include type-style('productive-heading-03');}
```

```
src/components/Info/Info.jsCopy to clipboard// Take in a phrase and separate the third word in an arrayfunction createArrayFromPhrase(phrase) {  const splitPhrase = phrase.split(' ');  const thirdWord = splitPhrase.pop();  return [splitPhrase.join(' '), thirdWord];}
```

```javascript
// Take in a phrase and separate the third word in an arrayfunction createArrayFromPhrase(phrase) {  const splitPhrase = phrase.split(' ');  const thirdWord = splitPhrase.pop();  return [splitPhrase.join(' '), thirdWord];}
```

```
src/components/Info/Info.jsCopy to clipboardconst InfoCard = (props) => {  const splitHeading = createArrayFromPhrase(props.heading);
  return (    <Column sm={4} md={8} lg={4} className="info-card">      <h4 className="info-card__heading">        {`${splitHeading[0]} `}        <strong>{splitHeading[1]}</strong>      </h4>Show more
```

```javascript
const InfoCard = (props) => {  const splitHeading = createArrayFromPhrase(props.heading);
  return (    <Column sm={4} md={8} lg={4} className="info-card">      <h4 className="info-card__heading">        {`${splitHeading[0]} `}        <strong>{splitHeading[1]}</strong>      </h4>
```

```
src/components/Info/_info.scssCopy to clipboard.info-card__body {  margin-top: $spacing-06;  flex-grow: 1; // fill space so pictograms are bottom aligned  @include type-style('body-long-01');
  // prevent large line lengths between small and medium viewports  @include breakpoint-between(321px, md) {    max-width: 75%;  }Show more
```

```scss
.info-card__body {  margin-top: $spacing-06;  flex-grow: 1; // fill space so pictograms are bottom aligned  @include type-style('body-long-01');
  // prevent large line lengths between small and medium viewports  @include breakpoint-between(321px, md) {    max-width: 75%;  }
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
yarn formatgit add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard
```

```bash
yarn formatgit add --all && git commit -m "feat(tutorial): complete step 4"
```

```
git push origin v11-next-step-4Copy to clipboard
```

```bash
git push origin v11-next-step-4
```
