# Typography – Carbon Design System

Source: https://www.carbondesignsystem.com/elements/typography/type-sets/

# Typography

Carbon uses a clear naming approach and type tokens to manage typography across
complex and layered layouts and patterns, and these tokens sit within two type
sets: expressive and productive.

- [Overview](https://carbondesignsystem.com/elements/typography/type-sets/#overview)

- [Utility styles](https://carbondesignsystem.com/elements/typography/type-sets/#utility-styles)

- [Body styles](https://carbondesignsystem.com/elements/typography/type-sets/#body-styles)

- [Fixed heading styles](https://carbondesignsystem.com/elements/typography/type-sets/#fixed-heading-styles)

- [Fluid heading styles](https://carbondesignsystem.com/elements/typography/type-sets/#fluid-heading-styles)

- [Fluid display styles](https://carbondesignsystem.com/elements/typography/type-sets/#fluid-display-styles)

- [Questions](https://carbondesignsystem.com/elements/typography/type-sets/#questions)

## Overview

Carbon uses type tokens to manage typography, and these tokens sit within two
type sets. The productive and expressive type sets support designers creating
for a full range of user needs and activities across product and web pages. To
understand when to use styles from each set, see
[Style strategies](https://carbondesignsystem.com/elements/typography/style-strategies).

#### Base type sizes

The productive type set uses a base type size of 14px, while the expressive type
set uses a base type size of 16px.

#### Style naming conventions

Within **Body styles** and **Supporting styles**, the same set of styles are
offered, and an easy way to spot which type set they belong to is to look at the
suffix. Productive styles are named with a suffix of `-01` and expressive style
names have a suffix of `-02`.

#### Two heading sets

There are two heading sets, one for productive and one for expressive. The major
difference between them is in how they are implemented in code because of the
nature of the pages.

- The productive type set uses _fixed_ headings. Product pages have a higher
density of information housed inside containers for space efficiency, and in
these situations fixed type styles are a must.

- The expressive type set has two fixed headings that are to be used where
smaller headings are needed. The remaining headings are _fluid_. Web pages
need to be able to flex and work at different breakpoints, and the fluid
heading styles change size at different breakpoints, and can
extrapolate/stretch in between sizes for smooth transitions.

## Utility styles

The utility styles are used with productive and expressive moments and include
styles for code snippets, labels for captions and helper text, as well as legal
copy. Productive styles have a suffix of `-01` and expressive styles have a
suffix of `-02`.

This is for inline code snippets and smaller code elements.

This is for large code snippets and larger code elements.

This is a multipurpose type style that can be used for field labels in components, error messages, and captions. It should not be used for body copy.

This is a multipurpose type style that can be used for field labels in components, error messages, and captions. It should not be used for body copy.

This is for explanatory helper text that appears below a field title within a component.

This is for explanatory helper text that appears below a field title within a component.

This is for legal copy appearing in product pages.

This is for legal copy appearing in web pages.

## Body styles

There are two body styles for productive and expressive moments. Productive
styles have a suffix of `-01` and expressive styles have a suffix of `-02`.

This is for short paragraphs with no more than four lines and is commonly used in components.

This is for short paragraphs with no more than four lines. Use in expressive components, such as button and link.

With a slightly taller line height than body-compact-01, this body style is used in productive layouts for long paragraphs with more than four lines. Use also for longer body copy in components such as accordion or structured list. It is always left-aligned. Body-long-01 can also be used for productive moments within expressive experiences.

With a slightly taller line height than body-compact-02, this style is commonly used in expressive layouts for long paragraphs with four lines or more. It is always left-aligned.

## Fixed heading styles

The fixed heading styles are used for product pages where multiple containers
are used and space efficiency is key. Fixed means they are not responsive. The
type size remains constant regardless of break point.

Creators of web pages also use the fixed headings `-01` and `-02` where smaller
headings are needed.

This is for component and layout headings. It pairs with $body-compact-01.

This is for smaller layout headings. It pairs with $body-compact-02.

This is for component and layout headings. It pairs with $body-01.

This is for smaller layout headings. It pairs with $body-02.

This is for component and layout headings.

This is for layout headings.

This is for layout headings.

This is for layout headings.

This is for layout headings.

## Fluid heading styles

The fluid heading styles are primarily used in web pages, and are therefore part
of the expressive set of type styles. These headings are responsive and the type
styles actually change size incrementally (almost imperceptibly) between the
different breakpoints — hence the name “fluid.”

Do not use these styles inside a container. They may be used in product pages
where text sits outside of a container, and a blend of expressive and productive
type styles is desired for hierarchy and distinction. For more information, see
[Style strategies](https://carbondesignsystem.com/elements/typography/style-strategies).

_Note: the slider below shows the type sizes jumping abruptly between
breakpoints, which is not a good representation of the actual behavior._

This is for component and layout headings.

This is for layout headings.

This is for layout headings.

This is for layout headings.

## Fluid display styles

The callout and display styles are part of the expressive set and being fluid,
they will adjust at different breakpoints. Do not use these styles inside a
container. For guidance about using display styles, see
[Style strategies](https://carbondesignsystem.com/elements/typography/style-strategies#expressive-use-cases).

This is for larger paragraphs of type that are usually three or more lines in length.

“Quote.”

“Quote.”

Display

Display

Display

Display

## Questions?

_For IBMers only:_ If you have any questions about using either of these
experiences, reach out to the teams on Slack or sign up to share your work in a
review.

#### Carbon Design System

- Slack channel:
[#carbon-design-system](https://ibm-studios.slack.com/messages/C0M053VPT/)

- [Meetups](https://www.carbondesignsystem.com/whats-happening/meetups/) with
Carbon Design System

#### Carbon for IBM Dotcom

- Slack channel:
[#carbon-for-ibm-dotcom](https://cognitive-app.slack.com/archives/C2PLX8GQ6)

- Office hours with Carbon for IBM.com. See our
[Slack channel](https://cognitive-app.slack.com/archives/C2PLX8GQ6) for
details.