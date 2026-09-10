# Button – Carbon Design System

Source: https://www.carbondesignsystem.com/components/button/accessibility/

# Button

Design annotations are needed for specific instances shown below, but for the
standard button component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/button/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/button/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/button/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interactions

Buttons can be reached by `Tab` and selected with `Space` or `Enter`.

Carbon buttons retain expected interactions.

### Behavior

Icon-only buttons, which do not persistently display a text label, expose their
label on hover and focus. When icon-only buttons are used to open menus, they
are treated as separate components in Carbon. See
[Dropdown](https://carbondesignsystem.com/components/dropdown/usage/) and
[Overflow menu](https://carbondesignsystem.com/components/overflow-menu/usage/).

Icon-only buttons have their labels exposed automatically on hover and focus.

Buttons that open menus are separate components in Carbon.

## Design recommendations

Design annotations are needed for the following instances.

### Labeling

When buttons do not have a persistently displayed label, they must be annotated
with a label that will be exposed on hover or focus.

Annotate the label for icon-only buttons so the proper tooltip appears.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component:

- Where links have been ‘repurposed’ as a button, they need to be coded so the
`Space` key can also activate (since links are only activated by default by
`Enter`).

- Toggle buttons can be accessibility supported by changing the value of
`aria-pressed` between `"true"` and `"false"` or with a change of name that
reflects a change in the icon shape (for example: “play” / “pause” )

- See the
[ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.2/#button)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Button | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)