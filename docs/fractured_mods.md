### `fractured_mods.json`

Describes which mods can appear on which item classes as fractured explicits.

The file is an array. Each element is an object describing one fractured mod combination.
These objects have the following fields:

- `item_classes`: The item classes on which the fractured mods can spawn.
- `mods`: The mods that are part of the fractured mod combination.
- `stat`: An object containing a stat id and value. Their purpose is currently unknown.

See `item_classes.json`, `mods.json` and `stats.json`.
