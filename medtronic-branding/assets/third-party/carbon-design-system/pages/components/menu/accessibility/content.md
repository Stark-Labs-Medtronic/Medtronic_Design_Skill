# Menu – Carbon Design System

Source: https://www.carbondesignsystem.com/components/menu/accessibility/

# Menu

No accessibility annotations are needed for menus, but keep these considerations
in mind if you are modifying Carbon or creating a custom component.

- [What Carbon provides](https://carbondesignsystem.com/components/menu/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/menu/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via keyboard. Carbon incorporates many other
accessibility considerations, some of which are described below.

### Keyboard interaction

The menu is reached by `Tab`. When the menu is open, the first item takes focus.
Use the `Up` and `Down` arrow keys to navigate between menu items.

Menu is reached by Tab and when opened, the first menu item takes focus. Arrow
keys move focus.

Pressing `Space` or `Enter` on a focused menu item activates it and collapses
the menu. Pressing `Space` or `Enter` on a submenu opens it. A submenu can also
be opened and closed using the right and left arrow keys respectively. When the
menu or submenu is open, the first item takes focus. An activated menu item can
have different results depending on its functionality. If the item is a link, it
launches the selection. If the item is selectable, it selects or deselects the
item. The menu item retains its selected or unselected state when the menu is
opened again.

Space and Enter keys activates, selects, or deselects the menu item with
focus. A submenu is opened and closed with the right and left arrow keys
respectively.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Each menu, including nested menus, are `ul` elements with `role="menu"`.

- Menu items are `li` elements with `role="menuitem"`.

- If a Menu item contains a sub-menu, it is given `aria-haspopup="true"` and
`aria-expanded` of true or false depending on if the sub-menu is open/visible.

- Selectable menu items are given `role="menuitemcheckbox"`.

- Menu item groups are `li` elements with `role="group"`.

- Menu item radio groups get `role="menuitemradio"`.

- Menu items with really long labels can get truncated depending on the screen
size. This label will be exposed by a browser rendered tooltip on hover or
focus.

- Menu implements the
[menu design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/)
defined in the ARIA Authoring Practices Guide (APG).

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Menu | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Partially testedSome tests are incomplete, in progress, invalid, or temporarily skipped. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)