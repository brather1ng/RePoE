from RePoE.util import call_with_default_args, write_json, get_if_cell_is_not_none


def write_item_classes(data_path, relational_reader, **kwargs):
    item_classes = {
        row['Id']: {
            'name': row['Name'],
            'elder_tag': get_if_cell_is_not_none(row['Elder_TagsKey'], 'Id'),
            'shaper_tag': get_if_cell_is_not_none(row['Shaper_TagsKey'], 'Id'),
        } for row in relational_reader['ItemClasses.dat']
    }
    write_json(item_classes, data_path, 'item_classes')


if __name__ == '__main__':
    call_with_default_args(write_item_classes)
