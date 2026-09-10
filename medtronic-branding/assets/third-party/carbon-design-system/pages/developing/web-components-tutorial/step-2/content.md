# 2. Building pages – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/web-components-tutorial/step-2/

# 2. Building pages

Now that we have our app using the UI Shell, it’s time to build a few static
pages. In this step, we’ll become comfortable with the Carbon grid and various
Carbon components.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#fork-clone-and-branch)

- [Add landing page grid](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#add-landing-page-grid)

- [Build landing page](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#build-landing-page)

- [Style landing page](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#style-landing-page)

- [Add repo page grid](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#add-repo-page-grid)

- [Build repo page](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#build-repo-page)

- [Push to GitHub](https://carbondesignsystem.com/developing/web-components-tutorial/step-2/#push-to-github)

## Preview

A
[preview](https://carbon-tutorial-nextjs-git-step-3-carbon-design-system.vercel.app/)
of what you’ll build:

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

git fetch upstreamgit checkout -b step-2 upstream/step-2Copy to clipboard

```

**Note:** This builds on top of step 1, but be sure to check out the upstream
step 2 branch because it includes the static assets required to get through this
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
[previous step](https://carbondesignsystem.com/developing/web-components-tutorial/step-1#fork-clone-and-branch/step-1)
left off.

## Add landing page grid

Let’s add our grid elements to our `LandingPage` page component.

In order to use the grid, we need to wrap everything in a `<cds-grid>`. Because
we’re building with the new CSS Grid, we won’t be using typical rows. We’ll use
a combination of `<cds-column>` and nested subgrids to create our layout.

The CSS Grid is a 16 column grid. We will specify the span of a `<cds-column>`
using the `sm`, `md`, and `lg` attributes. For example,
`<cds-column sm="4" md="8" lg="8"/>` means the column will span 4/4 columns at
the small breakpoint, 8/8 columns at the medium breakpoint, 8/16 columns at the
large breakpoint.

First in `main.js` we need to add the grid component.

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/grid/index';

```

Then in `index.html` replace `LANDING PAGE` with

```

index.htmlCopy to clipboard<cds-grid class="page page-landing" full-width>  <cds-column class="page-landing__banner" span="100%"> 1 </cds-column>  <cds-column class="page-landing__r2" span="100%">    <cds-grid full-width>      <cds-column class="page-landing__tab-content" sm="4" md="4" lg="7">        7/16      </cds-column>      <cds-column sm="4" md="4" lg="span:8 start:9"> 8/16 </cds-column>    </cds-grid>Show more

```

**Grid education** There are many options for the Carbon Grid. For more
information review
[2x Grid](https://carbondesignsystem.com/elements/2x-grid/overview/) on the
Carbon Design System website. If apply classes manually it is also well worth
checking out the
[CSS Grid Demo](https://carbon-elements.netlify.app/grid/examples/css-grid/) to

Then import the grid styles in `style.scss`.

```

style.scssCopy to clipboard@use '@carbon/styles/scss/grid';

```

We’ve included the designs for this tutorial app in the `design.figma` file
found as a top-level file in the `carbon-tutorial` repository. But, if you don’t
have Figma installed and available to inspect the design, we’ll provide
screenshots.

Landing page grid

**Pro tip:** `CTRL-L` toggles the layout in Figma.

## Build landing page

We’ll start adding HTML elements and components by row.

### First row

Banner vertical spacing

In our first row we’ll need a `Breadcrumb` component. First, let’s import the
components we need.

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/breadcrumb/index';

```

We can now add our component to the first row, replace the content of the `div`
with class `page-landing__banner` with:

```

index.htmlCopy to clipboard<cds-breadcrumb noTrailingSlash aria-label="Page navigation">  <cds-breadcrumb-item>    <a href="./">Getting started</a>  </cds-breadcrumb-item></cds-breadcrumb><h1 class="page-landing__heading">Design &amp; build with Carbon</h1>

```

### Second row

In our second row we’ll need `Tabs` and `Button` components. Add the following
import:

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/tabs/index';

```

The tabs come next going inside `page-landing__r2` and before `<cds-grid>`.

```

index.htmlCopy to clipboard<cds-tabs value="about" class="page-landing__tabs">  <cds-tab id="tab-about" value="about" target="panel-about">About</cds-tab>  <cds-tab id="tab-design" value="design" target="panel-design">Design</cds-tab>  <cds-tab id="tab-develop" value="develop" target="panel-develop"    >Develop</cds-tab  ></cds-tabs>

```

Each of the `cds-tab` components has a `target` attribute. This is used to
identify the content visible when that tab is selected.

Wrap the subgrid element immediately after the closing `</cds-tabs>` with the
following. This is where we will place our first tab panel and a containing
element for all three panels.

```

index.htmlCopy to clipboard<div class="page-landing__tab-panels">  <div id="panel-about" role="tabpanel" aria-labelledby="tab-about">    ... grid element is here  </div></div>

```

Replace the content of the first column `7/16` with:

```

index.htmlCopy to clipboard<h3 class="page-landing__subheading">What is Carbon?</h3><p class="page-landing__p">  Carbon is IBM’s open-source design system for digital products and  experiences. With the IBM Design Language as its foundation, the system  consists of working code, design tools and resources, human interface  guidelines, and a vibrant community of contributors.</p><cds-button>Learn more</cds-button>

```

The second column content `8/16` is replaced with:

```

index.htmlCopy to clipboard<img  class="page-landing__illo"  src="./tab-illo.png"  alt="Carbon illustration"  width="640"  height="498" />

```

The `tab-illo.png` image is already located in the `public` folder.

After the closing `</div>` of `id="panel-about"`, inside the new
`page-landing__tab-panels` we add two further tab panels. This one

```

index.htmlCopy to clipboard<cds-grid full-width>  <cds-column span="100%">    <div class="page-landing__tab-content">      <p class="page-landing__p">        Rapidly build beautiful and accessible experiences. The Carbon kit        contains all resources you need to get started.      </p>    </div>  </cds-column>Show more

```

and

```

index.htmlCopy to clipboard<div id="panel-develop" role="tabpanel" aria-labelledby="tab-develop">  <cds-grid full-width>    <cds-column span="100%">      <div class="page-landing__tab-content">        <p class="page-landing__p">          Carbon provides components and styles for all. Whether using Vanilla,          Web Components, React, or another reactive library, you can build with          Carbon.        </p>Show more

```

### Third row

Here we replace all four columns entirely adding some offsets for medium and
large column sizes after the first column.

```

index.htmlCopy to clipboard<cds-column class="page-landing__label" sm="4" md="2" lg="4">  The principles</cds-column><cds-column  class="page-landing__title"  sm="4"  md="span:6 start:3"  lg="span:4 start:5">  Carbon is openShow more

```

## Style landing page

### Page and tab layout

For consistent vertical spacing across page add the following SCSS.

```

style.scssCopy to clipboard@use '@carbon/styles/scss/breakpoint' as *; /* add near top of file */
.page :where(.page-landing__banner, .page-landing__r2, .page-landing__r3) {  padding-inline: $spacing-06;  margin-inline: 0;
  @include breakpoint-up(md) {    margin-inline: -1 * $spacing-05;  }Show more

```

### First row

Row one styling is fairly straight forward with some typography and positional
adjustment so to align it with our other content.

```

style.scssCopy to clipboard.page-landing__banner {  padding-block: $spacing-05 $spacing-13;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}
.page-landing__heading {  @include type-style('productive-heading-05');
Show more

```

### Second row

The styling for the second row adds further layout and typography changes. It
also positions the image and prevents it from causing horizontal overflow. In
order to make use of the Carbon SCSS mixin `breakpoint-down` we also add the
breakpoint import to our list of `@use` near the top of the file.

```

style.scssCopy to clipboard.page-landing__illo {  max-width: 100%;  float: inline-end;  height: auto;}
@include breakpoint-down(md) {  .page-landing__illo {    max-width: 528px;Show more

```

### Third row

```

style.scssCopy to clipboard.page-landing__r3 {  padding-block: $spacing-09;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}

```

Ta-da! You should see a step 2 complete landing page! Now we can move on to the
repo page.

## Build repo page

### Add a grid to contain our content

Now in our `repositories` page we will first add a grid wrapping
`REPOSITORIES PAGE`

```

repositories.htmlCopy to clipboard<cds-grid class="page page-repositories" full-width>  <cds-column class="repo-page__r1" span="100%"> REPOSITORIES PAGE </cds-column></cds-grid>

```

Add a minimal amount of styling to move our content away from the edge of the
page in `style.scss`.

```

.repo-page__r1 {  padding-block: $spacing-05;}Copy to clipboard

```

### Adding a table

Before we can add the table we need to import the web component. As this is only
used in our `repositories.html` page lets create a new script file `repos.js`
and then add.

```

repos.jsCopy to clipboardimport '@carbon/web-components/es/components/data-table/index.js';

```

We need to include this file in `repositories.html` which we can do by adding
the following next to the script tag that includes `main.js`.

```

repositories.htmlCopy to clipboard<script type="module" src="/repos.js"></script>

```

Next we add the table header and column titles to replace the text
`REPOSITORIES PAGE`

```

repositories.htmlCopy to clipboard<cds-table expandable>  <cds-table-header-title slot="title"    >Carbon Repositories</cds-table-header-title  >  <cds-table-header-description slot="description"    >A collection of public Carbon repositories.</cds-table-header-description  >  <cds-table-head>    <cds-table-header-row>Show more

```

The table header should already be visible on the repositories page.

Now we can add the rows replacing `Table body goes here` with:

```

repositories.htmlCopy to clipboard<cds-table-row>  <cds-table-cell>Repo 1</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>123</cds-table-cell>  <cds-table-cell>456</cds-table-cell>  <cds-table-cell>Links</cds-table-cell></cds-table-row><cds-table-expanded-row>Repo description</cds-table-expanded-row>Show more

```

### Using HTML templates

With the app running we can see that the repositories page now hosts a table.
However, it is not realistic to populate a table with hard coded data way so
we’ll refactor to build the table from data.

This involves the use of HTML Templates, take a look at
[W3 Schools](https://www.w3schools.com/tags/tag_template.asp) if you need a
quick refresh.

In `index.html` remove the contents of the `<cds-table-body>` tag and return it
to `Table body goes here`.

Then before the end of the html tag and after the body closing tag add the
following to define our table row template.

```

repositories.htmlCopy to clipboard<template id="template--table-row">  <cds-table-row>    <cds-table-cell key="name">Repo 1</cds-table-cell>    <cds-table-cell key="created">Date</cds-table-cell>    <cds-table-cell key="updated">Date</cds-table-cell>    <cds-table-cell key="openIssues">123</cds-table-cell>    <cds-table-cell key="stars">456</cds-table-cell>    <cds-table-cell key="links">Links</cds-table-cell>  </cds-table-row>Show more

```

Next in `repos.js` add the following data that we will use to populate the table
rows.

```

repos.jsCopy to clipboard// cds-table-row datalet data = [  {    name: 'Repo A',    created: 'Date',    updated: 'Date',    openIssues: 123,    stars: 456,    links: 'Links',Show more

```

Next we create the function `updateTable` and make a call to it to populate add
our rows.

```

repos.jsCopy to clipboardconst updateTable = () => {  const tableRowTemplate = document.querySelector(    'template#template--table-row'  );  const tableBody = document.querySelector('cds-table-body');  if (tableBody && tableRowTemplate) {    tableBody.innerHTML = '';    // iterate over data and render rows    data.forEach((row) => {Show more

```

Verify that the table rows are being generated by changing the data and running
the app.

Congratulations! We’ve now created our static repo page!

## Push to GitHub

That is it you are done. Just one more push to save your completion of step 2.

### Git commit and push

First, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard

```

Then, push to your repository:

```

git push -u origin step-2Copy to clipboard

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
git fetch upstreamgit checkout -b step-2 upstream/step-2Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b step-2 upstream/step-2
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
main.jsCopy to clipboardimport '@carbon/web-components/es/components/grid/index';
```

```javascript
import '@carbon/web-components/es/components/grid/index';
```

```
index.htmlCopy to clipboard<cds-grid class="page page-landing" full-width>  <cds-column class="page-landing__banner" span="100%"> 1 </cds-column>  <cds-column class="page-landing__r2" span="100%">    <cds-grid full-width>      <cds-column class="page-landing__tab-content" sm="4" md="4" lg="7">        7/16      </cds-column>      <cds-column sm="4" md="4" lg="span:8 start:9"> 8/16 </cds-column>    </cds-grid>Show more
```

```html
<cds-grid class="page page-landing" full-width>  <cds-column class="page-landing__banner" span="100%"> 1 </cds-column>  <cds-column class="page-landing__r2" span="100%">    <cds-grid full-width>      <cds-column class="page-landing__tab-content" sm="4" md="4" lg="7">        7/16      </cds-column>      <cds-column sm="4" md="4" lg="span:8 start:9"> 8/16 </cds-column>    </cds-grid>
```

```
style.scssCopy to clipboard@use '@carbon/styles/scss/grid';
```

```scss
@use '@carbon/styles/scss/grid';
```

```
main.jsCopy to clipboardimport '@carbon/web-components/es/components/breadcrumb/index';
```

```javascript
import '@carbon/web-components/es/components/breadcrumb/index';
```

```
index.htmlCopy to clipboard<cds-breadcrumb noTrailingSlash aria-label="Page navigation">  <cds-breadcrumb-item>    <a href="./">Getting started</a>  </cds-breadcrumb-item></cds-breadcrumb><h1 class="page-landing__heading">Design &amp; build with Carbon</h1>
```

```html
<cds-breadcrumb noTrailingSlash aria-label="Page navigation">  <cds-breadcrumb-item>    <a href="./">Getting started</a>  </cds-breadcrumb-item></cds-breadcrumb><h1 class="page-landing__heading">Design &amp; build with Carbon</h1>
```

```
main.jsCopy to clipboardimport '@carbon/web-components/es/components/tabs/index';
```

```javascript
import '@carbon/web-components/es/components/tabs/index';
```

```
index.htmlCopy to clipboard<cds-tabs value="about" class="page-landing__tabs">  <cds-tab id="tab-about" value="about" target="panel-about">About</cds-tab>  <cds-tab id="tab-design" value="design" target="panel-design">Design</cds-tab>  <cds-tab id="tab-develop" value="develop" target="panel-develop"    >Develop</cds-tab  ></cds-tabs>
```

```html
<cds-tabs value="about" class="page-landing__tabs">  <cds-tab id="tab-about" value="about" target="panel-about">About</cds-tab>  <cds-tab id="tab-design" value="design" target="panel-design">Design</cds-tab>  <cds-tab id="tab-develop" value="develop" target="panel-develop"    >Develop</cds-tab  ></cds-tabs>
```

```
index.htmlCopy to clipboard<div class="page-landing__tab-panels">  <div id="panel-about" role="tabpanel" aria-labelledby="tab-about">    ... grid element is here  </div></div>
```

```html
<div class="page-landing__tab-panels">  <div id="panel-about" role="tabpanel" aria-labelledby="tab-about">    ... grid element is here  </div></div>
```

```
index.htmlCopy to clipboard<h3 class="page-landing__subheading">What is Carbon?</h3><p class="page-landing__p">  Carbon is IBM’s open-source design system for digital products and  experiences. With the IBM Design Language as its foundation, the system  consists of working code, design tools and resources, human interface  guidelines, and a vibrant community of contributors.</p><cds-button>Learn more</cds-button>
```

```html
<h3 class="page-landing__subheading">What is Carbon?</h3><p class="page-landing__p">  Carbon is IBM’s open-source design system for digital products and  experiences. With the IBM Design Language as its foundation, the system  consists of working code, design tools and resources, human interface  guidelines, and a vibrant community of contributors.</p><cds-button>Learn more</cds-button>
```

```
index.htmlCopy to clipboard<img  class="page-landing__illo"  src="./tab-illo.png"  alt="Carbon illustration"  width="640"  height="498" />
```

```html
<img  class="page-landing__illo"  src="./tab-illo.png"  alt="Carbon illustration"  width="640"  height="498" />
```

```
index.htmlCopy to clipboard<cds-grid full-width>  <cds-column span="100%">    <div class="page-landing__tab-content">      <p class="page-landing__p">        Rapidly build beautiful and accessible experiences. The Carbon kit        contains all resources you need to get started.      </p>    </div>  </cds-column>Show more
```

```html
<cds-grid full-width>  <cds-column span="100%">    <div class="page-landing__tab-content">      <p class="page-landing__p">        Rapidly build beautiful and accessible experiences. The Carbon kit        contains all resources you need to get started.      </p>    </div>  </cds-column>
```

```
index.htmlCopy to clipboard<div id="panel-develop" role="tabpanel" aria-labelledby="tab-develop">  <cds-grid full-width>    <cds-column span="100%">      <div class="page-landing__tab-content">        <p class="page-landing__p">          Carbon provides components and styles for all. Whether using Vanilla,          Web Components, React, or another reactive library, you can build with          Carbon.        </p>Show more
```

```html
<div id="panel-develop" role="tabpanel" aria-labelledby="tab-develop">  <cds-grid full-width>    <cds-column span="100%">      <div class="page-landing__tab-content">        <p class="page-landing__p">          Carbon provides components and styles for all. Whether using Vanilla,          Web Components, React, or another reactive library, you can build with          Carbon.        </p>
```

```
index.htmlCopy to clipboard<cds-column class="page-landing__label" sm="4" md="2" lg="4">  The principles</cds-column><cds-column  class="page-landing__title"  sm="4"  md="span:6 start:3"  lg="span:4 start:5">  Carbon is openShow more
```

```html
<cds-column class="page-landing__label" sm="4" md="2" lg="4">  The principles</cds-column><cds-column  class="page-landing__title"  sm="4"  md="span:6 start:3"  lg="span:4 start:5">  Carbon is open
```

```
style.scssCopy to clipboard@use '@carbon/styles/scss/breakpoint' as *; /* add near top of file */
.page :where(.page-landing__banner, .page-landing__r2, .page-landing__r3) {  padding-inline: $spacing-06;  margin-inline: 0;
  @include breakpoint-up(md) {    margin-inline: -1 * $spacing-05;  }Show more
```

```scss
@use '@carbon/styles/scss/breakpoint' as *; /* add near top of file */
.page :where(.page-landing__banner, .page-landing__r2, .page-landing__r3) {  padding-inline: $spacing-06;  margin-inline: 0;
  @include breakpoint-up(md) {    margin-inline: -1 * $spacing-05;  }
```

```
style.scssCopy to clipboard.page-landing__banner {  padding-block: $spacing-05 $spacing-13;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}
.page-landing__heading {  @include type-style('productive-heading-05');
Show more
```

```scss
.page-landing__banner {  padding-block: $spacing-05 $spacing-13;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}
.page-landing__heading {  @include type-style('productive-heading-05');
```

```
style.scssCopy to clipboard.page-landing__illo {  max-width: 100%;  float: inline-end;  height: auto;}
@include breakpoint-down(md) {  .page-landing__illo {    max-width: 528px;Show more
```

```scss
.page-landing__illo {  max-width: 100%;  float: inline-end;  height: auto;}
@include breakpoint-down(md) {  .page-landing__illo {    max-width: 528px;
```

```
style.scssCopy to clipboard.page-landing__r3 {  padding-block: $spacing-09;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}
```

```scss
.page-landing__r3 {  padding-block: $spacing-09;  background: $layer-01;  box-shadow: $spacing-06 0 0 $layer-01, -1 * $spacing-06 0 0 $layer-01;}
```

```
repositories.htmlCopy to clipboard<cds-grid class="page page-repositories" full-width>  <cds-column class="repo-page__r1" span="100%"> REPOSITORIES PAGE </cds-column></cds-grid>
```

```html
<cds-grid class="page page-repositories" full-width>  <cds-column class="repo-page__r1" span="100%"> REPOSITORIES PAGE </cds-column></cds-grid>
```

```
.repo-page__r1 {  padding-block: $spacing-05;}Copy to clipboard
```

```scss
.repo-page__r1 {  padding-block: $spacing-05;}
```

```
repos.jsCopy to clipboardimport '@carbon/web-components/es/components/data-table/index.js';
```

```javascript
import '@carbon/web-components/es/components/data-table/index.js';
```

```
repositories.htmlCopy to clipboard<script type="module" src="/repos.js"></script>
```

```html
<script type="module" src="/repos.js"></script>
```

```
repositories.htmlCopy to clipboard<cds-table expandable>  <cds-table-header-title slot="title"    >Carbon Repositories</cds-table-header-title  >  <cds-table-header-description slot="description"    >A collection of public Carbon repositories.</cds-table-header-description  >  <cds-table-head>    <cds-table-header-row>Show more
```

```html
<cds-table expandable>  <cds-table-header-title slot="title"    >Carbon Repositories</cds-table-header-title  >  <cds-table-header-description slot="description"    >A collection of public Carbon repositories.</cds-table-header-description  >  <cds-table-head>    <cds-table-header-row>
```

```
repositories.htmlCopy to clipboard<cds-table-row>  <cds-table-cell>Repo 1</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>123</cds-table-cell>  <cds-table-cell>456</cds-table-cell>  <cds-table-cell>Links</cds-table-cell></cds-table-row><cds-table-expanded-row>Repo description</cds-table-expanded-row>Show more
```

```html
<cds-table-row>  <cds-table-cell>Repo 1</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>Date</cds-table-cell>  <cds-table-cell>123</cds-table-cell>  <cds-table-cell>456</cds-table-cell>  <cds-table-cell>Links</cds-table-cell></cds-table-row><cds-table-expanded-row>Repo description</cds-table-expanded-row>
```

```
repositories.htmlCopy to clipboard<template id="template--table-row">  <cds-table-row>    <cds-table-cell key="name">Repo 1</cds-table-cell>    <cds-table-cell key="created">Date</cds-table-cell>    <cds-table-cell key="updated">Date</cds-table-cell>    <cds-table-cell key="openIssues">123</cds-table-cell>    <cds-table-cell key="stars">456</cds-table-cell>    <cds-table-cell key="links">Links</cds-table-cell>  </cds-table-row>Show more
```

```html
<template id="template--table-row">  <cds-table-row>    <cds-table-cell key="name">Repo 1</cds-table-cell>    <cds-table-cell key="created">Date</cds-table-cell>    <cds-table-cell key="updated">Date</cds-table-cell>    <cds-table-cell key="openIssues">123</cds-table-cell>    <cds-table-cell key="stars">456</cds-table-cell>    <cds-table-cell key="links">Links</cds-table-cell>  </cds-table-row>
```

```
repos.jsCopy to clipboard// cds-table-row datalet data = [  {    name: 'Repo A',    created: 'Date',    updated: 'Date',    openIssues: 123,    stars: 456,    links: 'Links',Show more
```

```javascript
// cds-table-row datalet data = [  {    name: 'Repo A',    created: 'Date',    updated: 'Date',    openIssues: 123,    stars: 456,    links: 'Links',
```

```
repos.jsCopy to clipboardconst updateTable = () => {  const tableRowTemplate = document.querySelector(    'template#template--table-row'  );  const tableBody = document.querySelector('cds-table-body');  if (tableBody && tableRowTemplate) {    tableBody.innerHTML = '';    // iterate over data and render rows    data.forEach((row) => {Show more
```

```javascript
const updateTable = () => {  const tableRowTemplate = document.querySelector(    'template#template--table-row'  );  const tableBody = document.querySelector('cds-table-body');  if (tableBody && tableRowTemplate) {    tableBody.innerHTML = '';    // iterate over data and render rows    data.forEach((row) => {
```

```
git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 2"
```

```
git push -u origin step-2Copy to clipboard
```

```bash
git push -u origin step-2
```
