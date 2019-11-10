### `gem_tooltips.json`

Describes tooltips for skill gems and skill gem effects only provided by mods.

The file is an object where each key is a GrantedEffects (skill) id that has its
description object as value. That description object has fields `per_level` and 
`static`.

`per_level` contains the statistics that change with level and `static` those that
are the same for each level. The keys in the `per_level` object hold the 
statistics for the level corresponding to that key.

To get all statistics for one level, the `per_level` entry and `static`
have to be merged. This happens recursively.

To merge objects, keys that are only in one of the objects are taken as is, while the
values for keys that are in both are merged via recursion.

To merge arrays, entries that are null in one of the objects are taken from the object
where they are not null, while entries that are not null in both are merged via
recursion.

The merged object for each level has the following fields:

- `name`: In-game name of the skill.
- `description`: Textual description of the skill.
- `properties`: Skill innate properties, like skill level, mana cost and crit chance.
  The first line are the gems' tags or an empty string if it has none
  (always the case for skills that don't exist as gem items).
  The second line is the gems' level.
- `requirements`: Level and stat requirements of the skill.
- `stats`: Stats this level of the skill provides.
- `quality_stats`: Stats this skill gains with quality. The values are provided
  per point of quality (it would provide 20 times the value at max quality).

Each field (except `name` and `quality_stats`) is an array with an entry for each
line that appears on the tooltip. The lines are (almost) ordered like they appear
on tooltips. The tooltip first shows `properties`, then `requirements`, then
`description` and then `stats`. The lines from `quality_stats` are added to
`stats`, they might be merged with a line from `stats` if they describe the same
stat.

Array entries have four forms:

1. A string: no further processing required, this is the line. This is only used
  if the line contains no values, e.g. the gem's tags.
2. An object with the fields `text` and `values`: `text` is a format string that
  contains occurrences of `{i}`. Each of them references the entry of the array
  `values` with index `i`. These entries are numbers. If your language has
  format strings like this, just put `text` as the string and `values` as the
  parameters and the return value is the line. Values are referenced in order and
  each value is referenced exactly once (`{0}..{n}` occur in order in `text`,
  each `{i}` occurs exactly once and `n` is the number of `values`)
3. An object with the fields `text` and `value`: Replace `{0}` in `text` with the
  `value` (a number) to get the line.
  You can handle this the same as 2. but with a single value instead of an array.
4. An object with only the field `text`: The stat has no effect at this level and
  does not need to be displayed. You can assume values of 0 in most cases.
