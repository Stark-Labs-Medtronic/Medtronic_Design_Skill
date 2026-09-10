# 3. Using APIs – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/vue-tutorial/step-3/

# 3. Using APIs

This step takes our static components and populates them with data from the
GitHub GraphQL API – loading states and all. We’ll be displaying Carbon
repository information in a data table.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#fork-clone-and-branch)

- [Install dependencies](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#install-dependencies)

- [Create access token](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#create-access-token)

- [Connect to Apollo](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#connect-to-apollo)

- [Fetch data](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#fetch-data)

- [Populate data table](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#populate-data-table)

- [Add loading](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#add-loading)

- [Add pagination](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#add-pagination)

- [Submit pull request](https://carbondesignsystem.com/developing/vue-tutorial/step-3/#submit-pull-request)

### Preview

The [GitHub GraphQL API](https://developer.github.com/v4/) is very well
documented, and even though the focus of this tutorial isn’t learning and using
GraphQL, it’s a great opportunity to fetch Carbon-related data for this Carbon
tutorial.

To do so, we’ll be using Apollo Client, the front-end component of the
[Apollo Platform](https://www.apollographql.com/docs/intro/platform). Apollo
provides several open source tools for using GraphQL throughout your
application’s stack. Apollo Client is a sophisticated GraphQL client that
manages data and state in an application.

A [preview](https://vue-step-4--carbon-tutorial-vue.netlify.com/) of what you
will build (see repositories page):

## Fork, clone and branch

This tutorial has an accompanying GitHub repository called
[carbon-tutorial-vue](https://github.com/carbon-design-system/carbon-tutorial-vue)
that we’ll use as a starting point for each step. If you haven’t forked and
cloned that repository yet, and haven’t added the upstream remote, go ahead and
do so by following the
[step 2 instructions](https://carbondesignsystem.com/developing/vue-tutorial/step-1#fork-clone-and-branch).

### Branch

With your repository all set up, let’s check out the branch for this tutorial
step’s starting point.

```

git fetch upstreamgit checkout -b vue-step-3 upstream/vue-step-3Copy to clipboard

```

### Build and start app

Install the app’s dependencies:

```

yarnCopy to clipboard

```

Then, start the app:

```

yarn serveCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/vue-tutorial/step-2) left off. Stop your app with
`CTRL-C` and let’s get everything installed.

## Install dependencies

We’ll shortcut this using the Vue CLI, if you’d like more information head over
to
[Vue Apollo Installation](https://vue-apollo.netlify.com/guide/installation.html#vue-cli-plugin)
for details.

**Note:** If you have not yet installed the Vue CLI, you will need to
[install the Vue CLI](https://cli.vuejs.org/) before running the Vue Apollo
Installation.

Install the following

- `apollo-boost` - package containing everything you need to set up Apollo
Client

- `graphql` - parses your GraphQL queries

- `vue-apollo` - Apollo integration for Vue

Using the command:

```

vue add apolloCopy to clipboard

```

At the following prompts answer ‘No’ to each of the questions.

- Add example code? No

- Add a GraphQL API Server? No

- Configure Apollo Engine? No

## Create access token

You’ll need a personal access token from your GitHub account in order to make
requests to the GitHub API. Check out
[this guide](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
to see how to get one.

When you get to the scope/permissions step, you can leave them all unchecked. We
don’t need any special permissions, we just need access to the public API.

Once you have your token, we need to put it in a place where `create-vue-app`
can use it. When your application is being built and developed, create-vue-app
will parse environmental variables in any file that starts with `.env` and make
them available under `process.env.MY_VARIABLE`.

One caveat is that we need to start our variables with `VUE_APP_`. You can read
more about environmental variables in
[create-vue-app’s guide](https://cli.vuejs.org/guide/mode-and-env.html#environment-variables).

**Note:** If you already have a valid GitHub Personal Access Token, you can use
that token here.

Since we don’t want to commit this file to Git, we can put it in `.env.local`
which is in our `.gitignore` list. Your file should just have a single line like
this one, where the `x`s are replaced with your unique token.

```

.env.localCopy to clipboardVUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN=xxxxxx

```

Go ahead and start your app with `yarn serve`, or, if your app is running,
you’ll need to restart it to get access to this token.

## Connect to Apollo

The `vue-apollo` plugin has made a number of changes to our project.

If you open `src/main.js` you will see that the CLI has updated this file with
the following:.

```

src/main.jsCopy to clipboardimport { createProvider } from 'vue-apollo';
new Vue({  router,  apolloProvider: createProvider(),  render: (h) => h(App),}).$mount('#app');

```

This is loading from a file the CLI created for you `src/vue-apollo.js` which we
need to update to target the github api.

Update the following values:

```

src/vue-apollo.jsCopy to clipboard// Use our access tokenconst AUTH_TOKEN = process.env.VUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN;
// Target github apiconst httpEndpoint =  process.env.VUE_APP_GRAPHQL_HTTP || 'https://api.github.com/graphql';

```

Update only the `wsEndpoint` and `getAuth` properties of the `defaultOptions`
object:

```

const defaultOptions = {  // set wsEndpoint to null  wsEndpoint: process.env.VUE_APP_GRAPHQL_WS,
  // Use the form expected by github for authorization  getAuth: (tokenName) => `Bearer ${tokenName}`,};Copy to clipboard

```

## Fetch data

### Imports

Add the following imports to the top of the script section of `RepoPage.vue`:

```

src/views/RepoPage/RepoPage.vueCopy to clipboardimport gql from 'graphql-tag';

```

### Query

Next we’ll assemble our GraphQL query to fetch only the data we need from the
GraphQL API. We’ll do this using the `gql` helper we just imported. The `gql`
helper lets you write GraphQL queries using interpolated strings (backticks) in
JavaScript. In addition, we’ll be using the `Query` component from `vue-apollo`
which gives us some great information about our query’s loading state in
addition to the data.

You can use GitHub’s [explorer](https://developer.github.com/v4/explorer/) tool
to write and test your own queries. Try copying the query below and experiment
with changing the properties. You can also click the “Docs” button in the top
right of the explorer to view all of the available data and query parameters.

If you’d like some more information regarding writing queries and using the
Query component, we recommend
[Apollo’s documentation](https://www.apollographql.com/docs/tutorial/queries) on
this topic.

Add this after your imports:

```

src/views/RepoPage/RepoPage.vueCopy to clipboardconst REPO_QUERY = gql`  query REPO_QUERY {    # Let's use carbon as our organization    organization(login: "carbon-design-system") {      # We'll grab all the repositories in one go. To load more resources      # continuously, see the advanced topics.      repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {        totalCount        nodes {Show more

```

Next, we need to configure apollo in our component script, adding the following
after the data() declaration.

```

src/views/RepoPage/RepoPage.vueCopy to clipboardapollo: {  organization: REPO_QUERY},

```

At this point, we should run our query view the raw the results to verify that
the request is working.

In RepoPage.vue add the following before the `RepoTable` tag.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard{{ this.organization }}

```

When the data loads you should see the response rendered on your repository
page. If not, check the console to see if there are any errors and fix.

Revert this last change and continue.

This data is not quite in the format our `RepoTable` component is expecting so
we’ll use a computed property to transform it. Computed properties in Vue cache
and watch their reactive dependencies for us.

Remove the ‘rows’ constant and its use in the data declaration, and add this
computed property.

```

src/views/RepoPage/RepoPage.vueCopy to clipboardcomputed: {  rows() {      if (!this.organization) {      return [];    } else {      return this.organization.repositories.nodes.map(row => ({        ...row,        key: row.id,        stars: row.stargazers.totalCount,Show more

```

At this point you have a working table but the links column clearly isn’t what
we want.

### Helper component

This column in the data table will be a list of repository and home page links,
so let’s create a component called `LinkList`.

Add the following to create your component:

A template section:

```

src/views/RepoPage/LinkList.vueCopy to clipboard<ul class="link-list">  <li>    <cv-link :href="url">GitHub</cv-link>  </li>
  <li v-if="homepageUrl">    <span>&nbsp;|&nbsp;</span>    <cv-link :href="homepageUrl">Homepage</cv-link>  </li>Show more

```

A script section:

```

src/views/RepoPage/LinkList.vueCopy to clipboardexport default {  name: 'LinkList',  props: {    url: String,    homepageUrl: String,  },};

```

And a style section:

```

src/views/RepoPage/LinkList.vueCopy to clipboard.link-list {  display: flex;}

```

Now let’s make use of this component in our `RepoTable` component.

At the top of the script section import the link list component:

```

src/views/RepoPage/RepoTable.vueCopy to clipboardimport LinkList from './LinkList';

```

And below the name of the component add:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard  components: { LinkList },

```

Then make use of it in our template replacing:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>

```

with

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-cell v-for="(cell, cellIndex) in row.data" :key="`${cellIndex}`">  <template v-if="!cell.url">    {{cell}}  </template>  <link-list v-else :url="cell.url" :homepage-url="cell.homepageUrl" /></cv-data-table-cell>

```

Here in order to switch between the standard rendering of a data cell we’ve
wrapped our standard `{{cell}}` rendering in a template tag. The template tag is
non-rendering so it will disappear, leaving us with the same content as before.

Using the v-if and v-else directives we switch based on the contents of the cell
between the standard rendering and the LinkList component.

Checking our output again, you should now see the LinkList component rendering
the final column.

Next we’ll update our row description. Update the computed property data() in
`RepoTable.vue` to have the following description:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard  description: row.description

```

Check the output again and you should find the descriptions are updated.

After this many refreshes you may have noticed a slight delay in the data
loading. As outlined in the
[documentation](https://vue-apollo.netlify.com/guide/apollo/#apollo), all
components contained under one with an apolloProvider have a `$apollo`
attribute. As we added the `apolloProvider` to our app when creating the Vue
instance it is available to us everywhere.

We can use the property to react to
[loading state](https://vue-apollo.netlify.com/guide/apollo/queries.html#loading-state).

First let’s demonstrate that this works.

Pass the loading state into our `RepoTable` component by updating the template
with the following:

```

src/views/RepoPage/RepoPage.vueCopy to clipboard<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."  :loading="$apollo.loading" />

```

Next add this property to the `RepoTable` component:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard  props: {    headers: Array,    rows: Array,    title: String,    helperText: String,    loading: Boolean,  },

```

Making use of the property to display a loading message.

Replace:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>

```

with:

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<div v-if="loading">Loading...</div><cv-data-table  v-else  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>

```

Here we have made use of the v-if and v-else directives to switch content based
on the state of `$apollo.loading`. If you refresh your app you should see this
take effect.

Now that we know this is works let’s try something a bit more sophisticated and
replace the div containing our loading message with use of the
`CvDataTableSkeleton` component.

```

src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-skeleton  v-if="loading"  :columns="columns"  :title="title"  :helper-text="helperText"  :rows="10"/>

```

We need to tell the loading skeleton how many rows to render, so let’s use 10
skeleton rows to prepare for the next enhancement…

## Add pagination

Pagination! Instead of rendering every repository, let’s add pagination to the
data table to only render 10 at a time. Depending on your specific requirements,
you may need to fetch new data each time that you interact with the pagination
component, but for simplicity, we’re going to make one request to fetch all
data, and then paginate the in-memory row data.

Let’s start by adjusting our `PageTable` component template to add pagination.
If you review the
[storybook notes](http://vue.carbondesignsystem.com/?path=/info/components-cvdatatable--default)
you’ll see that pagination is added to the data table by supplying a pagination
object and listening for pagination events as follows.

```

src/views/RepoPage/RepoTable.vueCopy to clipboard  <cv-data-table    v-else    :columns="columns"    :title="title"    :helper-text="helperText"    :pagination="{ numberOfItems: this.totalRows }"    @pagination="$emit('pagination', $event)">

```

**Note:** `:prop` is an abbreviation of `v-bind:prop`. `@event` is an
abbreviation of `v-on:event`.

In the pagination event we’ve used $emit and $event to re-raise the pagination
event to our `RepoPage` component so that it can arrange to pass only the rows
we want to see to the `RepoTable` component.

We also need to add the `totalRows` property used in the data tables pagination
property.

```

src/views/RepoPage/RepoTable.vueCopy to clipboardtotalRows: Number,

```

Next to our `RepoPage` component, let’s first update our template by updating
our `RepoTable` use with the following attributes.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard:rows="pagedRows":totalRows="rows.length"@pagination="onPagination"

```

replacing

```

src/views/RepoPage/RepoPage.vueCopy to clipboard:rows="rows"

```

Next in the data property of our component add values for `pageSize`,
`pageStart` and `page` into the data method return to support our pagination.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard  data() {    return {      headers,      pageSize: 0,      pageStart: 0,      page: 0    };  },

```

**Note:** We could have passed values for `pageSize` and `page` into our
pagination component if we had a specific page or page size we wanted to start
with. Instead we are relying on the pagination component to set some sensible
defaults and provide us with the details through an event.

Then before we can see our paginated table we need to add: a `pagedRows`
computed property to select the slice of input rows we are interested in, and a
method to handle the pagination event.

```

src/views/RepoPage/RepoPage.vueCopy to clipboard  computed: {    // other computed properties    // ...    pagedRows() {      return this.rows.slice(this.pageStart, this.pageStart + this.pageSize);    }  },  methods: {    onPagination(val) {Show more

```

**Note:** Like the other Carbon Vue components, `Pagination` component examples
can be found in
[Storybook](http://vue.carbondesignsystem.com/?path=/story/components-cvpagination--default)
by browsing the story and knobs.

That does it! Your data table should fetch GitHub data on first render. You can
expand each row to see the repository’s description. You can modify the
pagination items per page and cycle through pages or jump to a specific page of
repositories.

## Mystery

Hmmm, there is at least one more issue to resolve. If you expand a row or two to
see the repository descriptions you will and then change page. What happens?

Assuming you didn’t catch this earlier you will find that the expanded rows,
stay expanded after paging. That is if row two was expanded before pagination it
is expanded after.

This is because we chose poor values to use as our row and cell keys as we
iterated over them. The result is that Vue sees these items as having the same
key and makes the assumption that content but not state has changed.

To fix this add the following to the RepoPage component you should be able to
find something better.

```

  watch: {    rows() {      if (this.organization) {        console.dir(this.organization.repositories.nodes);      }    }  },Copy to clipboard

```

_Hint: `id` and `url` are likely unique properties, you could use either of
these to update the prototype. In fact we already pass the id value to
RepoTable._

Can you fix it?

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

git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard

```

Then, push to your repository:

```

git push origin vue-step-3Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/vue-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-vue](https://github.com/carbon-design-system/carbon-tutorial-vue)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`vue-step-3` into `base: vue-step-3`.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

## Code samples

```
git fetch upstreamgit checkout -b vue-step-3 upstream/vue-step-3Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b vue-step-3 upstream/vue-step-3
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
vue add apolloCopy to clipboard
```

```bash
vue add apollo
```

```
.env.localCopy to clipboardVUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN=xxxxxx
```

```bash
VUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN=xxxxxx
```

```
src/main.jsCopy to clipboardimport { createProvider } from 'vue-apollo';
new Vue({  router,  apolloProvider: createProvider(),  render: (h) => h(App),}).$mount('#app');
```

```javascript
import { createProvider } from 'vue-apollo';
new Vue({  router,  apolloProvider: createProvider(),  render: (h) => h(App),}).$mount('#app');
```

```
src/vue-apollo.jsCopy to clipboard// Use our access tokenconst AUTH_TOKEN = process.env.VUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN;
// Target github apiconst httpEndpoint =  process.env.VUE_APP_GRAPHQL_HTTP || 'https://api.github.com/graphql';
```

```javascript
// Use our access tokenconst AUTH_TOKEN = process.env.VUE_APP_GITHUB_PERSONAL_ACCESS_TOKEN;
// Target github apiconst httpEndpoint =  process.env.VUE_APP_GRAPHQL_HTTP || 'https://api.github.com/graphql';
```

```
const defaultOptions = {  // set wsEndpoint to null  wsEndpoint: process.env.VUE_APP_GRAPHQL_WS,
  // Use the form expected by github for authorization  getAuth: (tokenName) => `Bearer ${tokenName}`,};Copy to clipboard
```

```javascript
const defaultOptions = {  // set wsEndpoint to null  wsEndpoint: process.env.VUE_APP_GRAPHQL_WS,
  // Use the form expected by github for authorization  getAuth: (tokenName) => `Bearer ${tokenName}`,};
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardimport gql from 'graphql-tag';
```

```javascript
import gql from 'graphql-tag';
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardconst REPO_QUERY = gql`  query REPO_QUERY {    # Let's use carbon as our organization    organization(login: "carbon-design-system") {      # We'll grab all the repositories in one go. To load more resources      # continuously, see the advanced topics.      repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {        totalCount        nodes {Show more
```

```graphql
const REPO_QUERY = gql`  query REPO_QUERY {    # Let's use carbon as our organization    organization(login: "carbon-design-system") {      # We'll grab all the repositories in one go. To load more resources      # continuously, see the advanced topics.      repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {        totalCount        nodes {
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardapollo: {  organization: REPO_QUERY},
```

```javascript
apollo: {  organization: REPO_QUERY},
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard{{ this.organization }}
```

```html
{{ this.organization }}
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboardcomputed: {  rows() {      if (!this.organization) {      return [];    } else {      return this.organization.repositories.nodes.map(row => ({        ...row,        key: row.id,        stars: row.stargazers.totalCount,Show more
```

```javascript
computed: {  rows() {      if (!this.organization) {      return [];    } else {      return this.organization.repositories.nodes.map(row => ({        ...row,        key: row.id,        stars: row.stargazers.totalCount,
```

```
src/views/RepoPage/LinkList.vueCopy to clipboard<ul class="link-list">  <li>    <cv-link :href="url">GitHub</cv-link>  </li>
  <li v-if="homepageUrl">    <span>&nbsp;|&nbsp;</span>    <cv-link :href="homepageUrl">Homepage</cv-link>  </li>Show more
```

```html
<ul class="link-list">  <li>    <cv-link :href="url">GitHub</cv-link>  </li>
  <li v-if="homepageUrl">    <span>&nbsp;|&nbsp;</span>    <cv-link :href="homepageUrl">Homepage</cv-link>  </li>
```

```
src/views/RepoPage/LinkList.vueCopy to clipboardexport default {  name: 'LinkList',  props: {    url: String,    homepageUrl: String,  },};
```

```javascript
export default {  name: 'LinkList',  props: {    url: String,    homepageUrl: String,  },};
```

```
src/views/RepoPage/LinkList.vueCopy to clipboard.link-list {  display: flex;}
```

```scss
.link-list {  display: flex;}
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboardimport LinkList from './LinkList';
```

```javascript
import LinkList from './LinkList';
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard  components: { LinkList },
```

```javascript
components: { LinkList },
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>
```

```html
<cv-data-table-cell  v-for="(cell, cellIndex) in row.data"  :key="`${cellIndex}`"  >{{cell}}</cv-data-table-cell>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-cell v-for="(cell, cellIndex) in row.data" :key="`${cellIndex}`">  <template v-if="!cell.url">    {{cell}}  </template>  <link-list v-else :url="cell.url" :homepage-url="cell.homepageUrl" /></cv-data-table-cell>
```

```html
<cv-data-table-cell v-for="(cell, cellIndex) in row.data" :key="`${cellIndex}`">  <template v-if="!cell.url">    {{cell}}  </template>  <link-list v-else :url="cell.url" :homepage-url="cell.homepageUrl" /></cv-data-table-cell>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard  description: row.description
```

```javascript
description: row.description
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."  :loading="$apollo.loading" />
```

```html
<repo-table  :headers="headers"  :rows="rows"  title="Carbon Repositories"  helperText="A collection of public Carbon repositories."  :loading="$apollo.loading" />
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard  props: {    headers: Array,    rows: Array,    title: String,    helperText: String,    loading: Boolean,  },
```

```javascript
props: {    headers: Array,    rows: Array,    title: String,    helperText: String,    loading: Boolean,  },
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>
```

```html
<cv-data-table  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<div v-if="loading">Loading...</div><cv-data-table  v-else  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>
```

```html
<div v-if="loading">Loading...</div><cv-data-table  v-else  :columns="columns"  :title="title"  :helper-text="helperText"></cv-data-table>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard<cv-data-table-skeleton  v-if="loading"  :columns="columns"  :title="title"  :helper-text="helperText"  :rows="10"/>
```

```html
<cv-data-table-skeleton  v-if="loading"  :columns="columns"  :title="title"  :helper-text="helperText"  :rows="10"/>
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboard  <cv-data-table    v-else    :columns="columns"    :title="title"    :helper-text="helperText"    :pagination="{ numberOfItems: this.totalRows }"    @pagination="$emit('pagination', $event)">
```

```html
<cv-data-table    v-else    :columns="columns"    :title="title"    :helper-text="helperText"    :pagination="{ numberOfItems: this.totalRows }"    @pagination="$emit('pagination', $event)">
```

```
src/views/RepoPage/RepoTable.vueCopy to clipboardtotalRows: Number,
```

```javascript
totalRows: Number,
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard:rows="pagedRows":totalRows="rows.length"@pagination="onPagination"
```

```html
:rows="pagedRows":totalRows="rows.length"@pagination="onPagination"
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard:rows="rows"
```

```html
:rows="rows"
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard  data() {    return {      headers,      pageSize: 0,      pageStart: 0,      page: 0    };  },
```

```javascript
data() {    return {      headers,      pageSize: 0,      pageStart: 0,      page: 0    };  },
```

```
src/views/RepoPage/RepoPage.vueCopy to clipboard  computed: {    // other computed properties    // ...    pagedRows() {      return this.rows.slice(this.pageStart, this.pageStart + this.pageSize);    }  },  methods: {    onPagination(val) {Show more
```

```javascript
computed: {    // other computed properties    // ...    pagedRows() {      return this.rows.slice(this.pageStart, this.pageStart + this.pageSize);    }  },  methods: {    onPagination(val) {
```

```
watch: {    rows() {      if (this.organization) {        console.dir(this.organization.repositories.nodes);      }    }  },Copy to clipboard
```

```javascript
watch: {    rows() {      if (this.organization) {        console.dir(this.organization.repositories.nodes);      }    }  },
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 3"
```

```
git push origin vue-step-3Copy to clipboard
```

```bash
git push origin vue-step-3
```
