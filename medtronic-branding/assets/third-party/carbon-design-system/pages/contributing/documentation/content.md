# Contribute docs – Carbon Design System

Source: https://www.carbondesignsystem.com/contributing/documentation/

# Contribute docs

All components and patterns require usage, style, code, and accessibility
guidance on the Carbon website. Check out the markdown templates and
instructions below to contribute documentation smoothly.

- [Documenting components](https://carbondesignsystem.com/contributing/documentation/#documenting-components)

- [Documenting patterns](https://carbondesignsystem.com/contributing/documentation/#documenting-patterns)

- [Writing better content](https://carbondesignsystem.com/contributing/documentation/#writing-better-content)

- [Publishing updates](https://carbondesignsystem.com/contributing/documentation/#publishing-updates)

## Documenting components

The website is written in markdown, which makes it easy for anyone to contribute
content in a systematic way. Some components require more complex documentation
than others, but you should cover each topic included in the following markdown
templates: usage, style, code, and accessibility.

Check out Carbon’s handy markdown
[styling cheatsheet](https://github.com/carbon-design-system/carbon-website/wiki/Markdown-cheatsheet)
for how to style content. You may also use the
[Figma template](https://www.figma.com/file/XQqHxu38CiY3Vx1iHdafIa/Image-production-guidelines?type=design&node-id=2651-218&mode=design&t=UbKwOlVeoU83hyGI-0)
to draft content and images

### Usage template: for components with one variant

The usage template helps describe when to use a component and how it works. The
template below provides example content from the
[Accordion](https://carbondesignsystem.com/components/accordion/usage) usage tab, along with many tips on best
ways to compose content and images. Check out
[Content switcher](https://carbondesignsystem.com/components/content-switcher/usage) or
[Checkbox](https://carbondesignsystem.com/components/checkbox/usage) for additional single variant references.

```

---title: Accordiondescription:  An accordion is a vertically stacked list of headers that reveal or hide  associated sections of content.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';Copy to clipboardShow more

```

### Usage template: for components with multiple variants

Use this template for documenting components that have multiple variants. You
can see this template in use for
[Dropdown](https://carbondesignsystem.com/components/dropdown/usage/),
[Button](https://carbondesignsystem.com/components/button/usage/), and
[Notification](https://carbondesignsystem.com/components/notification/usage/).

Follow this template when possible; however, for components with more complex
variants, it may be necessary to adapt the structure to more effectively
organize and group variant content. See the
[Tile](https://carbondesignsystem.com/components/tile/usage/) component for an
example of this approach.

```

---title: Component namedescription: Explains what the component is in one or two sentences.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--Copy to clipboardShow more

```

### Style template: for components with one variant

The style template helps describe how a component with one variant looks,
including visual specifications such as color, typography, structure, and size.
The template below provides example content from the
[Accordion](https://carbondesignsystem.com/components/accordion/style) style
tab, along with many tips on best ways to compose content and images.

```

---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,Copy to clipboardShow more

```

### Style template: for components with multiple variants

This style template helps describe how a component with multiple variants look,
including visual specifications such as color, typography, structure, and size.
The template below provides example content from the
[Text input](https://carbondesignsystem.com/components/text-input/style) style
tab, along with many tips on best ways to compose content and images.

```

---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,Copy to clipboardShow more

```

### Code template

The code template helps developers implement your component. Be specific,
include code snippets, and be sure to update as dependencies and versions
change.

```

---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--Copy to clipboardShow more

```

### Accessibility template

The accessibility template helps designers and developers ensure components are
accessible. The published information helps users understand all the
accessibility considerations that are baked into Carbon. Refer to our guidance
on creating the
[keyboard interaction visuals](https://github.com/hiraaeth/component-contribution-accessibility/wiki/High-fidelity-keyboard-interaction-visuals).
Also check out Button’s [Accessibility](https://carbondesignsystem.com/components/button/accessibility/) tab
for additional references.

```

---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';
<PageDescription>Copy to clipboardShow more

```

## Documenting patterns

Patterns show reusable combinations of components and templates that address
common user objectives with sequences and flows. Because they are more
complicated than components, you may need to adjust the topic order to best tell
the story — but your pattern should cover all of the topics outlined in the
following templates.

### Pattern template: for one variant

Use this template for documenting patterns that have a single variant. You can
see this template in use for [Toolbar](https://carbondesignsystem.com/patterns/text-toolbar-pattern/).

```

---title: Pattern namedescription: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
Copy to clipboardShow more

```

### Pattern template: for multiple variants

Use this template for documenting patterns that have multiple types or variants.
You can see this template in use for [Dialog](https://carbondesignsystem.com/patterns/dialog-pattern/) and
[Loading](https://carbondesignsystem.com/patterns/loading-pattern/).

```

---title: Pattern name (multiple variants)description: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
Copy to clipboardShow more

```

## Writing better content

As you fill out the templates above, please keep these things in mind when
writing content for Carbon.

- Aim for a friendly and encouraging tone.

- Speak directly to the user. You can use the second person pronoun (“you”).

- Keep sentences and paragraphs short and focused.

- Be clear and concise by removing unnecessary words. The more concise the text,
the easier it is for all users to understand.

- Use sentence case for everything, including component names, e.g. Content
switcher and Data table.

## Publishing updates

Ready to get your work reviewed and published? There are two ways to do this,
depending on your experience with GitHub. You may also draft your content and
bring it to
[office hours](https://ec.yourlearning.ibm.com/w3/series/10289694?layout=grid&_ga=2.129990351.257088430.1694013487-309583455.1691093939&_gl=1*16l2j5q*_ga*MzA5NTgzNDU1LjE2OTEwOTM5Mzk.*_ga_FYECCCS21D*MTY5NDAzMjgwMi4xMS4xLjE2OTQwMzQ0OTEuMC4wLjA.)
to get further guidance.

### Editing in browser

#### How to edit an existing page

If you are editing an existing docs page, the easiest option is to click on the
`Edit this page on GitHub` link that appears at the bottom of every page on the
site. The link opens the specific GitHub page where you can edit the content and
then propose the change with a pull request. Your changes will be reviewed by
the Carbon team. This is the easiest and most commonly used approach by
contributors.

#### How to add a new page or image

To start, go to the Carbon website repository
[here](https://github.com/carbon-design-system/carbon-website). Navigate to the
left hand corner above the files and click `main`. From here, type in a new
branch name that reflects your work. For
example,`add-accordion-accessibility-guidance`. Once that new branch is created,
navigate to where the new file will be stored for a
[component](https://github.com/carbon-design-system/carbon-website/tree/main/src/pages/components)
or
[pattern](https://github.com/carbon-design-system/carbon-website/tree/main/src/pages/patterns).

Ensure you are in the branch you created, then navigate to `Add file` in the
upper right-hand corner. To add a new guidance page, click `create new file`
button. Title the file one of the following: `usage.mdx`, `style.mdx`,
`code.mdx`, or `accessibility.mdx`. To add an image, make sure you are in the
image folder and click `Upload files`.

After filling out the markdown template or adding an image, click
`Commit changes`. Describe your work and double check that you are on the branch
you created. If you are in the wrong branch, you will have to copy your content
into the correct branch.

Once you have committed your changes, go to the
[Pull requests](https://github.com/carbon-design-system/carbon-website/pulls)
page. Compare `base: main` to your branch and click `Create new pull request`.
Your contribution will be reviewed by the Carbon team!

### Editing in a local environment

Alternatively, if you are planning regular or more comprehensive content updates
and are up for a more advanced option, you’ll want to fork the repo and install
some of the tools we use to build the website. This will create an easier
workflow for you long term, but takes some time to set up.

If you are familiar with this process, you can
[fork the repo](https://github.com/carbon-design-system/carbon-website/blob/main/.github/CONTRIBUTING.md#submission-guidelines)
and get started. Otherwise, reach out to the Carbon team on slack or
[office hours](https://ec.yourlearning.ibm.com/w3/series/10289694?layout=grid&_ga=2.129990351.257088430.1694013487-309583455.1691093939&_gl=1*16l2j5q*_ga*MzA5NTgzNDU1LjE2OTEwOTM5Mzk.*_ga_FYECCCS21D*MTY5NDAzMjgwMi4xMS4xLjE2OTQwMzQ0OTEuMC4wLjA.)
and we’ll help you find the best way to contribute.

## Code samples

```
---title: Accordiondescription:  An accordion is a vertically stacked list of headers that reveal or hide  associated sections of content.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';Copy to clipboardShow more
```

```markdown
---title: Accordiondescription:  An accordion is a vertically stacked list of headers that reveal or hide  associated sections of content.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';
```

```
---title: Component namedescription: Explains what the component is in one or two sentences.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--Copy to clipboardShow more
```

```markdown
---title: Component namedescription: Explains what the component is in one or two sentences.tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--
```

```
---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,Copy to clipboardShow more
```

```markdown
---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,
```

```
---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,Copy to clipboardShow more
```

```markdown
---title: [Component name]description: [Explains what the component is in one or two sentences.]tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
The following page documents visual specifications such as color, typography,
```

```
---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--Copy to clipboardShow more
```

```markdown
---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
<PageDescription>
<!--
```

```
---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';
<PageDescription>Copy to clipboardShow more
```

```markdown
---title: Component name (you won't need to write this)description: Component description (you won't need to write this)tabs: ['Usage', 'Style', 'Code', 'Accessibility']---
import A11yStatus from 'components/A11yStatus';
<PageDescription>
```

```
---title: Pattern namedescription: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
Copy to clipboardShow more
```

```markdown
---title: Pattern namedescription: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
```

```
---title: Pattern name (multiple variants)description: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
Copy to clipboardShow more
```

```markdown
---title: Pattern name (multiple variants)description: Explain the pattern in one or two sentences.---
<PageDescription>
Explain the pattern in one or two sentences.
```
