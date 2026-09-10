# 3. Using APIs – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/web-components-tutorial/step-3/

# 3. Using APIs

This step takes our static components and populates them with data from the
GitHub GraphQL API – loading states and all. We’ll be displaying Carbon
repository information in a data table.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/web-components-tutorial/step-3/#fork-clone-and-branch)

- [Install dependencies](https://carbondesignsystem.com/developing/web-components-tutorial/step-3/#install-dependencies)

- [Fetch and render data](https://carbondesignsystem.com/developing/web-components-tutorial/step-3/#fetch-and-render-data)

- [Pagination](https://carbondesignsystem.com/developing/web-components-tutorial/step-3/#pagination)

- [Push to GitHub](https://carbondesignsystem.com/developing/web-components-tutorial/step-3/#push-to-github)

## Preview

The [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) is
very well documented, we’ll use it to fetch Carbon-related data for this Carbon
tutorial.

To do so, we’ll be using
[Octokit Core](https://github.com/octokit/core.js/#readme), a client that makes
it easy to interact with GitHub’s APIs.

A
[preview](https://carbon-tutorial-nextjs-git-step-4-carbon-design-system.vercel.app/)
of what you will build (see repositories page):

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

git fetch upstreamgit checkout -b step-3 upstream/step-3Copy to clipboard

```

### Build and start app

Install the app’s dependencies and build the app:

```

pnpm iCopy to clipboard

```

Then, start the app:

```

pnpm devCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/web-components-tutorial/step-1#fork-clone-and-branch/step-2)
left off. Stop your app with `CTRL-C` and let’s get everything installed.

## Install dependencies

We’ll need to install `@octokit/core`, a package that allows us to query GitHub
APIs easily. Stop your development server with `CTRL-C` and install the octokit
dependency with:

```

pnpm add @octokit/coreCopy to clipboard

```

Then, start the app again. If your app’s currently running, you’ll need to
restart it.

```

pnpm devCopy to clipboard

```

## Fetch and render data

### Imports

Add the following import Octokit into `repos.js` and create a new instance of
Octokit.

```

repos.jsCopy to clipboardimport { Octokit } from '@octokit/core';
const octokitClient = new Octokit({});

```

### API Request

Next, we’ll assemble our GitHub API request to fetch a list of repositories that
belong to the `carbon-design-system` GitHub organization.

First empty the data array in `repos.js`

```

repos.jsCopy to clipboardlet data = [];

```

Then add the function `fetchData` calling it immediately afterwards.

```

repos.jsCopy to clipboardconst fetchData = async () => {  const res = await octokitClient.request('GET /orgs/{org}/repos', {    org: 'carbon-design-system',    per_page: 75,    sort: 'updated',    direction: 'desc',  });
  if (res.status === 200) {Show more

```

### Rendering the data

If you have the application running then the only change you see is an empty
table. Let’s fix that next.

In `repositories.html` just above the `<cds-table>` add a table skeleton.

```

repositories.htmlCopy to clipboard<cds-table-skeleton></cds-table-skeleton>

```

Then move the `<cds-table>` into a template called `template--table` at the
bottom of the file.

```

repositories.htmlCopy to clipboard<template id="template--table">  <cds-table expandable>    <cds-table-header-title slot="title"      >Carbon Repositories</cds-table-header-title    >    <cds-table-header-description slot="description"      >A collection of public Carbon repositories.</cds-table-header-description    >    <cds-table-head>Show more

```

With the application running the repositories page now shows the skeleton table.
Skeleton components are used in the Carbon Design System to information is still
being loaded. For further details on
[Carbon loading patterns](https://carbondesignsystem.com/patterns/loading-pattern/).

Returning to `repos.js` we will makes use of the fetched data to replace the
skeleton table. Find the current call to `updateTable`

```

repos.jsCopy to clipboardupdateTable();

```

and replace it with the new function called `replaceSkeleton` below:

```

repos.jsCopy to clipboardconst replaceSkeleton = () => {  const tableSkeleton = document.querySelector('cds-table-skeleton');  const tableTemplate = document.querySelector('template#template--table');
  if (tableSkeleton && tableTemplate) {    tableSkeleton.replaceWith(tableTemplate.content.cloneNode(true));    // update table rows    updateTable();  }Show more

```

This function locates the `template--table` and replaces the skeleton with it.
It then makes a call to `updateTable` to add the rows.

We are now ready to display the data by adjusting the function `fetchData` by
uncommenting the call to `replaceSkeleton`.

```

repos.jsCopy to clipboard// replace table here// replaceSkeleton();

```

to leave:

```

repos.jsCopy to clipboard// replace table herereplaceSkeleton();

```

At this point when you refresh the `repositories` page the table skeleton is
briefly shown before the table is populated with data from github. The link
column however just shows `link` we will fix that next.

At the top of `repos.js` import the `cds-link` component.

```

repos.jsCopy to clipboardimport '@carbon/web-components/es/components/link/index';

```

Find `links: 'link'` in the `fetchData` function and replace it with:

```

repos.jsCopy to clipboardlinks: { url: row.html_url, homepage: row.homepage },

```

In our `updateTable` function we need to do something different for the links
key. Replace

```

repos.jsCopy to clipboardkeyEl.innerHTML = row[key];

```

with

```

repos.jsCopy to clipboardif (key === 'links') {  keyEl.innerHTML = `<ul class="link-list">  <li>    <cds-link href="${row[key].url}">GitHub</cds-link>  </li>  <li>    <cds-link href="${row[key].homepage}">Homepage</cds-link>  </li></ul>`;Show more

```

Now it we could have added the HTML for the links in `repositories.html` but
this serves to demonstrate that as with standard HTML tags it is possible to
simply insert Carbon Web Components as innerHTML using a string. Just a little
bit of CSS is needed to present this as per our tutorial design.

Open `styles.scss` and add the following.

```

style.scssCopy to clipboard.link-list {  display: flex;  list-style: none;  padding: 0;}
.link-list li:not(:last-child) {  padding-inline-end: $spacing-02;
Show more

```

## Pagination

The data rendered in our table produces quite a tall page which grows with each
new Carbon repository. To complete our repositories page we will add pagination
to the table.

In `repos.js` import the pagination component.

```

repos.jsCopy to clipboardimport '@carbon/web-components/es/components/pagination/index';

```

Now, as part of the `template--table` template we can add the pagination to
`repositories.html` after the closing `<cds-table>` tag.

```

repositories.htmlCopy to clipboard<cds-pagination  backward-text="Previous page"  forward-text="Next page"  itemsPerPageText="Items per page">  <cds-select-item value="10">10</cds-select-item>  <cds-select-item value="20">20</cds-select-item>  <cds-select-item value="30">30</cds-select-item>  <cds-select-item value="40">40</cds-select-item>  <cds-select-item value="50">50</cds-select-item>Show more

```

**Note:** The `Pagination` component isn’t inherently connected in any way to
the `DataTable` - we need to tell it what to do when a change occurs using the
`onChange` prop. This includes both page size changes and displaying different
rows.

**Note:** Like the other Carbon Web Components components, `Pagination`
component examples can be found in
[Storybook](https://web-components.carbondesignsystem.com/?path=/story/components-pagination--overview)
by browsing the story and knobs.

If you scroll to the bottom of the `repositories` page in the browser you should
see the pagination component rendered.

Back in `repos.js` next to the declaration of our data array add two further
variables to work with the pagination component. Where we declare the data
variable, add variables for page size and row index.

```

repos.jsCopy to clipboardlet data = [];let pageSize = 10;let firstRowIndex = 0;

```

Next we need to add some script to handle events raised by the pagination
component and update it with the values defined for `pageSize` and
`firstRowIndex`.

```

repos.jsCopy to clipboardconst handlePageChangeCurrent = ({ detail }) => {  firstRowIndex = (detail.page - 1) * detail.pageSize;  updateTable();};
const handlePageSizeChange = ({ detail }) => {  pageSize = detail.pageSize;  updateTable();};Show more

```

Add a call to `updatePagination` in `replaceSkeleton` just after the call to
`updateTable`

```

repos.jsCopy to clipboard// update table rowsupdateTable();
// update paginationupdatePagination();

```

When triggered the handlers update `firstRowIndex` and `pageSize` before calling
`updateTable` which re-renders our table rows. Before it all works we need to
make a change to `updateTable` to render just the rows on the current page.

Currently, we iterate over the data as follows:

```

repos.jsCopy to clipboard// iterate over data and render rowsdata.forEach((row) => {  // rows update here});

```

Change this introducing a filter before the `forEach`.

```

repos.jsCopy to clipboard// iterate over data and render rowsdata  .filter((v, i) => i >= firstRowIndex && i < firstRowIndex + pageSize)  .forEach((row) => {    // rows update here  });

```

Refreshing the repositories page should now show just ten rows. Try changing the
page size and the current page number, this should result in new data being
loaded.

That does it! Your data table should fetch GitHub data on first render. You can
expand each row to see the repository’s description. You can modify the
pagination items per page and cycle through pages or jump to a specific page of
repositories.

## Push to GitHub

That is it you are done. Just one more push to save your completion of step 3.

### Git commit and push

First, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard

```

Then, push to your repository:

```

git push -u origin step-3Copy to clipboard

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
git fetch upstreamgit checkout -b step-3 upstream/step-3Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b step-3 upstream/step-3
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
pnpm add @octokit/coreCopy to clipboard
```

```bash
pnpm add @octokit/core
```

```
pnpm devCopy to clipboard
```

```bash
pnpm dev
```

```
repos.jsCopy to clipboardimport { Octokit } from '@octokit/core';
const octokitClient = new Octokit({});
```

```javascript
import { Octokit } from '@octokit/core';
const octokitClient = new Octokit({});
```

```
repos.jsCopy to clipboardlet data = [];
```

```javascript
let data = [];
```

```
repos.jsCopy to clipboardconst fetchData = async () => {  const res = await octokitClient.request('GET /orgs/{org}/repos', {    org: 'carbon-design-system',    per_page: 75,    sort: 'updated',    direction: 'desc',  });
  if (res.status === 200) {Show more
```

```javascript
const fetchData = async () => {  const res = await octokitClient.request('GET /orgs/{org}/repos', {    org: 'carbon-design-system',    per_page: 75,    sort: 'updated',    direction: 'desc',  });
  if (res.status === 200) {
```

```
repositories.htmlCopy to clipboard<cds-table-skeleton></cds-table-skeleton>
```

```html
<cds-table-skeleton></cds-table-skeleton>
```

```
repositories.htmlCopy to clipboard<template id="template--table">  <cds-table expandable>    <cds-table-header-title slot="title"      >Carbon Repositories</cds-table-header-title    >    <cds-table-header-description slot="description"      >A collection of public Carbon repositories.</cds-table-header-description    >    <cds-table-head>Show more
```

```html
<template id="template--table">  <cds-table expandable>    <cds-table-header-title slot="title"      >Carbon Repositories</cds-table-header-title    >    <cds-table-header-description slot="description"      >A collection of public Carbon repositories.</cds-table-header-description    >    <cds-table-head>
```

```
repos.jsCopy to clipboardupdateTable();
```

```javascript
updateTable();
```

```
repos.jsCopy to clipboardconst replaceSkeleton = () => {  const tableSkeleton = document.querySelector('cds-table-skeleton');  const tableTemplate = document.querySelector('template#template--table');
  if (tableSkeleton && tableTemplate) {    tableSkeleton.replaceWith(tableTemplate.content.cloneNode(true));    // update table rows    updateTable();  }Show more
```

```javascript
const replaceSkeleton = () => {  const tableSkeleton = document.querySelector('cds-table-skeleton');  const tableTemplate = document.querySelector('template#template--table');
  if (tableSkeleton && tableTemplate) {    tableSkeleton.replaceWith(tableTemplate.content.cloneNode(true));    // update table rows    updateTable();  }
```

```
repos.jsCopy to clipboard// replace table here// replaceSkeleton();
```

```javascript
// replace table here// replaceSkeleton();
```

```
repos.jsCopy to clipboard// replace table herereplaceSkeleton();
```

```javascript
// replace table herereplaceSkeleton();
```

```
repos.jsCopy to clipboardimport '@carbon/web-components/es/components/link/index';
```

```javascript
import '@carbon/web-components/es/components/link/index';
```

```
repos.jsCopy to clipboardlinks: { url: row.html_url, homepage: row.homepage },
```

```javascript
links: { url: row.html_url, homepage: row.homepage },
```

```
repos.jsCopy to clipboardkeyEl.innerHTML = row[key];
```

```javascript
keyEl.innerHTML = row[key];
```

```
repos.jsCopy to clipboardif (key === 'links') {  keyEl.innerHTML = `<ul class="link-list">  <li>    <cds-link href="${row[key].url}">GitHub</cds-link>  </li>  <li>    <cds-link href="${row[key].homepage}">Homepage</cds-link>  </li></ul>`;Show more
```

```javascript
if (key === 'links') {  keyEl.innerHTML = `<ul class="link-list">  <li>    <cds-link href="${row[key].url}">GitHub</cds-link>  </li>  <li>    <cds-link href="${row[key].homepage}">Homepage</cds-link>  </li></ul>`;
```

```
style.scssCopy to clipboard.link-list {  display: flex;  list-style: none;  padding: 0;}
.link-list li:not(:last-child) {  padding-inline-end: $spacing-02;
Show more
```

```scss
.link-list {  display: flex;  list-style: none;  padding: 0;}
.link-list li:not(:last-child) {  padding-inline-end: $spacing-02;
```

```
repos.jsCopy to clipboardimport '@carbon/web-components/es/components/pagination/index';
```

```javascript
import '@carbon/web-components/es/components/pagination/index';
```

```
repositories.htmlCopy to clipboard<cds-pagination  backward-text="Previous page"  forward-text="Next page"  itemsPerPageText="Items per page">  <cds-select-item value="10">10</cds-select-item>  <cds-select-item value="20">20</cds-select-item>  <cds-select-item value="30">30</cds-select-item>  <cds-select-item value="40">40</cds-select-item>  <cds-select-item value="50">50</cds-select-item>Show more
```

```html
<cds-pagination  backward-text="Previous page"  forward-text="Next page"  itemsPerPageText="Items per page">  <cds-select-item value="10">10</cds-select-item>  <cds-select-item value="20">20</cds-select-item>  <cds-select-item value="30">30</cds-select-item>  <cds-select-item value="40">40</cds-select-item>  <cds-select-item value="50">50</cds-select-item>
```

```
repos.jsCopy to clipboardlet data = [];let pageSize = 10;let firstRowIndex = 0;
```

```javascript
let data = [];let pageSize = 10;let firstRowIndex = 0;
```

```
repos.jsCopy to clipboardconst handlePageChangeCurrent = ({ detail }) => {  firstRowIndex = (detail.page - 1) * detail.pageSize;  updateTable();};
const handlePageSizeChange = ({ detail }) => {  pageSize = detail.pageSize;  updateTable();};Show more
```

```javascript
const handlePageChangeCurrent = ({ detail }) => {  firstRowIndex = (detail.page - 1) * detail.pageSize;  updateTable();};
const handlePageSizeChange = ({ detail }) => {  pageSize = detail.pageSize;  updateTable();};
```

```
repos.jsCopy to clipboard// update table rowsupdateTable();
// update paginationupdatePagination();
```

```javascript
// update table rowsupdateTable();
// update paginationupdatePagination();
```

```
repos.jsCopy to clipboard// iterate over data and render rowsdata.forEach((row) => {  // rows update here});
```

```javascript
// iterate over data and render rowsdata.forEach((row) => {  // rows update here});
```

```
repos.jsCopy to clipboard// iterate over data and render rowsdata  .filter((v, i) => i >= firstRowIndex && i < firstRowIndex + pageSize)  .forEach((row) => {    // rows update here  });
```

```javascript
// iterate over data and render rowsdata  .filter((v, i) => i >= firstRowIndex && i < firstRowIndex + pageSize)  .forEach((row) => {    // rows update here  });
```

```
git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 3"
```

```
git push -u origin step-3Copy to clipboard
```

```bash
git push -u origin step-3
```
