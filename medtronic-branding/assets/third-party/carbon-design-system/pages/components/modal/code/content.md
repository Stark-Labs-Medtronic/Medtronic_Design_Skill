# Modal – Carbon Design System

Source: https://www.carbondesignsystem.com/components/modal/code/

# Modal

Preview the modal component with the React live demo. For detailed code usage
documentation, see the Storybooks for each framework below.

## Documentation

### Feature flags

A [feature flag](https://carbondesignsystem.com/components/overview/feature-flags/) has been added to modal to
improve accessibility and changes parts of its functionality, not its visual
appearance. For more code-specific feature flag information, refer to the
[@carbon/react](https://react.carbondesignsystem.com/?path=/docs/components-modal-feature-flag--flag-details)
framework. Once the next major release (v12) is released in the future, this
feature flag will become the default version of the component.

The `enable-focus-wrap-without-sentinels` flag is a new approach to focus wrap
behavior, modifying the DOM to no longer include hidden “sentinel nodes” that
previously marked the beginning and end of the wrapped focus. This behavior
considers all interactive child nodes and wraps focus based on their tab order.

## Live demo

This live demo contains only a preview of functionality and styles available for this component. View the [full demo](https://react.carbondesignsystem.com/?path=/story/components-modal--default&globals=theme:white) on Storybook for additional information such as its version, controls, and API documentation.