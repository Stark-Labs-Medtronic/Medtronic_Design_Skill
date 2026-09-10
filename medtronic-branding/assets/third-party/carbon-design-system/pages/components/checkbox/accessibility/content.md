# Checkbox – Carbon Design System

Source: https://www.carbondesignsystem.com/components/checkbox/accessibility/

# Checkbox

Design annotations are needed for specific instances shown below, but for the
standard checkbox component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/checkbox/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/checkbox/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/checkbox/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

Each checkbox can be reached by `Tab` and selected with `Space` independently.
This matches the established HTML interaction pattern.

Carbon checkboxes retain expected interactions.

### Grouping

For groups of checkboxes, Carbon already provides the code for screen readers to
properly detect the set of checkboxes and announce the group label.

Carbon handles the accessibility of grouped checkboxes.

## Design recommendations

Design annotations are needed for the following instances.

### Meaningful order

Checkboxes can appear in multiple columns. If there is a meaningful order to the
items (such as days of the week), annotate whether the tab order is by row or by
column. See
[Specify the tab order](https://www.ibm.com/able/toolkit/design/ux/navigation/#tab-order).

Annotate if there is meaningful navigation order in rows of checkboxes.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component:

- Checkboxes are grouped using `<fieldset>` and `<legend>`.

- A tri-state checkbox that is partially checked (indeterminate) has
`aria-checked` set to `"mixed"`. See
[Behaviors](https://carbondesignsystem.com/components/checkbox/usage/#behaviors)
on the Usage tab for details.

- See the
[ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.2/#checkbox)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Checkbox | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)