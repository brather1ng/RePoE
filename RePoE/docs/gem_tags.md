### `gem_tags.json`

Simple object that contains all gem tags with their internal id as keys and their
translation as value.

If the value is `null`, the tag is not shown on items. `active_skill` and
`low_max_level` should be self explanatory. `dexterity`, `intelligence` and
`strength` set the primary attribute of the gem. This corresponds to the socket
colors they can be socketed into. For white gems none of these tags is present.
