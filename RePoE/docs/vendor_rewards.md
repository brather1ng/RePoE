### `vendor_rewards.json`

Describes the items offered by vendors after a quest is completed, as well as the classes the items
are offered to. 

The file is an object where each key is the metadata id of a vendor with a collection of
objects describing each item the vendor will offer after a specific quest is completed:

- `act`: The act the vendor is found in.
- `name`: The name of the vendor.
- `rewards`: An object containing all additional items the vendor well sell after completion of various
  quests.  Each reward contains the following fields:
  * The key of the object is the metadata id of the item, as found in `base_items.json`.
  * `classes`: An array of the classes that are eligible to receive the reward.
  * `name`: The name of the reward item from base_types.
  * `quest_id`: The id of the quest that must be completed before the vendor will offer the item for sale.

Base item information not specific to quest rewards can be found in `base_items.json`.
