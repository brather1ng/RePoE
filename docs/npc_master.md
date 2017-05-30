### `npc_master.json`

Object with a property for each master. The value of that property is an object
with only on property: `signature_mod`. Its value is an object with the following
properties:

- `id`: The mod id of the master's signature mod. See `mods.json` to get more 
  information about the mod.
- `spawn_weights`: The spawn tags the signature mod can spawn on in the master's
  vendor window. These work the same way as the `spawn_weights` in `mods.json`.
  Though the weights do not have any effect, only whether they are greater than 
  zero or not.
