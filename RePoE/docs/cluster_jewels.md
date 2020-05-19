### `cluster_jewels.json`

Describes how cluster jewels can be generated and how they influence the passive tree.

Each member of the root object has a base item id (see `base_items.json`) as key with the value describing that type
of cluster jewel. These values have the following members:

- `name`: Name of the base item.
- `size`: The cluster jewel size.
- `min_skills` and `max_skills`: The minimum and maximum values for the "Adds # Passive Skills" stat.
- `total_indices`: The number of possible values for the other `_indices` member. Possible indices range from 0 to
  `total_indices` - 1. I don't know the exact interactions between these members and how the passive tree is generated,
  so if someone does, feel free to add to this file.
- `small_indices`, `notable_indices`, `socket_indices`: The possible indices where small, notable and socket passive
  skills can appear. These also define the number of small/notable/socket passives that can be added by jewels of this
  base at most.
- `passive_skills`: The possible passives that can be a part of small passive skills added by this jewel base item
  ("Added Small Passive Skills (also) grant: ...").
  The value is an array of objects with each object having the following values:
  - `id`: Id of the passive skill.
  - `name`: Name of the passive skill.
  - `stats`: Object with stat ids as keys (see `stats.json`) and the stat values as values.
  - `tag`: Tag that is added to the item when it has the stat on it (maybe only if added as an enchant). Influences
    the spawning of other mods, see `mods.json`.
