### `fossils.json`

Describes fossils. Defines which items they can appear on and what tags they change

The file is an object where each key is a fossil id that has its description object
as value. That description object has the following fields:

**Mod and Tag Effects**
- `added_mods`: Gives the ids of the mods which are added to the pool of available mods
  with this fossil
- `forced_mods`: Gives the ids of the mods which are forced to spawn (like an essence) with
  this fossil
- `negative_mod_weights`: List of objects which detail both the tags and the multiplicative
  weights on those tags. When rolling, this affects a mod by looking at the tags in
  `mod["adds_tags"]`.
- `positive_mod_weights`: Same as `negative_mod_weights` but affects weights positively.
- `forbidden_tags`: List of tags which restrict the use of the fossil. Fossil can only be used
  on items which don't have any of listed tags
- `allowed_tags`: List of tags which restrict the use of the fossil. Fossil can only be used on
  items which have at least one listed tag.
- `sell_price_mods`: List of mod ids of which one is picked as an implicit. Only used for
  gilded fossil currently.

**Miscellaneous Effects**
- `corrupted_essence_chance`: Gives the chance the game forces a random corrupted essence
  modifier on the item.
- `mirrors`: Boolean indicating whether the fossil mirrors the item.
- `changes_quality`: Boolean indicating whether the fossil rerolls the quality of the item
  randomly from 15 to 30.
- `rolls_lucky`: Boolean indicating whether the numeric values in the mods are rolled lucky
  (rolled twice, keep better roll).
- `enchants`: Boolean indicating whether or not the fossil applies a random enchant to the
  item (not sure on distribution for different labs).
- `rolls_white_sockets`: Boolean indicating whether or not the fossil rerolls the colors with
  a chance of white socket (not sure on distribution).

**Descriptions**
- `name`: The name of the fossil as found in the `base_items` entry.
- `descriptions`: List of descriptions for the fossil.
- `blocked_descriptions`: List of descriptions blocked by the fossil. This is purely aesthetic
  (e.g. No mana + More mana only shows up as No mana).

See `tags.json` for the possible tags, though not all of those are relevant for fossils.
See `mods.json` for the possible mods, though not all of these are relevant for fossils.
