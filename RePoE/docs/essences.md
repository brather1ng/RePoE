### `essences.json`

Describes essences. Defines the mods they spawn on items of the different item classes and
general information like level and tier. 

The file is an object where each key is the base item metadata id of an Essence with an object
describing the Essence as a value. The description object has the following fields:

- `name`: The displayed name of the Essence.
- `spawn_level_min`, `spawn_level_max`: The area level range in which "statues" with this
  essence can spawn.
- `level`: The level of the Essence, corresponding to the prefix of its name, e.g.
  "Muttering" or "Screaming". The corruption-only Essences, having no prefix, have level 8.
- `item_level_restriction`: Using the Essence on an item limits its item level to this value
  when selecting the mods that can spawn. If this is `null`, the item level is not restricted.
- `type`: An object containing information that is the same for all Essences of the same type,
  corresponding to the suffix of its name e.g. "Anger" or "Greed". It contains the following
  fields:
  * `tier`: The tier index of the type.
  * `is_corruption_only`: True for types that can only be obtained through corruption using
    an Remnant of Corruption on a "statue" with Essences one tier lower.
- `mods`: An object containing item class ids (see `item_classes.json`) as keys and the
  mod this Essence spawns on items of the given class as values. All Essences have the same
  item classes in this object, except Remnant of Corruption, which has an empty object as
  value of `mods`.

Base item information not specific to Essences, e.g. the visual identity, can be found in
`base_items.json`.
