# FAQs – Carbon Design System

Source: https://www.carbondesignsystem.com/developing/react-tutorial/faq/

# FAQs

### I am getting an error that says yarn lockfile missing. How do I fix this?

- This error can occur when the `yarn.lock` file is either missing or differs
from the one used in the tutorial step. To fix this, you can go to the GitHub
branch for the step you are on, find the `yarn.lock` file, and copy that file
into your working directory. You may need to delete your `node_modules` folder
and run `yarn` afterwards.

### I am getting a yarn offline cache error. How do I fix this?

- Try running
`rm -rf .yarn-offline-mirror node_modules && yarn cache clean && yarn install`
and push up any changes. If this still does not work, ensure your `yarn.lock`
file matches the one at the start of the tutorial step

### How can I show others my completion status?

- Proof of your completion of the tutorial can be seen by filtering the PR list
to show your five PRs with the `status: approved` label.

- You can filter the pull request list to show only pull requests authored by
your username. Replace `YOURUSERNAMEHERE` with your username in the following
link:

[https://github.com/carbon-design-system/carbon-tutorial-nextjs/pulls?q=author%3AYOURUSERNAMEHERE](https://github.com/carbon-design-system/carbon-tutorial-nextjs/pulls?q=author%3AYOURUSERNAMEHERE)

- It can also be demonstrated by deploying your app. Please see further
documentation
[here](https://carbondesignsystem.com/developing/react-tutorial/step-5#build-for-production-and-deploy).