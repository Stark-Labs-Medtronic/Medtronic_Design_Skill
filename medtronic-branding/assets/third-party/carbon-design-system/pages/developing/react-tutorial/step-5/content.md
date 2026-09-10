# 5. Deploying the project – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/react-tutorial/step-5/

# 5. Deploying the project

This is an optional step that takes what we’ve built so far and optimizes the
app for a production environment.

- [Fork, clone and branch](https://carbondesignsystem.com/developing/react-tutorial/step-5/#fork-clone-and-branch)

- [Build for production and deploy](https://carbondesignsystem.com/developing/react-tutorial/step-5/#build-for-production-and-deploy)

## Preview

A [preview](https://carbon-tutorial-nextjs.vercel.app/) of what you’ll build
(visually no different, but built for production):

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

git fetch upstreamgit checkout -b v11-next-step-5 upstream/v11-next-step-5Copy to clipboard

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

yarn devCopy to clipboard

```

You should see something similar to where the
[previous step](https://carbondesignsystem.com/developing/react-tutorial/step-4) left off.

## Build for production and deploy

Before we deploy our app, we need to create an optimized production build with
this command. You may need to `CTRL-C` to stop the development environment
first.

```

yarn buildCopy to clipboard

```

Looking at `package.json`, you’ll find `yarn build` to run `next build`. This
builds the app for production to the `build` folder. It bundles Next.js in
production mode and optimizes the build for the best performance. It even goes
so far to minify files and include hashes in filenames for caching.

As a lot of this may seem like magic since the build configuration came from
Create Next App, go ahead and check out their
[going to production checklist](https://nextjs.org/docs/pages/building-your-application/deploying/production-checklist)
for a full description of what’s happening.

Next you can deploy your application to your preferred host, such as
[Vercel](https://nextjs.org/learn/basics/deploying-nextjs-app/deploy),
[IBM Cloud](https://www.ibm.com/cloud/free?utm_content=SRCWW&p1=Search&p4=43700074971942949&p5=e&gclid=CjwKCAjwjaWoBhAmEiwAXz8DBZSQ7ksqHmmFDCLGL-5erHPFytezo4q3fB6qJ13wkZROr3DYs95BGhoC6fUQAvD_BwE&gclsrc=aw.ds),
[GitHub Pages](https://docs.github.com/en/pages/quickstart).

## Code samples

```
git fetch upstreamgit checkout -b v11-next-step-5 upstream/v11-next-step-5Copy to clipboard
```

```bash
git fetch upstreamgit checkout -b v11-next-step-5 upstream/v11-next-step-5
```

```
yarnCopy to clipboard
```

```bash
yarn
```

```
yarn devCopy to clipboard
```

```bash
yarn dev
```

```
yarn buildCopy to clipboard
```

```bash
yarn build
```
