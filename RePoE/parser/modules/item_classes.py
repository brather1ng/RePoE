from RePoE.parser.util import call_with_default_args, write_json, get_id_or_none
from RePoE.parser import Parser_Module


class item_classes(Parser_Module):
    @staticmethod
    def write(file_system, data_path, relational_reader, translation_file_cache, ot_file_cache):
        item_classes = {row["Id"]: {"name": row["Name"],} for row in relational_reader["ItemClasses.dat"]}
        write_json(item_classes, data_path, "item_classes")


if __name__ == "__main__":
    call_with_default_args(item_classes.write)
