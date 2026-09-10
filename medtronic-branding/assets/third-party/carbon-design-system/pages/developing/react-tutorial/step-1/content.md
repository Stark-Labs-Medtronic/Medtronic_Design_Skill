# 1. Installing Carbon – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/react-tutorial/step-1/

# 1. Installing Carbon

Starting from a base Create Next App, let’s install Carbon and begin using
Carbon components. By the end you will have a Next.js app that uses the UI Shell
to navigate between pages.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/react-tutorial/step-1/#fork-clone-and-branch)

- [Build and start](https://carbondesignsystem.com/developing/react-tutorial/step-1/#build-and-start)

- [Install Carbon](https://carbondesignsystem.com/developing/react-tutorial/step-1/#install-carbon)

- [Install and build Sass](https://carbondesignsystem.com/developing/react-tutorial/step-1/#install-and-build-sass)

- [Add UI Shell](https://carbondesignsystem.com/developing/react-tutorial/step-1/#add-ui-shell)

- [Create pages](https://carbondesignsystem.com/developing/react-tutorial/step-1/#create-pages)

- [Add routing](https://carbondesignsystem.com/developing/react-tutorial/step-1/#add-routing)

- [Submit pull request](https://carbondesignsystem.com/developing/react-tutorial/step-1/#submit-pull-request)

## Preview

A
[preview](https://carbon-tutorial-nextjs-git-v11-next-step-2-carbon-design-system.vercel.app/)
of what you will build:

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-nextjs](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
that we’ll use as a starting point for each step.

### Fork

To begin, fork
[carbon-tutorial-nextjs](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
using your GitHub account. Please note when forking you must uncheck “Copy the
main branch only” so you can access all branches / steps of the tutorial.

### Clone

Go to your forked repository, copy the SSH or HTTPS URL and in your terminal run
the two commands to get the repository in your local file system and enter that
directory.

```

git clone [your fork SSH/HTTPS]cd carbon-tutorial-nextjsCopy to clipboard

```

### Add upstream remote

Add a remote called `upstream` so we can eventually submit a pull request once
you have completed this tutorial step. There are two choices: SSH or HTTPS

#### SSH

```

git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-nextjs.gitCopy to clipboard

```

#### HTTPS

```

git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-nextjs.gitCopy to clipboard

```

Verify that your forked repository remotes are correct:

```

git remote -vCopy to clipboard

```

Your terminal should output something like this:

```

origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (push)Copy to clipboard

```

### Branch

Now that we have our repository set up, let’s check out the branch for this
tutorial step’s starting point. Run the two commands:

```

git fetch upstreamgit checkout -b v11-next-step-1 upstream/v11-next-step-1Copy to clipboard

```

## Build and start

We have the repository forked to your GitHub account, cloned down to your
machine, and the starting branch checked out. Next, install the Next.js app’s
dependencies with:

```

yarnCopy to clipboard

```

After the dependencies are installed, create a build with:

```

yarn buildCopy to clipboard

```

After the build and dependencies are installed, you can start the app with:

```

yarn devCopy to clipboard

```

This is a Next.js 13 app with a home page, its root layout and a global style
sheet.

Your default browser should open up with an empty page that says:
`Hello Carbon! Well, not quite yet. This is the starting point for the Carbon React tutorial.`

## Install Carbon

Even though we installed existing dependencies, we’ve yet to install our v11
Carbon package, `@carbon/react`, which contains everything you need to build
with.

Stop your development server with `CTRL-C` and install Carbon dependencies with:

```

yarn add @carbon/react@1.33.0Copy to clipboard

```

## Install and build Sass

We need to run a Sass build as the Carbon styles are authored in Sass, so run
the following command to install `sass` as a dependency.

```

yarn add sass@1.63.6Copy to clipboard

```

Then, start the app again. If your app’s currently running, you’ll need to
restart it for the new environment variable to be used.

```

yarn devCopy to clipboard

```

The app looks as it did before. Next, let’s prepare our app for a Sass build.

In `src` directory, rename `globals.css` as `globals.scss` and change the import
in `layout.js` from `global.css` to `globals.scss`.

### Import carbon-component styles

In `globals.scss`, import the Carbon styles by adding the following at the top
of the file:

```

src/app/globals.scssCopy to clipboard@use '@carbon/react';
/// Remove overrides once Carbon bugs are fixed upstream./// Need grid option to not add page gutters at large viewports, to also use when nesting grids/// @link https://github.com/carbon-design-system/carbon/issues/2792@media (min-width: 42rem) {  .cds--grid--no-gutter {    padding-left: 1rem;    padding-right: 1rem;Show more

```

In Next.js 13 there is a global style sheet and then every page has it own,
optional, style sheet.

Next, we’ll import a `Button` from Carbon to test that our dependencies are
working properly. At the top of `page.js`, import the `Button` by adding the
following:

```

src/app/page.jsCopy to clipboard'use client';import { Button } from '@carbon/react';

```

We need `use client` since the Carbon components we use are all client
components. In Next 13 pages are pulled in as children to layout files (see
RootLayout `src/app/layout.js`) and these are always server side components.

In the `Page` component return, you can now replace:

```

src/app/page.jsCopy to clipboard<div>  Hello Carbon! Well, not quite yet. This is the starting point for the Carbon  React tutorial.</div>

```

with:

```

src/app/page.jsCopy to clipboard<Button>Button</Button>

```

Congratulations, you’ve imported your first component! You should see a Carbon
styled button on the page.

## Add UI Shell

Next, we’re going to create a React component called `TutorialHeader` to use
with the UI Shell Carbon component. In the `src` directory, create a
`components` directory and inside of that, a `TutorialHeader` directory. Create
the following files inside `src/components/TutorialHeader`:

```

src/components/TutorialHeader├──_tutorial-header.scss└──TutorialHeader.jsCopy to clipboard

```

### Add UI Shell Sass

Next, in `globals.scss`, we’ll import our `TutorialHeader` styles. Add this line
to the top of the file:

```

src/app/globals.scssCopy to clipboard@use '@/components/TutorialHeader/tutorial-header';

```

### Import and export the header

Next we’ll import our Carbon UI Shell components into `TutorialHeader.js`. Set
up the file like so:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport {  Header,  HeaderContainer,  HeaderName,  HeaderNavigation,  HeaderMenuButton,  HeaderMenuItem,  HeaderGlobalBar,  HeaderGlobalAction,Show more

```

**Note:** you can find a description of the different components used in the UI
Shell in our
[@carbon/react](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/UIShell)
package.

**Note:** When creating navigation headers, it’s important to have a
`Skip to content` link so keyboard users can skip the navigation items and go
straight to the main content.

### Import icons

First we will install the icons we will use in the header

```

yarn add @carbon/icons-reactCopy to clipboard

```

Now let’s import the icons. In the `TutorialHeader.js` file, we need to import
each individual icon we will use.

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport { Switcher, Notification, UserAvatar } from '@carbon/icons-react';

```

Then we need to add the `HeaderGlobalAction` component inside of the
`HeaderGlobalBar` where we will add our icons. These represent actions in the
header a user can make. Replace:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderGlobalBar />

```

With:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderGlobalBar>  <HeaderGlobalAction    aria-label="Notifications"    tooltipAlignment="center"    className="action-icons">    <Notification size={20} />  </HeaderGlobalAction>  <HeaderGlobalAction    aria-label="User Avatar"Show more

```

### Render the header

Next we’ll render our UI Shell by importing our `TutorialHeader` component and
`Content` into a provider components in the Root Layout. We do this because
layout components in Next.js 13 are server-side components.

**Note:** We can wrap the `{children}` in Root Layout with a Provider component
that will use to hold the components we want across all pages. See this
[explanation](https://nextjs.org/docs/getting-started/react-essentials#rendering-third-party-context-providers-in-server-components)
in Next docs.

```

src/app/layout.jsCopy to clipboardimport './globals.scss';import { Providers } from './providers';
export const metadata = {  title: 'Carbon + Next13',  description: 'IBM Carbon Tutorial with Next.js 13',};
export default function RootLayout({ children }) {Show more

```

Create a `providers.js` file within the app folder with the following content.

```

src/app/providers.jsCopy to clipboard'use client';
import TutorialHeader from '@/components/TutorialHeader/TutorialHeader';import { Content } from '@carbon/react';
export function Providers({ children }) {  return (    <div>      <TutorialHeader />Show more

```

You should now see a styled UI Shell header and a button below it.

## Create pages

Next thing we need to do is create the files for our content. We already have a
folder called `app` in `src`. This should be a sibling of `src/components`.

Since our app will have two pages, we’ll create two folders in `src/app`.

```

src/app├── home└── reposCopy to clipboard

```

Next.js uses these folders for page routing which is built into the framework,
we do not need separate React routing. In each there is a `page.js` and
optionally a `layout.js` and styling sheet.

Create the following files in the `home` folder:

```

src/app/home├── _landing-page.scss└── page.jsCopy to clipboard

```

Create the following files in the `repos` folder:

```

src/app/repos├── _repo-page.scss└── page.jsCopy to clipboard

```

### Set up content Sass

Next, we’ll import our content Sass files in `globals.scss`, like so:

```

src/app/globals.scssCopy to clipboard@use '@/app/home/landing-page';@use '@/app/repos/repo-page';

```

### Import and export content pages

Now that our stylesheets are set up, we need to create our pages’ components.
Starting with `LandingPage`, just like with our header, we need to export the
component in `javascript path=src/app/home/page.js` by adding:

```

src/app/home/page.jsCopy to clipboard`use client`;
export default function LandingPage() {  return <div>LANDING PAGE</div>;}

```

And we will add this into our root page:

```

src/app/page.jsCopy to clipboardimport LandingPage from './home/page';
export default function Page() {  return <LandingPage />;}

```

We’ll repeat this process with `RepoPage`.

```

src/app/repos/page.jsCopy to clipboard`use client`;
export default function RepoPage() {  return <div>REPO PAGE</div>;}

```

Navigate to the repos page by adding `/repos` at the end of your locally hosted
site to see your repos page.

Awesome! We’ve just created our content pages with automatic page routing
courtesy of Next.js.

After that we need to do a couple of quick fixes to the UI Shell to work with
Next.js links.

Add the `Link` import in `TutorialHeader.js`:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport Link from 'next/link';

```

We need to use the `Link` component instead of the default anchor elements to
prevent full page reload when navigating to different pages in Next.js
applications. To use `Link`, we wrap `HeaderName` component and pass through
`href` elements to it:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<Link href="/" passHref legacyBehavior>  <HeaderName prefix="IBM">Carbon Tutorial</HeaderName></Link>

```

Do the same with the components `HeaderNavigation` and `HeaderSideNavItems` that
contain `href="/repos"`, updating them to:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderNavigation aria-label="Carbon Tutorial">  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderNavigation>

```

and the following:

```

src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderSideNavItems>  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderSideNavItems>

```

You should now have a working header that routes to different pages without full
page reload! However, our page does not match the design specs. We need to
change the header theme to `g100` to match the specs.

In `providers.js` we will add inline theming for our navigation. First, we need
to import our new `Theme` component.

```

src/app/providers.jsCopy to clipboardimport { Content, Theme } from '@carbon/react';

```

Then, we will wrap `Theme` around our header, and set the zoned theme using the
`theme` prop, which accepts one of four strings: `"white"`, `"g10"`, `"g90"` or
`"g100"`.

```

src/app/providers.jsCopy to clipboard<div>  <Theme theme="g100">    <TutorialHeader />  </Theme>  <Content>{children}</Content></div>

```

We have one last thing to fix before we’re done. Because we changed the header
theme to dark, the `<HeaderGlobalAction>` tooltips are now light instead of
dark, and when you scroll the page, it blends into the content. To fix this,
we’ll add some overriding styles in `_tutorial-header.scss`:

```

src/components/TutorialHeader/_tutorial-header.scssCopy to clipboard@use '@carbon/react/scss/colors';
// overriding header tooltip bg color// because the navigation is dark themed while the content is white// which means the dark theme tooltip bg blends into the white content bg.cds--header__global .cds--popover-content {  background-color: colors.$gray-20;}
Show more

```

## Submit pull request

We’re going to submit a pull request to verify completion of this tutorial step
and demonstrate a couple of related concepts.

### Continuous integration (CI) check

We have a `ci-check` script defined in `package.json` that verifies file
formatting for files that have been touched since the last Git commit with a
tool called [Prettier](https://prettier.io/). You’d typically also have that
script run your test suite as part of your CI build. Go ahead and make sure
everything looks good with:

```

yarn ci-checkCopy to clipboard

```

**Note:** If the `ci-check` is giving an error, it’s likely that some of your
source files are not properly formatted. This could happen if your text editor
isn’t formatting with Prettier on save. To get `ci-check` to pass, run
`yarn format` then re-run `yarn ci-check`.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard

```

**Note:** You’ll notice that your commit includes binaries in the `.yarn/cache`
folder. That’s expected as the repository is configured to run
[Yarn offline](https://yarnpkg.com/blog/2016/11/24/offline-mirror) for more
reliable builds. Future tutorial steps that don’t install new packages won’t
have `.yarn/cache` commit changes.

Then, push to your repository:

```

git push origin v11-next-step-1Copy to clipboard

```

**Note:** If your Git remote protocol is HTTPS instead of SSH, you may be
prompted to authenticate with GitHub when you push changes. If your GitHub
account has two-factor authentication enabled, we recommend that you follow
these instructions to
[create a personal access token for the command line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line).
That lets you use your token instead of password when performing Git operations
over HTTPS.

**Note:** If you receive a `non-fast-forward` error, it’s likely that your
forked repository is behind the original repository and needs to be updated.
This can happen if the tutorial was updated after you began working on it. To
fix, run `git pull upstream v11-next-step-1` to merge the changes into your
branch, then you can try pushing again. Or, you can
[manually merge](https://help.github.com/en/articles/syncing-a-fork) in the
upstream changes.

### Pull request (PR)

Finally, visit
[carbon-react-tutorial](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`v11-next-step-1` into `base: v11-next-step-1`. Take notice of the
[Netlify](https://www.netlify.com/) bot that deploys a preview of your PR every
time that you push new commits. These previews can be shared and viewed by
anybody to assist the PR review process.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

**Note:** If your PR fails the CircleCI test with the error
`Can't make a request in offline mode`, try running the following command:
`rm -rf .yarn-offline-mirror node_modules && yarn cache clean && yarn install`.
Add and commit the changes once this completes, and try pushing again.

## Code samples

```
git clone [your fork SSH/HTTPS]cd carbon-tutorial-nextjsCopy to clipboard
```

```bash
git clone [your fork SSH/HTTPS]cd carbon-tutorial-nextjs
```

```
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-nextjs.gitCopy to clipboard
```

```bash
git remote add upstream git@github.com:carbon-design-system/carbon-tutorial-nextjs.git
```

```
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-nextjs.gitCopy to clipboard
```

```bash
git remote add upstream https://github.com/carbon-design-system/carbon-tutorial-nextjs.git
```

```
git remote -vCopy to clipboard
```

```bash
git remote -v
```

```
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (push)Copy to clipboard
```

```bash
origin	[your forked repo] (fetch)origin	[your forked repo] (push)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (fetch)upstream	git@github.com:carbon-design-system/carbon-tutorial-nextjs.git (push)
```

```
git fetch upstreamgit checkout -b v11-next-step-1 upstream/v11-next-step-1Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b v11-next-step-1 upstream/v11-next-step-1
```

```
yarnCopy to clipboard
```

```bash
yarn
```

```
yarn buildCopy to clipboard
```

```bash
yarn build
```

```
yarn devCopy to clipboard
```

```bash
yarn dev
```

```
yarn add @carbon/react@1.33.0Copy to clipboard
```

```bash
yarn add @carbon/react@1.33.0
```

```
yarn add sass@1.63.6Copy to clipboard
```

```bash
yarn add sass@1.63.6
```

```
yarn devCopy to clipboard
```

```bash
yarn dev
```

```
src/app/globals.scssCopy to clipboard@use '@carbon/react';
/// Remove overrides once Carbon bugs are fixed upstream./// Need grid option to not add page gutters at large viewports, to also use when nesting grids/// @link https://github.com/carbon-design-system/carbon/issues/2792@media (min-width: 42rem) {  .cds--grid--no-gutter {    padding-left: 1rem;    padding-right: 1rem;Show more
```

```scss
@use '@carbon/react';
/// Remove overrides once Carbon bugs are fixed upstream./// Need grid option to not add page gutters at large viewports, to also use when nesting grids/// @link https://github.com/carbon-design-system/carbon/issues/2792@media (min-width: 42rem) {  .cds--grid--no-gutter {    padding-left: 1rem;    padding-right: 1rem;
```

```
src/app/page.jsCopy to clipboard'use client';import { Button } from '@carbon/react';
```

```javascript
'use client';import { Button } from '@carbon/react';
```

```
src/app/page.jsCopy to clipboard<div>  Hello Carbon! Well, not quite yet. This is the starting point for the Carbon  React tutorial.</div>
```

```html
<div>  Hello Carbon! Well, not quite yet. This is the starting point for the Carbon  React tutorial.</div>
```

```
src/app/page.jsCopy to clipboard<Button>Button</Button>
```

```jsx
<Button>Button</Button>
```

```
src/components/TutorialHeader├──_tutorial-header.scss└──TutorialHeader.jsCopy to clipboard
```

```bash
src/components/TutorialHeader├──_tutorial-header.scss└──TutorialHeader.js
```

```
src/app/globals.scssCopy to clipboard@use '@/components/TutorialHeader/tutorial-header';
```

```scss
@use '@/components/TutorialHeader/tutorial-header';
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport {  Header,  HeaderContainer,  HeaderName,  HeaderNavigation,  HeaderMenuButton,  HeaderMenuItem,  HeaderGlobalBar,  HeaderGlobalAction,Show more
```

```javascript
import {  Header,  HeaderContainer,  HeaderName,  HeaderNavigation,  HeaderMenuButton,  HeaderMenuItem,  HeaderGlobalBar,  HeaderGlobalAction,
```

```
yarn add @carbon/icons-reactCopy to clipboard
```

```bash
yarn add @carbon/icons-react
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport { Switcher, Notification, UserAvatar } from '@carbon/icons-react';
```

```javascript
import { Switcher, Notification, UserAvatar } from '@carbon/icons-react';
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderGlobalBar />
```

```html
<HeaderGlobalBar />
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderGlobalBar>  <HeaderGlobalAction    aria-label="Notifications"    tooltipAlignment="center"    className="action-icons">    <Notification size={20} />  </HeaderGlobalAction>  <HeaderGlobalAction    aria-label="User Avatar"Show more
```

```jsx
<HeaderGlobalBar>  <HeaderGlobalAction    aria-label="Notifications"    tooltipAlignment="center"    className="action-icons">    <Notification size={20} />  </HeaderGlobalAction>  <HeaderGlobalAction    aria-label="User Avatar"
```

```
src/app/layout.jsCopy to clipboardimport './globals.scss';import { Providers } from './providers';
export const metadata = {  title: 'Carbon + Next13',  description: 'IBM Carbon Tutorial with Next.js 13',};
export default function RootLayout({ children }) {Show more
```

```javascript
import './globals.scss';import { Providers } from './providers';
export const metadata = {  title: 'Carbon + Next13',  description: 'IBM Carbon Tutorial with Next.js 13',};
export default function RootLayout({ children }) {
```

```
src/app/providers.jsCopy to clipboard'use client';
import TutorialHeader from '@/components/TutorialHeader/TutorialHeader';import { Content } from '@carbon/react';
export function Providers({ children }) {  return (    <div>      <TutorialHeader />Show more
```

```javascript
'use client';
import TutorialHeader from '@/components/TutorialHeader/TutorialHeader';import { Content } from '@carbon/react';
export function Providers({ children }) {  return (    <div>      <TutorialHeader />
```

```
src/app├── home└── reposCopy to clipboard
```

```bash
src/app├── home└── repos
```

```
src/app/home├── _landing-page.scss└── page.jsCopy to clipboard
```

```bash
src/app/home├── _landing-page.scss└── page.js
```

```
src/app/repos├── _repo-page.scss└── page.jsCopy to clipboard
```

```bash
src/app/repos├── _repo-page.scss└── page.js
```

```
src/app/globals.scssCopy to clipboard@use '@/app/home/landing-page';@use '@/app/repos/repo-page';
```

```scss
@use '@/app/home/landing-page';@use '@/app/repos/repo-page';
```

```
src/app/home/page.jsCopy to clipboard`use client`;
export default function LandingPage() {  return <div>LANDING PAGE</div>;}
```

```javascript
`use client`;
export default function LandingPage() {  return <div>LANDING PAGE</div>;}
```

```
src/app/page.jsCopy to clipboardimport LandingPage from './home/page';
export default function Page() {  return <LandingPage />;}
```

```javascript
import LandingPage from './home/page';
export default function Page() {  return <LandingPage />;}
```

```
src/app/repos/page.jsCopy to clipboard`use client`;
export default function RepoPage() {  return <div>REPO PAGE</div>;}
```

```javascript
`use client`;
export default function RepoPage() {  return <div>REPO PAGE</div>;}
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboardimport Link from 'next/link';
```

```javascript
import Link from 'next/link';
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<Link href="/" passHref legacyBehavior>  <HeaderName prefix="IBM">Carbon Tutorial</HeaderName></Link>
```

```javascript
<Link href="/" passHref legacyBehavior>  <HeaderName prefix="IBM">Carbon Tutorial</HeaderName></Link>
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderNavigation aria-label="Carbon Tutorial">  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderNavigation>
```

```javascript
<HeaderNavigation aria-label="Carbon Tutorial">  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderNavigation>
```

```
src/components/TutorialHeader/TutorialHeader.jsCopy to clipboard<HeaderSideNavItems>  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderSideNavItems>
```

```javascript
<HeaderSideNavItems>  <Link href="/repos" passHref legacyBehavior>    <HeaderMenuItem>Repositories</HeaderMenuItem>  </Link></HeaderSideNavItems>
```

```
src/app/providers.jsCopy to clipboardimport { Content, Theme } from '@carbon/react';
```

```javascript
import { Content, Theme } from '@carbon/react';
```

```
src/app/providers.jsCopy to clipboard<div>  <Theme theme="g100">    <TutorialHeader />  </Theme>  <Content>{children}</Content></div>
```

```javascript
<div>  <Theme theme="g100">    <TutorialHeader />  </Theme>  <Content>{children}</Content></div>
```

```
src/components/TutorialHeader/_tutorial-header.scssCopy to clipboard@use '@carbon/react/scss/colors';
// overriding header tooltip bg color// because the navigation is dark themed while the content is white// which means the dark theme tooltip bg blends into the white content bg.cds--header__global .cds--popover-content {  background-color: colors.$gray-20;}
Show more
```

```scss
@use '@carbon/react/scss/colors';
// overriding header tooltip bg color// because the navigation is dark themed while the content is white// which means the dark theme tooltip bg blends into the white content bg.cds--header__global .cds--popover-content {  background-color: colors.$gray-20;}
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
git add --all && git commit -m "feat(tutorial): complete step 1"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 1"
```

```
git push origin v11-next-step-1Copy to clipboard
```

```bash
git push origin v11-next-step-1
```
