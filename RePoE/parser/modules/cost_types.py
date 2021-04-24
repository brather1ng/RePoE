from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module


class cost_types(Parser_Module):
    @staticmethod
    def write(file_system, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        for row in relational_reader["CostTypes.dat"]:
            root[row["Id"]] = {
                "stat": row["StatsKey"]["Id"] if row["StatsKey"] else None,
                "format_text": row["FormatText"],
            }
        write_json(root, data_path, "cost_types")


if __name__ == "__main__":
    call_with_default_args(cost_types.write)
