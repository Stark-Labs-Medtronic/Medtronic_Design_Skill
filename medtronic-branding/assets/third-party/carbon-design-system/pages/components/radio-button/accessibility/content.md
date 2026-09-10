# Radio button – Carbon Design System

Source: https://www.carbondesignsystem.com/components/radio-button/accessibility/

# Radio button

No accessibility annotations are needed for radio buttons, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/radio-button/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/radio-button/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interaction

A group of radio buttons takes a single tab stop. Carbon does not require any
item to be selected by default, and the first item will always take focus in
case of no selection. The user changes the selected radio button using the arrow
keys (up/down or left/right). Pressing `Tab` again will move focus out of the
radio button group to the next component.

A radio button group is a single tab stop and radio buttons are selected using
arrow keys.

### Labeling and states

Carbon surfaces the labeling of radio buttons and groups to screen readers and
other assistive technologies. Carbon also provides state and context
information, such as the number of items in the radio button group.

JAWS screen reader output, based on the information provided by Carbon.

## Development considerations

Keep this in mind if you’re modifying Carbon or creating a custom component.

- Carbon uses `fieldset` and `legend` to group and label sets of radio buttons.

- Carbon uses `label` and `for` to programmatically connect radio buttons with
their labels.

- Required radio button groups must be identified programmatically, either via
the label or with `aria-required`.

- See the
[ARIA authoring practices](https://www.w3.org/WAI/ARIA/apg/patterns/radiobutton/)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Radio button | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)