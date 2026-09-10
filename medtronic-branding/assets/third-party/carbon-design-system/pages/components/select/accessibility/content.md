# Select – Carbon Design System

Source: https://www.carbondesignsystem.com/components/select/accessibility/

# Select

No accessibility annotations are needed for selects, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/select/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/select/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via keyboard. Carbon also incorporates other
accessibility considerations, some of which are described below.

### Keyboard interaction

A select component is reached by `Tab` and opened with `Space`, or the `Up` or
`Down` arrow keys. The currently selected option will have focus. The arrow keys
are also used for navigating between options. Users can jump about in the list
by pressing individual letter keys, which will reposition to the first option
beginning with that letter. Options are selected with `Space` or `Enter` keys,
which also close the select. Pressing `Esc` closes a select without changing the
selected option.

Selects are reached by Tab. Space and arrow keys open the list of options.

The arrow keys navigate the open list of options, with the Space or Enter keys
selecting the option with focus and closing the list. Esc closes the list
without changing the option.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Carbon uses the combined attributes `disabled`, `hidden`, and `selected` in
order to make a default prompt such as “Choose an option” not appear in the
list of options when the select is open.

- The component is built on the HTML `select` element and has limited styling,
with most of the visual appearance coming from the browser.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Select | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid select | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)