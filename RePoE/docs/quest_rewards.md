### `quest_rewards.json`

Describes the items offered as quest rewards, as well as the classes the rewards are offered to. 

The file is an object where each key is the quest metadata id of a quest with a collection of
objects describing each quest reward. The quest object has the following fields:

- `id`: The mnemonic id of the quest with reference to the act and quest number, such as a10q1.
- `act`: The act the quest is found in.
- `name`: The name of the quest.
- `rewards`: An object containing all rewards offered upon completion of the quest. Each reward
  contains the following fields:
  * The key of the object is the metadata id of the item, as found in `base_items.json`.
  * `classes`: An array of the classes that are eligible to receive the reward.
  * `name`: The name of the reward item from base_types.
  * `type`: The class id of the reward item from item_classes.

Base item information not specific to quest rewards can be found in `base_items.json`.
