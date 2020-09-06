from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module


class flavour(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        for flavour in relational_reader["FlavourText.dat"]:
            obj = {
                "text": flavour["Text"],
                "num": flavour["Unknown0"]
            }
            if flavour["Id"] in root:
                print("Duplicate flavour id:", flavour["Id"])
            else:
                root[flavour["Id"]] = obj

        write_json(root, data_path, "flavour")


if __name__ == "__main__":
    call_with_default_args(flavour.write)
