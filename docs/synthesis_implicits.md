### `synthesis_implicits.json`

Describes which mods can appear on which item classes as implicits through synthesis.

The file is an array. Each element is an object describing one implicit mod combination.
These objects have the following fields:

- `item_classes`: The item classes on which the mods can spawn.
- `mods`: The mods that are part of the implicit mod combination.
- `stat`: An object containing a stat id and value. Their purpose is currently unknown.

See `item_classes.json`, `mods.json` and `stats.json`.
