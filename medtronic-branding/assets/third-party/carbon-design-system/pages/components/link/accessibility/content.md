# Link – Carbon Design System

Source: https://www.carbondesignsystem.com/components/link/accessibility/

# Link

Design annotations are needed for specific instances shown below, but for the
standard link component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/link/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/link/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/link/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

No annotations for keyboard interactions are needed. All links are in the tab
order, and activated with standard keys. Where Carbon links are not persistently
underlined, they receive an underline on focus.

Links are reached by Tab key and activated with the Enter key.

### Contrast

Carbon’s link text and visited link text colors meet the minimum contrast
requirement of 4.5:1 with its background. Carbon also uses a link color and a
visited link color that contrast 3:1 against body text, so that they are
distinguishable even without an underline.

Link text has sufficient contrast with both its background and surrounding
body text.

Visited link text has sufficient contrast with both its background and
surrounding body text.

## Design recommendations

### Ensure link context

If your design uses generic link names such as “read more,” consider making them
unique. Otherwise, annotate a connection with other text in the design that
provides context. This will allow developers to implement in a way that
increases accessibility. See the Equal Access Toolkit
[link text topic](https://www.ibm.com/able/toolkit/design/content/#link-text).

Annotate the connection between generic links and text that gives context.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Associate generic links such as “read more” with other contextual text, using
either `aria-describedby` or `aria-labelledby` (to concatenate multiple text
strings). See the
[Equal Access Toolkit guidance](https://www.ibm.com/able/toolkit/develop/text-and-non-text/#aria-labelling)
for more details.

- See the [ARIA authoring practices](https://w3c.github.io/aria-practices/#link)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Link | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)