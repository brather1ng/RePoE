### `mod_types.json`

Describes mod types. Tells the name, the effect of fossil crafting on the types, and
the effect the types have on vendor sale price.

Mod types are associated to mods and are listed in `mods.json`. They are a strictly finer 
grading to mods than then `group` descriptor found in `mods.json`.
  
- `sell_price_types`: A list of the types which affect vendor sale price.  
