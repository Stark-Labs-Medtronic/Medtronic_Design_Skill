# Inline loading – Carbon Design System

Source: https://www.carbondesignsystem.com/components/inline-loading/accessibility/

# Inline loading

No accessibility annotations are needed for inline loading components, but keep
these considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/inline-loading/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/inline-loading/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via keyboard. Carbon also incorporates other
accessibility considerations, some of which are described below.

### Keyboard interaction

The inline loading component is not keyboard operable; however, when inline
loading is in an active state, it may temporarily replace or disable an
associated component. For instance, if inline loading is showing the result of a
button action, relevant input controls as well as other actions may be disabled
and inoperable until the loading state changes to either error or complete.

Inline loading components are not interactive, but may temporarily disable
dependent components.

### Labeling and states

Where there is displayed text for inline loading, Carbon provides the text as
the status to assistive technologies like screen readers. Where there is no
text, Carbon provides a text equivalent (“loading”) for the loading symbol.

Inline loading text is provided to assistive technologies.

Where there is no text, Carbon provides a text equivalent for the loading symbol.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Carbon uses an `aria-live` region set to “polite” to surface inline loading
text messages, where they are used.

- Where no text is displayed for inline loading, Carbon uses the SVG title of
the status icon to surface the status (“active”, “finished”, “error”) to
assistive technologies.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Inline loading | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)