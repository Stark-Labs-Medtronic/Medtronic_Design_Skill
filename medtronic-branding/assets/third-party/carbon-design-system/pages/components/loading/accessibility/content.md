# Loading – Carbon Design System

Source: https://www.carbondesignsystem.com/components/loading/accessibility/

# Loading

Design annotations are needed for specific instances shown below, but for the
standard loading component, Carbon already incorporates accessibility.

- [What Carbon provides](https://carbondesignsystem.com/components/loading/accessibility/#what-carbon-provides)

- [Design recommendations](https://carbondesignsystem.com/components/loading/accessibility/#design-recommendations)

- [Development considerations](https://carbondesignsystem.com/components/loading/accessibility/#development-considerations)

## What Carbon provides

The loading component has no keyboard accessibility considerations since it is
intentionally not operable or navigable. However, Carbon incorporates other
accessibility considerations, some of which are described below.

### Status updates

The primary accessibility consideration for the loading component is to convey
its meaning to assistive technologies so users are aware of changes in status.
Carbon achieves this by exposing the `title` value (normally “loading”) of the
spinning wheel SVG image.

Screen readers hear “loading” when a spinning icon appears on the screen.

## Design recommendations

Design annotations are needed for the following instance.

### Convey when loading has completed

When the loading indicator disappears, it conveys a second meaning, which is
‘not loading’ or ‘finished’. However, especially where loads may take more than
a few seconds, a user who cannot see the icon disappear needs to be made aware
the system is no longer “loading” and is thus available for usage.

There are several ways to do this. If new content takes focus when the loading
is completed (for instance after a full page load), then users will understand
the system is now available. Annotating what component takes focus will ensure
this is properly implemented.

Annotate if a control takes focus after a loading completes.

Where a change of focus is not appropriate when the loading icon disappears, the
information can be surfaced to users through a non-displayed status message,
such as “finished” or “loading complete,” that can be conveyed to users through
assistive technology.

Annotate the information that developers need to convey programmatically to
assistive technology.

## Development considerations

Keep these considerations in mind if you are modifying Carbon or creating a
custom component.

- Carbon uses `aria-live` set to “assertive” to immediately surface a loading
status to assistive technologies.

- Carbon provides an SVG `title` value for the loading icon, which is exposed
through the `aria-live` section.

- The completion of the loading state should be conveyed to assistive
technologies. A non-visible status message such as “loading complete” could be
put in the `aria-live` section or exposed through a `role="status"`.
Alternatively, focus could be set to an appropriate element.

- See the Equal Access Toolkit information on
[status messages](https://www.ibm.com/able/toolkit/develop/dynamic-updates/#role-status).

### Accessibility testing statusFor every latest release, Carbon runs tests on all components to meet the accessibility requirements. These different statuses report the work that Carbon has done in the back end. These tests appear only when the components are stable.

**Latest version:**  | **Framework:** React (@carbon/react)

| Component | Accessibility test | Status | Link to source code |

| --- | --- | --- | --- |

| Loading | Default stateTest(s) that ensure the initial render state of a component is accessible. | TestedPasses all automated tests with no reported accessibility violations. | GitHub link |

|  | Advanced statesTests that ensure additional states of the component are accessible. This could be interactive states of a component or its multiple variants. | Not testedAutomated or manual testing has been temporarily deferred. |  |

|  | Keyboard navigationTests that ensure focus is properly managed, and all interactive functions of a component have a proper keyboard-accessible equivalent. | Not availableTest data is either not available or not applicable for this component state. |  |

|  | Screen readerThis manual testing ensures that the visual information on the screen is properly conveyed and read correctly by screen readers such as JAWS, VoiceOver, and NVDA. | Manually testedA human has manually tested this component, e.g. screen reader testing. |  |

[Learn more about tag and test meaning](https://carbondesignsystem.com/components/overview/accessibility-status)
[View all component accessibility status](https://carbondesignsystem.com/components/overview/accessibility-status#all-component-accessibility-status-anchor)