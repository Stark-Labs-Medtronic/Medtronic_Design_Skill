# List – Carbon Design System

Source: https://www.carbondesignsystem.com/components/list/accessibility/

# List

No accessibility annotations are needed for lists, but keep these considerations
in mind if you are modifying Carbon or creating a custom component.

- [What Carbon provides](https://carbondesignsystem.com/components/list/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/list/accessibility/#development-considerations)

## What Carbon provides

Carbon incorporates many accessibility considerations, some of which are
described below.

### Keyboard interaction

Lists are not keyboard operable, unless the list items themselves are operable.
In such a situation, the list items will retain the component’s default keyboard
interaction. For example, in a list of links, each
[link](https://carbondesignsystem.com/components/link/usage) will be in the tab
order and can be activated by `Enter`.

## Development considerations

Keep this in mind if you’re modifying Carbon or creating a custom component:

- Carbon uses native
[HTML](https://www.w3.org/WAI/tutorials/page-structure/content/#lists)
unordered (`ul`) and ordered (`ol`) lists and list items (`li`), then styles
them with CSS.

- Carbon uses `::before` and `::marker` CSS pseudo-elements for the numbering
and bulleting of lists, which are properly read by assistive technologies such
as [screen readers](https://www.ibm.com/able/toolkit/verify/screen-reader/).

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Unordered list | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Ordered list | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)