# Tag – Carbon Design System

Source: https://www.carbondesignsystem.com/components/tag/accessibility/

# Tag

No accessibility annotations are needed for tags, but keep these considerations
in mind if you are modifying Carbon or creating a custom component.

- [What Carbon provides](https://carbondesignsystem.com/components/tag/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/tag/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/tag/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interaction

Read-only tags are not in the tab order, are not interactive, and do not receive
focus.

Dismissible tags are in the tab order and receive focus around the close icon.
Pressing `Enter` or `Space` will dismiss the tag. Tabbing away from the tag will
move focus to the next element in the tab order.

Selectable tags are in the tab order and focus is shown around each tag.
Pressing `Enter` or `Space` toggles the selection on and off.

Operational tags are in the tab order and focus is shown around each tag.
Pressing `Enter` or `Space` will disclose additional related tags.

## Design recommendations

Design annotations are not needed, but keep the following point in mind.

When the tag’s title is too long to fit within the available space of the tag
container, the title can be truncated with an ellipsis. By mouse, the full title
is disclosed in a browser tooltip on hover. By keyboard, the full title is
disclosed on focus in a tooltip. Truncation should be set at the title’s start,
middle, or end, depending on what is best for the given use case.

Truncated tag title disclosed in a tooltip on hover by mouse and on focus by
keyboard.

## Development considerations

Keep this in mind if you’re modifying Carbon or creating a custom component.

- Do not add an `onClick` functionality to the dismissible tag, and only reserve
interactions for the close icon in the tag.

- Do not nest buttons within the operational tag. Consider using the `as` prop
to change an element tag to avoid nesting buttons.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Tag | Default stateTest(s) that ensure the initial render state of a component is accessible. | Not testedAutomated or manual testing has been temporarily deferred. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)