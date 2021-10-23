from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module


class active_skill_types(Parser_Module):
    @staticmethod
    def write(file_system, data_path, relational_reader, translation_file_cache, ot_file_cache):
        types = [row["Id"] for row in relational_reader["ActiveSkillType.dat"]]
        write_json(types, data_path, "active_skill_types")


if __name__ == "__main__":
    call_with_default_args(active_skill_types.write)
