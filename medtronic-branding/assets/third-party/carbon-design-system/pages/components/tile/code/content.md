# Tile – Carbon Design System

Source: https://www.carbondesignsystem.com/components/tile/code/

# Tile

Preview the tile component with the React live demo. For detailed code usage
documentation, see the Storybooks for each framework below.

## Documentation

### Feature flags

[Feature flags](https://carbondesignsystem.com/components/overview/feature-flags/) have been added to the
clickable, selectable, and expandable variants of tile to improve accessibility
and changes its visual appearance, not its functionality. For more code-specific
feature flag information, refer to the
[@carbon/react](https://react.carbondesignsystem.com/?path=/docs/components-tile-feature-flag--flag-details)
framework. Once the next major release (v12) is released in the future, these
feature flags will become the default version of the component.

- The `enable-tile-contrast` flag adds a border to the tile with improved
contrast for accessibility and to visually indicate they are operable.

- The `enable-v12-tile-default-icons` flag enables the rendering of default
icons on the clickable variant of a tile, such as the ArrowRight icon for
navigation or the Error icon when the tile is disabled. If the user hasn’t
configured a different icon, these defaults will be used.

- The `enable-v12-tile-radio-icons` flag changes RadioTile to use radio button
icons instead of a checkmark icons.

## Live demo

This live demo contains only a preview of functionality and styles available for this component. View the [full demo](https://react.carbondesignsystem.com/?path=/story/components-tile--default&globals=theme:white) on Storybook for additional information such as its version, controls, and API documentation.