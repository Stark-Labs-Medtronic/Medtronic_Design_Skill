# 3. Using APIs – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/react-tutorial/step-3/

# 3. Using APIs

This step takes our static components and populates them with data from the
GitHub GraphQL API – loading states and all. We’ll be displaying Carbon
repository information in a data table.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/react-tutorial/step-3/#fork-clone-and-branch)

- [Install dependencies](https://carbondesignsystem.com/developing/react-tutorial/step-3/#install-dependencies)

- [Fetch data](https://carbondesignsystem.com/developing/react-tutorial/step-3/#fetch-data)

- [Populate data table](https://carbondesignsystem.com/developing/react-tutorial/step-3/#populate-data-table)

- [Add loading](https://carbondesignsystem.com/developing/react-tutorial/step-3/#add-loading)

- [Add pagination](https://carbondesignsystem.com/developing/react-tutorial/step-3/#add-pagination)

- [Submit pull request](https://carbondesignsystem.com/developing/react-tutorial/step-3/#submit-pull-request)

### Preview

The [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) is
very well documented, we’ll use it to fetch Carbon-related data for this Carbon
tutorial.

To do so, we’ll be using
[Octokit Core](https://github.com/octokit/core.js/#readme), a client that makes
it easy to interact with GitHub’s APIs.

A
[preview](https://carbon-tutorial-nextjs-git-v11-next-step-4-carbon-design-system.vercel.app/)
of what you will build (see repositories page):

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

git fetch upstreamgit checkout -b v11-next-step-3 upstream/v11-next-step-3Copy to clipboard

```

### Build and start app

Install the app’s dependencies and build the app:

```

yarn && yarn buildCopy to clipboard

```

Then, start the app:

```

yarn startCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/react-tutorial/step-2) left off. Stop your app with
`CTRL-C` and let’s get everything installed.

## Install dependencies

We’ll need to install `@octokit/core`, a package that allows us to query GitHub
APIs easily. Stop your development server with `CTRL-C` and install the octokit
dependency with:

```

yarn add @octokit/core@4.2.0Copy to clipboard

```

Then, start the app again. If your app’s currently running, you’ll need to
restart it.

```

yarn devCopy to clipboard

```

## Fetch data

### Imports

We’ll be using [React Hooks](https://reactjs.org/docs/hooks-intro.html) to call
a function to fetch our data when the component renders.

Import React’s [useEffect](https://reactjs.org/docs/hooks-effect.html) by
modifying the `React` import in `src/app/repos/page.js`.

```

src/app/repos/page.jsCopy to clipboardimport React, { useEffect } from 'react';

```

Add the following import below the react import in `RepoPage`:

```

src/app/repos/page.jsCopy to clipboardimport { Octokit } from '@octokit/core';

```

### Initializing Octokit client

Directly below all your imports, initialize an octokit client which we’ll use to
query our `RepoTable` data:

```

src/app/repos/page.jsCopy to clipboardconst octokitClient = new Octokit({});

```

### API Request

Next, we’ll assemble our GitHub API request to fetch a list of repositories that
belong to the `carbon-design-system` GitHub organization. We’ll do this by using
a `useEffect` hook that will use octokit to query GitHub’s API
[repositories endpoint](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories).

Let’s declare a `useEffect` hook immediately below the component definition and
above the return. We’ll use this to query GitHub’s API when the component first
renders:

```

src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  useEffect(() => {    async function getCarbonRepos() {      const res = await octokitClient.request('GET /orgs/{org}/repos', {        org: 'carbon-design-system',        per_page: 75,        sort: 'updated',        direction: 'desc',      });Show more

```

At this point, if you navigate to the Repositories page `/repos` in your running
app and view your browser’s console (e.g.
[Chrome DevTools](https://developer.chrome.com/docs/devtools/)), you should see
the response from GitHub!

### Helpers

Our last column in the data table will be a comma-separated list of repository
and home page links, so let’s create a component called `LinkList`.

Import `Link` at the top of `/app/repos/page.js`. The imports should look like
this.

```

src/app/repos/page.jsCopy to clipboardimport { Link, Grid, Column } from '@carbon/react';

```

Then use `Link` in this component. It has two props (`url` and `homepageUrl`)
and returns an unordered list. If the repository does not have a home page URL,
only render the repository link.

```

src/app/repos/page.jsCopy to clipboardconst LinkList = ({ url, homepageUrl }) => (  <ul style={{ display: 'flex' }}>    <li>      <Link href={url}>GitHub</Link>    </li>    {homepageUrl && (      <li>        <span>&nbsp;|&nbsp;</span>        <Link href={homepageUrl}>Homepage</Link>Show more

```

As a final helper, let’s create a function that transforms row data to our
expected header keys. Notice how we’re using our new `LinkList` component to
generate the value of the `links` key in each row.

```

src/app/repos/page.jsCopy to clipboardconst getRowItems = (rows) =>  rows.map((row) => ({    ...row,    key: row.id,    stars: row.stargazers_count,    issueCount: row.open_issues_count,    createdAt: new Date(row.created_at).toLocaleDateString(),    updatedAt: new Date(row.updated_at).toLocaleDateString(),    links: <LinkList url={row.html_url} homepageUrl={row.homepage} />,Show more

```

### Populate data table

Now that we have our data, let’s dispose of our dummy `rows` and populate the
data table with real data.

First, towards the top of `RepoPage` delete the `rows` array because we no
longer need the example rows.

Next, let’s add a couple variables that will help us store useful information
when fetching the data and keep track of the loading state.

We’ll be using [React Hooks](https://reactjs.org/docs/hooks-intro.html) again to
manage our state.

Import React’s [useState](https://reactjs.org/docs/hooks-state.html) by
modifying the `React` import.

```

src/app/repos/page.jsCopy to clipboardimport React, { useEffect, useState } from 'react';

```

Then, inside the `RepoPage` component:

```

src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  const [loading, setLoading] = useState(true);  const [error, setError] = useState();  const [rows, setRows] = useState([]);

```

Now, instead of using `console.log` to log the github data response, let’s treat
the response data by passing it through our `getRowItems` helper and saving the
result in our new `rows` variable. Replace the `console.log(res.data);` line
inside `if (res.status === 200)` with:

```

src/app/repos/page.jsCopy to clipboardsetRows(getRowItems(res.data));

```

Let’s also replace our error log line inside the `else` statement with:

```

src/app/repos/page.jsCopy to clipboardsetError('Error obtaining repository data');

```

To complete our `getCarbonRepos` function, let’s set the loading state to false
right after the `else` statement:

```

src/app/repos/page.jsCopy to clipboardif (res.status === 200) {  setRows(getRowItems(res.data));} else {  setError('Error obtaining repository data');}setLoading(false);

```

Finally, let’s modify our component’s `return()` statement to display different
information depending on the states of our request: loading, error or complete.
Replace the current return statement with:

```

src/app/repos/page.jsCopy to clipboardif (loading) {  return 'Loading...';}
if (error) {  return `Error! ${error}`;}
// If we're here, we've got our data!Show more

```

### Render repository descriptions

The data table component and its pieces use a common React pattern called
[render props](https://reactjs.org/docs/render-props.html). This is a really
powerful way for libraries to give developers control of rendering and
manipulating their data.

Revisiting `RepoTable.js`, we are already passing in our row objects along with
headers for each column. The `render` prop is being used to tell the data table
how to render the headers and rows. That prop takes a function that receives the
processed headers and rows as arguments as well as some helper functions for
rendering the table.

One common hurdle with the data table is how to access data that might not
correspond with a table column but is needed to compute the value of a cell that
does. The data table component processes and controls only the row properties
which corresponds to headers (columns). Because of this, the `rows` object you
get access to in the render prop function is _different_ than the one you passed
in to the `rows` prop.

We need to modify one aspect of the data table because if you expand a row, it
says `Row description`. We want to update that with the repository description
coming from the GitHub API. This is an example of where we need a simple look-up
function to find the data we care about - data that does not directly correspond
to a column.

To do so, in `RepoTable.js`, add this look-up function as the first lines inside
the `RepoTable`. This should go immediately before the component’s `return()`.

```

src/app/repos/RepoTable.jsCopy to clipboardconst getRowDescription = (rowId) => {  const row = rows.find(({ id }) => id === rowId);  return row ? row.description : '';};

```

Finally, in `RepoTable.js`, replace `<p>Row description</p>` with:

```

src/app/repos/RepoTable.jsCopy to clipboard<p>{getRowDescription(row.id)}</p>

```

## Add loading

At this point, the first time that you visit the repositories page, we’re
querying the GitHub API and rendering the response through the `DataTable`
component. We could stop here, but there’s more to be done! Let’s replace the
`Loading...` string with the
[DataTableSkeleton component](https://react.carbondesignsystem.com/?path=/story/components-datatable--skeleton).

To do so, back to `RepoPage`, add the `DataTableSkeleton` import by modifying
the existing `@carbon/react` import.

```

src/app/repos/page.jsCopy to clipboardimport { Link, DataTableSkeleton, Grid, Column } from '@carbon/react';

```

Then replace the `if (loading) return 'Loading...';` with:

```

src/app/repos/page.jsCopy to clipboardif (loading) {  return (    <Grid className="repo-page">      <Column lg={16} md={8} sm={4} className="repo-page__r1">        <DataTableSkeleton          columnCount={headers.length + 1}          rowCount={10}          headers={headers}        />Show more

```

We need to tell the loading skeleton how many rows to render, so let’s use 10
skeleton rows to prepare for the next enhancement…

## Add pagination

Pagination! Instead of rendering every repository, let’s add pagination to the
data table to only render 10 at a time. Depending on your specific requirements,
you may need to fetch new data each time that you interact with the pagination
component, but for simplicity, we’re going to make one request to fetch all
data, and then paginate the in-memory row data.

Initialize the new state variables that we’ll use for pagination as the first
lines inside the `RepoPage`.

```

src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  const [firstRowIndex, setFirstRowIndex] = useState(0);  const [currentPageSize, setCurrentPageSize] = useState(10);...

```

This initializes the total number of rows and the index of the first row to `0`,
and the page size to `10` as we also specified in our loading skeleton.

Then we need to update our `RepoTable` `rows` prop to only render the subset of
rows for the current “page”. Update
`<RepoTable headers={headers} rows={rows} />` to:

```

src/app/repos/page.jsCopy to clipboard<RepoTable  headers={headers}  rows={rows.slice(firstRowIndex, firstRowIndex + currentPageSize)}/>

```

**Note:** We only pass the rows that we want our table to display. We can do
this by slicing the array of rows depending on the first item and the page size.

Finally, let’s add the `Pagination` to update our state variables and cause the
data table to render new rows.

Import `Pagination` by updating the `@carbon/react` import.

```

src/app/repos/page.jsCopy to clipboardimport {  Link,  DataTableSkeleton,  Pagination,  Grid,  Column,} from '@carbon/react';

```

Immediately after the `RepoTable` closing tag (`/>`), add the `Pagination`
component using the state variables that we previously initialized.

```

src/app/repos/page.jsCopy to clipboard<Pagination  totalItems={rows.length}  backwardText="Previous page"  forwardText="Next page"  pageSize={currentPageSize}  pageSizes={[5, 10, 15, 25]}  itemsPerPageText="Items per page"  onChange={({ page, pageSize }) => {    if (pageSize !== currentPageSize) {Show more

```

**Note:** The `Pagination` component isn’t inherently connected in any way to
the `DataTable` - we need to tell it what to do when a change occurs using the
`onChange` prop. This includes both page size changes and displaying different
rows.

**Note:** Like the other Carbon React components, `Pagination` component
examples can be found in
[Storybook](https://react.carbondesignsystem.com/?path=/story/components-pagination--pagination)
by browsing the story and knobs.

That does it! Your data table should fetch GitHub data on first render. You can
expand each row to see the repository’s description. You can modify the
pagination items per page and cycle through pages or jump to a specific page of
repositories.

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

yarn formatgit add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard

```

Then, push to your repository:

```

git push origin v11-next-step-3Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/react-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-nextjs](https://github.com/carbon-design-system/carbon-tutorial-nextjs)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`v11-next-step-3` into `base: v11-next-step-3`.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

**Note:** If your PR fails the CircleCI test with the error
`Can't make a request in offline mode`, try running the following command:
`rm -rf .yarn-offline-mirror node_modules && yarn cache clean && yarn install`.
Add and commit the changes once this completes, and try pushing again.

## Code samples

```
git fetch upstreamgit checkout -b v11-next-step-3 upstream/v11-next-step-3Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b v11-next-step-3 upstream/v11-next-step-3
```

```
yarn && yarn buildCopy to clipboard
```

```bash
yarn && yarn build
```

```
yarn startCopy to clipboard
```

```bash
yarn start
```

```
yarn add @octokit/core@4.2.0Copy to clipboard
```

```bash
yarn add @octokit/core@4.2.0
```

```
yarn devCopy to clipboard
```

```bash
yarn dev
```

```
src/app/repos/page.jsCopy to clipboardimport React, { useEffect } from 'react';
```

```javascript
import React, { useEffect } from 'react';
```

```
src/app/repos/page.jsCopy to clipboardimport { Octokit } from '@octokit/core';
```

```javascript
import { Octokit } from '@octokit/core';
```

```
src/app/repos/page.jsCopy to clipboardconst octokitClient = new Octokit({});
```

```javascript
const octokitClient = new Octokit({});
```

```
src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  useEffect(() => {    async function getCarbonRepos() {      const res = await octokitClient.request('GET /orgs/{org}/repos', {        org: 'carbon-design-system',        per_page: 75,        sort: 'updated',        direction: 'desc',      });Show more
```

```javascript
function RepoPage() {  useEffect(() => {    async function getCarbonRepos() {      const res = await octokitClient.request('GET /orgs/{org}/repos', {        org: 'carbon-design-system',        per_page: 75,        sort: 'updated',        direction: 'desc',      });
```

```
src/app/repos/page.jsCopy to clipboardimport { Link, Grid, Column } from '@carbon/react';
```

```javascript
import { Link, Grid, Column } from '@carbon/react';
```

```
src/app/repos/page.jsCopy to clipboardconst LinkList = ({ url, homepageUrl }) => (  <ul style={{ display: 'flex' }}>    <li>      <Link href={url}>GitHub</Link>    </li>    {homepageUrl && (      <li>        <span>&nbsp;|&nbsp;</span>        <Link href={homepageUrl}>Homepage</Link>Show more
```

```javascript
const LinkList = ({ url, homepageUrl }) => (  <ul style={{ display: 'flex' }}>    <li>      <Link href={url}>GitHub</Link>    </li>    {homepageUrl && (      <li>        <span>&nbsp;|&nbsp;</span>        <Link href={homepageUrl}>Homepage</Link>
```

```
src/app/repos/page.jsCopy to clipboardconst getRowItems = (rows) =>  rows.map((row) => ({    ...row,    key: row.id,    stars: row.stargazers_count,    issueCount: row.open_issues_count,    createdAt: new Date(row.created_at).toLocaleDateString(),    updatedAt: new Date(row.updated_at).toLocaleDateString(),    links: <LinkList url={row.html_url} homepageUrl={row.homepage} />,Show more
```

```javascript
const getRowItems = (rows) =>  rows.map((row) => ({    ...row,    key: row.id,    stars: row.stargazers_count,    issueCount: row.open_issues_count,    createdAt: new Date(row.created_at).toLocaleDateString(),    updatedAt: new Date(row.updated_at).toLocaleDateString(),    links: <LinkList url={row.html_url} homepageUrl={row.homepage} />,
```

```
src/app/repos/page.jsCopy to clipboardimport React, { useEffect, useState } from 'react';
```

```javascript
import React, { useEffect, useState } from 'react';
```

```
src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  const [loading, setLoading] = useState(true);  const [error, setError] = useState();  const [rows, setRows] = useState([]);
```

```javascript
function RepoPage() {  const [loading, setLoading] = useState(true);  const [error, setError] = useState();  const [rows, setRows] = useState([]);
```

```
src/app/repos/page.jsCopy to clipboardsetRows(getRowItems(res.data));
```

```javascript
setRows(getRowItems(res.data));
```

```
src/app/repos/page.jsCopy to clipboardsetError('Error obtaining repository data');
```

```javascript
setError('Error obtaining repository data');
```

```
src/app/repos/page.jsCopy to clipboardif (res.status === 200) {  setRows(getRowItems(res.data));} else {  setError('Error obtaining repository data');}setLoading(false);
```

```javascript
if (res.status === 200) {  setRows(getRowItems(res.data));} else {  setError('Error obtaining repository data');}setLoading(false);
```

```
src/app/repos/page.jsCopy to clipboardif (loading) {  return 'Loading...';}
if (error) {  return `Error! ${error}`;}
// If we're here, we've got our data!Show more
```

```javascript
if (loading) {  return 'Loading...';}
if (error) {  return `Error! ${error}`;}
// If we're here, we've got our data!
```

```
src/app/repos/RepoTable.jsCopy to clipboardconst getRowDescription = (rowId) => {  const row = rows.find(({ id }) => id === rowId);  return row ? row.description : '';};
```

```javascript
const getRowDescription = (rowId) => {  const row = rows.find(({ id }) => id === rowId);  return row ? row.description : '';};
```

```
src/app/repos/RepoTable.jsCopy to clipboard<p>{getRowDescription(row.id)}</p>
```

```html
<p>{getRowDescription(row.id)}</p>
```

```
src/app/repos/page.jsCopy to clipboardimport { Link, DataTableSkeleton, Grid, Column } from '@carbon/react';
```

```javascript
import { Link, DataTableSkeleton, Grid, Column } from '@carbon/react';
```

```
src/app/repos/page.jsCopy to clipboardif (loading) {  return (    <Grid className="repo-page">      <Column lg={16} md={8} sm={4} className="repo-page__r1">        <DataTableSkeleton          columnCount={headers.length + 1}          rowCount={10}          headers={headers}        />Show more
```

```javascript
if (loading) {  return (    <Grid className="repo-page">      <Column lg={16} md={8} sm={4} className="repo-page__r1">        <DataTableSkeleton          columnCount={headers.length + 1}          rowCount={10}          headers={headers}        />
```

```
src/app/repos/page.jsCopy to clipboardfunction RepoPage() {  const [firstRowIndex, setFirstRowIndex] = useState(0);  const [currentPageSize, setCurrentPageSize] = useState(10);...
```

```javascript
function RepoPage() {  const [firstRowIndex, setFirstRowIndex] = useState(0);  const [currentPageSize, setCurrentPageSize] = useState(10);...
```

```
src/app/repos/page.jsCopy to clipboard<RepoTable  headers={headers}  rows={rows.slice(firstRowIndex, firstRowIndex + currentPageSize)}/>
```

```javascript
<RepoTable  headers={headers}  rows={rows.slice(firstRowIndex, firstRowIndex + currentPageSize)}/>
```

```
src/app/repos/page.jsCopy to clipboardimport {  Link,  DataTableSkeleton,  Pagination,  Grid,  Column,} from '@carbon/react';
```

```javascript
import {  Link,  DataTableSkeleton,  Pagination,  Grid,  Column,} from '@carbon/react';
```

```
src/app/repos/page.jsCopy to clipboard<Pagination  totalItems={rows.length}  backwardText="Previous page"  forwardText="Next page"  pageSize={currentPageSize}  pageSizes={[5, 10, 15, 25]}  itemsPerPageText="Items per page"  onChange={({ page, pageSize }) => {    if (pageSize !== currentPageSize) {Show more
```

```javascript
<Pagination  totalItems={rows.length}  backwardText="Previous page"  forwardText="Next page"  pageSize={currentPageSize}  pageSizes={[5, 10, 15, 25]}  itemsPerPageText="Items per page"  onChange={({ page, pageSize }) => {    if (pageSize !== currentPageSize) {
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
yarn formatgit add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard
```

```bash
yarn formatgit add --all && git commit -m "feat(tutorial): complete step 3"
```

```
git push origin v11-next-step-3Copy to clipboard
```

```bash
git push origin v11-next-step-3
```
