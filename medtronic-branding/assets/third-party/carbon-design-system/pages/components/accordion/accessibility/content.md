# Accordion – Carbon Design System

Source: https://www.carbondesignsystem.com/components/accordion/accessibility/

# Accordion

Design annotations are needed for specific instances shown below, but for the
standard accordion component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/accordion/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/accordion/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/accordion/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

Each accordion is a tab stop. `Space` or `Enter` keys expand or collapse
accordions, which are collapsed by default. Interactive elements within expanded
accordions integrate into the tab order automatically.

Accordions and interactive elements in the expanded content are in the tab
order and keyboard operable.

### Labeling and states

The collapsed or expanded state of the accordions is
[programmatically set](https://www.ibm.com/able/requirements/requirements/#4_1_2)
by default, eliminating the need for designers to provide
[text equivalents](https://www.ibm.com/able/toolkit/design/content/#alternative-text-for-visuals)
for the chevron icons.

Carbon handles the accessibility of the chevron indicators.

## Design recommendations

Design annotations are needed for the following instances.

### Headings

Carbon accordions are not set as headings by default. For improved
accessibility, annotate accordions as headings on the first occurrence in a
product. Annotate the heading level of accordions as needed. See
[Indicate heading levels](https://www.ibm.com/able/toolkit/design/content/#headings).

If accordion titles act as headings, annotate for development.

### Alignment

Carbon chevrons are right-aligned by default, but left-aligned chevrons are more
accessible for users with low vision, as the expanded/collapsed indicator is
closer to the accordion title.

Annotate if the accordion chevrons should be left-aligned.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component:

- The accordion header has a role of `<button>`, with an `aria-expanded`
attribute set to `"true"` or `"false"`.

- The button has an `aria-controls` property set to the unique id of the panel
it controls.

- Since accordions are typically grouped together, Carbon puts each button
inside a list item in an unordered list, which provides additional context to
screen reader users; where only one accordion is used, it should not be put in
a list.

- When accordion titles are used as headings, the buttons are also wrapped in an
element with an appropriate heading level; ARIA can be used to set both the
heading role and the level (via `aria-level`).

- See the
[ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.2/#accordion)
for more guidance.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Accordion | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)