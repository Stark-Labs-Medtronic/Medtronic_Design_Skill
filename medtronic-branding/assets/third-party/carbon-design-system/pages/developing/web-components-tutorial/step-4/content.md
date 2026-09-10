# 4. Landing the principles – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/web-components-tutorial/step-4/

# 4. Landing the principles

With two pages comprised mostly of Carbon components, let’s revisit the landing
page and complete the principles section using Carbon pictograms and tokens.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#fork-clone-and-branch)

- [Review design](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#review-design)

- [The info section](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#the-info-section)

- [The info card](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#the-info-card)

- [Add styling](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#add-styling)

- [Check accessibility](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#check-accessibility)

- [Push to GitHub](https://carbondesignsystem.com/developing/web-components-tutorial/step-4/#push-to-github)

## Preview

Carbon provides a solid foundation for building web applications through its
color palette, layout, spacing, type, as well as common building blocks in the
form of components. So far, we’ve only used Carbon components to build out two
pages.

Other tutorials at this point build a component using Carbon, as we are staying
vanilla here, and we don’t want to turn this into a Web Component tutorial, we
will use a HTML template and BEM class names to prevent our CSS affecting
others.

A
[preview](https://carbon-tutorial-nextjs-git-step-5-carbon-design-system.vercel.app/)
of what you’ll build (see bottom of page):

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-web-components](https://github.com/carbon-design-system/carbon-tutorial-web-components)
that we’ll use as a starting point for each step. If you haven’t forked and
cloned that repository yet, and haven’t added the upstream remote, go ahead and
do so by following the [step 1
instructions]([previous step](https://carbondesignsystem.com/developing/web-components-tutorial/step-1#fork-clone-and-branch).

### Branch

With your repository all set up, let’s check out the branch for this tutorial
step’s starting point.

```

git fetch upstreamgit checkout -b step-4 upstream/step-4Copy to clipboard

```

**Note:** This builds on top of step 3, but be sure to check out the upstream
step 4 branch because it includes the static assets required to get through this
step.

### Build and start app

Install the app’s dependencies (in case you’re starting fresh in your current
directory and not continuing from the previous step):

```

pnpm iCopy to clipboard

```

Then, start the app:

```

pnpm devCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/web-components-tutorial/step-1#fork-clone-and-branch/step-3)
left off.

## Review design

Here’s what we’re building – an informational section that has a heading and
three subheadings. Each subheading has accompanying copy and a pictogram. We’ll
assume that this informational section is used elsewhere on the site, meaning
it’s a great opportunity to build it as a reusable component. As for naming,
we’ll call it an `InfoSection` with three `InfoCard`s as children.

Info section layout

## The info section

Inside `page-landing__r3` in `index.html` we will make a couple of small
changes. Add the class `info-section` to the `<cds-grid>`

```

index.htmlCopy to clipboard<cds-grid full-width class="info-section"></cds-grid>

```

and replace `The principles` and surrounding column with which changes the
column settings and provides a class for us to style the section heading.

```

index.htmlCopy to clipboard<cds-column  class="info-section__column page-landing__label"  sm="4"  md="8"  lg="16"  xlg="4">  <h3 class="info-section__heading">The Principles</h3></cds-column>

```

Style the `info-section__heading` with:

```

style.scssCopy to clipboard.info-section__heading {  @include type-style('heading-01');
  padding-block-end: $spacing-08;}

```

## The info card

At the bottom of `index.html` between the closing body and html tags add the
info card template.

### The template

```

index.htmlCopy to clipboard<template id="template--info-card">  <cds-column class="info-card" sm="4" md="8" lg="5" xlg="4">    <div class="info-card__uppder">      <h4 class="info-card__heading">        Carbon is        <strong class="info-card__heading--strong">thing goes here</strong>      </h4>      <p class="info-card__body">Body goes here</p>    </div>Show more

```

Before we make use of the template we need to remove the column settings from
the remaining three elements `page-landing__title` and replace with `info-card
to leave:

```

<div class="info-card">Carbon is open</div><div class="info-card">Carbon is modular</div><div class="info-card">Carbon is consistent</div>Copy to clipboard

```

### The script

As the script in this file only affects our landing page, first lets create
`landing.js`. Kicking things off by moving the breadcrumb and tabs import from
`main.js`.

```

landing.jsCopy to clipboardimport '@carbon/web-components/es/components/breadcrumb/index';import '@carbon/web-components/es/components/tabs/index';

```

Then add a script tag to `index.html` to import `landing.js`

```

index.htmlCopy to clipboard<script type="module" src="/landing.js"></script>

```

After making sure everything add, to `landing.js`, the script to create the info
card elements. First adding the data we will use to construct the info cards
from.

```

landing.jsCopy to clipboardconst infoCardDetails = [  {    strongMsg: 'Open',    bodyMsg: `It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute.`,    pictogramName: 'advocate',  },  {    strongMsg: 'Modular',    bodyMsg: `Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user.`,Show more

```

Then create the utility function `updateInfoCard`

```

landing.jsCopy to clipboardconst updateInfoCard = (here, { strongMsg, bodyMsg, pictogramName }) => {  const infoCardTemplate = document.querySelector(    'template#template--info-card'  );
  if (here && infoCardTemplate) {    const newInfoCard = infoCardTemplate.content.cloneNode(true);
    const strongEl = newInfoCard.querySelector('.info-card__heading--strong');Show more

```

Followed by a query to find the info card elements and a loop to add our data.

```

landing.jsCopy to clipboardconst infoCards = document.querySelectorAll('.info-card');[...infoCards].forEach((infoCard, index) => {  updateInfoCard(infoCard, infoCardDetails[index]);});

```

### The styles

Looking at the landing page you should see the updated information where
previously only the title was rendered. In order to complete our info card we
need to add some styling.

First up let’s make the picograms visible with the following.

```

style.scssCopy to clipboard.info-card__pictogram {  width: $spacing-10;  height: $spacing-10;  background-color: $text-primary;}
.info-card__pictogram--accelerating-transformation {  mask: url('/accelerating-transformation.svg') no-repeat center;}Show more

```

The remaining styling is to make the info cards pleasing on the eye. Use of
Carbon breakpoints, which also control the number of grid columns, keeps our
page looking great even on the narrowest of devices.

```

style.scssCopy to clipboard.info-card {  display: flex;  height: 300px;  flex-direction: column;  justify-content: space-between;  padding-inline: $spacing-05;  border-left: 1px solid $border-subtle;
  @include breakpoint-down(xlg) {Show more

```

## Check accessibility

We’ve added new markup and styles, so it’s a good practice to check
[Equal Access Checker](https://www.ibm.com/able/toolkit/tools/) and make sure
our rendered markup is on the right track for accessibility.

With the browser extension installed, Chrome in this example, open Dev Tools and
run Accessibility Assessment.

## Push to GitHub

That is it you are done. Just one more push to save your completion of step 4.

### Git commit and push

First, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard

```

Then, push to your repository:

```

git push -u origin step-4Copy to clipboard

```

**Note:** If your Git remote protocol is HTTPS instead of SSH, you may be
prompted to authenticate with GitHub when you push changes. If your GitHub
account has two-factor authentication enabled, we recommend that you follow
these instructions to
[create a personal access token for the command line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).
That lets you use your token instead of password when performing Git operations
over HTTPS.

## Code samples

```
git fetch upstreamgit checkout -b step-4 upstream/step-4Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b step-4 upstream/step-4
```

```
pnpm iCopy to clipboard
```

```bash
pnpm i
```

```
pnpm devCopy to clipboard
```

```bash
pnpm dev
```

```
index.htmlCopy to clipboard<cds-grid full-width class="info-section"></cds-grid>
```

```html
<cds-grid full-width class="info-section"></cds-grid>
```

```
index.htmlCopy to clipboard<cds-column  class="info-section__column page-landing__label"  sm="4"  md="8"  lg="16"  xlg="4">  <h3 class="info-section__heading">The Principles</h3></cds-column>
```

```html
<cds-column  class="info-section__column page-landing__label"  sm="4"  md="8"  lg="16"  xlg="4">  <h3 class="info-section__heading">The Principles</h3></cds-column>
```

```
style.scssCopy to clipboard.info-section__heading {  @include type-style('heading-01');
  padding-block-end: $spacing-08;}
```

```scss
.info-section__heading {  @include type-style('heading-01');
  padding-block-end: $spacing-08;}
```

```
index.htmlCopy to clipboard<template id="template--info-card">  <cds-column class="info-card" sm="4" md="8" lg="5" xlg="4">    <div class="info-card__uppder">      <h4 class="info-card__heading">        Carbon is        <strong class="info-card__heading--strong">thing goes here</strong>      </h4>      <p class="info-card__body">Body goes here</p>    </div>Show more
```

```html
<template id="template--info-card">  <cds-column class="info-card" sm="4" md="8" lg="5" xlg="4">    <div class="info-card__uppder">      <h4 class="info-card__heading">        Carbon is        <strong class="info-card__heading--strong">thing goes here</strong>      </h4>      <p class="info-card__body">Body goes here</p>    </div>
```

```
<div class="info-card">Carbon is open</div><div class="info-card">Carbon is modular</div><div class="info-card">Carbon is consistent</div>Copy to clipboard
```

```html
<div class="info-card">Carbon is open</div><div class="info-card">Carbon is modular</div><div class="info-card">Carbon is consistent</div>
```

```
landing.jsCopy to clipboardimport '@carbon/web-components/es/components/breadcrumb/index';import '@carbon/web-components/es/components/tabs/index';
```

```javascript
import '@carbon/web-components/es/components/breadcrumb/index';import '@carbon/web-components/es/components/tabs/index';
```

```
index.htmlCopy to clipboard<script type="module" src="/landing.js"></script>
```

```html
<script type="module" src="/landing.js"></script>
```

```
landing.jsCopy to clipboardconst infoCardDetails = [  {    strongMsg: 'Open',    bodyMsg: `It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute.`,    pictogramName: 'advocate',  },  {    strongMsg: 'Modular',    bodyMsg: `Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user.`,Show more
```

```javascript
const infoCardDetails = [  {    strongMsg: 'Open',    bodyMsg: `It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute.`,    pictogramName: 'advocate',  },  {    strongMsg: 'Modular',    bodyMsg: `Carbon's modularity ensures maximum flexibility in execution. It's components are designed to work seamlessly with each other, in whichever combination suits the needs of the user.`,
```

```
landing.jsCopy to clipboardconst updateInfoCard = (here, { strongMsg, bodyMsg, pictogramName }) => {  const infoCardTemplate = document.querySelector(    'template#template--info-card'  );
  if (here && infoCardTemplate) {    const newInfoCard = infoCardTemplate.content.cloneNode(true);
    const strongEl = newInfoCard.querySelector('.info-card__heading--strong');Show more
```

```javascript
const updateInfoCard = (here, { strongMsg, bodyMsg, pictogramName }) => {  const infoCardTemplate = document.querySelector(    'template#template--info-card'  );
  if (here && infoCardTemplate) {    const newInfoCard = infoCardTemplate.content.cloneNode(true);
    const strongEl = newInfoCard.querySelector('.info-card__heading--strong');
```

```
landing.jsCopy to clipboardconst infoCards = document.querySelectorAll('.info-card');[...infoCards].forEach((infoCard, index) => {  updateInfoCard(infoCard, infoCardDetails[index]);});
```

```javascript
const infoCards = document.querySelectorAll('.info-card');[...infoCards].forEach((infoCard, index) => {  updateInfoCard(infoCard, infoCardDetails[index]);});
```

```
style.scssCopy to clipboard.info-card__pictogram {  width: $spacing-10;  height: $spacing-10;  background-color: $text-primary;}
.info-card__pictogram--accelerating-transformation {  mask: url('/accelerating-transformation.svg') no-repeat center;}Show more
```

```scss
.info-card__pictogram {  width: $spacing-10;  height: $spacing-10;  background-color: $text-primary;}
.info-card__pictogram--accelerating-transformation {  mask: url('/accelerating-transformation.svg') no-repeat center;}
```

```
style.scssCopy to clipboard.info-card {  display: flex;  height: 300px;  flex-direction: column;  justify-content: space-between;  padding-inline: $spacing-05;  border-left: 1px solid $border-subtle;
  @include breakpoint-down(xlg) {Show more
```

```scss
.info-card {  display: flex;  height: 300px;  flex-direction: column;  justify-content: space-between;  padding-inline: $spacing-05;  border-left: 1px solid $border-subtle;
  @include breakpoint-down(xlg) {
```

```
git add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 4"
```

```
git push -u origin step-4Copy to clipboard
```

```bash
git push -u origin step-4
```
