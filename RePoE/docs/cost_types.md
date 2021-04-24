### `cost_types.json`

Defines the resource cost types used in `gems.json`.

The file is an object where each key is the id of cost type with an object describing
the cost type as a value. The description object has the following fields:

- `format_text`: A format string used to display costs of this cost type. The format parameter is the cost value.
- `stat`: A stat id (see `stats.json`) or `null`.
