# 3. Using APIs – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/angular-tutorial/step-3/

# 3. Using APIs

This step takes our static components and populates them with data from the
GitHub GraphQL API – loading states and all. We’ll be displaying Carbon
repository information in a data table.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#fork-clone-and-branch)

- [Install dependencies](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#install-dependencies)

- [Create access token](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#create-access-token)

- [Connect to Apollo](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#connect-to-apollo)

- [Fetch data](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#fetch-data)

- [Populate data table](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#populate-data-table)

- [Add loading](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#add-loading)

- [Add pagination](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#add-pagination)

- [Submit pull request](https://carbondesignsystem.com/developing/angular-tutorial/step-3/#submit-pull-request)

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

A [preview](https://angular-step-4-carbon-tutorial.netlify.com/) of what you will
build (see repositories page):

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

git fetch upstreamgit checkout -b angular-step-3 upstream/angular-step-3Copy to clipboard

```

### Build and start app

Install the app’s dependencies:

```

npm installCopy to clipboard

```

Then, start the app:

```

npm startCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/angular-tutorial/step-2) left off. Stop your app
with `CTRL-C` and let’s get everything installed.

## Install dependencies

We’ll shortcut this using the Angular CLI, if you’d like more information head
over to
[Angular Apollo Installation](https://www.apollographql.com/docs/angular/recipes/angular-cli/)
for details.

**Note:** If you have not yet installed the Angular CLI, you will need to
[install the Angular CLI](https://cli.angular.io/) before running the Angular
Apollo Installation.

Install the following

- `apollo-client` - package containing everything you need to set up Apollo
Client

- `graphql` - parses your GraphQL queries

- `apollo-angular` - Apollo integration for Angular

Using the command:

```

ng add apollo-angular@v1ng lint --fixCopy to clipboard

```

​**Note:** In case you receive
`ERROR in ../node_modules/graphql/subscription/subscribe.d.ts:44:3 - error TS2304: Cannot find name 'AsyncIterableIterator'.`,
you’ll have to add the code below in `tsconfig.app.json` `lib`: ​

```

src/tsconfig.app.jsonCopy to clipboard"lib": [  "es2016",  "dom",  "esnext.asynciterable"],

```

**Note:** In case you receive
`typings.d.ts:2:13 - error TS2403: Subsequent variable declarations must have the same type. Variable 'module' must be of type 'NodeModule', but here has type '{ id: string; }'.`,
you’ll have to comment out or remove the code below in `typings.d.ts`:

```

src/typings.d.tsCopy to clipboarddeclare var module: {  id: string,};

```

## Create access token

You’ll need a personal access token from your GitHub account in order to make
requests to the GitHub API. Check out
[this guide](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
to see how to get one.

When you get to the scope/permissions step, you can leave them all unchecked. We
don’t need any special permissions, we just need access to the public API.

Once you have your token, we need to put it in a place where we can use it in
our app. When your application is being built and developed, our app will parse
environmental variables in any `environment` file and make them available.

​

```

src/environment/environment.tsCopy to clipboardexport const environment = {  production: false,  githubPersonalAccessToken: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',};

```

Go ahead and start your app with `npm start`, or, if your app is running, you’ll
need to restart it to get access to this token.

## Connect to Apollo

We need to import the environment at the top of every file that we decide to use
it in:

```

import { environment } from '../environments/environment';Copy to clipboard

```

Next, make your client by providing a URI for the GitHub GraphQL API as well as
an authorization header using the environmental variable you just added to
`environment.ts`.

```

src/app/graphql.module.tsCopy to clipboardimport { HttpHeaders } from '@angular/common/http';
const uri = 'https://api.github.com/graphql'; // <-- add the URL of the GraphQL server hereexport function createApollo(httpLink: HttpLink) {  return {    link: httpLink.create({      uri,      headers: new HttpHeaders({        Authorization: `Bearer ${environment.githubPersonalAccessToken}`,Show more

```

## Fetch data

### Imports

Add the following import at the top of `repo-table.component.ts`:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardimport { Apollo } from 'apollo-angular';import gql from 'graphql-tag';

```

### Query

Next we’ll assemble our GraphQL query to fetch only the data we need from the
GraphQL API. We’ll do this using the `gql` helper we just imported. The `gql`
helper lets you write GraphQL queries using interpolated strings (backticks) in
JavaScript.

You can use GitHub’s [explorer](https://developer.github.com/v4/explorer/) tool
to write and test your own queries. Try copying the query below and experiment
with changing the properties. You can also click the “Docs” button in the top
right of the explorer to view all of the available data and query parameters.

If you’d like some more information regarding writing queries, we recommend
[Apollo’s documentation](https://www.apollographql.com/docs/tutorial/queries) on
this topic.

First, we will add a private apollo parameter of type Apollo to the constructor
to get access to the Apollo service.

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardconstructor(private apollo: Apollo) { }

```

Next, we will fetch the data in `ngOnInit()`. Add the following code right below
the `model.header` declaration:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.apollo.watchQuery({  query: gql`    query REPO_QUERY {      # Let's use carbon as our organization      organization(login: "carbon-design-system") {        # We'll grab all the repositories in one go. To load more resources        # continuously, see the advanced topics.        repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {          totalCountShow more

```

### Custom data

Our last column in the data table will be a comma-separated list of repository
and home page links, so let’s create a custom cell template.

The column will have two values (`url` and `homepageUrl`) and will have the
structure of an unordered list. If the repository does not have a home page URL,
only render the repository link.

```

src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ng-template #linkTemplate let-data="data">  <ul style="display: flex">    <li>      <a ibmLink [href]="data.github">GitHub</a>    </li>    <li *ngIf="data.homepage">      <span>&nbsp;|&nbsp;</span>      <a ibmLink [href]="data.homepage">HomePage</a>    </li>Show more

```

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard@ViewChild('linkTemplate', null)protected linkTemplate: TemplateRef<any>;

```

**Note:** Don’t forget to import `ViewChild` and `TemplateRef`.

Now let’s create a function that transforms row data to our expected header
keys. Notice how we’re using our new `linkTemplate` to generate the value of the
`links` key in each row.

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardprepareData(data) {  const newData = [];
  for (const datum of data) {    newData.push([      new TableItem({ data: datum.name, expandedData: datum.description }),      new TableItem({ data: new Date(datum.createdAt).toLocaleDateString() }),      new TableItem({ data: new Date(datum.updatedAt).toLocaleDateString() }),      new TableItem({ data: datum.issues.totalCount }),Show more

```

### Query component

At this point, we should run our query and `console.log()` the results to verify
that the request is working.

If there’s an issue, we’ll render the corresponding error message. We will also
check when loading is true, but add the implementation in the following steps.

Finally, if neither of those are true, it means we have our data! One nice
advantage of GraphQL is that as long as there are no errors, we can be certain
the properties on the data we requested aren’t `undefined`.

At the end of the `watchQuery` in `ngOnInit()`:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard.valueChanges.subscribe((response: any) => {  if (response.error) {    const errorData = [];    errorData.push([      new TableItem({data: 'error!' })    ]);    this.model.data = errorData;  } else if (response.loading) {    // Add loading stateShow more

```

The page will look the same as we’re still rendering our static example rows,
but if you view your browser’s console (e.g.
[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)),
you should see the response from GitHub!

## Populate data table

Now that we have that data, let’s populate the data table. Replace
`console.log(response);` with the following that destructures the `organization`
object. Once we have the repositories, we can call our `prepareData()` to build
the data table rows.

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard// If we're here, we've got our data!this.model.data = this.prepareData(  response.data.organization.repositories.nodes);

```

Then, in `ngOnInit()` delete the static rows since we no longer need them.

## Add loading

At this point, the first time that you visit the repositories page, we’re
querying the GitHub API and rendering the response through the `DataTable`
component. We could stop here, but there’s more to be done! Let’s add the
[Table Skeleton](https://angular.carbondesignsystem.com/?path=/story/table--skeleton).

To do so, we will need to modify `repo-table.component.html` and
`repo-table.component.ts`:

```

src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-table  [skeleton]="skeleton"  [model]="skeleton ? skeletonModel : model"  [showSelectionColumn]="false"  [striped]="false"></ibm-table>

```

We need to tell the loading skeleton how many rows to render, so let’s use 10
skeleton rows to prepare for the next enhancement…

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardskeletonModel = Table.skeletonModel(10, 6);skeleton = true;

```

**Note:** Don’t forget to import `Table`.

Then replace the comment with:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardelse if (response.loading) {  this.skeleton = true;}

```

and at the top of the `prepareData()` function add:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.skeleton = false;

```

## Add pagination

Pagination! Instead of rendering every repository, let’s add pagination to the
data table to only render 10 at a time. Depending on your specific requirements,
you may need to fetch new data each time that you interact with the pagination
component, but for simplicity, we’re going to make one request to fetch all
data, and then paginate the in-memory row data.

First we will create an array and populate it with 10 rows at a time.

```

data = [];Copy to clipboard

```

Next, replace the code where we call `prepareData()` with:

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.data = response.data.organization.repositories.nodes;this.model.pageLength = 10;this.model.totalDataLength = response.data.organization.repositories.totalCount;this.selectPage(1);

```

This initializes the page size to `10` as we also specified in our loading
skeleton.

Next we will call `selectPage()`. This will initialize the offset and use
`prepareData()` to only render the subset of rows for the current “page”.

```

src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardselectPage(page) {  const offset = this.model.pageLength * (page - 1);  const pageRawData = this.data.slice(offset, offset + this.model.pageLength);  this.model.data = this.prepareData(pageRawData);  this.model.currentPage = page;}

```

**Note:** We only pass the rows that we want our table to display. We can do
this by slicing our array of rows depending on the first item and the page size.

Finally, let’s import the `LinkModule` and `PaginationModule` to
`repositories.module.ts` and `repo-table.component.spec` and add the template
for pagination.

```

src/app/repositories/repositories.module.ts,src/app/repositories/repo-table/repo-table.component.spec.tsCopy to clipboardimport { LinkModule, PaginationModule } from 'carbon-components-angular';

```

```

src/app/repositories/repositories.module.ts,src/app/repositories/repo-table/repo-table.component.spec.tsCopy to clipboardimports: [LinkModule, PaginationModule];

```

Immediately after the `ibm-table` closing tag (`/>`), add the `ibm-pagination`
component.

```

src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-pagination  [model]="model"  (selectPage)="selectPage($event)"></ibm-pagination>

```

**Note:** Like the other Carbon Angular component, `pagination` component
examples can be found in
[Storybook](https://angular.carbondesignsystem.com/?path=/story/table--with-pagination)
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

ng lint --fixnpm run lint && npm testCopy to clipboard

```

**Note:** Having issues running the CI check?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#continuous-integration-(ci)-check)
has troubleshooting notes that may help.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard

```

Then, push to your repository:

```

git push origin angular-step-3Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`angular-step-3` into `base: angular-step-3`.

**Note:** Your tutorial step will be automatically reviewed based on the status
of your tests. Ensure that your tests pass when you submit your PR. Expect your
tutorial step PRs to be reviewed by the Carbon team but not merged. We’ll close
your PR so we can keep the repository’s remote branches pristine and ready for
the next person!

## Code samples

```
git fetch upstreamgit checkout -b angular-step-3 upstream/angular-step-3Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b angular-step-3 upstream/angular-step-3
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
ng add apollo-angular@v1ng lint --fixCopy to clipboard
```

```bash
ng add apollo-angular@v1ng lint --fix
```

```
src/tsconfig.app.jsonCopy to clipboard"lib": [  "es2016",  "dom",  "esnext.asynciterable"],
```

```javascript
"lib": [  "es2016",  "dom",  "esnext.asynciterable"],
```

```
src/typings.d.tsCopy to clipboarddeclare var module: {  id: string,};
```

```javascript
declare var module: {  id: string,};
```

```
src/environment/environment.tsCopy to clipboardexport const environment = {  production: false,  githubPersonalAccessToken: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',};
```

```javascript
export const environment = {  production: false,  githubPersonalAccessToken: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',};
```

```
import { environment } from '../environments/environment';Copy to clipboard
```

```javascript
import { environment } from '../environments/environment';
```

```
src/app/graphql.module.tsCopy to clipboardimport { HttpHeaders } from '@angular/common/http';
const uri = 'https://api.github.com/graphql'; // <-- add the URL of the GraphQL server hereexport function createApollo(httpLink: HttpLink) {  return {    link: httpLink.create({      uri,      headers: new HttpHeaders({        Authorization: `Bearer ${environment.githubPersonalAccessToken}`,Show more
```

```javascript
import { HttpHeaders } from '@angular/common/http';
const uri = 'https://api.github.com/graphql'; // <-- add the URL of the GraphQL server hereexport function createApollo(httpLink: HttpLink) {  return {    link: httpLink.create({      uri,      headers: new HttpHeaders({        Authorization: `Bearer ${environment.githubPersonalAccessToken}`,
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardimport { Apollo } from 'apollo-angular';import gql from 'graphql-tag';
```

```javascript
import { Apollo } from 'apollo-angular';import gql from 'graphql-tag';
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardconstructor(private apollo: Apollo) { }
```

```javascript
constructor(private apollo: Apollo) { }
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.apollo.watchQuery({  query: gql`    query REPO_QUERY {      # Let's use carbon as our organization      organization(login: "carbon-design-system") {        # We'll grab all the repositories in one go. To load more resources        # continuously, see the advanced topics.        repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {          totalCountShow more
```

```graphql
this.apollo.watchQuery({  query: gql`    query REPO_QUERY {      # Let's use carbon as our organization      organization(login: "carbon-design-system") {        # We'll grab all the repositories in one go. To load more resources        # continuously, see the advanced topics.        repositories(first: 75, orderBy: { field: UPDATED_AT, direction: DESC }) {          totalCount
```

```
src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ng-template #linkTemplate let-data="data">  <ul style="display: flex">    <li>      <a ibmLink [href]="data.github">GitHub</a>    </li>    <li *ngIf="data.homepage">      <span>&nbsp;|&nbsp;</span>      <a ibmLink [href]="data.homepage">HomePage</a>    </li>Show more
```

```html
<ng-template #linkTemplate let-data="data">  <ul style="display: flex">    <li>      <a ibmLink [href]="data.github">GitHub</a>    </li>    <li *ngIf="data.homepage">      <span>&nbsp;|&nbsp;</span>      <a ibmLink [href]="data.homepage">HomePage</a>    </li>
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard@ViewChild('linkTemplate', null)protected linkTemplate: TemplateRef<any>;
```

```javascript
@ViewChild('linkTemplate', null)protected linkTemplate: TemplateRef<any>;
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardprepareData(data) {  const newData = [];
  for (const datum of data) {    newData.push([      new TableItem({ data: datum.name, expandedData: datum.description }),      new TableItem({ data: new Date(datum.createdAt).toLocaleDateString() }),      new TableItem({ data: new Date(datum.updatedAt).toLocaleDateString() }),      new TableItem({ data: datum.issues.totalCount }),Show more
```

```javascript
prepareData(data) {  const newData = [];
  for (const datum of data) {    newData.push([      new TableItem({ data: datum.name, expandedData: datum.description }),      new TableItem({ data: new Date(datum.createdAt).toLocaleDateString() }),      new TableItem({ data: new Date(datum.updatedAt).toLocaleDateString() }),      new TableItem({ data: datum.issues.totalCount }),
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard.valueChanges.subscribe((response: any) => {  if (response.error) {    const errorData = [];    errorData.push([      new TableItem({data: 'error!' })    ]);    this.model.data = errorData;  } else if (response.loading) {    // Add loading stateShow more
```

```javascript
.valueChanges.subscribe((response: any) => {  if (response.error) {    const errorData = [];    errorData.push([      new TableItem({data: 'error!' })    ]);    this.model.data = errorData;  } else if (response.loading) {    // Add loading state
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboard// If we're here, we've got our data!this.model.data = this.prepareData(  response.data.organization.repositories.nodes);
```

```javascript
// If we're here, we've got our data!this.model.data = this.prepareData(  response.data.organization.repositories.nodes);
```

```
src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-table  [skeleton]="skeleton"  [model]="skeleton ? skeletonModel : model"  [showSelectionColumn]="false"  [striped]="false"></ibm-table>
```

```html
<ibm-table  [skeleton]="skeleton"  [model]="skeleton ? skeletonModel : model"  [showSelectionColumn]="false"  [striped]="false"></ibm-table>
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardskeletonModel = Table.skeletonModel(10, 6);skeleton = true;
```

```javascript
skeletonModel = Table.skeletonModel(10, 6);skeleton = true;
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardelse if (response.loading) {  this.skeleton = true;}
```

```javascript
else if (response.loading) {  this.skeleton = true;}
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.skeleton = false;
```

```javascript
this.skeleton = false;
```

```
data = [];Copy to clipboard
```

```javascript
data = [];
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardthis.data = response.data.organization.repositories.nodes;this.model.pageLength = 10;this.model.totalDataLength = response.data.organization.repositories.totalCount;this.selectPage(1);
```

```javascript
this.data = response.data.organization.repositories.nodes;this.model.pageLength = 10;this.model.totalDataLength = response.data.organization.repositories.totalCount;this.selectPage(1);
```

```
src/app/repositories/repo-table/repo-table.component.tsCopy to clipboardselectPage(page) {  const offset = this.model.pageLength * (page - 1);  const pageRawData = this.data.slice(offset, offset + this.model.pageLength);  this.model.data = this.prepareData(pageRawData);  this.model.currentPage = page;}
```

```javascript
selectPage(page) {  const offset = this.model.pageLength * (page - 1);  const pageRawData = this.data.slice(offset, offset + this.model.pageLength);  this.model.data = this.prepareData(pageRawData);  this.model.currentPage = page;}
```

```
src/app/repositories/repositories.module.ts,src/app/repositories/repo-table/repo-table.component.spec.tsCopy to clipboardimport { LinkModule, PaginationModule } from 'carbon-components-angular';
```

```javascript
import { LinkModule, PaginationModule } from 'carbon-components-angular';
```

```
src/app/repositories/repositories.module.ts,src/app/repositories/repo-table/repo-table.component.spec.tsCopy to clipboardimports: [LinkModule, PaginationModule];
```

```javascript
imports: [LinkModule, PaginationModule];
```

```
src/app/repositories/repo-table/repo-table.component.htmlCopy to clipboard<ibm-pagination  [model]="model"  (selectPage)="selectPage($event)"></ibm-pagination>
```

```html
<ibm-pagination  [model]="model"  (selectPage)="selectPage($event)"></ibm-pagination>
```

```
ng lint --fixnpm run lint && npm testCopy to clipboard
```

```bash
ng lint --fixnpm run lint && npm test
```

```
git add --all && git commit -m "feat(tutorial): complete step 3"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 3"
```

```
git push origin angular-step-3Copy to clipboard
```

```bash
git push origin angular-step-3
```
