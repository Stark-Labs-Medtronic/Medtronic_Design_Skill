# 1. Installing Carbon – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/web-components-tutorial/step-1/

# 1. Installing Carbon

Starting from a base `create-vite` app, created using the `Vanilla` and
`Javascript` options, let’s install Carbon and begin using Carbon components. By
the end you will have a Vanilla app that uses the UI Shell to navigate between
pages.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#fork-clone-and-branch)

- [Build and start](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#build-and-start)

- [Install Carbon](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#install-carbon)

- [Install Sass](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#install-sass)

- [A working Carbon button](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#a-working-carbon-button)

- [Add UI Shell](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#add-ui-shell)

- [Push to GitHub](https://carbondesignsystem.com/developing/web-components-tutorial/step-1/#push-to-github)

## Preview

A [preview](https://solid-carnival-1pg38np.pages.github.io/) of what you will
build:

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-web-components](https://github.com/carbon-design-system/carbon-tutorial-web-components)
that we’ll use as a starting point for each step.

### Fork

To begin, fork
[carbon-tutorial-web-components](https://github.com/carbon-design-system/carbon-tutorial-web-components)
using your GitHub account. Please note when forking you must uncheck “Copy the
main branch only” so you can access all branches / steps of the tutorial.

### Clone

Go to your forked repository, copy the SSH or HTTPS URL and in your terminal run
the two commands to get the repository in your local file system and enter that
directory.

```

git clone [your fork SSH/HTTPS]cd carbon-tutorial-web-componentsCopy to clipboard

```

### Add upstream remote

Add a remote called `upstream` so we can eventually submit a pull request once
you have completed this tutorial step. There are two choices: SSH or HTTPS

#### SSH

```

git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-web-components.gitCopy to clipboard

```

#### HTTPS

```

git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-web-components.gitCopy to clipboard

```

Verify that your forked repository remotes are correct:

```

git remote -vCopy to clipboard

```

Your terminal should output something like this:

```

origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (push)Copy to clipboard

```

### Branch

Now that we have our repository set up, let’s check out the branch for this
tutorial step’s starting point. Run the two commands:

```

git fetch upstreamgit checkout -b step-1 upstream/step-1Copy to clipboard

```

## Build and start

We have the repository forked to your GitHub account, cloned down to your
machine, and the starting branch checked out. Next, install the app’s
dependencies (Vite) with:

```

pnpm iCopy to clipboard

```

After the dependencies are installed, you can start the app with:

```

pnpm devCopy to clipboard

```

Open Your default browser should open up with an empty page that says:
`Hello Carbon! Well, not quite yet. This is the starting point for the Carbon Web Components tutorial.`

## Install Carbon

Even though we installed existing dependencies, we’ve yet to install our any
Carbon packages.

Stop your development server with `CTRL-C` and install Carbon dependencies with:

```

pnpm add @carbon/web-components @carbon/stylesCopy to clipboard

```

## Install Sass

We need to run a Sass build as the Carbon styles are authored in Sass, so run
the following command to install `sass` as a dependency.

```

pnpm add sassCopy to clipboard

```

Before restarting our app rename `style.css` to `style.scss` and change the
import in `main.js` from `import './style.css';` to `import './style.scss';`.

Then, start the app again. If your app’s currently running, you’ll need to
restart it for the new packages to be used.

```

pnpm devCopy to clipboard

```

The app looks as it did before. We, need to import Carbon styles have an impact.

### Import Carbon styles

Replace the contents of `style.scss` with

```

style.scssCopy to clipboard@use '@carbon/styles/scss/reset';

```

This has reset the styles to a common base from which Carbon applications are
built. What you see, if you run the application, is a largely unstyled page. It
is however making use of the IBM Plex font, standard in all Carbon applications.

## A working Carbon button

### Import the button

Next, we’ll import a `Button` from Carbon to test that our dependencies are
working properly. At the top of `main.js`, import the `Button` and delete
everything else, leaving just:

```

main.jsCopy to clipboardimport './style.scss';import '@carbon/web-components/es/components/button/button.js';

```

### Tidy up our HTML file

In `index.html` first move this script tag up inside the `head` tag, so we don’t
accidentally delete it later. It’s location does not matter in this tutorial.

```

index.htmlCopy to clipboard<script type="module" src="/main.js"></script>

```

Then replace the Vite logo

```

index.htmlCopy to clipboard<link rel="icon" type="image/svg+xml" href="/vite.svg" />

```

with the Carbon one:

```

index.htmlCopy to clipboard<link rel="icon" type="image/svg+xml" href="/carbon.svg" />

```

Update the title `Vite App` to `Carbon tutorial web components`.

### Add the button by replacing:

```

index.htmlCopy to clipboard<div id="app"></div>

```

with:

```

index.htmlCopy to clipboard<cds-button class="button">Click more than once</cds-button>

```

Congratulations, you’ve imported your first component! You should see a Carbon
styled button on the page.

### Make the button do something

Before giving the button something to do, add the following to `style.scss`
which will allow our button to theme the app.

```

style.scssCopy to clipboard@use '@carbon/styles/scss/theme' as *;@use '@carbon/styles/scss/themes';
:root {  @include theme(themes.$g10);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g100);  }Show more

```

Then in `main.js` add the following code to handle the button clicks.

```

main.jsCopy to clipboardconst bodyEl = document.querySelector('body');
// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
Show more

```

After these changes clicking the button will toggle theme classes, which in the
app changes the background color.

## Add UI Shell

Now we’re going to add the UI shell.

### UI Shell for the landing page

First import the header into `main.js`

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/ui-shell/index';

```

**Note:** you can find a description of the different components used in the UI
Shell in our
[Storybook](https://web-components.carbondesignsystem.com/?path=/docs/components-ui-shell--overview)
package.

Before we add the header to `index.html` add the class `app` to the body tag.

```

index.htmlCopy to clipboard<body class="app"></body>

```

Wrap the button as follows.

```

index.htmlCopy to clipboard<main class="main">  <cds-button class="button">Click more than once</cds-button></main>

```

Then above `<main>` add our header.

```

index.htmlCopy to clipboard<header>  <cds-header class="g100">    <cds-header-name href="./" prefix="IBM">Carbon Tutorial</cds-header-name>  </cds-header></header>

```

Running the application at this point it looks like the button has disappeared.
Add the following to `style.scss`.

```

@use '@carbon/styles/scss/spacing' as *; /* near top of file */
.app {  display: grid;  grid-template-rows: $spacing-09 1fr;  height: 100vh;  overflow: hidden;}
Copy to clipboardShow more

```

This imports the Carbon `spacing` and establishes a grid to contain our header
and main. The overflow settings are there to ensure it is our `<main>` that
scrolls if needed.

### Adding the repositories page

After the `<cds-header-name>` closing tag add a link to a new page.

```

index.htmlCopy to clipboard<cds-header-nav menu-bar-label="Carbon Tutorial">  <cds-header-nav-item href="./repositories.html"    >Repositories</cds-header-nav-item  ></cds-header-nav>

```

Duplicate `index.html` and name it `repositories.html`.

In this new file replace the contents of the `main` tag with the words
`REPOSITORIES PAGE`.

You can now switch between the two pages by clicking on `Repositories` and
`IBM Carbon Tutorial` in the header. This will look a little glitchy, this is
because it is a genuine page navigation, and the CSS is still being processed.
When using Web Components inside libraries such as Lit, React, Angular, Vue etc
this is resolved by taking control of the routing. We will not investigate
further here.

### Behaving responsively

Switch back to the landing page by clicking on `IBM Carbon Tutorial`.

Checking responsive behavior (window narrower than 1080px) you will notice the
repositories page disappear from the menu. This goes into a sidebar controlled
by a hamburger menu as follows.

Before the `<cds-header-name>` tag add

```

index.htmlCopy to clipboard<cds-header-menu-button  button-label-active="Close menu"  button-label-inactive="Open menu"></cds-header-menu-button>

```

Then after the closing `</cds-header-nav>` add

```

index.htmlCopy to clipboard<cds-side-nav  is-not-persistent  aria-label="Side navigation"  collapse-mode="${SIDE_NAV_COLLAPSE_MODE.RESPONSIVE}">  <cds-side-nav-items>    <cds-side-nav-link href="./repositories.html">      Repositories    </cds-side-nav-link>  </cds-side-nav-items>Show more

```

### Global actions

As part of the Carbon header we can also add global actions this involves making
use of some Carbon Icons so first we will add that dependency.

```

pnpm add @carbon/iconsCopy to clipboard

```

There are various ways to add SVGs to our page. Often the SVG is copied directly
into source HTML or a bundler is used to load it. Rather than rely on a bundler
or add them inline, which can make our HTML harder to read, we will use CSS to
add refer directly to the icon files (which have been conveniently copied into
the `./public` folder) from the `@carbon/icons` package.

```

style.scssCopy to clipboard.action-icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
.notification .action-icon {  mask: url('/notification.svg') no-repeat center;}Show more

```

The above CSS allows us to simply add the two classes associated with each icon
to display it in a themeable way in our application.

Next we need to add the global actions and related panels to the `index.html`
file after the closing `</cds-side-nav>`. The Carbon icons are applied to the
slotted icon element using CSS.

```

index.htmlCopy to clipboard<div class="cds--header__global">  <cds-header-global-action    aria-label="Notifications"    class="notification"    panel-id="notification-panel">    <div class="action-icon" slot="icon"></div>  </cds-header-global-action>  <cds-header-global-action    aria-label="User Profile"Show more

```

**Note:** this is the first time we have seen the `slot` attribute. Standard
HTML elements often have the ability to host child content. Web components are
more flexible allowing both the default child and named child areas, it uses the
term `slot` to refer to these. The slot attribute is used to target named slots,
in this case `icon`.

Further details on slots can be found on the
[mdn docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
package.

The global action buttons are passed a `panel-id` used to identify the panels
they toggle the visibility of. Just below the last global action add the
following HTML.

```

index.htmlCopy to clipboard<cds-header-panel id="notification-panel" aria-label="Notification Panel"  >Notification Panel</cds-header-panel><cds-header-panel id="user-profile-panel" aria-label="User profile Panel"  >User profile Panel</cds-header-panel><cds-header-panel id="app-switcher-panel" aria-label="App switcher Panel"  >App switcher Panel</cds-header-panel>

```

Note as web components behave like native components we can add event handlers
and interact with them directly.

The default panel behavior simply toggles the panel when clicked. This can
result in multiple panels being open at once. Adding the following to `main.js`
changes this behavior by listening for clicks and closing the other panels.

```

main.jsCopy to clipboardconst handleGlobalActionClick = (ev) => {  const targetPanelId = ev.currentTarget.getAttribute('panel-id');  const panels = document.querySelectorAll('cds-header-panel');  // check to see if other panels are open and close them  panels.forEach((panel) => {    if (panel.id !== targetPanelId) {      panel.expanded = false;    }  });Show more

```

### A better theme switcher

The current theme switcher is not very practical, here we will move it inside
the profile panel.

First replace the button in `index.html` with `LANDING PAGE` leaving the main
tag looking like this.

```

index.htmlCopy to clipboard<main class="main">LANDING PAGE</main>

```

In `main.js` remove this code handling the button click and initial load.

```

main.jsCopy to clipboard// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
// set initial theme based on preferencesif (matchMedia('(prefers-color-scheme: dark)')) {Show more

```

Still in `main.js` add imports for checkbox and content-switcher.

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/checkbox/index';import '@carbon/web-components/es/components/content-switcher/index';

```

Locate the `cds-header-panel` with the id=“user-profile-panel” in `index.html`
and replace it’s content with the following.

```

index.htmlCopy to clipboard<div class="header-panel__content">  <h2 class="header-panel__title">User profile Panel</h2>
  <cds-content-switcher value="system" class="theme-selector">    <cds-content-switcher-item icon value="light">      <div class="theme-selector__icon theme-selector__icon--light"></div>      <span slot="tooltip-content">Light theme</span>    </cds-content-switcher-item>    <cds-content-switcher-item icon value="system">Show more

```

This adds a content switcher and checkbox to our user profile side panel. If you
view it now it works but is in need of some styling.

These styles import the Carbon typography features, define a layout for our
panel, and set the title size.

```

style.scssCopy to clipboard@use '@carbon/styles/scss/type' as *; /* place at top of file */
.header-panel__content {  display: flex;  flex-direction: column;  gap: $spacing-05;  padding: $spacing-05;}
Show more

```

As per the global actions we will use additional styling to add icons to our
content switcher.

```

style.scssCopy to clipboard.theme-selector__icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
cds-content-switcher-item[selected] .theme-selector__icon {  /* switch icon color when selected */  background-color: $background;Show more

```

Currently the theme switcher looks good but needs the following Javascript to
switch themes.

```

main.jsCopy to clipboardconst handleSwitch = (ev) => {  // Applies new theme or defers to system preferences by removing theme  switch (ev.detail.item.value) {    case 'light':      bodyEl.classList.remove('g100');      bodyEl.classList.add('g10');      break;    case 'dark':      bodyEl.classList.remove('g10');Show more

```

At this point our theme switcher is mostly working, only the checkbox
`Global header reverse theme` appears to do nothing. In the script above the
class `compliment` is being toggled on and off in the `<header>` tag.

A little more CSS is needed to make this functionality work. Add the following
in addition to the existing theme classes.

```

style.scssCopy to clipboard:root .compliment {  @include theme(themes.$g100);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g10);  }}
.g10 .compliment {Show more

```

Then replace the cds-header tags `g100` class in `index.html` with `compliment`.

```

index.htmlCopy to clipboard<cds-header class="compliment"> . . . </cds-header>

```

### Skip to content

When creating navigation headers, it’s important to have a `Skip to content`
link so keyboard users can skip the navigation items and go straight to the main
content.

Import the component in `main.js`

```

main.jsCopy to clipboardimport '@carbon/web-components/es/components/skip-to-content/index.js';

```

Add in to our header in `index.html` as the first child of our `cds-header`
component.

```

index.htmlCopy to clipboard<cds-header class="compliment">  <cds-skip-to-content href="#main-content"></cds-skip-to-content>  <!-- keep existing content   .    .    .   --></cds-header>

```

Then update the main tag to include the id `main-content`

```

index.htmlCopy to clipboard<main id="main-content" class="main">  <!-- keep existing content   .    .    .   --></main>

```

### Update the repositories page

One final task before completing step 1. Our repositories page has missed out on
all of the HTML updates we have been making to the landing page. Simply copy the
contents of `index.html` to `repositories.html` and replace `LANDING` with
`REPOSITORIES`.

NOTE: We could do something better than duplicating our pages. This could be
pure Javascript, HTML templates or native Web Components. However, that might
distract from the message that no library is required.

## Push to GitHub

That is it you are done. Just one more push to save your completion of step 1.

### Git commit and push

First, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard

```

Then, push to your repository:

```

git push -u origin step-1Copy to clipboard

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
git clone [your fork SSH/HTTPS]cd carbon-tutorial-web-componentsCopy to clipboard
```

```bash
git clone [your fork SSH/HTTPS]cd carbon-tutorial-web-components
```

```
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-web-components.gitCopy to clipboard
```

```bash
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-web-components.git
```

```
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-web-components.gitCopy to clipboard
```

```bash
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-web-components.git
```

```
git remote -vCopy to clipboard
```

```bash
git remote -v
```

```
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (push)Copy to clipboard
```

```bash
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-web-components.git (push)
```

```
git fetch upstreamgit checkout -b step-1 upstream/step-1Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b step-1 upstream/step-1
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
pnpm add @carbon/web-components @carbon/stylesCopy to clipboard
```

```bash
pnpm add @carbon/web-components @carbon/styles
```

```
pnpm add sassCopy to clipboard
```

```bash
pnpm add sass
```

```
pnpm devCopy to clipboard
```

```bash
pnpm dev
```

```
style.scssCopy to clipboard@use '@carbon/styles/scss/reset';
```

```scss
@use '@carbon/styles/scss/reset';
```

```
main.jsCopy to clipboardimport './style.scss';import '@carbon/web-components/es/components/button/button.js';
```

```javascript
import './style.scss';import '@carbon/web-components/es/components/button/button.js';
```

```
index.htmlCopy to clipboard<script type="module" src="/main.js"></script>
```

```html
<script type="module" src="/main.js"></script>
```

```
index.htmlCopy to clipboard<link rel="icon" type="image/svg+xml" href="/vite.svg" />
```

```html
<link rel="icon" type="image/svg+xml" href="/vite.svg" />
```

```
index.htmlCopy to clipboard<link rel="icon" type="image/svg+xml" href="/carbon.svg" />
```

```html
<link rel="icon" type="image/svg+xml" href="/carbon.svg" />
```

```
index.htmlCopy to clipboard<div id="app"></div>
```

```html
<div id="app"></div>
```

```
index.htmlCopy to clipboard<cds-button class="button">Click more than once</cds-button>
```

```html
<cds-button class="button">Click more than once</cds-button>
```

```
style.scssCopy to clipboard@use '@carbon/styles/scss/theme' as *;@use '@carbon/styles/scss/themes';
:root {  @include theme(themes.$g10);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g100);  }Show more
```

```scss
@use '@carbon/styles/scss/theme' as *;@use '@carbon/styles/scss/themes';
:root {  @include theme(themes.$g10);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g100);  }
```

```
main.jsCopy to clipboardconst bodyEl = document.querySelector('body');
// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
Show more
```

```javascript
const bodyEl = document.querySelector('body');
// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
```

```
main.jsCopy to clipboardimport '@carbon/web-components/es/components/ui-shell/index';
```

```javascript
import '@carbon/web-components/es/components/ui-shell/index';
```

```
index.htmlCopy to clipboard<body class="app"></body>
```

```html
<body class="app"></body>
```

```
index.htmlCopy to clipboard<main class="main">  <cds-button class="button">Click more than once</cds-button></main>
```

```html
<main class="main">  <cds-button class="button">Click more than once</cds-button></main>
```

```
index.htmlCopy to clipboard<header>  <cds-header class="g100">    <cds-header-name href="./" prefix="IBM">Carbon Tutorial</cds-header-name>  </cds-header></header>
```

```html
<header>  <cds-header class="g100">    <cds-header-name href="./" prefix="IBM">Carbon Tutorial</cds-header-name>  </cds-header></header>
```

```
@use '@carbon/styles/scss/spacing' as *; /* near top of file */
.app {  display: grid;  grid-template-rows: $spacing-09 1fr;  height: 100vh;  overflow: hidden;}
Copy to clipboardShow more
```

```path
@use '@carbon/styles/scss/spacing' as *; /* near top of file */
.app {  display: grid;  grid-template-rows: $spacing-09 1fr;  height: 100vh;  overflow: hidden;}
```

```
index.htmlCopy to clipboard<cds-header-nav menu-bar-label="Carbon Tutorial">  <cds-header-nav-item href="./repositories.html"    >Repositories</cds-header-nav-item  ></cds-header-nav>
```

```html
<cds-header-nav menu-bar-label="Carbon Tutorial">  <cds-header-nav-item href="./repositories.html"    >Repositories</cds-header-nav-item  ></cds-header-nav>
```

```
index.htmlCopy to clipboard<cds-header-menu-button  button-label-active="Close menu"  button-label-inactive="Open menu"></cds-header-menu-button>
```

```html
<cds-header-menu-button  button-label-active="Close menu"  button-label-inactive="Open menu"></cds-header-menu-button>
```

```
index.htmlCopy to clipboard<cds-side-nav  is-not-persistent  aria-label="Side navigation"  collapse-mode="${SIDE_NAV_COLLAPSE_MODE.RESPONSIVE}">  <cds-side-nav-items>    <cds-side-nav-link href="./repositories.html">      Repositories    </cds-side-nav-link>  </cds-side-nav-items>Show more
```

```html
<cds-side-nav  is-not-persistent  aria-label="Side navigation"  collapse-mode="${SIDE_NAV_COLLAPSE_MODE.RESPONSIVE}">  <cds-side-nav-items>    <cds-side-nav-link href="./repositories.html">      Repositories    </cds-side-nav-link>  </cds-side-nav-items>
```

```
pnpm add @carbon/iconsCopy to clipboard
```

```bash
pnpm add @carbon/icons
```

```
style.scssCopy to clipboard.action-icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
.notification .action-icon {  mask: url('/notification.svg') no-repeat center;}Show more
```

```scss
.action-icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
.notification .action-icon {  mask: url('/notification.svg') no-repeat center;}
```

```
index.htmlCopy to clipboard<div class="cds--header__global">  <cds-header-global-action    aria-label="Notifications"    class="notification"    panel-id="notification-panel">    <div class="action-icon" slot="icon"></div>  </cds-header-global-action>  <cds-header-global-action    aria-label="User Profile"Show more
```

```html
<div class="cds--header__global">  <cds-header-global-action    aria-label="Notifications"    class="notification"    panel-id="notification-panel">    <div class="action-icon" slot="icon"></div>  </cds-header-global-action>  <cds-header-global-action    aria-label="User Profile"
```

```
index.htmlCopy to clipboard<cds-header-panel id="notification-panel" aria-label="Notification Panel"  >Notification Panel</cds-header-panel><cds-header-panel id="user-profile-panel" aria-label="User profile Panel"  >User profile Panel</cds-header-panel><cds-header-panel id="app-switcher-panel" aria-label="App switcher Panel"  >App switcher Panel</cds-header-panel>
```

```html
<cds-header-panel id="notification-panel" aria-label="Notification Panel"  >Notification Panel</cds-header-panel><cds-header-panel id="user-profile-panel" aria-label="User profile Panel"  >User profile Panel</cds-header-panel><cds-header-panel id="app-switcher-panel" aria-label="App switcher Panel"  >App switcher Panel</cds-header-panel>
```

```
main.jsCopy to clipboardconst handleGlobalActionClick = (ev) => {  const targetPanelId = ev.currentTarget.getAttribute('panel-id');  const panels = document.querySelectorAll('cds-header-panel');  // check to see if other panels are open and close them  panels.forEach((panel) => {    if (panel.id !== targetPanelId) {      panel.expanded = false;    }  });Show more
```

```javascript
const handleGlobalActionClick = (ev) => {  const targetPanelId = ev.currentTarget.getAttribute('panel-id');  const panels = document.querySelectorAll('cds-header-panel');  // check to see if other panels are open and close them  panels.forEach((panel) => {    if (panel.id !== targetPanelId) {      panel.expanded = false;    }  });
```

```
index.htmlCopy to clipboard<main class="main">LANDING PAGE</main>
```

```html
<main class="main">LANDING PAGE</main>
```

```
main.jsCopy to clipboard// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
// set initial theme based on preferencesif (matchMedia('(prefers-color-scheme: dark)')) {Show more
```

```javascript
// button click handlerconst handleClick = () => {  bodyEl.classList.toggle('g10');  bodyEl.classList.toggle('g100');};document.querySelector('.button').addEventListener('click', handleClick);
// set initial theme based on preferencesif (matchMedia('(prefers-color-scheme: dark)')) {
```

```
main.jsCopy to clipboardimport '@carbon/web-components/es/components/checkbox/index';import '@carbon/web-components/es/components/content-switcher/index';
```

```javascript
import '@carbon/web-components/es/components/checkbox/index';import '@carbon/web-components/es/components/content-switcher/index';
```

```
index.htmlCopy to clipboard<div class="header-panel__content">  <h2 class="header-panel__title">User profile Panel</h2>
  <cds-content-switcher value="system" class="theme-selector">    <cds-content-switcher-item icon value="light">      <div class="theme-selector__icon theme-selector__icon--light"></div>      <span slot="tooltip-content">Light theme</span>    </cds-content-switcher-item>    <cds-content-switcher-item icon value="system">Show more
```

```html
<div class="header-panel__content">  <h2 class="header-panel__title">User profile Panel</h2>
  <cds-content-switcher value="system" class="theme-selector">    <cds-content-switcher-item icon value="light">      <div class="theme-selector__icon theme-selector__icon--light"></div>      <span slot="tooltip-content">Light theme</span>    </cds-content-switcher-item>    <cds-content-switcher-item icon value="system">
```

```
style.scssCopy to clipboard@use '@carbon/styles/scss/type' as *; /* place at top of file */
.header-panel__content {  display: flex;  flex-direction: column;  gap: $spacing-05;  padding: $spacing-05;}
Show more
```

```scss
@use '@carbon/styles/scss/type' as *; /* place at top of file */
.header-panel__content {  display: flex;  flex-direction: column;  gap: $spacing-05;  padding: $spacing-05;}
```

```
style.scssCopy to clipboard.theme-selector__icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
cds-content-switcher-item[selected] .theme-selector__icon {  /* switch icon color when selected */  background-color: $background;Show more
```

```scss
.theme-selector__icon {  width: 1.25rem;  height: 1.25rem;  background-color: $text-primary;}
cds-content-switcher-item[selected] .theme-selector__icon {  /* switch icon color when selected */  background-color: $background;
```

```
main.jsCopy to clipboardconst handleSwitch = (ev) => {  // Applies new theme or defers to system preferences by removing theme  switch (ev.detail.item.value) {    case 'light':      bodyEl.classList.remove('g100');      bodyEl.classList.add('g10');      break;    case 'dark':      bodyEl.classList.remove('g10');Show more
```

```javascript
const handleSwitch = (ev) => {  // Applies new theme or defers to system preferences by removing theme  switch (ev.detail.item.value) {    case 'light':      bodyEl.classList.remove('g100');      bodyEl.classList.add('g10');      break;    case 'dark':      bodyEl.classList.remove('g10');
```

```
style.scssCopy to clipboard:root .compliment {  @include theme(themes.$g100);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g10);  }}
.g10 .compliment {Show more
```

```scss
:root .compliment {  @include theme(themes.$g100);
  @media (prefers-color-scheme: dark) {    @include theme(themes.$g10);  }}
.g10 .compliment {
```

```
index.htmlCopy to clipboard<cds-header class="compliment"> . . . </cds-header>
```

```html
<cds-header class="compliment"> . . . </cds-header>
```

```
main.jsCopy to clipboardimport '@carbon/web-components/es/components/skip-to-content/index.js';
```

```javascript
import '@carbon/web-components/es/components/skip-to-content/index.js';
```

```
index.htmlCopy to clipboard<cds-header class="compliment">  <cds-skip-to-content href="#main-content"></cds-skip-to-content>  <!-- keep existing content   .    .    .   --></cds-header>
```

```html
<cds-header class="compliment">  <cds-skip-to-content href="#main-content"></cds-skip-to-content>  <!-- keep existing content   .    .    .   --></cds-header>
```

```
index.htmlCopy to clipboard<main id="main-content" class="main">  <!-- keep existing content   .    .    .   --></main>
```

```html
<main id="main-content" class="main">  <!-- keep existing content   .    .    .   --></main>
```

```
git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 1"
```

```
git push -u origin step-1Copy to clipboard
```

```bash
git push -u origin step-1
```
