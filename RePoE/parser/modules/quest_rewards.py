from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module


class quest_rewards(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        all_classes = ["Duelist", "Marauder", "Ranger", "Scion", "Shadow", "Templar", "Witch"]
        for reward_row in relational_reader['QuestRewards.dat']:
            if reward_row["BaseItemTypesKey"] is None:
                continue

            quest = reward_row["QuestRewardOffersKey"]["QuestKey"]
            quest_id = quest["Id"]
            reward_id = reward_row["BaseItemTypesKey"]["Id"]

            if quest_id not in root:
                root[quest_id] = {
                    "name": quest["Name"],
                    "act": quest["Act"],
                    "rewards": {}
                }
            rewards = root[quest_id]["rewards"]

            if reward_id not in rewards:
                rewards[reward_id] = {
                    "classes": [],
                    "name": reward_row["BaseItemTypesKey"]["Name"],
                    "type": reward_row["BaseItemTypesKey"]["ItemClassesKey"]["Id"]
                }
            reward = rewards[reward_id]

            if reward_row["CharactersKey"] is None:
                reward["classes"] = all_classes
            else:
                char_class = reward_row["CharactersKey"]["Name"]
                if char_class not in reward["classes"]:
                    reward["classes"].append(char_class)

        write_json(root, data_path, 'quest_rewards')


if __name__ == '__main__':
    call_with_default_args(quest_rewards.write)
