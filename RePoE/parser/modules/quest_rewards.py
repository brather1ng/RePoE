from RePoE.parser.util import call_with_default_args, write_json, get_release_state, ignore_mod_domain
from RePoE.parser import Parser_Module

class quest_rewards(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        all_classes = [ "Duelist", "Marauder", "Ranger", "Scion", "Shadow", "Templar", "Witch" ]
        for reward_row in relational_reader['QuestRewards.dat']:
            if reward_row["BaseItemTypesKey"] is None:
                continue
            questId = reward_row["QuestKey"]["Id"]
            rewardId = reward_row["BaseItemTypesKey"]["Id"]

            if reward_row["BaseItemTypesKey"] is not None:
                rewardName = reward_row["BaseItemTypesKey"]["Name"].replace("'", "")
                if reward_row["CharactersKey"] is not None:
                    charClass = reward_row["CharactersKey"]["Name"]
                else:
                    charClass = "All"
                

                # Add an entry for the quest into the root node
                if questId not in root:
                    root[questId] = {
                        "name": reward_row["QuestKey"]["Name"],
                        "act": reward_row["QuestKey"]["Act"],
                        "rewards": {}
                    }
                
                ##### This is for root->quest->rewards->class
                # Add an entry for the reward into the quest node
                if rewardName not in root[questId]["rewards"]:
                    root[questId]["rewards"][rewardId] = {
                        "classes": [],
                        "name": rewardName,
                        "type": reward_row["BaseItemTypesKey"]["ItemClassesKey"]["Id"]
                    }
                if charClass == "All":
                    root[questId]["rewards"][rewardId]["classes"] = all_classes
                else:
                    if charClass not in root[questId]["rewards"][rewardId]["classes"]:
                        root[questId]["rewards"][rewardId]["classes"].append(charClass)
        write_json(root, data_path, 'quest_rewards')

if __name__ == '__main__':
    call_with_default_args(quest_rewards.write)
