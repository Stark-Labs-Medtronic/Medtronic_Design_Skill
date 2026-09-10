# 5. Deploying to IBM Cloud – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/vue-tutorial/step-5/

# 5. Deploying to IBM Cloud

This step takes what we’ve built so far and optimizes the app for a production
environment. We’ll be deploying the production build to IBM Cloud.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#fork-clone-and-branch)

- [Create IBM Cloud account](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#create-ibm-cloud-account)

- [Optimize Sass](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#optimize-sass)

- [Build for production](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#build-for-production)

- [Create manifest file](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#create-manifest-file)

- [Create static file](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#create-static-file)

- [Deploy app](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#deploy-app)

- [Submit pull request](https://carbondesignsystem.com/developing/vue-tutorial/step-5/#submit-pull-request)

## Preview

A [preview](https://vue-step-6--carbon-tutorial-vue.netlify.com/) of what you’ll
build (visually no different, but built for production):

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

git fetch upstreamgit checkout -b vue-step-5 upstream/vue-step-5Copy to clipboard

```

**Note:** This builds on top of step 4, but be sure to check out the upstream
step 5 branch because it includes the static assets required to get through this
step.

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
[previous step](https://carbondesignsystem.com/developing/vue-tutorial/step-4) left off.

## Create IBM Cloud account

Before we get started,
[create an IBM Cloud account](https://cloud.ibm.com/registration) if you don’t
already have one, as we’ll be deploying there in a bit.

## Optimize Sass

So far we’ve been developing in a, well, development environment where static
asset optimization hasn’t been a priority. If you reference
`/src/styles/_carbon.scss`, you’ll see one `@import` that is pulling in Carbon’s
full Sass build.

```

src/styles/_carbon.scssCopy to clipboard$feature-flags: (  grid-columns-16: true,);
@import 'carbon-components/scss/globals/scss/styles.scss';

```

To give you an idea of what’s all included, open up
`node_modules/carbon-components/scss/globals/scss/styles.scss`. You’ll see
imports for components like accordion, slider, tooltip, etc. Since we aren’t
using those components, let’s exclude them from our built stylesheets. Keeping
the `$feature-flags` Sass map, replace the `styles.scss` import only with:

```

src/styles/_carbon.scssCopy to clipboard// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import 'carbon-components/scss/globals/scss/css--font-face';@import 'carbon-components/scss/globals/grid/grid';
// Carbon componentsShow more

```

In comparing to the included `styles.scss`, you may be asking what happened to
importing `_vars.scss`, `_colors.scss`, `_theme.scss`, etc.? Many of those
global Sass partials get imported through the components. For example, open
`node_modules/carbon-components/scss/components/button/_button.scss` to see its
dependencies. No harm in importing them as `styles.scss` does, but for
simplicity here, we’ll let the components pull them in.

You can read more about optimizing Carbon’s Sass in the
[Carbon Design System publication](https://medium.com/carbondesign/minimal-css-with-carbon-b0c089ccfa71)
on Medium.

## Build for production

Before we deploy our app, we need to create an optimized production build with
this command. You may need to `CTRL-C` to stop the development environment
first.

```

yarn buildCopy to clipboard

```

Looking at `package.json`, you’ll find `yarn build` to run
`vue-cli-service build`. This builds the app for production to the `dist`
folder. It bundles Vue in production mode and optimizes the build for the best
performance. It even goes so far to minify files and include hashes in filenames
for caching.

As a lot of this may seem like magic since the build configuration came from the
Vue CLI, go ahead and check out their
[production build guidelines](https://cli.vuejs.org/guide/build-targets.html#app)
for a full description of what’s happening.

## Create manifest file

Now that we have a production build, let’s get it on the cloud. We’re going to
use
[staticfile-buildpack](https://github.com/cloudfoundry/staticfile-buildpack.git)
to deploy our webapp. We’ll be using the `cf` command line interface (CLI). If
running `cf --help` doesn’t work for you, chances are you need to
[install the CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html).

**Note:** If unfamiliar with buildpacks, the
[staticfile buildpack docs](https://docs.cloudfoundry.org/buildpacks/staticfile/index.html)
has good definitions and configuration documentation.

With the IBM Cloud CLI installed, next, we need to create a `manifest.yml` file
in the root of the project. To prevent multiple apps trying to use the
`carbon-tutorial-vue` name, replace `USERNAME` with your GitHub username below
to make sure our apps are uniquely named.

```

manifest.ymlCopy to clipboard---applications:  - name: carbon-tutorial-vue-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git

```

**Note:** With this set-up we’re still using a GitHub personal access token
saved in `.env.local`. If you haven’t created a GitHub access token yet, see
[step 3](https://carbondesignsystem.com/developing/vue-tutorial/step-3#create-access-token). You can put the
environment variable in the manifest file, or manually add it in the IBM Cloud
dashboard, but since we’re building off previous tutorial steps nothing more is
needed.

## Create static file

Create a new static file in the root of the project named `Staticfile`. This
tells the app to deploy from the `dist` folder and not the root of the project.

```

StaticfileCopy to clipboardroot: dist

```

### Cloud Foundry ignore

After telling Cloud Foundry what to include, we can also specify what to ignore.
Create a top-level `.cfignore` file. Cloud Foundry doesn’t let you push
read-only files (specifically, files with permissions <`400`), so to prevent
issues with the deploy, add:

```

.cfignoreCopy to clipboardnode_modules/.cache

```

You can speed up deploys by decreasing the files uploaded through IBM Cloud. To
accomplish this, ignore any folder not required by the production application on
IBM Cloud. For example, in the case of serving static files, you can ignore
`node_modules/` and `src/` because the only folder being served is `dist/`.

## Deploy app

Login to IBM Cloud with:

```

cf login -a https://api.us-south.cf.cloud.ibm.com --ssoCopy to clipboard

```

Deploy app using the `cf push` command. Since `manifest.yml` is in our root
directory, we don’t need to specify it in the push command. But, if you have
multiple manifest files that target different environments, it’s good practice
to specify the file.

**Note:** This step assumes your spaces are in the US South region. To
successfully deploy, you might need to update the region code (for example,
`api.[REGION].cf.cloud.ibm.com`) to the region where your spaces were created,
or create a space in the US South region.
[Learn more](https://cloud.ibm.com/docs/overview?topic=overview-whatsnew&origin_team=T02M79KSB#new-cloud-foundry-api-endpoints)

```

cf push -f manifest.ymlCopy to clipboard

```

To make it easy on ourselves by not needing to remember that command, let’s add
a script in `package.json`. We can combine the build and deploy steps to make
sure we only deploy immediately after running the build. In the `"scripts"`
object in `package.json`, add:

##### package.json

```

"deploy": "rm -rf ./dist && yarn build && cf push -f manifest.yml"Copy to clipboard

```

Next time you want to deploy, you can simply run `yarn deploy`.

## Submit pull request

That does it! We’re going to submit a pull request to verify completion of this
tutorial step. In doing so, **please include the mybluemix.net URL for your
deployed app in your pull request description**.

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

git add --all && git commit -m "feat(tutorial): complete step 5"Copy to clipboard

```

Then, push to your repository:

```

git push origin vue-step-5Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/vue-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-vue](https://github.com/carbon-design-system/carbon-tutorial-vue)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`vue-step-5` into `base: vue-step-5`.

**Note:** Expect your tutorial step PRs to be reviewed by the Carbon team but
not merged. We’ll close your PR so we can keep the repository’s remote branches
pristine and ready for the next person!

## Code samples

```
git fetch upstreamgit checkout -b vue-step-5 upstream/vue-step-5Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b vue-step-5 upstream/vue-step-5
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
src/styles/_carbon.scssCopy to clipboard$feature-flags: (  grid-columns-16: true,);
@import 'carbon-components/scss/globals/scss/styles.scss';
```

```scss
$feature-flags: (  grid-columns-16: true,);
@import 'carbon-components/scss/globals/scss/styles.scss';
```

```
src/styles/_carbon.scssCopy to clipboard// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import 'carbon-components/scss/globals/scss/css--font-face';@import 'carbon-components/scss/globals/grid/grid';
// Carbon componentsShow more
```

```scss
// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import 'carbon-components/scss/globals/scss/css--font-face';@import 'carbon-components/scss/globals/grid/grid';
// Carbon components
```

```
yarn buildCopy to clipboard
```

```bash
yarn build
```

```
manifest.ymlCopy to clipboard---applications:  - name: carbon-tutorial-vue-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git
```

```bash
---applications:  - name: carbon-tutorial-vue-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git
```

```
StaticfileCopy to clipboardroot: dist
```

```bash
root: dist
```

```
.cfignoreCopy to clipboardnode_modules/.cache
```

```bash
node_modules/.cache
```

```
cf login -a https://api.us-south.cf.cloud.ibm.com --ssoCopy to clipboard
```

```bash
cf login -a https://api.us-south.cf.cloud.ibm.com --sso
```

```
cf push -f manifest.ymlCopy to clipboard
```

```bash
cf push -f manifest.yml
```

```
"deploy": "rm -rf ./dist && yarn build && cf push -f manifest.yml"Copy to clipboard
```

```bash
"deploy": "rm -rf ./dist && yarn build && cf push -f manifest.yml"
```

```
yarn ci-checkCopy to clipboard
```

```bash
yarn ci-check
```

```
git add --all && git commit -m "feat(tutorial): complete step 5"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 5"
```

```
git push origin vue-step-5Copy to clipboard
```

```bash
git push origin vue-step-5
```
