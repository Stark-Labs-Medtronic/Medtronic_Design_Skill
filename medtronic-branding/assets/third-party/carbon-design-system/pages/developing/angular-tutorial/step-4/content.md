# 4. Creating components – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/angular-tutorial/step-4/

# 4. Creating components

With two pages comprised entirely of Carbon components, let’s revisit the
landing page and build a couple components of our own by using Carbon icons and
tokens.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#fork-clone-and-branch)

- [Review design](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#review-design)

- [Create components](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#create-components)

- [Use components](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#use-components)

- [Add styling](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#add-styling)

- [Submit pull request](https://carbondesignsystem.com/developing/angular-tutorial/step-4/#submit-pull-request)

## Preview

Carbon provides a solid foundation for building web applications through its
color palette, layout, spacing, type, as well as common building blocks in the
form of components. So far, we’ve only used Carbon components to build out two
pages.

Next, we’re going to use Carbon assets to build application-specific components.
We’ll create our components with considerations for accessibility and
responsiveness.

A [preview](https://angular-step-5-carbon-tutorial.netlify.com/) of what you’ll
build (see bottom of page):

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

git fetch upstreamgit checkout -b angular-step-4 upstream/angular-step-4Copy to clipboard

```

**Note:** This builds on top of step 3, but be sure to check out the upstream
step 4 branch because it includes the static assets required to get through this
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
[previous step](https://carbondesignsystem.com/developing/angular-tutorial/step-3) left off.

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

### Generate modules & components using the Angular CLI

Let’s generate a new module that’ll handle our `InfoCard` and `InfoSection`
components:

```

ng generate module infoCopy to clipboard

```

Now we generate our `InfoCard` and `InfoSection` components:

```

ng generate component info/info-card --lint-fixCopy to clipboard

```

```

ng generate component info/info-section --lint-fixCopy to clipboard

```

**Note:** The `--lint-fix` flag will automatically resolve lint issues in the
newly generated files.

Running the above commands should get you the folder structure below:

```

src/app/info└──info.module.ts└──info-card	├──info-card.component.scss	├──info-card.component.ts	├──info-card.component.spec.ts	└──info-card.component.html└──info-section	├──info-section.component.scssCopy to clipboardShow more

```

Now let’s create a JSON file that’ll include our content to be shown in the
components:

```

src/app/info/info.jsonCopy to clipboard{  "title": "The Principles",  "items": [    {      "heading": "Carbon is Open",      "content": "It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    },    {      "heading": "Carbon is Modular",Show more

```

Now we also need to tell typescript to resolve JSON files as modules when
compiling:

```

src/tsconfig.app.jsonCopy to clipboard{	"compilerOptions": {		"sourceMap": true,		"declaration": false,		...		"resolveJsonModule": true	},	...}

```

### InfoSection component

Let’s create the parent component that includes the “The Principles” heading.
That markup currently looks like this in `landing-page.component.html`:

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>

```

We want to do a few things when abstracting it to a component. Firstly, we want
to encapsulate the component’s styles within it’s dedicated stylesheet. We don’t
want to include `landing-page__r3` within the component template as that’s
specific to the landing page. In order to allow the landing page to have access
to styling this specific instance of an `InfoSection` component we could pass
the class into the instance of the component. However, we won’t need to do any
additional styling from the `landing-page` so we can just go ahead use the
component as is.

We’ll also:

- Add component class names like `.info-section` and `.info-section__heading`

- Semantically use `<section>` instead of `<div>`

- Update the grid columns to match the design

- Update the component content to use `info.json`

- Replace columns 2 - 4 with `InfoCard` components

- Remove class styling from `landing-page` component

```

src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<app-info-section></app-info-section>

```

```

src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 8, 'lg': 4}">    <h3 class="info-section__heading">The Principles</h3>  </div>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card></section>

```

As you can see we’ve added instances of the `InfoCard` component. There is a few
things that we need to do to resolve the errors in the browser. Firstly we need
to update `InfoModule` to be able to use the `GridModule`. At the same time we
will export the `InfoSection` and `InfoCard` components from the `InfoModule` so
that we can use them in the `HomeModule` components (specifically
`landing-page`).

```

src/app/info/info.module.tsCopy to clipboardimport { NgModule } from "@angular/core";...import { GridModule } from "carbon-components-angular";

@NgModule({	declarations: [InfoCardComponent, InfoSectionComponent],	imports: [		CommonModule,Show more

```

We also need to import `InfoModule` into `HomeModule` otherwise we cannot use
the `InfoSection` component within `landing-page`.

```

src/app/home/home.module.tsCopy to clipboard...import { InfoModule } from "./../info/info.module";import {	BreadcrumbModule,	ButtonModule,	GridModule,	TabsModule} from "carbon-components-angular";
Show more

```

Now we’re going to go into the `InfoSection` component to add content from
`info.json`.

```

src/app/info/info-section/info-section.component.tsCopy to clipboardimport { Component, OnInit } from '@angular/core';import * as data from '../info.json';
@Component({  selector: 'app-info-section',  templateUrl: './info-section.component.html',  styleUrls: ['./info-section.component.scss'],})export class InfoSectionComponent implements OnInit {Show more

```

We essentially have added a `heading` and `items` variable into the model of `InfoSectionComponent`, which we’ll be using later to pass content into the children components `InfoCard`.

We’ve also added class names that are specific to this component that we’ll target in our stylesheet:

```

src/app/info/info-section/info-section.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family";
@mixin info-section-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';Show more

```

### InfoCard component

Next up we’re going to build a component for columns 2 - 4, which currently
looks like
`<div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>`. We’ve
added the data into the parent component but we have not told `info-section`
component to give any data to the `InfoCard` because we first need to tell
`InfoCard` that it will have data to display. In
`src/app/info/info-card/info-card.component.html`, add:

```

src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  <h4 class="info-card__heading">{{heading}}</h4>  <div class="info-card__body">{{content}}</div></div>

```

Now we’ve setup our `InfoCard` to display a heading and some content. We will
setup the component `.ts` file to accept a `heading` and `content` input to be
displayed.

```

src/app/info/info-card/info-card.component.tsCopy to clipboardimport { Component, OnInit, Input } from "@angular/core";
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;Show more

```

Finally, we’ll update `InfoSection` to use the new `InfoCard` component.

```

src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">Show more

```

## Use components

Next we’re going to use Carbon Icon components in our custom components. We’re
going to place the icons within the `InfoCard` components as children. In the
`InfoModule` we will import the modules we need for the Carbon Angular Icons:

```

src/info/info.module.tsCopy to clipboardimport { NgModule } from "@angular/core";...
import { PersonFavorite32Module } from "@carbon/icons-angular/lib/person--favorite/32";import { Globe32Module } from "@carbon/icons-angular/lib/globe/32";import { Application32Module } from "@carbon/icons-angular/lib/application/32";
import { GridModule } from "carbon-components-angular";
Show more

```

Next we will use `<ng-content>` so that we can inject icons into the `InfoCard`
from it’s parent component (`InfoSection`)

```

src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  ...  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div></div>

```

We also need to update `InfoSection` with the icon components:

```

src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">Show more

```

## Add styling

We currently have the components displaying the content we created. We need to
add more styling for Carbon breakpoints, icon alignments, as well as the
`InfoCard` title styling.

### Layout

Starting with layout, add the following to
`src/app/info/info-card/info-card.component.scss`.

```

src/app/info/info-card/info-card.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  display: flex;  flex-direction: column;
  .info-card__heading {    @include type-style("productive-heading-03");Show more

```

Once you save, go ahead and resize your browser to see the responsive layout at
the different breakpoints. Make sure to review these color and spacing tokens.
There are also a few breakpoint mixins that may be new to you.

### Type

Our `InfoCard` headings have to be updated to match the specs. We need to make
the last word of each heading bold. Add the below custom function
(`createArrayFromPhrase`) to `src/app/info/info-card/info-card.component.ts`:

```

src/app/info/info-card/info-card.component.tsCopy to clipboardimport { Component, OnInit, Input } from '@angular/core';
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;Show more

```

This will allow us to still accept `heading` as an input to the component, but
we’ll need to change the template to use `splitHeading` rather than `heading` to
display our heading content.

Update the component template to use `splitHeading`:

```

src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  <h4 class="info-card__heading">    {{splitHeading[0]}}    <strong>{{splitHeading[1]}}</strong>  </h4>  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div>Show more

```

Then, add some styling for the icons within our `InfoCard` component:

```

src/app/info/info-card/info-card.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  ... .info-card__icon {    margin-top: $spacing-09;  }}

```

Finally, we need styles for the `InfoCard` borders. We will use the
`InfoSection` to apply styles using the children selectors. Update the
`InfoSection` stylesheet to include styles targeting the `InfoCard`:

```

src/app/info/info-section/info-section.component.scssCopy to clipboard.info-section {  ... app-info-card {    margin-top: $spacing-09;  }
  // top border in only small breakpoints to prevent overrides  @include breakpoint-down(md) {    app-info-card:not(:nth-child(2)) {      border-top: 1px solid $ui-03;Show more

```

## Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard

```

Then, push to your repository:

```

git push origin angular-step-4Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial](https://github.com/carbon-design-system/carbon-tutorial-angular)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`angular-step-4` into `base: angular-step-4`.

**Note:** Your tutorial step will be automatically reviewed based on the status
of your tests. Ensure that your tests pass when you submit your PR. Expect your
tutorial step PRs to be reviewed by the Carbon team but not merged. We’ll close
your PR so we can keep the repository’s remote branches pristine and ready for
the next person!

## Code samples

```
git fetch upstreamgit checkout -b angular-step-4 upstream/angular-step-4Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b angular-step-4 upstream/angular-step-4
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
ng generate module infoCopy to clipboard
```

```bash
ng generate module info
```

```
ng generate component info/info-card --lint-fixCopy to clipboard
```

```bash
ng generate component info/info-card --lint-fix
```

```
ng generate component info/info-section --lint-fixCopy to clipboard
```

```bash
ng generate component info/info-section --lint-fix
```

```
src/app/info└──info.module.ts└──info-card	├──info-card.component.scss	├──info-card.component.ts	├──info-card.component.spec.ts	└──info-card.component.html└──info-section	├──info-section.component.scssCopy to clipboardShow more
```

```bash
src/app/info└──info.module.ts└──info-card	├──info-card.component.scss	├──info-card.component.ts	├──info-card.component.spec.ts	└──info-card.component.html└──info-section	├──info-section.component.scss
```

```
src/app/info/info.jsonCopy to clipboard{  "title": "The Principles",  "items": [    {      "heading": "Carbon is Open",      "content": "It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    },    {      "heading": "Carbon is Modular",Show more
```

```json
{  "title": "The Principles",  "items": [    {      "heading": "Carbon is Open",      "content": "It's a distributed effort, guided by the principles of the open-source movement. Carbon's users are also it's makers, and everyone is encouraged to contribute."    },    {      "heading": "Carbon is Modular",
```

```
src/tsconfig.app.jsonCopy to clipboard{	"compilerOptions": {		"sourceMap": true,		"declaration": false,		...		"resolveJsonModule": true	},	...}
```

```json
{	"compilerOptions": {		"sourceMap": true,		"declaration": false,		...		"resolveJsonModule": true	},	...}
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>
```

```html
<div ibmRow class="landing-page__r3">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="landing-page__label">The Principles</h3>  </div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Open</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Modular</div>  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">Carbon is Consistent</div></div>
```

```
src/app/home/landing-page/landing-page.component.htmlCopy to clipboard<app-info-section></app-info-section>
```

```html
<app-info-section></app-info-section>
```

```
src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 8, 'lg': 4}">    <h3 class="info-section__heading">The Principles</h3>  </div>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card></section>
```

```html
<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 8, 'lg': 4}">    <h3 class="info-section__heading">The Principles</h3>  </div>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card>  <app-info-card ibmCol [columnNumbers]="{'md': 4, 'lg': 4}"> </app-info-card></section>
```

```
src/app/info/info.module.tsCopy to clipboardimport { NgModule } from "@angular/core";...import { GridModule } from "carbon-components-angular";

@NgModule({	declarations: [InfoCardComponent, InfoSectionComponent],	imports: [		CommonModule,Show more
```

```ts
import { NgModule } from "@angular/core";...import { GridModule } from "carbon-components-angular";

@NgModule({	declarations: [InfoCardComponent, InfoSectionComponent],	imports: [		CommonModule,
```

```
src/app/home/home.module.tsCopy to clipboard...import { InfoModule } from "./../info/info.module";import {	BreadcrumbModule,	ButtonModule,	GridModule,	TabsModule} from "carbon-components-angular";
Show more
```

```ts
...import { InfoModule } from "./../info/info.module";import {	BreadcrumbModule,	ButtonModule,	GridModule,	TabsModule} from "carbon-components-angular";
```

```
src/app/info/info-section/info-section.component.tsCopy to clipboardimport { Component, OnInit } from '@angular/core';import * as data from '../info.json';
@Component({  selector: 'app-info-section',  templateUrl: './info-section.component.html',  styleUrls: ['./info-section.component.scss'],})export class InfoSectionComponent implements OnInit {Show more
```

```ts
import { Component, OnInit } from '@angular/core';import * as data from '../info.json';
@Component({  selector: 'app-info-section',  templateUrl: './info-section.component.html',  styleUrls: ['./info-section.component.scss'],})export class InfoSectionComponent implements OnInit {
```

```
src/app/info/info-section/info-section.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family";
@mixin info-section-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';Show more
```

```scss
@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/vendor/@carbon/type/scss/font-family";
@mixin info-section-background() {  background-color: $ui-01;  position: relative;
  &::before {    content: '';
```

```
src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  <h4 class="info-card__heading">{{heading}}</h4>  <div class="info-card__body">{{content}}</div></div>
```

```html
<div class="info-card">  <h4 class="info-card__heading">{{heading}}</h4>  <div class="info-card__body">{{content}}</div></div>
```

```
src/app/info/info-card/info-card.component.tsCopy to clipboardimport { Component, OnInit, Input } from "@angular/core";
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;Show more
```

```ts
import { Component, OnInit, Input } from "@angular/core";
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;
```

```
src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">Show more
```

```html
<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">
```

```
src/info/info.module.tsCopy to clipboardimport { NgModule } from "@angular/core";...
import { PersonFavorite32Module } from "@carbon/icons-angular/lib/person--favorite/32";import { Globe32Module } from "@carbon/icons-angular/lib/globe/32";import { Application32Module } from "@carbon/icons-angular/lib/application/32";
import { GridModule } from "carbon-components-angular";
Show more
```

```ts
import { NgModule } from "@angular/core";...
import { PersonFavorite32Module } from "@carbon/icons-angular/lib/person--favorite/32";import { Globe32Module } from "@carbon/icons-angular/lib/globe/32";import { Application32Module } from "@carbon/icons-angular/lib/application/32";
import { GridModule } from "carbon-components-angular";
```

```
src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  ...  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div></div>
```

```html
<div class="info-card">  ...  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div></div>
```

```
src/app/info/info-section/info-section.component.htmlCopy to clipboard<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">Show more
```

```html
<section ibmRow class="info-section info-section__r1">  <div ibmCol [columnNumbers]="{'md': 4, 'lg': 4}">    <h3 class="info-section__heading">{{heading}}</h3>  </div>  <app-info-card    ibmCol    [columnNumbers]="{'md': 4, 'lg': 4}"    [heading]="items[0].heading"    [content]="items[0].content">
```

```
src/app/info/info-card/info-card.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  display: flex;  flex-direction: column;
  .info-card__heading {    @include type-style("productive-heading-03");Show more
```

```scss
@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  display: flex;  flex-direction: column;
  .info-card__heading {    @include type-style("productive-heading-03");
```

```
src/app/info/info-card/info-card.component.tsCopy to clipboardimport { Component, OnInit, Input } from '@angular/core';
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;Show more
```

```ts
import { Component, OnInit, Input } from '@angular/core';
@Component({  selector: "app-info-card",  templateUrl: "./info-card.component.html",  styleUrls: ["./info-card.component.scss"],})export class InfoCardComponent implements OnInit {  @Input() heading;
```

```
src/app/info/info-card/info-card.component.htmlCopy to clipboard<div class="info-card">  <h4 class="info-card__heading">    {{splitHeading[0]}}    <strong>{{splitHeading[1]}}</strong>  </h4>  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div>Show more
```

```html
<div class="info-card">  <h4 class="info-card__heading">    {{splitHeading[0]}}    <strong>{{splitHeading[1]}}</strong>  </h4>  <div class="info-card__body">{{content}}</div>  <div class="info-card__icon">    <ng-content></ng-content>  </div>
```

```
src/app/info/info-card/info-card.component.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  ... .info-card__icon {    margin-top: $spacing-09;  }}
```

```scss
@import "~carbon-components/scss/globals/scss/typography";@import "~carbon-components/scss/globals/scss/layout";
.info-card {  ... .info-card__icon {    margin-top: $spacing-09;  }}
```

```
src/app/info/info-section/info-section.component.scssCopy to clipboard.info-section {  ... app-info-card {    margin-top: $spacing-09;  }
  // top border in only small breakpoints to prevent overrides  @include breakpoint-down(md) {    app-info-card:not(:nth-child(2)) {      border-top: 1px solid $ui-03;Show more
```

```scss
.info-section {  ... app-info-card {    margin-top: $spacing-09;  }
  // top border in only small breakpoints to prevent overrides  @include breakpoint-down(md) {    app-info-card:not(:nth-child(2)) {      border-top: 1px solid $ui-03;
```

```
git add --all && git commit -m "feat(tutorial): complete step 4"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 4"
```

```
git push origin angular-step-4Copy to clipboard
```

```bash
git push origin angular-step-4
```
