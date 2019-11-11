### `gems.json`

Describes skill gems and skill effects only provided by mods.

The file is an object where each key is a GrantedEffects (skill) id that has its
description object as value. That description object has the following fields:

#### General information

- `is_support`: True iff the skill is a support and no active skill.
- `cast_time`: Cast time of the skill in milliseconds. Only set for active skills.
- `stat_translation_file`: The file in `data` that can be used to translate the skill's
  stats if you don't want to use `gem_tooltips.json`.
- `secondary_granted_effect`: If specified, gaining this effect from a skill gem (item)
  will also grant the `secondary_granted_effect`. E.g. Vaal gems also grant the base skill.

#### `per_level` and `static`

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

- `required_level`: Character level required to equip and use the skill.
- `cooldown`: Cooldown (in ms) to wait between uses. Skill has no cooldown if this field
  is not set.
- `cooldown_bypass_type`: How the cooldown can be bypassed (cast the skill before the
  cooldown runs out). See
  [`RePoE.parser.constants.CooldownBypassType`](https://github.com/brather1ng/RePoE/blob/master/RePoE/constants.py#L133)
  for the possible values and their meaning. The cooldown can not be bypassed if this
  field is not set.
- `stored_uses`: Number of uses of the skill that can be stored. Each time the cooldown
  runs out, a use is stored. Up to this maximum. 1 in most cases. This field is only
  set for spells with a cooldown.
- `mana_multiplier`: Mana multiplier of the support gem. Only set for support gems.
- `mana_cost`: Mana cost required to cast the skill. Only set for active skills.
- `mana_reservation_override`: Set mana cost of supported skill to mana reservation
  of this amount (in percent). Only set for Blasphemy.
- `damage_effectiveness`: Damage effectiveness of the skill. Only set when not 0.
  Acts as a multiplier on added damage from support gems and other sources.
  Given as percentage with 0 = 100%.
- `damage_multiplier`: Damage multiplier for attack skills. Only set when not 0.
  Divide by 100 and add 100 to get as percentage.
- `crit_chance`: Critical strike chance of the skill. Only set when not 0.
  Divide by 100 to get as percentage.
- `attack_speed_multiplier`: Attack speed multiplier for attack skills. Only set when not 0.
  Divide by 100 and add 1 to get a floating point multiplier.
- `vaal`: Set for vaal skills. Contains the field `souls` and `stored_uses`.
- `stats`: Array of the stats this skill provides. Each array element is an object
  containing the stat id (`id`) and value (`value`) of the stat at the given level.
- `quality_stats`: Array of the quality stats this skill provdes. Each array element 
  is an object containing the stat id (`id`) and value (`value`) of the stat. The
  value is the value with 1000 quality, divide by 1000 to get the value per
  point of quality.
- `stat_requirements`: Character stats required to equip and use the skill.
  Only set for skills that exist as actual gem item (see below).
  Is an object that has the fields `str`, `dex` and `int`, each containing the
  requirement for the corresponding stat.

#### Information for gems that exist as items

Some fields are only set for effects that come from actual gem items, not skills that
are only provided by other items (e.g. Icestorm from Whispering Ice). These are
described below.

- `stat_requirements` in `static`/`per_level`: Character stats required to equip and
  use the skill, see above.
- `base_item`: Object containing some general information about the item:
  * `display_name`: Name of the skill as shown on in-game tooltips for the
    item.
  * `id`: Internal identifier of the item. Can be used to obtain more information
    from `BaseItemTypes.dat`.
  * `release_state`: In what state that item is currently in-game. See
    [`RePoE.parser.constants.ReleaseState`](https://github.com/brather1ng/RePoE/blob/master/RePoE/constants.py#L173)
    for possible values and their meaning. 
- `projectile_speed`: Projectile speed of the primary projectile of the skill
  in internal units (per second?).
- `tags`: Array of the gem tags of the item. See `gem_tags.json` for possible
  values and translations to their in-game display text.

Base item information not specific to gems, e.g. the visual identity, can be found in
`base_items.json`.

#### Active skill information

The `active_skill` field is only set for active skills. It has the following fields.

- `id`: Id of the active skill in `ActiveSkills.dat`. 
- `display_name`: Name of the skill as shown on in-game tooltips for the item and
  skill. Also used as tab name on the in-game character panel.
- `description`: Description of the skill as shown on the tooltip of its item.
- `is_manually_casted`: Whether the skill is manually casted. True for all skills
  except triggered skills.
- `is_skill_totem`: True iff the skill is a totem.
- `skill_totem_life_multiplier`: Life multiplier of totems this skill summons.
  The base life is the `ally_life`/`life` entry in `default_monster_stats.md` for
  the `required_level` of the skill. Only present if `is_skill_totem`.
- `stat_conversions`: Dictionary of skill specific stats that are converted to be
   applied to this skill. Generally (only?) used for enchantments to map skill
   specific enchant stats to the generic stat of the skill that is affected. Keys
   are the stat that is converted and values the stat the keys are converted to.
- `types`: Internal types/tags this skill has. See
  [`RePoE.parser.constants.ActiveSkillType`](https://github.com/brather1ng/RePoE/blob/master/RePoE/constants.py#L5)
  for possible values and their meaning. These are reverse-engineered so they
  might be incorrect. One purpose is to determine the support gems that can
  support this skill.
- `minion_types`: Like `types` but for the skills used by minions summoned by this skill.
  If not specified, this skill does not summon minions. These are also used for determining
  whether a support gem can support this skill.
- `weapon_restrictions`: If the array is not empty, this attack skill is restricted
   to the weapon classes in the array. The values are ids in `ItemClasses.dat`.

#### Information for support gems

The `support_gem` field is only set for support gems. It has the following fields:

- `letter`: The letter added on skill icons when they are supported by this
  gem. Only set for support gems.
- `supports_gems_only`: If true, this support gem only supports active skills coming from gems,
  not those provided by mods on items.
- `allowed_types`: Active skills must have at least one of these types to be supportable
  by this support gem.
- `excluded_types`: Active skills must have not have any of these types to be supportable
  by this support gem.
- `added_types`: The active skill types this support gems adds to supported active skills.
