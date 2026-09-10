# Text input – Carbon Design System

Source: https://www.carbondesignsystem.com/components/text-input/accessibility/

# Text input

No accessibility annotations are needed for text inputs, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/text-input/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/text-input/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard navigation

Carbon’s text inputs and text areas replicate the default HTML component
operation. Each input field is a tab stop, as are any preceding information
icons (which open with `Enter`/`Space` and close with `Esc`). For password
inputs, Carbon provides a keyboard-operable ability to toggle the password
value’s visibility using `Enter` or `Space`.

Each input is a tab stop, as are any information icons.

### Keyboard interaction

On focus, users can type directly into the input field. Any existing text in the
input is highlighted on focus and will be replaced when the user begins typing.
(Existing text in a text area is not highlighted on focus; instead the cursor is
placed at the start or the user’s prior point of interaction.) Users can
interact inside text inputs and text areas using standard arrow keys and
modifiers (`Ctrl` for Windows, `Option` for Mac).

Users can move around in text inputs and text areas using arrows keys and
modifiers.

### Labeling and helper text

Carbon programmatically surfaces both the input’s label and any helper text to
assistive technologies such as screen readers. Any error messages for text
inputs are also accessibly revealed.

Labels and helper text are accessibly provided.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Labels are properly associated with inputs using the `for` attribute.

- Helper text is surfaced to assistive technology through `aria-describedby`.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Text input | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Text area | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid text input | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid text area | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)