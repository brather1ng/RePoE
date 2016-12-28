# RePoE

Repository of Path of Exile resources for tool developers.

Contains information about stat and mod id resolution to supplement the
[unofficial Wiki's API](https://pathofexile.gamepedia.com/api.php). See the `data`
folder for those files.

For the actual GGPK parsing, [PyPoE](https://github.com/OmegaK2/PyPoE) is used.
The code here just converts PyPoE's Python objects to JSON.

Developed to allow [PoESkillTree](https://github.com/EmmittJ/PoESkillTree) full
usage of the Wiki's API, so only information the Wiki's API doesn't contain is extracted
here.

## Files

The `data` folder contains the generated data in Json format. Each file has a nicely
formatted and a compact version. The formatted versions complement the descriptions
below.

### `stat_translations`

Maps stat ids together with their values to human-readable text. This is the text
that appears on items in-game.

The file is an array of translation objects. Each object contains one more stat
ids that are translated together (`ids`) and the translation information (only to
English, `English`). A combination of ids may only appear once.

The translation information is stored in an array under `English`. Each array element
is an object that contains information about when that object is used for translation
in `conditions`. The other fields describe how the translation is formatted.
 
The first array element whose condition applies is used for translation. `conditions`
is an array that contains an element for each id (same applies to the other array
fields). The value of the stat with the ith id is checked against the ith condition.
A condition has the fields `min` and `max`. If `min` is not specified, it is
negative infinity. If `max` is not specified, it is positive infinity. The stat value
`v` matches the condition iff `min <= v <= max`.  The first translation for which
all `conditions` elements match the stat values is used for translation.

Stat values may be a range instead of a single value (e.g. `(10 to 20)`). In that case,
the first condition that matches both values in the range (e.g. 10 and 20) is taken.
If no condition matches both values, the first condition that matches at least one
value is taken.

If no translation matches the values, it is not displayed. If the combination of stat
ids has no entry, it is not displayed. If the stat ids only have entries with more
that have more ids ("partial" matches), the values for missing ids are set to 0. If
all values are 0, the stats are not displayed.

If the entry for the ids has the field `hidden` set to `true`, the translation is not
actually displayed in in-game tooltips (e.g. the implicit movement speed penalties
on body armours and shield). The Wiki suffixes these with " (Hidden)", for example.
These ids were manually translated in PyPoE.

Once the correct translation entry matching the stat ids and values is found, the text
can be created with the information found in the fields `string`, `formats` and
`index_handlers`. Values are inserted into `string` by replacing `{i}` entries with
them. `i` references the value of the stat id with the (zero-based) index `i`. Before
being inserted, they may be modified. How is defined in `formats` and `index_handlers`.

`formats` define the value formatting:

- `#`: value is inserted unchanged
- `+#`: value is prepended with a '+' character, iff the value (or all values if the
  stat value is a range) is (are) positive
- `#%`: a '%' character is appended after the value
- `ignored`: the value is not referenced in the format string

Range values are inserted as `(value1 to value2)`. If both values of the range are
negative, the '-' character is moved outside the parentheses (e.g. `(-20, -10)` is
formatted as `-(20 to 10)`). 

`index_handlers` are applied to values before formatting. These change the actual
values, see `PyPoE.poe.file.translations`, line 861ff, for their Python definitions.
If, for example, `divide_by_one_hundred` is a handler for a value, the value must
be divided by 100 before being formatted.

### `mods`

Describes mod ids. Defines which items they can appear on and what stats with what
values they have.

The file is an object where each key is a mod id that has its description object
as value. That description object has the following fields:

- `buff`: The stats of this mod may be applied to allies or enemies around the mod
  carrier. If they are, this field contains the buff id (resolved in `Buffs.dat`)
  and the range the buff is applied. If the range is 0 and the buff is applied to
  allies, it only affects the carrier. The buff referenced by the id specifies
  the stats of this mod that are applied to others and some information for
  display purposes.
- `domain`: The domain this mod appears on. Can be `wearable_item` (body armour,
  weapons, shields, jewellery, etc.), `flask`, `monster`, `chest` (chests and
  strongboxes), `area` (maps and other areas), `monster_behaviour`, `master_crafted`,
  `jewel` or `sextant`.
- `generation_type`: How this mod is generated. Can be `prefix`, `suffix`, `other`
  (e.g. unique explicits, base item implicits or prophecies), `item_corruption`,
  `item_enchantment`, `map_tempest`, `monster_nemesis`, `monster_bloodlines`,
  `monster_torment`, `monster_talisman` or `monster_essence`.
- `group`: Some kind of mod grouping, see the file for examples. For normally spawnable
  mods, only one mod of a group can appear on an item at the same time.
- `is_essence_only`: True iff the mod can only be generated by essences.
- `level`: The level requirement of the mod.
- `name`: The display name of the mod in case of "normally" spawnable mods (Prefixes
  and Suffixes).
  Can be an empty string or some other string in case it is never seen (can't appear
  on magic items).
- `spawns_on`: Defines on which items of the domain this mod can be spawned/crafted
  on. Only contains elements for mods that appear "normally", e.g. not for
  master crafted mods or essences. The array elements are evaluated in order,
  the first element that has a tag as a key that the item in question has is taken.
  If the object with that tag as key has `true` as value, the mod can spawn on the
  item. If it has `false` as value, the mod can not spawn. *This might actually
  not be true but seems to be correct for the mods I checked.* The mod
  `AddedChaosDamageCorrupted1`, for example, has `"no_attack_mods": false`,
  `"ring": true` and `"default": false`. It can therefore spawn on items that do
  not have Catarina's "Cannot roll Attack Mods" mod and are rings, but not on
  any other item.
- `stats`: Array of the stats this mod gives. `id` is the stat id and `min` and `max`
  (both inclusive) define the range the stat can roll. These can be converted to
  text with the help of `stat_translations.json` (see above).

Mods of the domains 'monster', 'chest', 'area', 'monster_behaviour' and 'sextant' are
not included. These are not necessary for my use cases atm and would nearly double
the file size.
