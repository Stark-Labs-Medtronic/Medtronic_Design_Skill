# 2. Building pages – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/angular-tutorial/step-2/

# 2. Building pages

Now that we have a base Angular app, it’s time to build a few static pages. In
this step, we’ll become comfortable with the Carbon UI Shell, grid and various
Carbon components.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#fork-clone-and-branch)

- [Add grid](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#add-grid)

- [Add landing page grid](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#add-landing-page-grid)

- [Build landing page](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#build-landing-page)

- [Style landing page](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#style-landing-page)

- [Add repo page grid](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#add-repo-page-grid)

- [Build repo page](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#build-repo-page)

- [Style repo page](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#style-repo-page)

- [Submit pull request](https://carbondesignsystem.com/developing/angular-tutorial/step-2/#submit-pull-request)

## Preview

A [preview](https://angular-step-3-carbon-tutorial.netlify.com/) of what you’ll
build:

**Note:** If you get lint errors when you copy the code from the snippets, run
`ng lint --fix` to fix them.

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
that we’ll use as a starting point for each step. If you haven’t forked and
cloned that repository yet, and haven’t added the upstream remote, go ahead and
do so by following the
[step 1 instructions](https://carbondesignsystem.com/developing/angular-tutorial/step-1#fork-clone-and-branch).

### Branch

With your repository all set up, let’s check out the branch for this tutorial
step’s starting point.

```

git fetch upstreamgit checkout -b angular-step-2 upstream/angular-step-2Copy to clipboard

```

**Note:** This builds on top of step 1, but be sure to check out the upstream
step 2 branch because it includes the static assets required to get through this
step.

### Build and start app

Install the app’s dependencies (in case you’re starting fresh in your current
directory and not continuing from the previous step):

```

npm installCopy to clipboard

```

Then, start the app:

```

npm startCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/angular-tutorial/step-1) left off.

## Add grid

In our last step we added our styles, components and icon packages. Now we are
going to build the pages with the grid component.

In `styles.scss`, we need to configure our grid to use 16 columns instead of the
default 12 columns. We do this by adding `grid-columns-16: true` in our
`$feature-flags`. `$feature-flags` **must** be set before importing from
`carbon-components`, otherwise they won’t take affect.

```

src/styles.scssCopy to clipboard$feature-flags: (  grid-columns-16: true);

```

Next we’ll import our Carbon grid component into `home.module.ts` and
`landing-page.component.spec.ts`.

```

src/app/home/landing-page/landing-page.component.spec.ts,src/app/home/home.module.tsCopy to clipboardimport { GridModule } from 'carbon-components-angular';...@NgModule({  ...  imports: [GridModule]})

```

## Add landing page grid

Let’s add our grid elements to `landing-page.component.html`.

In order to use the grid, we need to wrap everything in a `<div ibmGrid>`. We
can continue to make rows by adding a `<div ibmRow>` inside the grid, as well as
make columns within those rows by adding
`<div ibmCol [columnNumbers]="{'[breakpoint]': [size]}"`.

Our column sizes are specified by the number of columns they’ll be spanning. If
we use `[columnNumbers]="{'lg': 4}"`, it means it’ll span 4 of the 16 columns.
If we use `[columnNumbers]="{'lg': 8}"` it means it’ll span 8 of the 16 columns,
and so on.

We’ve included the designs for this tutorial app in the `design.sketch` file
found as a top-level file in the `carbon-tutorial-angular` repository. But, if
you don’t have Sketch installed and available to inspect the design, we provide
screenshots.

Landing page grid

**Pro tip:** `CTRL-L` toggles the layout in Sketch.

We’ll break this down into three rows. The first row with the gray background
doesn’t appear to need any columns. The second row with the white background
looks like it has two columns of different widths. The third row with the gray
background looks like it has four columns of equal width.

We’ll make rows like so:

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width landing-page">  <div ibmRow class="landing-page__banner">    <div ibmCol [columnNumbers]="{'lg': 16}">1</div>  </div>  <div ibmRow class="landing-page__r2">    <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>    <div ibmCol class="cds--offset-lg-1" [columnNumbers]="{'md': 4, 'lg': 7}">      8/16    </div>Show more

```

We added a class of `cds--grid--full-width` to the grid container since our rows
need to expand the whole page without any margins. We also added some custom
classes like `landing-page`, `landing-page__banner`, `landing-page__r2`, etc.,
which we will use later.

Also, take notice of the second row. The tab content only covers 7 columns at
this large viewport to prevent overly-large line lengths, so we needed to add a
1 column offset `cds--offset-lg-1` to the second column to fill the full 16
columns in the grid. Then, both of those columns have `'md': 4` so they are of
equal width at medium-sized viewports.

## Build landing page

We’ll start adding HTML elements and components by row.

### First row

In our first row we’ll need a `Breadcrumb` component. First, let’s import the
components we need in `home.module.ts` and `landing-page.component.spec.ts`.

```

src/app/home/home.module.tsCopy to clipboardimport { BreadcrumbModule, GridModule } from 'carbon-components-angular';

```

```

src/app/home/landing-page/landing-page.component.spec.tsCopy to clipboardimports: [BreadcrumbModule, GridModule];

```

We can now add our component to the first row, along with a header, like so:

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__banner">  <div ibmCol [columnNumbers]="{'lg': 16}">    <ibm-breadcrumb noTrailingSlash="true">      <ibm-breadcrumb-item href="/"> Getting started </ibm-breadcrumb-item>    </ibm-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div></div>

```

You may notice that the styles look off. Don’t worry, we’ll fix these later.

### Second row

In our second row we’ll need `Tabs` and `Button` components also in
`home.module.ts` and `landing-page.component.spec.ts`. We’ll update the
`carbon-components-angular` import to:

```

src/app/home/home.module.tsCopy to clipboardimport {  BreadcrumbModule,  ButtonModule,  GridModule,  TabsModule,} from 'carbon-components-angular';

```

```

src/app/home/landing-page/landing-page.component.spec.tsCopy to clipboardimports: [BreadcrumbModule, ButtonModule, GridModule, TabsModule];

```

Now we need to modify the second row to use the `Tab` component.

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r2">  <div ibmCol class="cds--no-gutter">    <ibm-tabs>      <ibm-tab heading="About">        <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">          <div ibmRow class="landing-page__tab-content">            <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>            <div              ibmColShow more

```

**Note:** We’re using the grid for the page layout, but we also need to apply
the grid within the tab content. When doing so, make sure the nested grid has
the expected `grid` > `row` > `col` DOM structure.

Hold up! If you were to run
[DAP](https://www.ibm.com/able/dynamic-assessment-plug-in.html) to check for
accessibility violations, you’d see
`Multiple navigation landmarks must have unique labels specified with aria-label or aria-labelledby`
because both the `Breadcrumb` and `Tabs` components use `<nav>` elements. To
fix, add `ariaLabel` to the `Breadcrumb` opening tag:

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<ibm-breadcrumb noTrailingSlash="true" ariaLabel="Page navigation">

```

Same goes for the `Tabs` opening tag:

```

<ibm-tabs ariaLabel="Tab navigation">Copy to clipboard

```

Next, we’ll need to add a styling override to move the tabs to the right on
large viewports, and tidy up the alignment of the grid. Create a file
`carbon-overrides.scss` in `src/assets/scss` with this declaration block.

```

src/assets/scss/carbon-overrides.scssCopy to clipboard// makes the grid fit the entire width of the page.cds--grid--full-width {  padding-left: 1rem;  padding-right: 1rem;}
// removes excess padding for nested full width grids.cds--grid--full-width .cds--grid--full-width {  padding-left: 0;Show more

```

Then in `styles.scss` add this import after the Carbon `styles.scss` import.

```

src/styles.scssCopy to clipboard@import './assets/scss/carbon-overrides.scss';

```

**Note:** We don’t have to include this in a separate file, but it’s nice to
keep overrides separate from your application’s styling so when migrating to
future Carbon versions and if there are breaking changes via different class
names, you have a consolidated list of styling declaration blocks to review.

We can now add our images and text for each column in the first `Tab` in
`landing-page.component.html`.

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<ibm-tab heading="About">  <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">    <div ibmRow class="landing-page__tab-content">      <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">        <h2 class="landing-page__subheading">          What is Carbon?        </h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digitalShow more

```

Now let’s download the image in `src/assets` and set the image size in
`landing-page.component.scss`:

```

curl -o tab-illo.png https://raw.githubusercontent.com/carbon-design-system/carbon-tutorial-vue/vue-step-3/src/assets/tab-illo.pngCopy to clipboard

```

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__illo {  max-width: 100%;}

```

Assuming that the second and third tab would have a similar design, we would set
them up in the same way. However, since our design specs don’t show those tabs,
we’ll leave the code as is.

### Third row

The third row will be created in a later tutorial, so we’ll just add the headers
for now.

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>

```

## Style landing page

We’ve added basic layout styles in `landing-page.component.scss` and
`styles.scss`, so now let’s add type, color and spacing styles to match the
design. We’ll be using our [spacing tokens](https://carbondesignsystem.com/elements/spacing/overview). In
`landing-page.component.scss`, add these imports at the **top** of the file so
we can use Carbon breakpoints, tokens, and typography Sass mixins and functions:

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family';@import '~carbon-components/scss/globals/scss/typography';

```

### Banner

Banner vertical spacing

**Pro tip:** `CTRL-G` toggles the grid in Sketch.

Now, we need to add a space above the breadcrumb and below the heading. For
that, add:

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}

```

Referencing the [spacing token table](https://carbondesignsystem.com/elements/spacing/overview#spacing-scale),
`16px` can be set with the `$spacing-05` token. The design calls for `128px` of
space below the heading and that’s not in the spacing scale, we can achieve that
in Sass by multiplying 32px (`$spacing-07`) by 4. We could use `128px` or `8rem`
directly in our styling, but using our tokens preserves consistency should the
token values get updated in the future.

Looking at the design, we need a wall-to-wall light gray background behind the
banner and also behind the third row. This is a great opportunity to use a Sass
mixin. We will put this at the top of `landing-page.component.scss`.

Per the design we need to use Gray 10 for our banner background color, which can
be set with the `$ui-01`
[color token](https://www.carbondesignsystem.com/elements/color/usage). Also, we
want the background to extend into the grid’s outermost gutters to go the full
width of the viewport, so given the DOM structure, we can achieve that by
setting the background in an absolutely positioned pseudo element.

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-05;    top: 0;Show more

```

Now to use the new mixin, update the `.landing-page__banner` declaration block
to:

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}

```

Next, we can see that the `h1` is using the `heading-05` type token.

Banner heading type

The Sketch symbol naming is consistent with the development Sass tokens to help
translate design to development. So, looking up the
[type token](https://www.carbondesignsystem.com/elements/typography/productive),
we know to use `productive-heading-05`:

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__heading {  @include type-style('productive-heading-05');}

```

### Row two

For our second row, we need to fix the tabs vertical positioning to match the
design. By inspecting the tabs component, you can see that the tab height
computes to `40px`. We can use that to create our negative top margin in rem
units.

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__r2 {  margin-top: rem(-40px);}

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

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include carbon--font-weight('semibold');}Show more

```

### Row three

Row 3 vertical spacing

Let’s also add some styles for the last row, even though that will get used
later in the tutorial. You’ll notice that we get to re-use the
`landing-page-background` mixin that we just created.

```

src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}

```

Ta-da! You should see a finished landing page! Now we can move on to the repo
page.

## Add repo page grid

First, we’ll add our grid and table by importing a few components in
`repositories.module.ts` and `repo-page.component.spec.ts`:

```

src/app/repositories/repositories.module.tsCopy to clipboardimport { GridModule, TableModule } from 'carbon-components-angular';

```

```

src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboardimports: [GridModule, TableModule];

```

Now in our `repo-page.component.html` we will add our grid containers.

```

src/app/repositories/repo-page/repo-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">Data table will go here</div>  </div></div>

```

## Build repo page

We currently have the `repo-page` that just contains a grid and placeholder
content for the time being. In the next tutorial step we’re going to be querying
an API to populate the `Table` component in this page. As a best practice to
separate data fetching from the presentation components, go ahead and create a
`repo-table` component as a sibling to `repo-page`.

```

ng g component repositories/repo-tableCopy to clipboard

```

##### Folder structure

```

src/app/repositories├── repo-table.component.html├── repo-table.component.scss├── repo-table.component.spec.ts└── repo-table.component.tsCopy to clipboard

```

Next we will add our newly generated repo-table to the declarations in
`repo-page.component.spec.ts`

```

src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboardimport { RepoTableComponent } from '../repo-table/repo-table.component';

```

```

src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboarddeclarations: [ RepoPageComponent, RepoTableComponent ],

```

### Build data table

Then, let’s create the table in `repo-table.component.html`

```

src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-table-container>	<ibm-table-header>		<h4 ibmTableHeaderTitle>Carbon Repositories</h4>		<p ibmTableHeaderDescription>A collection of public Carbon repositories.</p>	</ibm-table-header>	<ibm-table		[model]="model"		[showSelectionColumn]="false"		[striped]="false">Show more

```

Instead of the usual write-your-own-html approach you had with `<table>`, Carbon
table uses the model-view-controller approach.

Here, you create a view (with built-in controller) and provide it a model.
Changes you make to the model are reflected in the view.

### Render data table

Then include the following arrays to pass into the `repo-table.component.ts`
component. We’ll be setting the `rows` array from an API in the next tutorial
step, but for now, static example rows will suffice.

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardimport { Component, OnInit } from '@angular/core';
import {  TableModel,  TableItem,  TableHeaderItem,} from 'carbon-components-angular';
@Component({Show more

```

At this point, go to `repo-page.component.html` because now we need to render a
static `repo-table`.

```

src/app/repositories/repo-page/repo-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">      <app-repo-table></app-repo-table>    </div>  </div></div>

```

## Style repo page

Our styles for the repo page are mostly fine. We just need to update a few
vertical spacing issues.

In `repo-page.component.scss`, add the following styles:

```

src/app/repositories/repo-page/repo-page.component.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/typography';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}

```

Congratulations! We’ve now created our static repo page!

## Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step.

### Continuous integration (CI) check

Run the `lint` and `test` scripts to make sure we’re all set to submit a pull
request.

```

ng lint --fixnpm run lint && npm testCopy to clipboard

```

**Note:** Having issues running this?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#continuous-integration-(ci)-check)
has troubleshooting notes that may help.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard

```

Then, push to your repository:

```

git push origin angular-step-2Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`angular-step-2` into `base: angular-step-2`.

**Note:** Your tutorial step will be automatically reviewed based on the status
of your tests. Ensure that your tests pass when you submit your PR. Expect your
tutorial step PRs to be reviewed by the Carbon team but not merged. We’ll close
your PR so we can keep the repository’s remote branches pristine and ready for
the next person!

## Code samples

```
git fetch upstreamgit checkout -b angular-step-2 upstream/angular-step-2Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b angular-step-2 upstream/angular-step-2
```

```
npm installCopy to clipboard
```

```bash
npm install
```

```
npm startCopy to clipboard
```

```bash
npm start
```

```
src/styles.scssCopy to clipboard$feature-flags: (  grid-columns-16: true);
```

```css
$feature-flags: (  grid-columns-16: true);
```

```
src/app/home/landing-page/landing-page.component.spec.ts,src/app/home/home.module.tsCopy to clipboardimport { GridModule } from 'carbon-components-angular';...@NgModule({  ...  imports: [GridModule]})
```

```javascript
import { GridModule } from 'carbon-components-angular';...@NgModule({  ...  imports: [GridModule]})
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width landing-page">  <div ibmRow class="landing-page__banner">    <div ibmCol [columnNumbers]="{'lg': 16}">1</div>  </div>  <div ibmRow class="landing-page__r2">    <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>    <div ibmCol class="cds--offset-lg-1" [columnNumbers]="{'md': 4, 'lg': 7}">      8/16    </div>Show more
```

```html
<div ibmGrid class="cds--grid--full-width landing-page">  <div ibmRow class="landing-page__banner">    <div ibmCol [columnNumbers]="{'lg': 16}">1</div>  </div>  <div ibmRow class="landing-page__r2">    <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>    <div ibmCol class="cds--offset-lg-1" [columnNumbers]="{'md': 4, 'lg': 7}">      8/16    </div>
```

```
src/app/home/home.module.tsCopy to clipboardimport { BreadcrumbModule, GridModule } from 'carbon-components-angular';
```

```javascript
import { BreadcrumbModule, GridModule } from 'carbon-components-angular';
```

```
src/app/home/landing-page/landing-page.component.spec.tsCopy to clipboardimports: [BreadcrumbModule, GridModule];
```

```javascript
imports: [BreadcrumbModule, GridModule];
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__banner">  <div ibmCol [columnNumbers]="{'lg': 16}">    <ibm-breadcrumb noTrailingSlash="true">      <ibm-breadcrumb-item href="/"> Getting started </ibm-breadcrumb-item>    </ibm-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div></div>
```

```html
<div ibmRow class="landing-page__banner">  <div ibmCol [columnNumbers]="{'lg': 16}">    <ibm-breadcrumb noTrailingSlash="true">      <ibm-breadcrumb-item href="/"> Getting started </ibm-breadcrumb-item>    </ibm-breadcrumb>    <h1 class="landing-page__heading">Design &amp; build with Carbon</h1>  </div></div>
```

```
src/app/home/home.module.tsCopy to clipboardimport {  BreadcrumbModule,  ButtonModule,  GridModule,  TabsModule,} from 'carbon-components-angular';
```

```javascript
import {  BreadcrumbModule,  ButtonModule,  GridModule,  TabsModule,} from 'carbon-components-angular';
```

```
src/app/home/landing-page/landing-page.component.spec.tsCopy to clipboardimports: [BreadcrumbModule, ButtonModule, GridModule, TabsModule];
```

```javascript
imports: [BreadcrumbModule, ButtonModule, GridModule, TabsModule];
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r2">  <div ibmCol class="cds--no-gutter">    <ibm-tabs>      <ibm-tab heading="About">        <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">          <div ibmRow class="landing-page__tab-content">            <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>            <div              ibmColShow more
```

```html
<div ibmRow class="landing-page__r2">  <div ibmCol class="cds--no-gutter">    <ibm-tabs>      <ibm-tab heading="About">        <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">          <div ibmRow class="landing-page__tab-content">            <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">7/16</div>            <div              ibmCol
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<ibm-breadcrumb noTrailingSlash="true" ariaLabel="Page navigation">
```

```html
<ibm-breadcrumb noTrailingSlash="true" ariaLabel="Page navigation">
```

```
<ibm-tabs ariaLabel="Tab navigation">Copy to clipboard
```

```html
<ibm-tabs ariaLabel="Tab navigation">
```

```
src/assets/scss/carbon-overrides.scssCopy to clipboard// makes the grid fit the entire width of the page.cds--grid--full-width {  padding-left: 1rem;  padding-right: 1rem;}
// removes excess padding for nested full width grids.cds--grid--full-width .cds--grid--full-width {  padding-left: 0;Show more
```

```scss
// makes the grid fit the entire width of the page.cds--grid--full-width {  padding-left: 1rem;  padding-right: 1rem;}
// removes excess padding for nested full width grids.cds--grid--full-width .cds--grid--full-width {  padding-left: 0;
```

```
src/styles.scssCopy to clipboard@import './assets/scss/carbon-overrides.scss';
```

```scss
@import './assets/scss/carbon-overrides.scss';
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<ibm-tab heading="About">  <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">    <div ibmRow class="landing-page__tab-content">      <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">        <h2 class="landing-page__subheading">          What is Carbon?        </h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digitalShow more
```

```html
<ibm-tab heading="About">  <div ibmGrid class="cds--grid--no-gutter cds--grid--full-width">    <div ibmRow class="landing-page__tab-content">      <div ibmCol [columnNumbers]="{'md': 4, 'lg': 7}">        <h2 class="landing-page__subheading">          What is Carbon?        </h2>        <p class="landing-page__p">          Carbon is IBM’s open-source design system for digital
```

```
curl -o tab-illo.png https://raw.githubusercontent.com/carbon-design-system/carbon-tutorial-vue/vue-step-3/src/assets/tab-illo.pngCopy to clipboard
```

```bash
curl -o tab-illo.png https://raw.githubusercontent.com/carbon-design-system/carbon-tutorial-vue/vue-step-3/src/assets/tab-illo.png
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__illo {  max-width: 100%;}
```

```scss
.landing-page__illo {  max-width: 100%;}
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>
```

```html
<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family';@import '~carbon-components/scss/globals/scss/typography';
```

```scss
@import '~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family';@import '~carbon-components/scss/globals/scss/typography';
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}
```

```scss
.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;}
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-05;    top: 0;Show more
```

```scss
@mixin landing-page-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';    position: absolute;    left: -$spacing-05;    top: 0;
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}
```

```scss
.landing-page__banner {  padding-top: $spacing-05;  padding-bottom: $spacing-07 * 4;  @include landing-page-background;}
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__heading {  @include type-style('productive-heading-05');}
```

```scss
.landing-page__heading {  @include type-style('productive-heading-05');}
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__r2 {  margin-top: rem(-40px);}
```

```scss
.landing-page__r2 {  margin-top: rem(-40px);}
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include carbon--font-weight('semibold');}Show more
```

```scss
.landing-page__tab-content {  padding-top: $layout-05;  padding-bottom: $layout-05;}
.landing-page__subheading {  @include type-style('productive-heading-03');  @include carbon--font-weight('semibold');}
```

```
src/app/home/landing-page/landing-page.component.scssCopy to clipboard.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}
```

```scss
.landing-page__r3 {  padding-top: $spacing-09;  padding-bottom: $spacing-09;  @include landing-page-background;}
.landing-page__label {  @include type-style('heading-01');}
```

```
src/app/repositories/repositories.module.tsCopy to clipboardimport { GridModule, TableModule } from 'carbon-components-angular';
```

```javascript
import { GridModule, TableModule } from 'carbon-components-angular';
```

```
src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboardimports: [GridModule, TableModule];
```

```javascript
imports: [GridModule, TableModule];
```

```
src/app/repositories/repo-page/repo-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">Data table will go here</div>  </div></div>
```

```html
<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">Data table will go here</div>  </div></div>
```

```
ng g component repositories/repo-tableCopy to clipboard
```

```bash
ng g component repositories/repo-table
```

```
src/app/repositories├── repo-table.component.html├── repo-table.component.scss├── repo-table.component.spec.ts└── repo-table.component.tsCopy to clipboard
```

```bash
src/app/repositories├── repo-table.component.html├── repo-table.component.scss├── repo-table.component.spec.ts└── repo-table.component.ts
```

```
src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboardimport { RepoTableComponent } from '../repo-table/repo-table.component';
```

```javascript
import { RepoTableComponent } from '../repo-table/repo-table.component';
```

```
src/app/repositories/repo-page/repo-page.component.spec.tsCopy to clipboarddeclarations: [ RepoPageComponent, RepoTableComponent ],
```

```javascript
declarations: [ RepoPageComponent, RepoTableComponent ],
```

```
src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-table-container>	<ibm-table-header>		<h4 ibmTableHeaderTitle>Carbon Repositories</h4>		<p ibmTableHeaderDescription>A collection of public Carbon repositories.</p>	</ibm-table-header>	<ibm-table		[model]="model"		[showSelectionColumn]="false"		[striped]="false">Show more
```

```html
<ibm-table-container>	<ibm-table-header>		<h4 ibmTableHeaderTitle>Carbon Repositories</h4>		<p ibmTableHeaderDescription>A collection of public Carbon repositories.</p>	</ibm-table-header>	<ibm-table		[model]="model"		[showSelectionColumn]="false"		[striped]="false">
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardimport { Component, OnInit } from '@angular/core';
import {  TableModel,  TableItem,  TableHeaderItem,} from 'carbon-components-angular';
@Component({Show more
```

```javascript
import { Component, OnInit } from '@angular/core';
import {  TableModel,  TableItem,  TableHeaderItem,} from 'carbon-components-angular';
@Component({
```

```
src/app/repositories/repo-page/repo-page.component.htmlCopy to clipboard<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">      <app-repo-table></app-repo-table>    </div>  </div></div>
```

```html
<div ibmGrid class="cds--grid--full-width cds--grid--no-gutter repo-page">  <div ibmRow class="repo-page__r1">    <div ibmCol [columnNumbers]="{'lg': 16}">      <app-repo-table></app-repo-table>    </div>  </div></div>
```

```
src/app/repositories/repo-page/repo-page.component.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/typography';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}
```

```scss
@import '~carbon-components/scss/globals/scss/typography';
.repo-page .cds--row {  padding-top: $spacing-05;  padding-bottom: $spacing-05;}
```

```
ng lint --fixnpm run lint && npm testCopy to clipboard
```

```bash
ng lint --fixnpm run lint && npm test
```

```
git add --all && git commit -m "feat(tutorial): complete step 2"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 2"
```

```
git push origin angular-step-2Copy to clipboard
```

```bash
git push origin angular-step-2
```
