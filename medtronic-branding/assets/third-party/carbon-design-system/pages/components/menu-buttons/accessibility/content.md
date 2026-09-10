# Menu buttons – Carbon Design System

Source: https://www.carbondesignsystem.com/components/menu-buttons/accessibility/

# Menu buttons

Design annotations are needed for specific instances shown below, but for the
standard menu button, combo button, and overflow menu, Carbon already
incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/menu-buttons/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/menu-buttons/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/menu-buttons/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via keyboard. Carbon incorporates other
accessibility considerations, some of which are described below.

### Keyboard interaction

#### Menu button

The menu button is set in the tab order and is activated by `Space` or `Enter`.
When the menu is open, the first item takes focus. Focus is moved between menu
items with the `Up` and `Down` arrow keys. `Space` or `Enter` activates the item
with focus, which causes focus to go somewhere else and the menu to close. `Esc`
collapses the menu and puts focus back onto the menu button.

Menu button is reached by Tab. Space and Enter keys open the menu as well as
activating menu items with focus.

When opened, the first item in the menu takes focus. Arrow keys move focus and
Esc closes the menu.

#### Combo button

The combo button is set in the tab order where the first tab brings focus on the
primary button and the second tab brings focus on the icon button that contains
the menu. The respective buttons are activated by `Space` or `Enter`. When the
menu is open, the first item takes focus. Focus is moved between menu items with
the `Up` and `Down` arrow keys. `Space` or `Enter` activates the item with
focus, which causes focus to go somewhere else and the menu to close. `Esc`
collapses the menu and puts focus back onto the icon button.

Combo button items are reached by two Tab stops. Space and Enter keys open the
menu as well as activating menu items with focus.

When opened, the first item in the menu takes focus. Arrow keys move focus and
Esc closes the menu.

#### Overflow menu

Each overflow menu is in the tab order and is activated by `Space` or `Enter`.
When the menu is open, the first item takes focus. Focus is moved between menu
items with the `Up` and `Down` arrow keys. `Space` or `Enter` activates the item
with focus, which causes focus to go somewhere else and the menu to close. `Esc`
collapses the menu and puts focus onto the menu button.

Overflow menus are reached by Tab. Space and Enter keys open the menu as well
as activating menu items with focus.

When opened, the first item in the menu takes focus. Arrow keys move focus and
Esc closes the menu.

## Design recommendations

Design annotations are needed for the following instances.

### Labeling

#### Combo button

Combo button has a prop that can be used to change the tooltip label and is only
intended to be changed to translate _“Additional actions”_ into other languages.
If translation is required, the translation must be annotated with a label that
is exposed on hover or focus.

Annotate the label for combo button so the proper tooltip appears, which
should only be used for translation purposes.

#### Overflow menu

Overflow menu’s
[custom icon variant](https://react.carbondesignsystem.com/?path=/story/components-overflowmenu--render-custom-icon)
has a prop that can be used to change the tooltip label. If the tooltip label is
changed, they must be annotated with a label that will be exposed on hover or
focus.

Annotate the label for overflow menu’s custom icon variant so the proper
tooltip appears.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Menu button, combo button, and the overflow menu are buttons with
`aria-haspopup` set to “true”.

- The menu button, combo button, and the overflow menu is named with
`aria-label`.

- Each menu item across menu button, combo button, and overflow menu is an `li`
in a `ul`.

- Each list item across menu button, combo button, and overflow menu contains a
button with `role="menuitem"` and `tabindex="-1"`. See the
[ARIA authoring practices on menubutton](https://w3c.github.io/aria-practices/#menubutton)
for more considerations.

- Combo button and overflow menu has an `iconDescription` prop that can be used
to change the tooltip label. See the
[design recommendations](https://carbondesignsystem.com/components/menu-buttons/accessibility/#design-recommendations) for more guidelines on
tooltip labels.

- For combo button, the menu is given an `id`. When the menu is open, the icon
button is given `aria-controls` with a value of the menu `id`. `aria-expanded`
is also set based on the open state.

- When the combo button menu is open, the element (`div`) wrapping the entire
combo button is given `aria-owns` with a value of the menu `id`.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Menu button | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Combo button | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

| Overflow menu | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)