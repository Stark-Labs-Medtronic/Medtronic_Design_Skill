# Form – Carbon Design System

Source: https://www.carbondesignsystem.com/components/form/accessibility/

# Form

Design annotations are needed for specific instances shown below, but Carbon
already incorporates accessibility into the components that make up a form.
Refer to form components’ individual accessibility tabs for specific
considerations.

- [What Carbon provides](https://carbondesignsystem.com/components/form/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/form/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/form/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into the components that make up a form,
improving the experience of blind users and others who operate via the keyboard.
Carbon incorporates many other accessibility considerations, some of which are
described below.

### Information icons

A common challenge for forms is how to surface additional information to the
user without making the form too dense. Carbon provides an information icon
[toggletip](https://carbondesignsystem.com/components/toggletip/usage) to ensure such information is
predictable and keyboard accessible. The toggletip is a button, which is in the
tab order. Both `Space` and `Enter` open the tip, and `Esc` dismisses it.

The toggletip pattern is used to make form help text keyboard accessible.

### Error handling

Carbon incorporates accessible inline error and warning messages into many
components, such as text inputs. Error states are also conveyed programmatically
to assistive technologies.

## Design recommendations

Design annotations and considerations are needed for the following situations.

### Identify requirements at the start of the form

Traditionally, a legend at the start of a form identifies the symbol (often an
asterisk) used for required fields, and the symbol is repeated as part of the
label for each appropriate field. This is still considered the most accessible
implementation. However, as discussed in
[Optional versus required fields](https://carbondesignsystem.com/components/form/usage/#optional-versus-required-fields),
Carbon allows for either the required or optional fields to be the inputs
identified. Especially where only optional fields are indicated, an instruction
should precede a form, providing the context for whether required or optional
fields are indicated. The traditional phrasing is “All fields are required
unless marked as optional” (or the reverse). See the Equal Access Toolkit topic
[Required fields](https://www.ibm.com/able/toolkit/design/visual/#required-fields)
for more information.

By convention, simple username/password login forms do not need such an
instruction (or even to be marked as required), since the context is clear to
users.

### Be familiar with the accessibility of common form components

The following topics each have their own accessibility considerations, which
improve the overall form experience:

- [Checkbox](https://carbondesignsystem.com/components/checkbox/accessibility)

- [Date picker](https://carbondesignsystem.com/components/date-picker/accessibility)

- [Dropdown](https://carbondesignsystem.com/components/dropdown/accessibility)

- [File uploader](https://carbondesignsystem.com/components/file-uploader/accessibility)

- [Loading](https://carbondesignsystem.com/components/loading/accessibility)

- [Modal](https://carbondesignsystem.com/components/modal/accessibility)

- [Notification](https://carbondesignsystem.com/components/notification/accessibility)

- [Number input](https://carbondesignsystem.com/components/number-input/accessibility)

- [Radio button](https://carbondesignsystem.com/components/radio-button/accessibility)

- [Select](https://carbondesignsystem.com/components/select/accessibility)

- [Slider](https://carbondesignsystem.com/components/slider/accessibility)

- [Text input](https://carbondesignsystem.com/components/text-input/accessibility)

## Development considerations

Keep these considerations in mind if you are modifying Carbon patterns or
creating a custom form or input component.

- A form must be wrapped in a `<form>` element.

- Required fields must be identified programmatically, either via the label or
with `aria-required`.

- Remember to supply an `aria-label`, `aria-labelledby` or `title` to the
component to comply with
[accessible naming](https://able.ibm.com/rules/archives/latest/doc/en-US/aria_accessiblename_exists.html)

- Helper text and other instructions should be surfaced to users via
`aria-describedby` or other accessible techniques. See
[Programmatically associate inputs with labels](https://www.ibm.com/able/toolkit/develop/user-input/#inputs).

- See the ARIA authoring practices on
[forms](https://w3c.github.io/aria-practices/#aria_lh_form) and
[labels](https://w3c.github.io/aria-practices/#naming_with_labels) for more
considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Form | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Form group | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Form label | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Fluid form | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Not availableTest data is either not available or not applicable for this component state. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)