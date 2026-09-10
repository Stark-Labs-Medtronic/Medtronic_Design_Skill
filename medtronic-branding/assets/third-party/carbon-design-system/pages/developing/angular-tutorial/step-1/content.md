# 1. Installing Carbon – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/angular-tutorial/step-1/

# 1. Installing Carbon

Starting with the Carbon Angular, there are two ways to begin working with
Carbon components. By the end, these two methods will produce the same result.

- [Prerequisites](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#prerequisites)

- [Install Angular CLI](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#install-angular-cli)

- [Create an Angular App](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#create-an-angular-app)

- [Install Carbon](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#install-carbon)

- [Run the app](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#run-the-app)

- [Add UI Shell](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#add-ui-shell)

- [Create pages](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#create-pages)

- [Add routing](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#add-routing)

- [Submit pull request](https://carbondesignsystem.com/developing/angular-tutorial/step-1/#submit-pull-request)

## Preview

A [preview](https://angular-step-2-carbon-tutorial.netlify.com/) of what you will
build:

**Note:** If you get lint errors when you copy the code from the snippets, run
`ng lint --fix` to fix them.

## Prerequisites

### Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
that we’ll use as a starting point for each step.

### Fork

To begin, fork
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
using your GitHub account.

### Clone

Go to your forked repository, copy the SSH or HTTPS URL and in your terminal run
the two commands to get the repository in your local file system and enter that
directory.

```

git clone [your fork SSH/HTTPS]cd carbon-tutorial-angularCopy to clipboard

```

### Add upstream remote

Add a remote called `upstream` so we can eventually submit a pull request once
you have completed this tutorial step.

##### SSH:

```

git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-angular.gitCopy to clipboard

```

Or, if you prefer to use HTTPS instead of SSH with your remotes:

##### HTTPS:

```

git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-angular.gitCopy to clipboard

```

Verify that your forked repository remotes are correct:

```

git remote -vCopy to clipboard

```

Your terminal should output something like this:

```

origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (push)Copy to clipboard

```

### Branch

Now that we have our repository set up, let’s check out the branch for this
tutorial step’s starting point. Run the two commands:

```

git fetch upstreamgit checkout -b angular-step-1 upstream/angular-step-1Copy to clipboard

```

### Install Angular CLI

Since we are starting from scratch, we need to first install Angular CLI.
Currently you need to install Angular CLI Version 8.x to work through this
tutorial.

```

npm install -g @angular/cliCopy to clipboard

```

**Note:** If you are using macOS you might need to execute as a `sudo` command.

### Create an Angular App

Now that we have our environment set up, starting a new Angular app is easy! If
you haven’t set up the environment yet, please do so using the steps provided in
Prerequisites (above). We will be using the Angular CLI to create and generate
our components. It can also generate services, router, components, and
directives.

To create a new Angular project with Angular CLI, just run:

```

ng new carbon-angular-tutorialCopy to clipboard

```

This will create the new project within the current directory. Make sure you do
this within the cloned fork of the project. When you get prompted, enter the
following.

```

? Would you like to add Angular routing? Yes? Which stylesheet format would you like to use? SCSSCopy to clipboard

```

This command will install the Angular app with all the configurations needed.
Within the project folder `carbon-angular-tutorial`, the `src` directory should
have the following structure:

```

carbon-angular-tutorial...  ├── src    ├── app    │   ├── app-routing.module.ts    │   ├── app.component.html    │   ├── app.component.scss    │   ├── app.component.spec.ts    │   ├── app.component.tsCopy to clipboardShow more

```

### Install Carbon

Even though we installed some dependencies while creating the new app, we’ve yet
to install the Carbon packages:

- `carbon-components` - Component styles

- `carbon-components-angular` - Angular components

- `@carbon/icons` - Carbon icons

Run the following command to install the packages:

```

npm install carbon-components carbon-components-angular @carbon/iconsCopy to clipboard

```

The following links can be useful depending on the versions of Angular and
Carbon you wish to use. They provide detailed information about the components
and the global configuration of the design system. Additionally, they may cover
alternative methods for configuring Carbon, which can vary based on the Angular
version and any additional libraries available. Keep in mind that the
configuration for ‘styles.scss’ may also vary.:

- [Getting Started with Carbon for Angular](https://angular.carbondesignsystem.com/?path=/docs/getting-started--docs)

- [Carbon Design System Documentation](https://angular.carbondesignsystem.com/documentation/index.html)

#### Import carbon-components styles

In `src/styles.scss`, import the Carbon styles by adding the following to the
top of the file:

```

src/styles.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/styles';

```

### Run the app

Now we can run our app for a quick preview inside the browser.

```

npm startCopy to clipboard

```

Your app should now be running with the message:
`** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **`

Before we start adding components we want to start with an empty project, so
delete everything in `app.component.html` except for the `router-outlet`. We
will also have to delete the test that was associated with this code. So in
`app.component.spec.ts`, delete the `should render title` and
`should have as title 'carbon-angular-tutorial'` test.

### Add UI Shell

Next, we’re going to create an Angular component called `Header` to use with the
UI Shell Carbon component. Using Angular CLI we will create this component
inside the `src/app` directory.

```

ng g component header --lint-fixCopy to clipboard

```

##### Folder structure

```

src/app/header├── header.component.html├── header.component.scss├── header.component.spec.ts└── header.component.tsCopy to clipboard

```

#### Import UI Shell

Next we’ll import our Carbon UI Shell components into `app.module.ts`,
`app.component.spec.ts` and `header.component.spec.ts`. Set up the file like so:

```

src/app/app.module.tsCopy to clipboardimport { BrowserModule } from '@angular/platform-browser';import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';import { AppComponent } from './app.component';import { HeaderComponent } from './header/header.component';
// carbon-components-angular default importsimport { UIShellModule, IconModule } from 'carbon-components-angular';Show more

```

```

src/app/app.component.spec.ts,src/app/header/header.component.spec.tsCopy to clipboardimport { UIShellModule } from 'carbon-components-angular/ui-shell/ui-shell.module';

```

```

src/app/app.component.spec.ts,src/app/header/header.component.spec.tsCopy to clipboardTestBed.configureTestingModule({  declarations: [HeaderComponent],  imports: [UIShellModule]});

```

**Note:** You can find a description of the different components used in UI
Shell in our
[carbon-components-angular](https://github.com/IBM/carbon-components-angular/tree/master/src/ui-shell)
package.

#### Import and register icons

Now let’s import the icons from our `@carbon/icons` package. To improve tree
shaking & keep the size of our app small, import only the required icons. To do
so, import `Notification20`, `UserAvatar20`, and `AppSwitcher20` in
`app.module.ts`.

```

src/app/header/app.modules.tsCopy to clipboardimport Notification20 from '@carbon/icons/es/notification/20';import UserAvatar20 from '@carbon/icons/es/user--avatar/20';import AppSwitcher20 from '@carbon/icons/es/app-switcher/20';

```

Now you need to register the icon via `IconService` that also needs to be
imported from `carbon-components-angular` module. After importing IconService
you need to inject it in component constructor and us it in OnInit life cycle
component hook. There are 2 methods for icon registration `.register()` which
accepts only one icon and `.registerAll()` which accepts array of icons. As we
are going to use more than one icon we are going to use the later method as
below.

```

src/app/header/header.component.tsCopy to clipboardimport { IconService } from "carbon-components-angular";...
constructor(protected iconService: IconService) {}
  ngOnInit() {    this.iconService.registerAll([Notification20]);  }

```

Next step is to import the `IconModule` in the `AppModule` module where the
`HeaderComponent` is declared.

```

src/app/header/header.component.tsCopy to clipboardimport { IconModule } from "carbon-components-angular";...
imports: [  ...  IconModule]

```

Now the icon is ready to be used in template code. Template in
`header.component.html` should look like this:

```

src/app/header/header.component.htmlCopy to clipboard<ibm-header name="Carbon Tutorial Angular">  <ibm-header-navigation ariaLabel="Carbon Tutorial Angular">    <ibm-header-item href="/repos">Repositories</ibm-header-item>  </ibm-header-navigation>  <ibm-header-global>    <ibm-header-action title="action">      <svg ibmIcon="notification" size="20"></svg>    </ibm-header-action>    <ibm-header-action title="action">Show more

```

Notice that the icon names are the same as their file path. This how the
directive queries the service for the icon.

Next import the header component in `app.component.spec.ts` and add the
component in `app.component.html`

```

src/app/app.component.spec.tsCopy to clipboardimport { HeaderComponent } from './header/header.component';

```

```

src/app/app.component.spec.tsCopy to clipboarddeclarations: [HeaderComponent];

```

```

src/app/app.component.htmlCopy to clipboard<app-header></app-header><main class="cds--content">  <router-outlet></router-outlet></main>

```

Let’s add some padding to the top of the document, so the content is below the
header. We are going to do this by using the `cds--header` class provided by
carbon. So in `header.component.ts` lets hostbind that class.

```

import { Component, HostBinding } from '@angular/core';  ...  @HostBinding('class.cds--header') headerClass = true;Copy to clipboard

```

### Create pages

Next thing we need to do is create the files for our content. These files will
be located in the `app` folder inside of `src`. It should be a sibling of
`header`.

Our app will have two pages. First, we need a landing page. Go ahead and stop
your development server (with `CTRL-C`) and then:

```

ng g module home --routing --lint-fixng g component home/landing-page --lint-fixCopy to clipboard

```

##### Folder structure

```

src/app/home├── landing-page│   ├── landing-page.component.html│   ├── landing-page.component.scss│   ├── landing-page.component.spec.ts│   └── landing-page.component.ts├── home-routing.module.ts└── home-page.module.tsCopy to clipboard

```

And a repo page:

```

ng g module repositories --routing --lint-fixng g component repositories/repo-page --lint-fixCopy to clipboard

```

##### Folder structure

```

src/app/repositories├── repo-page│   ├── repo-page.component.html│   ├── repo-page.component.scss│   ├── repo-page.component.spec.ts│   └── repo-page.component.ts├── repositories-routing.module.ts└── repositories.module.tsCopy to clipboard

```

Now you can restart your server with `npm start`.

### Add routing

We need to update routing functionality to enable the loading of `repositories`.
Inside `app-routing.module.ts` we’ll add the following code in the routes array:

```

src/app-routing.module.tsCopy to clipboardconst routes: Routes = [  {    path: '',    loadChildren: () => import('./home/home.module').then((m) => m.HomeModule),  },  {    path: 'repos',    loadChildren: () =>      import('./repositories/repositories.module').then(Show more

```

And modify the `NgModule` declaration to use the hash router:

```

src/app-routing.module.tsCopy to clipboard@NgModule({  imports: [RouterModule.forRoot(routes, { useHash: true })],  exports: [RouterModule],})export class AppRoutingModule {}

```

And add routes for the landing and repo pages:

```

src/app/home/home-routing.module.tsCopy to clipboardimport { LandingPageComponent } from './landing-page/landing-page.component';
const routes: Routes = [  {    path: '',    component: LandingPageComponent,  },];

```

```

src/app/repositories/repositories-routing.module.tsCopy to clipboardimport { RepoPageComponent } from './repo-page/repo-page.component';
const routes: Routes = [  {    path: '',    component: RepoPageComponent  }];

```

After that we need to do a couple quick fixes to the UI Shell to have it route
to the repo page.

```

src/app/header/header.component.htmlCopy to clipboard<ibm-header-item [route]="['/repos']">Repositories</ibm-header-item>

```

You should now have a working header that routes to the repos pages without full
page reload!

### Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step
and demonstrate a couple related concepts.

#### Continuous integration (CI) check

**Note:** Before you run any tests, make sure that you are using ChromeHeadless
in `karma.conf.js` instead of Chrome.

We have `lint` and `test` scripts defined in `package.json` that verify file
formatting for files that have been touched since the last Git commit. You’d
typically also have that script run your test suite as part of your CI build. Go
ahead and make sure everything looks good with:

```

ng lint --fixnpm run lint && npm testCopy to clipboard

```

**Note:** If this gives an error, it’s likely that some of your source files are
not properly formatted.

#### Git commit and push

Before we can create a pull request, we need to stage and commit all of our
changes:

```

git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard

```

Then, push to your repository:

```

git push origin angular-step-1Copy to clipboard

```

**Note:** If your Git remote protocol is HTTPS instead of SSH, you may be
prompted to authenticate with GitHub when you push changes. If your GitHub
account has two-factor authentication enabled, we recommend that you follow
these instructions to
[create a personal access token for the command line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).
That lets you use your token instead of password when performing Git operations
over HTTPS.

**Note:** If you receive a `non-fast-forward` error, it’s likely that your
forked repository is behind the original repository and needs updated. This can
happen if the tutorial was updated after you began working on it. To fix, run
`git pull upstream angular-step-1` to merge the changes into your branch, then
you can try pushing again. Or, you can
[manually merge](https://help.github.com/en/articles/syncing-a-fork) in the
upstream changes.

#### Pull request (PR)

Finally, visit
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`angular-step-1` into `base: angular-step-1`. Take notice of the
[Netlify](https://www.netlify.com/) bot that deploys a preview of your PR every
time that you push new commits. These previews can be shared and viewed by
anybody to assist the PR review process.

**Note:** Your tutorial step will be automatically reviewed based on the status
of your tests. Ensure that your tests pass when you submit your PR. Expect your
tutorial step PRs to be reviewed by the Carbon team but not merged. We’ll close
your PR so we can keep the repository’s remote branches pristine and ready for
the next person!

## Code samples

```
git clone [your fork SSH/HTTPS]cd carbon-tutorial-angularCopy to clipboard
```

```bash
git clone [your fork SSH/HTTPS]cd carbon-tutorial-angular
```

```
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-angular.gitCopy to clipboard
```

```bash
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-angular.git
```

```
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-angular.gitCopy to clipboard
```

```bash
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-angular.git
```

```
git remote -vCopy to clipboard
```

```bash
git remote -v
```

```
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (push)Copy to clipboard
```

```bash
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-angular.git (push)
```

```
git fetch upstreamgit checkout -b angular-step-1 upstream/angular-step-1Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b angular-step-1 upstream/angular-step-1
```

```
npm install -g @angular/cliCopy to clipboard
```

```bash
npm install -g @angular/cli
```

```
ng new carbon-angular-tutorialCopy to clipboard
```

```bash
ng new carbon-angular-tutorial
```

```
? Would you like to add Angular routing? Yes? Which stylesheet format would you like to use? SCSSCopy to clipboard
```

```bash
? Would you like to add Angular routing? Yes? Which stylesheet format would you like to use? SCSS
```

```
carbon-angular-tutorial...  ├── src    ├── app    │   ├── app-routing.module.ts    │   ├── app.component.html    │   ├── app.component.scss    │   ├── app.component.spec.ts    │   ├── app.component.tsCopy to clipboardShow more
```

```bash
carbon-angular-tutorial...  ├── src    ├── app    │   ├── app-routing.module.ts    │   ├── app.component.html    │   ├── app.component.scss    │   ├── app.component.spec.ts    │   ├── app.component.ts
```

```
npm install carbon-components carbon-components-angular @carbon/iconsCopy to clipboard
```

```bash
npm install carbon-components carbon-components-angular @carbon/icons
```

```
src/styles.scssCopy to clipboard@import '~carbon-components/scss/globals/scss/styles';
```

```scss
@import '~carbon-components/scss/globals/scss/styles';
```

```
npm startCopy to clipboard
```

```bash
npm start
```

```
ng g component header --lint-fixCopy to clipboard
```

```bash
ng g component header --lint-fix
```

```
src/app/header├── header.component.html├── header.component.scss├── header.component.spec.ts└── header.component.tsCopy to clipboard
```

```bash
src/app/header├── header.component.html├── header.component.scss├── header.component.spec.ts└── header.component.ts
```

```
src/app/app.module.tsCopy to clipboardimport { BrowserModule } from '@angular/platform-browser';import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';import { AppComponent } from './app.component';import { HeaderComponent } from './header/header.component';
// carbon-components-angular default importsimport { UIShellModule, IconModule } from 'carbon-components-angular';Show more
```

```javascript
import { BrowserModule } from '@angular/platform-browser';import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';import { AppComponent } from './app.component';import { HeaderComponent } from './header/header.component';
// carbon-components-angular default importsimport { UIShellModule, IconModule } from 'carbon-components-angular';
```

```
src/app/app.component.spec.ts,src/app/header/header.component.spec.tsCopy to clipboardimport { UIShellModule } from 'carbon-components-angular/ui-shell/ui-shell.module';
```

```javascript
import { UIShellModule } from 'carbon-components-angular/ui-shell/ui-shell.module';
```

```
src/app/app.component.spec.ts,src/app/header/header.component.spec.tsCopy to clipboardTestBed.configureTestingModule({  declarations: [HeaderComponent],  imports: [UIShellModule]});
```

```javascript
TestBed.configureTestingModule({  declarations: [HeaderComponent],  imports: [UIShellModule]});
```

```
src/app/header/app.modules.tsCopy to clipboardimport Notification20 from '@carbon/icons/es/notification/20';import UserAvatar20 from '@carbon/icons/es/user--avatar/20';import AppSwitcher20 from '@carbon/icons/es/app-switcher/20';
```

```javascript
import Notification20 from '@carbon/icons/es/notification/20';import UserAvatar20 from '@carbon/icons/es/user--avatar/20';import AppSwitcher20 from '@carbon/icons/es/app-switcher/20';
```

```
src/app/header/header.component.tsCopy to clipboardimport { IconService } from "carbon-components-angular";...
constructor(protected iconService: IconService) {}
  ngOnInit() {    this.iconService.registerAll([Notification20]);  }
```

```javascript
import { IconService } from "carbon-components-angular";...
constructor(protected iconService: IconService) {}
  ngOnInit() {    this.iconService.registerAll([Notification20]);  }
```

```
src/app/header/header.component.tsCopy to clipboardimport { IconModule } from "carbon-components-angular";...
imports: [  ...  IconModule]
```

```javascript
import { IconModule } from "carbon-components-angular";...
imports: [  ...  IconModule]
```

```
src/app/header/header.component.htmlCopy to clipboard<ibm-header name="Carbon Tutorial Angular">  <ibm-header-navigation ariaLabel="Carbon Tutorial Angular">    <ibm-header-item href="/repos">Repositories</ibm-header-item>  </ibm-header-navigation>  <ibm-header-global>    <ibm-header-action title="action">      <svg ibmIcon="notification" size="20"></svg>    </ibm-header-action>    <ibm-header-action title="action">Show more
```

```html
<ibm-header name="Carbon Tutorial Angular">  <ibm-header-navigation ariaLabel="Carbon Tutorial Angular">    <ibm-header-item href="/repos">Repositories</ibm-header-item>  </ibm-header-navigation>  <ibm-header-global>    <ibm-header-action title="action">      <svg ibmIcon="notification" size="20"></svg>    </ibm-header-action>    <ibm-header-action title="action">
```

```
src/app/app.component.spec.tsCopy to clipboardimport { HeaderComponent } from './header/header.component';
```

```javascript
import { HeaderComponent } from './header/header.component';
```

```
src/app/app.component.spec.tsCopy to clipboarddeclarations: [HeaderComponent];
```

```javascript
declarations: [HeaderComponent];
```

```
src/app/app.component.htmlCopy to clipboard<app-header></app-header><main class="cds--content">  <router-outlet></router-outlet></main>
```

```html
<app-header></app-header><main class="cds--content">  <router-outlet></router-outlet></main>
```

```
import { Component, HostBinding } from '@angular/core';  ...  @HostBinding('class.cds--header') headerClass = true;Copy to clipboard
```

```javascript
import { Component, HostBinding } from '@angular/core';  ...  @HostBinding('class.cds--header') headerClass = true;
```

```
ng g module home --routing --lint-fixng g component home/landing-page --lint-fixCopy to clipboard
```

```bash
ng g module home --routing --lint-fixng g component home/landing-page --lint-fix
```

```
src/app/home├── landing-page│   ├── landing-page.component.html│   ├── landing-page.component.scss│   ├── landing-page.component.spec.ts│   └── landing-page.component.ts├── home-routing.module.ts└── home-page.module.tsCopy to clipboard
```

```bash
src/app/home├── landing-page│   ├── landing-page.component.html│   ├── landing-page.component.scss│   ├── landing-page.component.spec.ts│   └── landing-page.component.ts├── home-routing.module.ts└── home-page.module.ts
```

```
ng g module repositories --routing --lint-fixng g component repositories/repo-page --lint-fixCopy to clipboard
```

```bash
ng g module repositories --routing --lint-fixng g component repositories/repo-page --lint-fix
```

```
src/app/repositories├── repo-page│   ├── repo-page.component.html│   ├── repo-page.component.scss│   ├── repo-page.component.spec.ts│   └── repo-page.component.ts├── repositories-routing.module.ts└── repositories.module.tsCopy to clipboard
```

```bash
src/app/repositories├── repo-page│   ├── repo-page.component.html│   ├── repo-page.component.scss│   ├── repo-page.component.spec.ts│   └── repo-page.component.ts├── repositories-routing.module.ts└── repositories.module.ts
```

```
src/app-routing.module.tsCopy to clipboardconst routes: Routes = [  {    path: '',    loadChildren: () => import('./home/home.module').then((m) => m.HomeModule),  },  {    path: 'repos',    loadChildren: () =>      import('./repositories/repositories.module').then(Show more
```

```javascript
const routes: Routes = [  {    path: '',    loadChildren: () => import('./home/home.module').then((m) => m.HomeModule),  },  {    path: 'repos',    loadChildren: () =>      import('./repositories/repositories.module').then(
```

```
src/app-routing.module.tsCopy to clipboard@NgModule({  imports: [RouterModule.forRoot(routes, { useHash: true })],  exports: [RouterModule],})export class AppRoutingModule {}
```

```javascript
@NgModule({  imports: [RouterModule.forRoot(routes, { useHash: true })],  exports: [RouterModule],})export class AppRoutingModule {}
```

```
src/app/home/home-routing.module.tsCopy to clipboardimport { LandingPageComponent } from './landing-page/landing-page.component';
const routes: Routes = [  {    path: '',    component: LandingPageComponent,  },];
```

```javascript
import { LandingPageComponent } from './landing-page/landing-page.component';
const routes: Routes = [  {    path: '',    component: LandingPageComponent,  },];
```

```
src/app/repositories/repositories-routing.module.tsCopy to clipboardimport { RepoPageComponent } from './repo-page/repo-page.component';
const routes: Routes = [  {    path: '',    component: RepoPageComponent  }];
```

```javascript
import { RepoPageComponent } from './repo-page/repo-page.component';
const routes: Routes = [  {    path: '',    component: RepoPageComponent  }];
```

```
src/app/header/header.component.htmlCopy to clipboard<ibm-header-item [route]="['/repos']">Repositories</ibm-header-item>
```

```html
<ibm-header-item [route]="['/repos']">Repositories</ibm-header-item>
```

```
ng lint --fixnpm run lint && npm testCopy to clipboard
```

```bash
ng lint --fixnpm run lint && npm test
```

```
git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 1"
```

```
git push origin angular-step-1Copy to clipboard
```

```bash
git push origin angular-step-1
```
