### `crafting_bench_options.json`

Array of objects describing master crafting options. Each object has the following
properties:

- `item_classes`: The classes of items the mod can be crafted on.
- `master`: Can be Helena, Jun, Navali or Zana. Zana mods are craftable at the Map Device,
  all other at the Crafting Bench. Jun mods are unlocked by unveiling and Navali mods are the
  meta crafting mods that are unlocked by completing the main prophecy chains. All other mods
  have Helena in this property.
- `bench_tier`: The crafting tier/rank as displayed at the Crafting Bench.
- `cost`: The currency it costs to craft this mod. The keys are base item ids. They can be resolved using
  `base_items.json`. The values are the amount of currency of the key's type crafting costs.
- `actions`: An object containing a property for each action on applying the crafting option. At the time of writing
  this, each option has exactly one action. Actions can be the following:
  - `add_mod`: The options adds an explicit mod to the item. The value is he id of the mod. Use `mods.json` to
    get more information about them.
  - `add_enchantment`: The options adds an enchantment mod to the item. The value is he id of the mod. Use `mods.json`
    to get more information about them.
  - `link_sockets`: The option links sockets on the item. The value is the amount of linked sockets.
  - `color_sockets`: The option colors sockets on the item. The value specifies the colors.
  - `change_socket_count`: The option changes the socket count on the item. The value is the amount.
  - `remove_crafted_mods`: The option removes crafted mods from the item. The value is boolean and always true.
