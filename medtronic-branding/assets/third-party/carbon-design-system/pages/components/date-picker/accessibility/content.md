# Date picker – Carbon Design System

Source: https://www.carbondesignsystem.com/components/date-picker/accessibility/

# Date picker

No accessibility annotations are needed for date pickers, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [Accessibility considerations](https://carbondesignsystem.com/components/date-picker/accessibility/#accessibility-considerations)

- [Resources](https://carbondesignsystem.com/components/date-picker/accessibility/#resources)

- [Accessibility testing](https://carbondesignsystem.com/components/date-picker/accessibility/#accessibility-testing)

## Accessibility considerations

1. The date picker labels should clearly describe the dates that the user needs
to input, such as arrival date or departure date when making travel
arrangements.

## Resources

- [W3C WAI-ARIA Authoring Practices Date Picker Design Pattern](https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/datepicker-dialog.html)
covers the usage of ARIA names, state and roles, as well as the expected
keyboard interactions.

- [IBM Accessibility Requirements](https://www.ibm.com/able/requirements/requirements/):

[1.3.1 Info and Relationships](https://www.ibm.com/able/requirements/requirements/#1_3_1)
(WCAG Success Criteria
[1.3.1](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships))
[1.3.2 Meaningful Sequence](https://www.ibm.com/able/requirements/requirements/#1_3_2)
(WCAG Success Criteria
[1.3.2](https://www.w3.org/WAI/WCAG21/Understanding/meaningful-sequence))
[2.1.1 Keyboard](https://www.ibm.com/able/requirements/requirements/#2_1_1)
(WCAG Success Criteria
[2.1.1](https://www.w3.org/WAI/WCAG21/Understanding/keyboard))
[2.1.2 No Keyboard Trap](https://www.ibm.com/able/requirements/requirements/#2_1_2)
(WCAG Success Criteria
[2.1.2](https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap))
[2.4.3 Focus Order](https://www.ibm.com/able/requirements/requirements/#2_4_3)
(WCAG Success Criteria
[2.4.3](https://www.w3.org/WAI/WCAG21/Understanding/focus-order))
[2.4.6 Headings and Labels](https://www.ibm.com/able/requirements/requirements/#2_4_6)
(WCAG Success Criteria
[2.4.6](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels))
[2.4.7 Focus Visible](https://www.ibm.com/able/requirements/requirements/#2_4_7)
(WCAG Success Criteria
[2.4.7](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible))
[4.1.2 Name, Role, Value](https://www.ibm.com/able/requirements/requirements/#4_1_2)
(WCAG Success Criteria
[4.1.2](https://www.w3.org/TR/UNDERSTANDING-WCAG20/ensure-compat-rsv.html))

## Accessibility testing

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Date picker | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid date picker | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)