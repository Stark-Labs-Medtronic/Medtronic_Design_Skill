# Dropdown – Carbon Design System

Source: https://www.carbondesignsystem.com/components/dropdown/accessibility/

# Dropdown

No accessibility annotations are needed for dropdowns, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/dropdown/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/dropdown/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

A dropdown component and its variants multiselect and combo box are reached by
`Tab`, with navigation of the options by `Up` and `Down` arrow keys. However,
the keys for opening the component and selecting its options are different for
each variant.

Dropdowns are in the tab order and operable by Up and Down arrow keys, once
opened.

#### Dropdown

The default dropdown opens with `Enter`, `Space`, or `Down arrow`. If an option
is already selected or if `Down arrow` is used to open the component, the focus
moves to the first or currently selected option. Arrow keys change options, and
any option with focus is selected with `Space` or `Enter`, which also closes the
dropdown. Pressing `Esc` or `Tab` closes a dropdown without changing the
selected option.

The Space and Enter keys can be used to open dropdowns and also select an
option with focus. Esc cancels and closes the interaction.

#### Multiselect

The multiselect opens with `Down arrow`, or with the `Enter` or `Space` keys,
which are also used to toggle the selection of any option. Focus handling is the
same as with the default dropdown: focus is only moved to the options list if an
item is already selected or if the multiselect is opened with the `Down arrow`.
Once items are selected, a tag appears in the field, showing a numerical
representation of the number of items selected along with an ‘x’. Pressing `Esc`
closes the multiselect. Pressing `Delete` while focus is in the collapsed field
will clear all selected options.

Space and Enter keys open multiselects and toggle the state of the checkboxes
in the list. Esc closes the list.

#### Combo box

The combo box’s operation (as well as the filterable multiselect’s) is quite
different, since it is a combination of a text input and a dropdown. `Enter` or
the `Up` or `Down arrow` keys will open the list of options, as will typing any
matching character or string of characters (which will also filter the list to
only show items that match the typed string). Focus handling in the options list
is similar to the default dropdown: focus is only moved to the options list if
an item is already selected, a matching string is entered, or if opened with an
arrow key. Pressing `Esc` will collapse the list or clear the typed string.
Pressing `Enter` will select a highlighted option and collapse the list. (If
nothing is highlighted in the list, pressing `Enter` will toggle the combo box
open and closed.) `Space` cannot be used for selecting, as pressing it will
submit a space character into the filter string.

Combo boxes can be opened with the Enter or Up and Down arrow keys. Enter
selects the highlighted option in the list. Esc clears the input and closes
the combo box.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- The dropdown and multiselect variant use a `button` with
`aria-haspopup="listbox"`.

- Ensure the ID of the referenced label, such as “Access role” in the code
example, is unique when there are multiple dropdown components on a page

- The combo box uses an input with `role="combo box"`,
`aria-autocomplete="list"`, `aria-haspopup="listbox"` and
`autocomplete="off"`.

- The combo box uses `aria-controls` for a div with `role="listbox"`.

- All variants use `aria-expanded` to track the state of the listbox.

- See the
[ARIA authoring practices for combo box](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Dropdown | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Multiselect | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Combo box | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid dropdown | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

| Fluid multiselect | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

| Fluid combo box | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not testedAutomated or manual testing has been temporarily deferred. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)