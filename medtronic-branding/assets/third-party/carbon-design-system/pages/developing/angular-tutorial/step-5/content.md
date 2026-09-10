# 5. Deploying to IBM Cloud – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/angular-tutorial/step-5/

# 5. Deploying to IBM Cloud

This step takes what we’ve built so far and optimizes the app for a production
environment. We’ll be deploying the production build to IBM Cloud.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#fork-clone-and-branch)

- [Create IBM Cloud account](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#create-ibm-cloud-account)

- [Optimize Sass](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#optimize-sass)

- [Build for production](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#build-for-production)

- [Create manifest file](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#create-manifest-file)

- [Create static file](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#create-static-file)

- [Deploy app](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#deploy-app)

- [Submit pull request](https://carbondesignsystem.com/developing/angular-tutorial/step-5/#submit-pull-request)

## Preview

A [preview](https://angular-step-6-carbon-tutorial.netlify.com/) of what you’ll
build (visually no different, but built for production):

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

git fetch upstreamgit checkout -b angular-step-5 upstream/angular-step-5Copy to clipboard

```

**Note:** This builds on top of step 4, but be sure to check out the upstream
step 5 branch because it includes the static assets required to get through this
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
[previous step](https://carbondesignsystem.com/developing/angular-tutorial/step-4) left off.

## Create IBM Cloud account

Before we get started,
[create an IBM Cloud account](https://cloud.ibm.com/registration) if you don’t
already have one, as we’ll be deploying there in a bit.

## Optimize Sass

So far we’ve been developing in a, well, development environment where static
asset optimization hasn’t been a priority. If you reference `/src/styles.scss`,
you’ll see one `@import` that is pulling in Carbon’s full Sass build.

```

src/styles.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/styles";

```

To give you an idea of what’s all included, open up
`node_modules/carbon-components/scss/globals/scss/styles.scss`. You’ll see
imports for components like accordion, slider, tooltip, etc. Since we aren’t
using those components, let’s exclude them from our built stylesheets. Keeping
the `$feature-flags` Sass map, and `carbon-overrides.scss`, replace the
`styles.scss` import with:

```

src/styles.scssCopy to clipboard// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import "~carbon-components/scss/globals/scss/css--font-face";@import "~carbon-components/scss/globals/grid/grid";
// Carbon componentsShow more

```

Looking at the new `styles.scss` file, you may be asking what happened to
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

npm run buildCopy to clipboard

```

Looking at `package.json`, you’ll find `ng build`. This builds the app for
production to the `dist` folder. It bundles Angular in production mode and
optimizes the build for the best performance. It even goes so far to minify
files and include hashes in filenames for caching.

As a lot of this may seem like magic since the build configuration came from
Create React App, go ahead and check out their
[production build guidelines](https://facebook.github.io/create-react-app/docs/production-build)
for a full description of what’s happening.

## Create manifest file

Now that we have a production build, let’s get it on the cloud. We’re going to
use
[staticfile-buildpack](https://github.com/cloudfoundry/staticfile-buildpack.git)
to deploy our webapp. Since this is a Cloud Foundry buildpack, we’ll be using
the `cf` command line interface (CLI). If running `cf --help` doesn’t work for
you, chances are you need to
[install the CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html).

**Note:** If unfamiliar with buildpacks, the
[staticfile buildpack docs](https://docs.cloudfoundry.org/buildpacks/staticfile/index.html)
has good definitions and configuration documentation.

With the Cloud Foundry CLI installed, next, we need to create a `manifest.yml`
file in the root of the project. To prevent multiple apps trying to use the
`carbon-tutorial-angular` name, replace `USERNAME` with your GitHub username
below to make sure our apps are uniquely named.

```

manifest.ymlCopy to clipboard---applications:  - name: carbon-tutorial-angular-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git

```

**Note:** With this set-up we’re still using a GitHub personal access token
saved in `.env.local`. If you haven’t created a GitHub access token yet, see
[step 3](https://carbondesignsystem.com/tutorial/react/step-3#create-access-token). You can put the
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

You can speed up deploys by decreasing the files uploaded through cloud foundry.
To accomplish this, ignore any folder not required by the production application
on IBM Cloud. For example, in the case of serving static files, you can ignore
`node_modules/` and `src/` because the only folder being served is `build/`.

## Deploy app

Login to IBM Cloud with:

```

cf login -a https://api.us-south.cf.cloud.ibm.com --ssoCopy to clipboard

```

Deploy app using the `cf push` command. Since `manifest.yml` is in our root
directory, we don’t need to specify it in the push command. But, if you have
multiple manifest files that target different environments, it’s good practice
to specify the file.

**Note:** If you do not have an org or space created, you will need to create
these in your account “Cloud foundry orgs” settings.

Additionally, this step assumes your spaces are in the US South region. To
successfully deploy, you might need to update the region code (for example,
`api.[REGION].cf.cloud.ibm.com`) to the region where your spaces were created,
or create a space in the US South region.
[Learn more](https://cloud.ibm.com/docs/cloud-foundry-public?topic=cloud-foundry-public-endpoints)

```

cf push -f manifest.ymlCopy to clipboard

```

To make it easy on ourselves by not needing to remember that command, let’s add
a script in `package.json`. We can combine the build and deploy steps to make
sure we only deploy immediately after running the build. In the `"scripts"`
object in `package.json`, add:

```

package.jsonCopy to clipboard"deploy": "rm -rf ./dist && ng build --prod --aot && cf push -f manifest.yml"

```

Next time you want to deploy, you can simply run `npm run-script deploy`.

## Submit pull request

That does it! We’re going to submit a pull request to verify completion of this
tutorial step. In doing so, **please include the mybluemix.net URL for your
deployed app in your pull request description**.

### Git commit and push

Before we can create a pull request, stage and commit all of your changes:

```

git add --all && git commit -m "feat(tutorial): complete step 5"Copy to clipboard

```

Then, push to your repository:

```

git push origin angular-step-5Copy to clipboard

```

**Note:** Having issues pushing your changes?
[Step 1](https://carbondesignsystem.com/developing/angular-tutorial/step-1#git-commit-and-push) has
troubleshooting notes that may help.

### Pull request (PR)

Finally, visit
[carbon-tutorial-angular](https://github.com/carbon-design-system/carbon-tutorial-angular)
to “Compare & pull request”. In doing so, make sure that you are comparing to
`angular-step-5` into `base: angular-step-5`.

**Note:** Your tutorial step will be automatically reviewed based on the status
of your tests. Ensure that your tests pass when you submit your PR. Expect your
tutorial step PRs to be reviewed by the Carbon team but not merged. We’ll close
your PR so we can keep the repository’s remote branches pristine and ready for
the next person!

## Code samples

```
git fetch upstreamgit checkout -b angular-step-5 upstream/angular-step-5Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b angular-step-5 upstream/angular-step-5
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
src/styles.scssCopy to clipboard@import "~carbon-components/scss/globals/scss/styles";
```

```scss
@import "~carbon-components/scss/globals/scss/styles";
```

```
src/styles.scssCopy to clipboard// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import "~carbon-components/scss/globals/scss/css--font-face";@import "~carbon-components/scss/globals/grid/grid";
// Carbon componentsShow more
```

```scss
// Feature flags$css--font-face: true;$css--plex: true;
// Global styles@import "~carbon-components/scss/globals/scss/css--font-face";@import "~carbon-components/scss/globals/grid/grid";
// Carbon components
```

```
npm run buildCopy to clipboard
```

```bash
npm run build
```

```
manifest.ymlCopy to clipboard---applications:  - name: carbon-tutorial-angular-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git
```

```bash
---applications:  - name: carbon-tutorial-angular-USERNAME    memory: 64M    buildpack: https://github.com/cloudfoundry/staticfile-buildpack.git
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
package.jsonCopy to clipboard"deploy": "rm -rf ./dist && ng build --prod --aot && cf push -f manifest.yml"
```

```bash
"deploy": "rm -rf ./dist && ng build --prod --aot && cf push -f manifest.yml"
```

```
git add --all && git commit -m "feat(tutorial): complete step 5"Copy to clipboard
```

```bash
git add --all && git commit -m "feat(tutorial): complete step 5"
```

```
git push origin angular-step-5Copy to clipboard
```

```bash
git push origin angular-step-5
```
