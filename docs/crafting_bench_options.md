### `crafting_bench_options.json`

Array of objects describing the master craftable mods. Each object has the following
properties:

- `mod_id`: The id of the mod. Use `mods.json` to get more information about the mods.
- `item_classes`: The classes of items the mod can be crafted on. Only non-empty for map
  mods. For other mods, use their `spawn_weights`.
