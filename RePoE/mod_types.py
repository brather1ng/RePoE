from RePoE.util import write_json, call_with_default_args




def write_types(data_path, relational_reader, **kwargs):
	root = {}
	for row in relational_reader['ModType.dat']:
		id = row["Name"]
		obj = {
            "sell_price_types" : [ key["Id"] for key in row["ModSellPriceTypesKeys"]],
            "tags" : [ key["Id"] for key in row["TagsKeys"]]
        }

		root[id] = obj

	write_json(root, data_path, 'mod_types')


if __name__ == '__main__':
	call_with_default_args(write_types)
