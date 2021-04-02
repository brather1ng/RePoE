### `stat_translations.json`

Maps stat ids together with their values to human-readable text. This is the text
that appears on items in-game. 

The file only completely covers equipment item stats (everything but chest, gem, 
area, sextant, passive skill tree, leaguestone and monster stats). The files 
in the `stat_translations` folder cover other stats:

- `areas.json` covers stats on areas.
- `atlas.json` covers sextant stats as shown on the Atlas.
- `strongbox.json` covers stats on strongboxes.
- `passive_skill.json` covers stats on the passive skill tree.
- `passive_skill_aura.json` covers stats of auras provided by stats on the passive
  skill tree.
- `monster.json` covers stats on monsters.
- `support_gem.json` covers stats on support gems.
- `skill.json` and all other files ending in `skill` cover stats
  on active skill gems and other skills. Each skill is fully described by one of
  these files. Which one depends on the skill.

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
`v` matches the condition iff `min <= v <= max`. If `negated` is present and true, the
condition result is negated. The first translation for which
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
- `ignored`: the value is not referenced in the format string

Range values are inserted as `(value1 to value2)`. If both values of the range are
negative, the '-' character is moved outside the parentheses (e.g. `(-20, -10)` is
formatted as `-(20 to 10)`). 

`index_handlers` are applied to values before formatting. These change the actual
values, see 
[`PyPoE.poe.file.translations`, line 2071ff](https://github.com/OmegaK2/PyPoE/blob/dev/PyPoE/poe/file/translations.py#L2071)
for their Python definitions.
If, for example, `divide_by_one_hundred` is a handler for a value, the value must
be divided by 100 before being formatted.
