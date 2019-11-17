### `crafting_bench_options.json`

Array of objects describing the master craftable mods. Each object has the following
properties:

- `mod_id`: The id of the mod. Use `mods.json` to get more information about the mods.
- `item_classes`: The classes of items the mod can be crafted on.
- `master`: Can be Helena, Jun, Navali or Zana. Zana mods are craftable at the Map Device,
  all other at the Crafting Bench. Jun mods are unlocked by unveiling and Navali mods are the
  meta crafting mods that are unlocked by completing the main prophecy chains. All other mods
  have Helena in this property.
- `bench_group`: Mods with the same value are placed into the same drop-down at the
  Crafting Bench.
- `bench_tier`: The crafting tier/rank as displayed at the Crafting Bench.
- `cost`: The currency it costs to craft this mod. The keys are base item ids. They can be resolved using
  `base_items.json`. The values are the amount of currency of the key's type crafting costs.
