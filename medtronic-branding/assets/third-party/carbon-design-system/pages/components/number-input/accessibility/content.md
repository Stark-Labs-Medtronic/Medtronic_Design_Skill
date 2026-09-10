# Number input – Carbon Design System

Source: https://www.carbondesignsystem.com/components/number-input/accessibility/

# Number input

Design annotations are needed for specific instances shown below, but for the
standard number input component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/number-input/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/number-input/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/number-input/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interaction

The Carbon number input replicates the behavior of the stock HTML component. The
number input takes a single tab stop. The + and - buttons, operable by pointer,
are not in the tab order. When the input has focus, the arrow keys give keyboard
users the same ability to incrementally adjust the values. As well, users can
directly type numeric values in the input. Only numerals are allowed to be
entered.

The number input is reachable by Tab and changed with the arrow keys or by
directly entering a number.

### Error handling

Carbon provides errors and warning messages to assistive technology. This is an
improvement on the stock HTML number input, which simply prevents the typing of
alphabetic characters without explanation. Carbon also adds an error or warning
icon and puts error messages in red as a further visual cue.

Messages are surfaced to assistive technologies, and color alone is not used
to visually signal errors.

## Design recommendations

Design annotations are needed for the following instance.

### Cue users for value and step

Carbon offers the ability for the author to set minimum and maximum values for
the input. When setting limits on number entry, designers should warn the user
in advance, instead of users discovering limits through an error message. This
is particularly the case if designers alter the step value, which determines the
increment change when activating the +/- buttons or arrow keys. If a user
directly enters a value that does not match the step increment, it will be
disallowed for no apparent reason, so advanced warnings are crucial.

Notify users of allowable input ranges through helper text.

## Development considerations

Keep this in mind if you’re modifying Carbon or creating a custom component.

- Carbon uses `aria-describedby` to associate the helper text and error messages
with the input.

- The red error SVG icons have `aria-hidden="true"` set, since the helper text
provides the same information.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Number input | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid number input | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)