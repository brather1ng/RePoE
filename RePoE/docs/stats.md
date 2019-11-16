### `stats.json`

Describes stat ids. Defines whether they are local and whether they are aliased
depending on main-hand or off-hand.

For converting stat ids to human-readable translations, see `stat_translations.json`.

The file is an object where each key is a stat id that has its description object
as value. That description object has the following fields:

- `is_local`: True iff the stat is applied locally to the item it is on.
  If false, the stat is global.
- `is_aliased`: True iff the stat is aliased to another stat depending on
  the hand the item it is on is in. Locality is still defined by `is_local`
  on this stat in these cases.
- `alias`: If `is_aliased` is true and the item this stat is on is in main-hand,
  this stat is considered the same as the stat in `when_in_main_hand`.
  If `is_aliased` is true and the item this stat is on is in off-hand,
  this stat is considered the same as the stat in `when_in_off_hand`.
