from RePoE.util import write_json, call_with_default_args


def write(data_path, relational_reader, **kwargs):
    mod_types = {
        row['Name']: {
            "sell_price_types": [key["Id"] for key in row["ModSellPriceTypesKeys"]],
            "tags": [key["Id"] for key in row["TagsKeys"]]
        } for row in relational_reader['ModType.dat']
    }

    write_json(mod_types, data_path, 'mod_types')


if __name__ == '__main__':
    call_with_default_args(write)
