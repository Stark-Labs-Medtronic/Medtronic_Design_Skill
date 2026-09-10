# AI label – Carbon Design System

Source: https://www.carbondesignsystem.com/components/ai-label/accessibility/

# AI label

No accessibility annotations are needed for AI labels, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/ai-label/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/ai-label/accessibility/#development-considerations)

## What Carbon provides

### Keyboard interactions

The AI labels is the trigger button. The AI label is in the tab order and is
activated by pressing `Enter` or `Space`. The activation toggles the
explainability popover open and closed, and focus remains on the trigger.

When the popover contains interactive elements, pressing `Tab` will move focus
to the first component in the popover. When the popover only has non-interactive
text, or when the focus is on the last component in the popover, pressing `Tab`
will close the popover and move focus to the next tab stop on the page. Pressing
`Esc` in an open popover closes it and returns focus to the trigger.

The AI label icon button that triggers the popover is in the page tab order,
as are interactive elements inside an open popover.

#### Input interactions

The AI label can appear inside user inputs, where it adds an additional tab
stop. For example, a text input will take focus as normal (the existing value
will be selected), and then the AI label will take a second tab stop. If the
user clears the existing AI-supplied value, (with the `Delete` key), then the AI
label becomes a `revert` icon, which on activation will restore the AI-supplied
value in the input.

The AI label button is a second tab stop after the initial tab stop for the
input.

The AI label changes to a “revert” symbol if a user modifies the input value.
Activating “revert” restores the prior AI value.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- The icon button has `aria-label="AI - Show information"`.

- The button uses `aria-expanded` to set toggletip visibility and
`aria-controls` to handle navigation to the content.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| AI label | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)