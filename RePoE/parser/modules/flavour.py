from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module


class flavour(Parser_Module):
    @staticmethod
    def write(file_system, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        for flavour in relational_reader["FlavourText.dat"]:
            if flavour["Id"] in root:
                print("Duplicate flavour id:", flavour["Id"])
            else:
                root[flavour["Id"]] = flavour["Text"]

        write_json(root, data_path, "flavour")


if __name__ == "__main__":
    call_with_default_args(flavour.write)
