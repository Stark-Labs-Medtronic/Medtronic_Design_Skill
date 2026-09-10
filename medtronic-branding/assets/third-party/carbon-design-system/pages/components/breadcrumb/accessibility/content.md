# Breadcrumb – Carbon Design System

Source: https://www.carbondesignsystem.com/components/breadcrumb/accessibility/

# Breadcrumb

No accessibility annotations are needed for breadcrumbs, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/breadcrumb/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/breadcrumb/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

Each page link in the breadcrumb is reached by `Tab` and activated by `Enter`.
The current page, if listed in the breadcrumb, is not a link. If the breadcrumb
is truncated, the ellipsis button for the overflow menu is in the tab order. See
[overflow menu](https://carbondesignsystem.com/components/overflow-menu/usage/)
for details on its keyboard operation.

The breadcrumb’s links are reached by Tab and activated by Enter.

### Labeling and regions

Carbon implements each page link as a list item inside a navigation region named
“breadcrumb.” The ellipsis symbol is a button called “more breadcrumbs” which
opens the
[overflow menu](https://carbondesignsystem.com/components/overflow-menu/usage/).

Carbon provides the accessibility information about the breadcrumb’s
structure.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component:

- The Carbon implementation uses an html5 `<nav>` element; this could also be
achieved with a “navigation” landmark on a `<div>`.

- Each link in the breadcrumb is implemented as an unordered list item so that
screen readers provide more context.

- The visual / separators do not need to be text (Carbon uses CSS) and are not
intended to be navigable.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Breadcrumb | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)