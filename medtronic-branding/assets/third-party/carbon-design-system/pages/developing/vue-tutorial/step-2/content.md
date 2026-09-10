# 2. Building pages – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/vue-tutorial/step-2/

# 2. Building pages

Now that we have a Vue app using the UI Shell, it’s time to build a few static
pages. In this step, we’ll become comfortable with the Carbon grid and various
Carbon components.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#fork-clone-and-branch)

- [Install grid](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#install-grid)

- [Add landing page grid](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#add-landing-page-grid)

- [Build landing page](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#build-landing-page)

- [Style landing page](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#style-landing-page)

- [Add repo page grid](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#add-repo-page-grid)

- [Build repo page](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#build-repo-page)

- [Style repo page](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#style-repo-page)

- [Submit pull request](https://carbondesignsystem.com/developing/vue-tutorial/step-2/#submit-pull-request)

## Preview

A [preview](https://vue-step-3--carbon-tutorial-vue.netlify.com/) of what you’ll
build:

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-vue](https://github.com/carbon-design-system/carbon-tutorial-vue)
that we’ll use as a starting point for each step. If you haven’t forked and
cloned that repository yet, and haven’t added the upstream remote, go ahead and
do so by following the
[step 1 instructions](https://carbondesignsystem.com/developing/vue-tutorial/step-1#fork-clone-and-branch).

### Branch

With your repository all set up, let’s check out the branch for this tutorial
step’s starting point.

```

git fetch upstreamgit checkout -b vue-step-2 upstream/vue-step-2Copy to clipboard

```

**Note:** This builds on top of step 1, but be sure to check out the upstream
step 2 branch because it includes the static assets and fixes required to get
through this step.

### Build and start app

Install the app’s dependencies (in case you’re starting fresh in your current
directory and not continuing from the previous step):

```

yarnCopy to clipboard

```

Then, start the app:

```

yarn serveCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/vue-tutorial/step-1) left off.

## Install grid

In our last step we added our styles, component and icon packages. Now that
we’re building the pages with grid, we need to install one more Carbon package.
Stop your development environment (`CTRL-C`) and:

```

yarn add @carbon/gridCopy to clipboard

```

In `_carbon.scss`, we need to configure our grid to use 16 columns instead of
the default 12 columns. We do this by adding `grid-columns-16: true` in our
`$feature-flags`.

```

src/styles/_carbon.scssCopy to clipboard$feature-flags: (  grid-columns-16: true);

```

**Note:** Like before, the feature flag still needs to come before the Carbon
`styles.scss` import.

Run `yarn serve` so we can begin building.

## Add landing page grid

Let’s add our grid elements to `LandingPage.vue`.

In order to use the grid, we need to wrap everything in a
`<div class="cds--grid">`. We can continue to make rows by adding a
`<div class="cds--row">` inside the grid, as well as make columns within those
rows by adding `<div class="cds--col-[breakpoint]-[size]">`.

Our column sizes are specified by the number of columns they’ll be spanning. If
we use `cds--col-lg-4`, it means it’ll span 4 of the 16 columns. If we use
`cds--col-lg-8` it means it’ll span 8 of the 16 columns, and so on.

We’ve included the designs for this tutorial app in the `design.sketch` file
found as a top-level file in the `carbon-tutorial-vue` repository. But, if you
don’t have Sketch installed and available to inspect the design, we’ll provide
screenshots.

Landing page grid

**Pro tip:** `CTRL-L` toggles the layout in Sketch.

We’ll break this down into three rows. The first row with the gray background
doesn’t appear to need any columns. The second row with the white background
looks like it has two columns of different widths. The third row with the gray
background looks like it has four columns of equal width.

We’ll make rows like so:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<template>  <div class="cds--grid cds--grid--full-width landing-page">    <div class="cds--row landing-page__banner">      <div class="cds--col-lg-16">1</div>    </div>    <div class="cds--row landing-page__r2">      <div class="cds--col-md-4 cds--col-lg-7">7/16</div>      <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>    </div>Show more

```

We added a class of `cds--grid--full-width` to the grid container since our rows
need to expand the whole page without any margins. We also added some custom
classes like `landing-page`, `landing-page__banner`, `landing-page__r2`, etc.,
which we will use later.

Also, take notice of the second row. The tab content only covers 7 columns at
this large viewport to prevent overly-large line lengths, so we needed to add a
1 column offset `cds--offset-lg-1` to second column to fill the full 16 columns
in the grid. Then, both of those columns have `cds--col-md-4` classes so they
are of equal width at medium-sized viewports.

## Build landing page

We’ll start adding HTML elements and components by row.

### First row

In our first row we’ll use a `CvBreadcrumb` component.

We can now add our component to the first row, along with a header, like so:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__banner">  <div class="cds--col-lg-16">    <cv-breadcrumb noTrailingSlash>      <cv-breadcrumb-item>        <cv-link href="/">Getting started</cv-link>      </cv-breadcrumb-item>    </cv-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div>Show more

```

You may notice that the styles look off. Don’t worry, we’ll fix these later.

### Second row

In our second row we’ll use `CvTabs` and `CvButton` components.

Modify the second row to use the `Tab` component.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__r2">  <div class="cds--col cds--no-gutter">    <cv-tabs selected="0">      <cv-tab label="About">        <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">          <div class="cds--row landing-page__tab-content">            <div class="cds--col-md-4 cds--col-lg-7">7/16</div>            <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>          </div>Show more

```

**Note:** We’re using the grid for the page layout, but we also need to apply
the grid within the tab content. When doing so, make sure the nested grid has
the expected `grid` > `row` > `col` DOM structure.

Hold up! If you were to run
[DAP](https://www.ibm.com/able/dynamic-assessment-plug-in.html) to check for
accessibility violations, you’d see
`Multiple navigation landmarks must have unique labels specified with aria-label or aria-labelledby`
because both the `CvBreadcrumb` and `CvTabs` components use `<nav>` elements. To
fix, add `aria-label` to the `CvBreadcrumb` opening tag:

```

<cv-breadcrumb noTrailingSlash aria-label="Page navigation">Copy to clipboard

```

Same goes for the `CvTabs` opening tag:

```

<cv-tabs selected="0" aria-label="Tab navigation">Copy to clipboard

```

Give yourself a pat on the back if you actually ran the DAP tool. We’ll install
the DAP tool in a later step, so don’t worry if you didn’t.

Next, we’ll need to add a styling override to move the tabs to the right on
large viewports. Create a file `_carbon-overrides.scss` in
`src/views/LandingPage` with this declaration block.

```

src/views/LandingPage/_carbon-overrides.scssCopy to clipboard.landing-page__r2 .cds--tabs__nav {  right: 0;}

```

Then in `LandingPage.vue` add a style section with this import.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<style lang="scss">@import "./carbon-overrides";</style>

```

**Note:** We don’t have to include this in a separate file, but it’s nice to
keep overrides separate from your application’s styling so when migrating to
future Carbon versions and if there are breaking changes via different class
names, you have a consolidated list of styling declaration blocks to review. We
can now add our images and text for each column in the first `CvTab` in
`LandingPage.vue`.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<cv-tab label="About">  <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">    <div class="cds--row landing-page__tab-content">      <div class="cds--col-md-4 cds--col-lg-7">        <h2 class="landing-page__subheading">What is Carbon?</h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digital          products and experiences. With the IBM Design Language as          its foundation, the system consists of working code, designShow more

```

Now let’s set the image size in the style section of `LandingPage.vue`:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__illo {  max-width: 100%;}

```

Assuming that the second and third tab would have a similar design, we would set
them up in the same way. However, since our design specs don’t show those tabs,
we’ll leave the code as is.

### Third row

The third row will be created in a later tutorial, so we’ll just add the headers
for now.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__r3">  <div class="cds--col-md-4 cds--col-lg-4">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Open</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Modular</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Consistent</div></div>

```

## Style landing page

We’ve added basic layout styles in `LandingPage.vue`, so now let’s add type,
color and spacing styles to match the design. We’ll be using our
[spacing tokens](https://carbondesignsystem.com/elements/spacing/overview#spacing-scale). In a new file
`src/styles/_carbon-utils.scss`, add these imports at the **top** of the file so
we can use Carbon breakpoints, tokens, and typography Sass mixins and functions:

```

src/styles/_carbon-utils.scssCopy to clipboard@import 'carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family.scss';@import 'carbon-components/scss/globals/scss/vendor/@carbon/layout/scss/breakpoint.scss';@import 'carbon-components/scss/globals/scss/typography.scss';@import 'carbon-components/scss/globals/scss/vars.scss';

```

Adding these tokens, mixins etc. here means we can import them with a single
line into any component that needs them.

### Banner

Banner vertical spacing

**Pro tip:** `CTRL-G` toggles the grid in Sketch.

Back to `LandingPage.vue`, we need to add space above the breadcrumb and below
the heading. For that, add:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard@import '../../styles/carbon-utils';

```

with the other imports and

```

.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}Copy to clipboard

```

Referencing the [spacing token table](https://carbondesignsystem.com/elements/spacing/overview#spacing-scale),
`16px` can be set with the `$spacing-05` token. The design calls for `128px` of
space below the heading and that’s not in the spacing scale, we can achieve that
in Sass by multiplying 32px (`$spacing-07`) by 4. We could use `128px` or `8rem`
directly in our styling, but using our tokens preserves consistency should the
token values get updated in the future.

Looking at the design, we need a wall-to-wall light gray background behind the
banner and also behind the third row. This is a great opportunity to use a Sass
mixin. We could put this at the top of `LandingPage.vue`, but it’s best practice
to place mixins in a dedicated file, so create a `_mixins.scss` file in
`src/views/LandingPage`.

Add the following in `_mixins.scss`. Per the design we need to use Gray 10 for
our banner background color, which can be set with the `$ui-01`
[color token](https://www.carbondesignsystem.com/elements/color/usage). Also, we
want the background to extend into the grid’s outermost gutters to go the full
width of the viewport, so given the DOM structure, we can achieve that by
setting the background in an absolutely positioned pseudo element.

```

src/views/LandingPage/_mixins.scssCopy to clipboard@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-06;    top: 0;Show more

```

After you have created `_mixins.scss`, import it at the **top** of
`LandingPage.vue`. By now you should have three imports:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard@import '../../styles/carbon-utils';@import './carbon-overrides';@import './mixins';

```

Now to use the new mixin, update the `.landing-page__banner` declaration block
to:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}

```

Next, we can see that the `h1` is using the `heading-05` type token.

Banner heading type

The Sketch symbol naming is consistent with the development Sass tokens to help
translate design to development. So, looking up the
[type token](https://www.carbondesignsystem.com/elements/typography/productive),
we know to use `productive-heading-05`:

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__heading {  @include type-style('productive-heading-05');}

```

### Row two

For our second row, we need to fix the tabs vertical positioning to match the
design. By inspecting the tabs component, you can see that the tab height
computes to `40px`. We can use that to create our negative top margin in rem
units.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__r2 {  margin-top: rem(-40px);}

```

We also need to adjust our vertical spacing and type treatment. Like before,
it’s a matter of using spacing and type tokens like so:

Row 2 vertical spacing

**Note:** You may be wondering why there are vertical gaps between the type and
spacers. Each type token has a line height that’s suited for its font size. The
vertical spacers adjacently touch the line height boundaries and not the
baseline, for consistency as well as development ease so `margins` and
`paddings` don’t need to offset line heights.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include font-weight('semibold');}Show more

```

### Row three

Row 3 vertical spacing

Let’s also add some styles for the last row, even though that will get used
later in the tutorial. You’ll notice that we get to re-use the
`landing-page-background` mixin that we just created.

```

src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}

```

Ta-da! You should see a finished landing page! Now we can move on to the repo
page.

## Add repo page grid

Now in our `RepoPage.vue` we’ll add our grid containers in the template section.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard<template>  <div class="cds--grid cds--grid--full-width cds--grid--no-gutter repo-page">    <div class="cds--row repo-page__r1">      <div class="cds--col-lg-16">Data table will go here</div>    </div>  </div></template>

```

## Build repo page

We currently have `RepoPage.vue` that just contains a grid and placeholder
content for the time being. In the next tutorial step we’re going to be querying
an API to populate the `CvDataTable` component in this page. As a best practice
to separate data fetching from the presentation components, go ahead and create
a `RepoTable.vue` as a sibling to `RepoPage.vue` in `src/views/RepoPage`.

### Build data table

First, let’s pretend we’ve already built our table component and update
`RepoPage.vue` with a script section.

Import `RepoTable` in `RepoPage.vue`.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard<script>import RepoTable from "./RepoTable";
export default {  name: "RepoPage"};</script>

```

Then below the import, include the following arrays to pass into the `RepoTable`
component. We’ll be setting the `rows` array from an API in the next tutorial
step, but for now, static example rows will suffice.

```

src/views/RepoPage/RepoPage.vueCopy to clipboardconst headers = [  {    key: 'name',    header: 'Name',  },  {    key: 'createdAt',    header: 'Created',  },Show more

```

Next we need to make sure the RepoTable component and these arrays are available
to our `RepoPage` component template. Your component export should look like the
following to achieve this.

```

src/views/RepoPage/RepoPage.vueCopy to clipboardexport default {  name: 'RepoPage',  components: { RepoTable },  data() {    return {      headers,      rows,    };  },Show more

```

Here we used the data method of the component as the values logically are data
in our component.

Lastly in the `RepoPage.vue` template, we need to simply replace
`Data table will go here` with:

```

src/views/RepoPage/RepoPage.vueCopy to clipboard<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."/>

```

OK. So now our `RepoPage.vue` component is ready to use a component called
‘RepoTable’ so let’s create it so our page displays again.

First create a script section as follows:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<script>  export default {    name: 'RepoTable',    props: {      headers: Array,      rows: Array,      title: String,      helperText: String,    },Show more

```

In this component script we:

- Named our new component `RepoTable`.

- Added component properties for the headers and rows as well as two further
properties title and helperText.

- Added the computed properties columns and headers which transform headers and
rows into a format convenient for rendering with the CvDataTable components.

Next, let’s create the `RepoTable` template starting with the cv-data-table
component.

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<template>  <cv-data-table :columns="columns" :title="title" :helper-text="helperText">  </cv-data-table></template>

```

Here we pass in the columns, title and helper text. If you view this you will
see an empty table with headings.

Next add the rows inside of cv-data-table.

```

<template slot="data">  <cv-data-table-row v-for="(row, rowIndex) in data" :key="`${rowIndex}`"> </cv-data-table-row></template>Copy to clipboard

```

Here we use v-for to iterate through the data assigning a key and value to each
row. The rendered output may not appear to have changed, although if you inspect
using the developer tools you will find three empty rows. Next add the cell data
inside the `cv-data-table-row` component.

```

<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>Copy to clipboard

```

Again we’ve used the v-for directive to iterate through our data adding key,
value and the contents of the cell.

The last item we need to add is the description shown in the expanded content.
Add the following as a sibling of cv-data-table-cell component.

```

<template slot="expandedContent">{{ row.description }}</template>Copy to clipboard

```

Now you should have a working page rendering the sample content from the rows
array.

This component consumes our properties and returns a Carbon `CvDataTable`. As
for where the various `CvDataTable*` components came from? The
[CvDataTable story](http://vue.carbondesignsystem.com/?path=/story/components-cvdatatable--default)
in Storybook was used to put together the data table structure.

## Style repo page

Our styles for the repo page are mostly fine. We just need to update a few
vertical spacing issues.

In `RepoPage.vue`, add the following style section:

```

src/views/RepoPage/RepoPage.vueCopy to clipboard<style lang="scss">@import '../../styles/carbon-utils';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}</style>

```

Congratulations! We’ve now created our static repo page!

## Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step.

### Continuous integration (CI) check

Run the CI check to make sure we’re all set to submit a pull request.

```

yarn ci-checkCopy to clipboard

```

**Note:** Having issues running the CI check?
[Step 1](https://carbondesignsystem.com/developing/vue-tutorial/step-1#continuous-integration-ci-check) has
troubleshooting notes that may help.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard

```

Then, push to your repository:

```

git push origin vue-step-2Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/vue-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-vue](https://github.com/carbon-design-system/carbon-tutorial-vue)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`vue-step-2` into `base: vue-step-2`.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

## Code samples

```
git fetch upstreamgit checkout -b vue-step-2 upstream/vue-step-2Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b vue-step-2 upstream/vue-step-2
```

```
yarnCopy to clipboard
```

```bash
yarn
```

```
yarn serveCopy to clipboard
```

```bash
yarn serve
```

```
yarn add @carbon/gridCopy to clipboard
```

```bash
yarn add @carbon/grid
```

```
src/styles/_carbon.scssCopy to clipboard$feature-flags: (  grid-columns-16: true);
```

```css
$feature-flags: (  grid-columns-16: true);
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<template>  <div class="cds--grid cds--grid--full-width landing-page">    <div class="cds--row landing-page__banner">      <div class="cds--col-lg-16">1</div>    </div>    <div class="cds--row landing-page__r2">      <div class="cds--col-md-4 cds--col-lg-7">7/16</div>      <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>    </div>Show more
```

```html
<template>  <div class="cds--grid cds--grid--full-width landing-page">    <div class="cds--row landing-page__banner">      <div class="cds--col-lg-16">1</div>    </div>    <div class="cds--row landing-page__r2">      <div class="cds--col-md-4 cds--col-lg-7">7/16</div>      <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>    </div>
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__banner">  <div class="cds--col-lg-16">    <cv-breadcrumb noTrailingSlash>      <cv-breadcrumb-item>        <cv-link href="/">Getting started</cv-link>      </cv-breadcrumb-item>    </cv-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div>Show more
```

```html
<div class="cds--row landing-page__banner">  <div class="cds--col-lg-16">    <cv-breadcrumb noTrailingSlash>      <cv-breadcrumb-item>        <cv-link href="/">Getting started</cv-link>      </cv-breadcrumb-item>    </cv-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div>
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__r2">  <div class="cds--col cds--no-gutter">    <cv-tabs selected="0">      <cv-tab label="About">        <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">          <div class="cds--row landing-page__tab-content">            <div class="cds--col-md-4 cds--col-lg-7">7/16</div>            <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>          </div>Show more
```

```html
<div class="cds--row landing-page__r2">  <div class="cds--col cds--no-gutter">    <cv-tabs selected="0">      <cv-tab label="About">        <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">          <div class="cds--row landing-page__tab-content">            <div class="cds--col-md-4 cds--col-lg-7">7/16</div>            <div class="cds--col-md-4 cds--offset-lg-1 cds--col-lg-8">8/16</div>          </div>
```

```
<cv-breadcrumb noTrailingSlash aria-label="Page navigation">Copy to clipboard
```

```html
<cv-breadcrumb noTrailingSlash aria-label="Page navigation">
```

```
<cv-tabs selected="0" aria-label="Tab navigation">Copy to clipboard
```

```html
<cv-tabs selected="0" aria-label="Tab navigation">
```

```
src/views/LandingPage/_carbon-overrides.scssCopy to clipboard.landing-page__r2 .cds--tabs__nav {  right: 0;}
```

```scss
.landing-page__r2 .cds--tabs__nav {  right: 0;}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<style lang="scss">@import "./carbon-overrides";</style>
```

```scss
<style lang="scss">@import "./carbon-overrides";</style>
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<cv-tab label="About">  <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">    <div class="cds--row landing-page__tab-content">      <div class="cds--col-md-4 cds--col-lg-7">        <h2 class="landing-page__subheading">What is Carbon?</h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digital          products and experiences. With the IBM Design Language as          its foundation, the system consists of working code, designShow more
```

```html
<cv-tab label="About">  <div class="cds--grid cds--grid--no-gutter cds--grid--full-width">    <div class="cds--row landing-page__tab-content">      <div class="cds--col-md-4 cds--col-lg-7">        <h2 class="landing-page__subheading">What is Carbon?</h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digital          products and experiences. With the IBM Design Language as          its foundation, the system consists of working code, design
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__illo {  max-width: 100%;}
```

```scss
.landing-page__illo {  max-width: 100%;}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard<div class="cds--row landing-page__r3">  <div class="cds--col-md-4 cds--col-lg-4">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Open</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Modular</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Consistent</div></div>
```

```html
<div class="cds--row landing-page__r3">  <div class="cds--col-md-4 cds--col-lg-4">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Open</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Modular</div>  <div class="cds--col-md-4 cds--col-lg-4">Carbon is Consistent</div></div>
```

```
src/styles/_carbon-utils.scssCopy to clipboard@import 'carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family.scss';@import 'carbon-components/scss/globals/scss/vendor/@carbon/layout/scss/breakpoint.scss';@import 'carbon-components/scss/globals/scss/typography.scss';@import 'carbon-components/scss/globals/scss/vars.scss';
```

```scss
@import 'carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family.scss';@import 'carbon-components/scss/globals/scss/vendor/@carbon/layout/scss/breakpoint.scss';@import 'carbon-components/scss/globals/scss/typography.scss';@import 'carbon-components/scss/globals/scss/vars.scss';
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard@import '../../styles/carbon-utils';
```

```scss
@import '../../styles/carbon-utils';
```

```
.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}Copy to clipboard
```

```scss
.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}
```

```
src/views/LandingPage/_mixins.scssCopy to clipboard@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-06;    top: 0;Show more
```

```scss
@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-06;    top: 0;
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard@import '../../styles/carbon-utils';@import './carbon-overrides';@import './mixins';
```

```scss
@import '../../styles/carbon-utils';@import './carbon-overrides';@import './mixins';
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}
```

```scss
.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__heading {  @include type-style('productive-heading-05');}
```

```scss
.landing-page__heading {  @include type-style('productive-heading-05');}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__r2 {  margin-top: rem(-40px);}
```

```scss
.landing-page__r2 {  margin-top: rem(-40px);}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include font-weight('semibold');}Show more
```

```scss
.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include font-weight('semibold');}
```

```
src/views/LandingPage/LandingPage.vueCopy to clipboard.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}
```

```scss
.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard<template>  <div class="cds--grid cds--grid--full-width cds--grid--no-gutter repo-page">    <div class="cds--row repo-page__r1">      <div class="cds--col-lg-16">Data table will go here</div>    </div>  </div></template>
```

```html
<template>  <div class="cds--grid cds--grid--full-width cds--grid--no-gutter repo-page">    <div class="cds--row repo-page__r1">      <div class="cds--col-lg-16">Data table will go here</div>    </div>  </div></template>
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard<script>import RepoTable from "./RepoTable";
export default {  name: "RepoPage"};</script>
```

```javascript
<script>import RepoTable from "./RepoTable";
export default {  name: "RepoPage"};</script>
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardconst headers = [  {    key: 'name',    header: 'Name',  },  {    key: 'createdAt',    header: 'Created',  },Show more
```

```javascript
const headers = [  {    key: 'name',    header: 'Name',  },  {    key: 'createdAt',    header: 'Created',  },
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardexport default {  name: 'RepoPage',  components: { RepoTable },  data() {    return {      headers,      rows,    };  },Show more
```

```javascript
export default {  name: 'RepoPage',  components: { RepoTable },  data() {    return {      headers,      rows,    };  },
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."/>
```

```html
<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."/>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<script>  export default {    name: 'RepoTable',    props: {      headers: Array,      rows: Array,      title: String,      helperText: String,    },Show more
```

```javascript
<script>  export default {    name: 'RepoTable',    props: {      headers: Array,      rows: Array,      title: String,      helperText: String,    },
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<template>  <cv-data-table :columns="columns" :title="title" :helper-text="helperText">  </cv-data-table></template>
```

```html
<template>  <cv-data-table :columns="columns" :title="title" :helper-text="helperText">  </cv-data-table></template>
```

```
<template slot="data">  <cv-data-table-row v-for="(row, rowIndex) in data" :key="`${rowIndex}`"> </cv-data-table-row></template>Copy to clipboard
```

```html
<template slot="data">  <cv-data-table-row v-for="(row, rowIndex) in data" :key="`${rowIndex}`"> </cv-data-table-row></template>
```

```
<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>Copy to clipboard
```

```html
<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>
```

```
<template slot="expandedContent">{{ row.description }}</template>Copy to clipboard
```

```html
<template slot="expandedContent">{{ row.description }}</template>
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard<style lang="scss">@import '../../styles/carbon-utils';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}</style>
```

```scss
<style lang="scss">@import '../../styles/carbon-utils';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}</style>
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 2"
```

```
git push origin vue-step-2Copy to clipboard
```

```bash
git push origin vue-step-2
```
