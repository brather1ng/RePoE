from RePoE.parser.util import call_with_default_args, write_json, get_release_state, ignore_mod_domain
from RePoE.parser import Parser_Module

# def write_quests(data_path, relational_reader, **kwargs):

class quests(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        root = {}
        all_quest_states = {}
        for reward_row in relational_reader['QuestRewards.dat']:
            questId = reward_row["QuestKey"]["Id"]
            if reward_row["BaseItemTypesKey"] is not None:
                rewardName = reward_row["BaseItemTypesKey"]["Name"].replace("'", "")
                if reward_row["CharactersKey"] is not None:
                    charClass = reward_row["CharactersKey"]["Name"]
                else:
                    charClass = "All"
                

                # Add an entry for the quest into the root node
                if questId not in root:
                    root[questId] = {
                        "id": reward_row["QuestKey"]["Id"],
                        "name": reward_row["QuestKey"]["Name"],
                        "act": reward_row["QuestKey"]["Act"],
                        "rewards": {}
                    }
                
                ##### This is for root->quest->rewards->class
                # Add an entry for the reward into the quest node
                if rewardName not in root[questId]["rewards"]:
                    root[questId]["rewards"][rewardName] = {
                        "classes": [],
                        "name": rewardName,
                        "item_id": reward_row["BaseItemTypesKey"]["Id"],
                        "type": reward_row["BaseItemTypesKey"]["ItemClassesKey"]["Name"]
                    }
                if charClass not in root[questId]["rewards"][rewardName]["classes"]:
                    root[questId]["rewards"][rewardName]["classes"].append(charClass)


        for state_row in relational_reader['QuestStates.dat']:
            questId = state_row["QuestKey"]["Id"]
            # Add an entry for the quest into the root node, this should never happen
            if questId not in root:
                continue
            # root[questId]["states"] += state_row["QuestStates"]
            for state in state_row["QuestStates"]:
                all_quest_states[state] = questId

        write_json(root, data_path, 'quests')

        ###### quest vendor rewards
        root = {}
        for reward_row in relational_reader['QuestVendorRewards.dat']:
            npcId = reward_row["NPCKey"]["Id"]
            npcName = reward_row["NPCKey"]["Name"]
            npcAct = reward_row["NPCKey"]["Unknown1"]
            if len(reward_row["CharactersKeys"]) > 0:
                charClass = reward_row["CharactersKeys"][0]["Name"]
            else:
                charClass = "All"

            if npcName not in root:
                root[npcName] = {
                    "name": npcName,
                    "id": npcId,
                    "act": npcAct,
                    "rewards": {}
                }

            for key in reward_row["BaseItemTypesKeys"]:
                rewardName = key["Name"]
                if rewardName not in root[npcName]["rewards"]:
                    root[npcName]["rewards"][rewardName] = {
                        "name": rewardName,
                        "item_id": key["Id"],
                        "classes": [],
                        "vendor_reward_quest_id": ""
                    }

                
                if charClass not in root[npcName]["rewards"][rewardName]["classes"]:
                    root[npcName]["rewards"][rewardName]["classes"].append(charClass)
                if ((npcName != "Lilly Roth") and (npcName != "Siosa")):
                    if reward_row["QuestState"] in all_quest_states:
                        root[npcName]["rewards"][rewardName]["vendor_reward_quest_id"] = all_quest_states[reward_row["QuestState"]]
                    else:
                        # BLATANT KLUDGE: Quest state 244 = a2q6, but isn't in QuestStates.dat
                        if reward_row["QuestState"] == 244:
                            root[npcName]["rewards"][rewardName]["vendor_reward_quest_id"] = "a2q6"

                # if quest_state not in root[npcName]["rewards"][rewardName]["quest_states"]:
                #     root[npcName]["rewards"][rewardName]["quest_states"].append(quest_state)
        write_json(root, data_path, 'quests_vendor')

if __name__ == '__main__':
    call_with_default_args(quests.write)
