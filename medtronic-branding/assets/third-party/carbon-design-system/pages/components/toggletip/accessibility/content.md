# Toggletip – Carbon Design System

Source: https://www.carbondesignsystem.com/components/toggletip/accessibility/

# Toggletip

Toggletips display and hide additional information upon the click of a UI
trigger element and can contain interactive elements.

- [What Carbon provides](https://carbondesignsystem.com/components/toggletip/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/toggletip/accessibility/#development-considerations)

## What Carbon provides

Carbon already incorporates accessibility into the toggletip component.
Designers only need to indicate the toggletip’s content.

### Keyboard interactions

Toggletips use an information icon button for the trigger. These buttons are in
the tab order and are activated by pressing `Enter` or `Space`. The activation
toggles the tip open and closed, and focus remains on the trigger.

When the toggletip contains interactive elements, pressing`Tab` will move focus
to the first component in the toggletip. When the toggletip only has
non-interactive text, or when the focus is on the last component in the
toggletip, pressing `Tab` will close the toggletip and move focus to the next
tab stop on the page. Pressing `Esc` also closes an open toggletip and returns
focus to the trigger if the focus is inside the tooltip.

The information icon button that triggers the toggletip is in the page tab
order, as are interactive elements inside an open toggletip.

Toggletips appear when the information icon button is activated and disappear
by activating the icon again, pressing Esc, or tabbing away from the
toggletip.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- The icon button has `aria-label="Show information"`.

- The button uses `aria-expanded` to set toggletip visibility and
`aria-controls` to handle navigation to the content.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Toggletip | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)