# Code snippet – Carbon Design System

Source: https://www.carbondesignsystem.com/components/code-snippet/accessibility/

# Code snippet

No accessibility annotations are needed for code snippets, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/code-snippet/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/code-snippet/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, as well as many other
accessibility considerations.

### Keyboard interaction

For all three variants, the code snippet can be copied with `Space` or `Enter`.
Arrow keys can operate scroll bars.

By default, each inline code snippet is reachable by `Tab` and copied with
`Space` or `Enter`.

The single line code snippet tabstop supports left and right arrow key
scrolling.

The multi-line’s buttons are reachable by `Tab` and activated with `Space` or
`Enter`.

### Labeling and updates

Carbon provides the copy button’s default label and tooltip behavior. Carbon
handles notices about the success of the copy function, as well as updates to
the Show more mechanism.

The code snippet’s buttons expose their labels on hover or focus.

The results of activating buttons are provided in text.

## Development considerations

Keep this in mind if you are modifying Carbon or creating a custom component:

- the inline code text is implemented as a button so its text can be copied

- single line snippets take an additional tabstop to support arrow key scrolling

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Code snippet | Default stateTest(s) that ensure the initial render state of a component is accessible. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)