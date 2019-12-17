### `item_classes.json`

Defines the item class ids and the tags added to items when they are Shaper/Elder items.

The file is an object where each key is the id of an item class with an object describing
the item class as a value. The description object has the following fields:

- `name`: A more "displayable" version of the id, e.g. it does not combine words with Camel
  Case but always with spaces. I'm not sure where this is used in-game. This is the naming
  used for item classes in the Wiki.
- All fields ending in `_tag`: The tag added to items of this class if the item has the respective influence.
  `null` if items of the class can't have the influence.
