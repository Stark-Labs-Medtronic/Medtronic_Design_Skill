# Remove – Carbon Design System

Source: https://www.carbondesignsystem.com/community/patterns/remove-pattern/

# Remove

#### Maintainer:

[Vikki Paterson](https://github.com/vikkipaterson)

“Removing” is an action that moves information from one location to another.
Removal can be both destructive and non-destructive. “Deletion” is the most
common type of removal and is destructive.

- [High-impact deletion](https://carbondesignsystem.com/community/patterns/remove-pattern/#high-impact-deletion)

- [Medium-impact deletion](https://carbondesignsystem.com/community/patterns/remove-pattern/#medium-impact-deletion)

- [Low-impact deletion](https://carbondesignsystem.com/community/patterns/remove-pattern/#low-impact-deletion)

- [Medium-impact removal](https://carbondesignsystem.com/community/patterns/remove-pattern/#medium-impact-removal)

- [Low-impact removal](https://carbondesignsystem.com/community/patterns/remove-pattern/#low-impact-removal)

- [Anatomy](https://carbondesignsystem.com/community/patterns/remove-pattern/#anatomy)

### Delete / Remove variations

| Action | Variation | Description |

| --- | --- | --- |

| Delete | High impact | Action can’t be reversed and causes significant loss. The user types the resource name into the modal to confirm deletion. |

|  | Medium impact | Action can’t be reversed and causes some loss. The user sees a modal and confirms the consequence of deletion. |

|  | Low impact | Action is reversible or very low impact. A confirmation modal may not be required. |

| Remove | Medium impact | Action can’t be reversed and causes some loss. The user sees a modal and confirms the consequence of removal. |

|  | Low impact | Action is reversible or very low impact. A confirmation modal may not be required. |

## High-impact deletion

A high-impact deletion cannot be reversed. The action would result in a
significant loss for a user if done accidentally.

When deleting is high-impact, a confirmation dialog should be presented to the
user which displays:

- The name of the resource

- Consequences of the deletion

- This action cannot be undone.

- An editable text field for the name of the resource to be entered

For high-impact scenarios, a user should confirm the action by manually entering
the name of the resource. The ‘Delete’ button is enabled when the text entered
perfectly matches the resource name.

Optionally a [Done modal](https://carbondesignsystem.com/community/patterns/remove-pattern/#done-modal), [Requested modal](https://carbondesignsystem.com/community/patterns/remove-pattern/#requested-modal) or
[Notification](https://carbondesignsystem.com/community/patterns/remove-pattern/#notification) can be used to confirm the action (or a
combination of one modal and a notification).

The user needs to enter the resource name in order to confirm deletion.

When the resource name is entered the Delete button is enabled.

## Medium-impact deletion

A medium-impact deletion is one that cannot be reversed, but would not be
catastrophic if done accidentally. When deleting is medium-impact, a
confirmation dialog should be presented to the user which displays:

- The name of the resource

- Consequences of the deletion

- The action cannot be undone.

Optionally an [Optional passive modal](https://carbondesignsystem.com/community/patterns/remove-pattern/#optional-passive-modal) or
[Notification](https://carbondesignsystem.com/community/patterns/remove-pattern/#notification) can be used to confirm the action (or a
combination of one modal and a notification).

An example of a standard delete modal

## Low-impact deletion

Requiring the user to confirm deletion is generally recommended. However, in low
impact situations, or when an ‘undo’ option is available, user confirmation may
not be required.

Low impact delete options

Low impact delete options requiring overrides to Carbon

## Medium-impact removal

Removing has a medium impact when the action can’t be reversed, and could have
some impact if done accidentally.

Text should tell the user the consequences of the removal and that the action
cannot be undone.

Removal modals should include consequences of removal, and “This action cannot
be undone” statement.

## Low-impact removal

As removing does not destroy an asset, typically user confirmation is not
required.

Example low impact remove options

Low impact remove options requiring overrides to Carbon.

## Anatomy

### Optional passive modal

In high or medium impact flows, an optional passive modal can be used to signify
the state at the end of a remove or delete action. Some deletion or removal
actions don’t happen immediately, in these situations it’s recommended to inform
the user through the optional passive modal.

Use a success modal to show that a delete request has been made / is in progress.

Use a success modal to show that removing is complete.

### Notification

An optional notification can be used to confirm a delete or remove action has
completed. This is useful when the action takes more than a few moments.

An optional notification can be used to confirm the delete or remove action with
medium or high impact actions.