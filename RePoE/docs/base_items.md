### `base_items.json`

Describes base item types. Contains information applicable to all item types, e.g. inventory
size, item class and tags, as well as attribute requirements and properties.

Only bases for equippable items (weapons, armor, jewellery, jewels, flasks, ...), currency and
gems are included. For the exact included item classes, see the whitelist at
[`RePoE.base_items.ITEM_CLASS_WHITELIST`](https://github.com/brather1ng/RePoE/blob/master/RePoE/base_items.py#L93). 

Properties specific to skill gems and essences are not included. See `gems.json` and 
`gem_tooltips.json` for skill gems and `essences.json` for essences.

The file is an object where each key is the metadata id of a base item with an object describing
the base item as a value. The description object has the following fields:

- `drop_level`: The minimum item level at which the base drops.
- `implicits`: An array of the mod ids of the implicit modifiers of the base item. More
  information about the mods can be found in `mods.json`, the mod ids are the keys in that file.
- `inventory_height`: The amount of grid cells items of the base take up vertically.
- `inventory_width`: The amount of grid cells items of the base take up horizontally.
- `item_class`: The item class id of the base.
- `name`: The name under which items of the base are displayed in-game.
- `release_state`: In what state that item is currently in-game. See
  [`RePoE.parser.constants.ReleaseState`](https://github.com/brather1ng/RePoE/blob/master/RePoE/constants.py#L173)
  for possible values and their meaning.
- `tags`: The tags all items of the base have. This determines the mods that can spawn on items
  of this base and allows for classification beyond just `item_class`.
  See `tags.json` for the possible tags, though not all of those appear on item bases.
- `visual_identity`: An object describing how items of this base are normally displayed in-game.
  * `id`: The id of the referenced visual identity in `ItemVisualIdentity.dat`.
  * `dds_file`: The path to the item's 2D-Art file.
- `requirements`: An object containing the requirements to be able to equip the base items.
  The object is either `null` (the base has no requirements from itself) or contains
  the fields `strength`, `dexterity`, `intelligence` and `level`.
  The requirements are only base requirements. They may be modified by implicit/explicit
  modifiers (the level upwards to 80% of the highest mod level requirement, the attributes
  in either direction) or by socketed gems (upwards).
  If present, `level` is identical to `drop_level`.
- `properties`: An object describing the properties of the base. The properties vary from
  item to item, generally based on the base's item class.
  * `armour`, `evasion`, `energy_shield`: The base Armour, Evasion and Energy Shield values
    provided by this base.
  * `movement_speed`: The implicit movement speed increase provided by this base.
  * `block`: The base chance to block as percentage provided by this base.
  * `life_per_use`, `mana_per_use`: The base amount of life/mana recovered by this flask.
  * `duration`, `charges_max`, `charges_per_use`: The base duration, base maximum amount of
    charges and base amount of charges used per use of this flask.
  * `critical_strike_chance`: The base critical strike chance of this weapon.
    Divide this value by 100 to get the chance as percentage.
  * `attack_time`: The base attack time of this weapon in ms. Divide 1000 by this value to get
    the attacks per second.
  * `physical_damage_max`, `physical_damage_min`: The base maximum and minimum physical damage
    dealt by this weapon.
  * `range`: The base maximum range of this weapon.
  * `stack_size`, `stack_size_currency_tab`: The normal and currency tab stack size of this
    currency.
  * `directions`, `description`: Usage directions and description of this currency.
  * `full_stack_turns_into`: The base item this currency turns into when its `stack_size` is
    reached.
- `grants_buff`: An object describing the buff provided by this flask.
  - `id`: The provided buff's id (resolved in `BuffDefinitions.dat`).
  - `stats`: An object with the stats (their ids) provided by the buff as keys and the
     stat values as values.
- `domain`: The domain of this item. Only mods with the same domain can regularly spawn
  on the item. Things like crafted mods, corruptions or delve mods have their own domains
  and are not affected by this. See 
  [`PyPoE.poe.constants.MOD_DOMAIN`](http://omegak2.net/poe/PyPoE/_autosummary/PyPoE.poe.constants.html#PyPoE.poe.constants.MOD_DOMAIN)
  for the possible values and explanation.
