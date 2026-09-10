# Breadcrumb – Carbon Design System

Source: https://www.carbondesignsystem.com/components/breadcrumb/usage/

# Breadcrumb

The breadcrumb is a secondary navigation pattern that helps a user understand
the hierarchy among levels and navigate back through them.

- [Live demo](https://carbondesignsystem.com/components/breadcrumb/usage/#live-demo)

- [Overview](https://carbondesignsystem.com/components/breadcrumb/usage/#overview)

- [Formatting](https://carbondesignsystem.com/components/breadcrumb/usage/#formatting)

- [Content](https://carbondesignsystem.com/components/breadcrumb/usage/#content)

- [Behaviors](https://carbondesignsystem.com/components/breadcrumb/usage/#behaviors)

- [Modifiers](https://carbondesignsystem.com/components/breadcrumb/usage/#modifiers)

- [Related](https://carbondesignsystem.com/components/breadcrumb/usage/#related)

- [Feedback](https://carbondesignsystem.com/components/breadcrumb/usage/#feedback)

## Live demo

This live demo contains only a preview of functionality and styles available for this component. View the [full demo](https://react.carbondesignsystem.com/?path=/story/components-breadcrumb--default&globals=theme:white) on Storybook for additional information such as its version, controls, and API documentation.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

## Overview

Breadcrumbs show users their current location relative to the information
architecture and enable them to quickly move up to a parent level or previous
step.

### When to use

Breadcrumbs are effective in products and experiences that have a large amount
of content organized in a hierarchy of more than two levels. They take up little
space but still provide context for the user’s place in the navigation
hierarchy.

### When not to use

Breadcrumbs are always treated as secondary and should never entirely replace
the primary navigation. They shouldn’t be used for products that have single
level navigation because they create unnecessary clutter.

If you are taking users through a multistep process use a
[progress indicator](https://carbondesignsystem.com/components/progress-indicator/usage/) instead.

### Types

Carbon supports two types of breadcrumbs. Both types are styled the same, but
the methods for populating the breadcrumb trail are different. The breadcrumb
type used should be consistent across a product.

| Breadcrumb type | Purpose |

| --- | --- |

| Location-based | These illustrate the site’s hierarchy and show the user where they are within that hierarchy. |

| Path-based | These show the actual steps the user took to get to the current page, rather than reflecting the site’s information architecture. Path-based breadcrumbs are always dynamically generated. |

## Formatting

### Anatomy

1. **Page link:** Directs users to the parent-level page.

2. **Separator:** Clearly distinguishes between each page.

### Sizing

There are two different sizes of breadcrumbs: **small** and **medium**. The
small breadcrumb uses the `$label-01` type token, while the medium breadcrumb
uses the `$body-compact-01` type token.

Small and medium sizes of breadcrumb

#### Small size

Small breadcrumbs are commonly used in page headers. They can also be used in
condensed spaces and for smaller breakpoints. You may also choose to use the
small breadcrumb when trying to achieve a balanced content hierarchy and need a
smaller breadcrumb to pair with.

Example shows the use of small breadcrumbs

#### Medium size

Medium breadcrumbs are typically used when there is no page header and are
placed at the top of a page. The default size of breadcrumb is the medium size.

Example shows the use of medium default breadcrumbs

### Placement

Breadcrumbs are placed in the top left portion of the page. They sit underneath
the header and navigation, but above the page title.

## Content

### Main elements

#### Page link

- Each page link should be short and clearly reflect the location or entity it
links to.

- Start with the highest level parent page and move deeper into the information
architecture as the breadcrumb trail progresses.

- By default, the current page is not listed in the breadcrumb trail. However,
if a page doesn’t have a title or the current page is not clear, the current
page can be included in the breadcrumb trail if it is more suitable for your
products use case. If the current page is included in a breadcrumb trail, it
is always the last text listed and is not an interactive link.

### Overflow content

When space becomes limited, use an
[overflow menu](https://carbondesignsystem.com/components/overflow-menu/usage) to truncate the breadcrumbs.
The first and last two page links should be shown, but the remaining breadcrumbs
in between are condensed into an overflow menu. Breadcrumbs should never wrap
onto a second line.

### Truncation

For most use cases at larger breakpoints, keep the first home breadcrumb link
for as long as possible in breakpoints, even when an overflow might be present.
Also for mobile or small viewpoints, start with the overflow first, following by
one breadcrumb.

### Further guidance

For further content guidance, see Carbon’s
[content guidelines](https://carbondesignsystem.com/guidelines/content/overview).

## Behaviors

### Interactions

All the pages in the breadcrumb component should be interactive (except the
current page) and link to their respective pages.

#### Mouse

Users can trigger an item by clicking on a breadcrumb page link. The separators
between page links are not interactive.

#### Keyboard

Users can navigate between breadcrumb links by pressing `Tab` and `Shift-Tab`.
Users can trigger a breadcrumb link by pressing `Enter` while the link has
focus. For additional keyboard interactions, see
the [accessibility tab](https://www.carbondesignsystem.com/components/breadcrumb/accessibility).

## Modifiers

By default, Carbon breadcrumb trails should not include the current page. If a
page doesn’t have a title or the current page is not clear, it can be included
in the breadcrumb trail. If the current page is included in a breadcrumb trail,
it is always the last text listed and is not an interactive link.

## Related

- [Global header](https://carbondesignsystem.com/patterns/global-header)

- [Progress indicator](https://carbondesignsystem.com/components/progress-indicator/usage/)

- [UI shell header](https://carbondesignsystem.com/components/UI-shell-header/usage)

- [Overflow menu](https://carbondesignsystem.com/components/overflow-menu/usage/)

## Feedback

Help us improve this component by providing feedback, asking questions, and
leaving any other comments on
[GitHub](https://github.com/carbon-design-system/carbon-website/issues/new?assignees=&labels=feedback&template=feedback.md).