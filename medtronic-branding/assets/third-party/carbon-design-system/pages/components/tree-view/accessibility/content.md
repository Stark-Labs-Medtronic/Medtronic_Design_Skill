# Tree view – Carbon Design System

Source: https://www.carbondesignsystem.com/components/tree-view/accessibility/

# Tree view

No accessibility annotations are needed for a tree view, but keep these
considerations in mind if you are modifying Carbon or creating a custom
component.

- [What Carbon provides](https://carbondesignsystem.com/components/tree-view/accessibility/#what-carbon-provides)

- [Development considerations](https://carbondesignsystem.com/components/tree-view/accessibility/#development-considerations)

## What Carbon provides

Carbon bakes keyboard operation into its components, improving the experience of
blind users and others who operate via the keyboard. Carbon incorporates many
other accessibility considerations, some of which are described below.

### Keyboard interaction

The tree view takes a single tab stop, with focusing landing on the selected
node or the first node of an unselected tree. When trees have focus, arrow keys
provide navigation. The `Right arrow` key expands a closed branch node. If a
branch is open, the `Right arrow` moves into the first child node. Pressing the
`Left arrow` key on an open branch collapses it. Left arrowing on a child moves
the focus to the parent branch. `Up` and `Down arrow` keys move vertically
through open branches and their child nodes. A node or branch is selected by
`Space` or `Enter` keys.

The tree view takes a single tab stop.

Arrow keys operate and move around in the nodes of a tree. Space or Enter
selects the current node.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- The component uses a `tree` role on a `ul` with all nodes in `li` given a role
of `treeitem` with a `tabindex="-1"` and `aria-selected="false"` (except the
currently selected node).

- All branch nodes contain an `aria-expanded` attribute.

- See the
[ARIA authoring practice Tree View pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/)
for more considerations.

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Tree view | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | TestedPasses all automated tests with no reported accessibility violations. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)