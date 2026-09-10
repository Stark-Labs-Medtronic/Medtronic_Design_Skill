# Modal – Carbon Design System

Source: https://www.carbondesignsystem.com/components/modal/accessibility/

# Modal

Design annotations are needed for specific instances shown below, but for the
standard modal dialog component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/modal/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/modal/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/modal/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

Modal dialogs take focus on appearance, and the tab order is constrained to the
modal’s controls until the modal is closed by choosing one of the buttons with
`Enter` or `Space`, or is dismissed by pressing `Esc`.

Keyboard navigation is constrained to the dialog. Tab cycles through the
components that take focus.

The dialog is resolved by the user pressing Esc or activating a button.

### Focus handling

When the dialog appears, the first item that gets focus depends on the type of
dialog. Passive dialogs only contain a close button (X), so that takes focus.
For dialogs which prompt for confirmation or user decision, the primary button
takes focus (regardless of number of buttons). For destructive interactions, the
“cancel” button takes focus, not the red danger/delete button. The tab order
should proceed left and down from whichever item has focus then wrap back to the
close button (X).

The first item with focus varies depending on dialog type.

## Design recommendations

### Designate the input that takes focus in a transactional

The only time the starting focus would not be on a button is where a dialog
contains input fields. For such transactional dialogs, designers should annotate
that the first input field should receive focus. Note that text links are not
considered a user input in this context.

Annotate the starting input that should take focus on a transactional dialog.

Do not give a link focus when a modal opens.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Carbon assigns the container a role of “dialog” and sets `aria-modal` to
`"true"`.

- The dialog is labelled via `aria-label`, using the same string used for the
modal’s title; `aria-labelledby` could also be used to assign the title’s
string.

- See the modal pattern in the
[ARIA authoring practices](https://w3c.github.io/aria-practices/#dialog_modal)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Modal | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Composed modal | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)