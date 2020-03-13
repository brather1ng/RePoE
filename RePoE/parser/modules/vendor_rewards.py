from RePoE.parser.util import call_with_default_args, write_json, get_release_state, ignore_mod_domain
from RePoE.parser import Parser_Module

class vendor_rewards(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        ###### quest vendor rewards
        root = {}
        all_quest_states = {}
        all_classes = [ "Duelist", "Marauder", "Ranger", "Scion", "Shadow", "Templar", "Witch" ]
        for state_row in relational_reader['QuestStates.dat']:
            questId = state_row["QuestKey"]["Id"]
            for state in state_row["QuestStates"]:
                all_quest_states[state] = questId

        for reward_row in relational_reader['QuestVendorRewards.dat']:
            if len(reward_row["CharactersKeys"]) > 0:
                charClass = reward_row["CharactersKeys"][0]["Name"]
            else:
                charClass = "All"

            for npc in reward_row["NPCKeys"]:
                npcId = npc["Id"]
                npcName = npc["Name"]
                npcAct = npc["Unknown1"]
                # We skip Act10 and Epilogue Lilly - They are identical to Act6 Lilly and they make the
                # json file much larger.
                if npcId == "Metadata/NPC/Epilogue/Lilly" or npcId == "Metadata/NPC/Act10/Lilly"\
                        or npcId == "Metadata/NPC/Epilogue/Lilly2":
                    continue

                if npcId not in root:
                    root[npcId] = {
                        "name": npcName,
                        "act": npcAct,
                        "rewards": {}
                    }

                for key in reward_row["BaseItemTypesKeys"]:
                    rewardId = key["Id"]
                    if rewardId not in root[npcId]["rewards"]:
                        root[npcId]["rewards"][rewardId] = {
                            "name": key["Name"],
                            "classes": [],
                            "quest_id": ""
                        }

                    if charClass == "All":
                        root[npcId]["rewards"][rewardId]["classes"] = all_classes
                    else:
                        if charClass not in root[npcId]["rewards"][rewardId]["classes"]:
                            root[npcId]["rewards"][rewardId]["classes"].append(charClass)

                    if ((npcName != "Lilly Roth") and (npcName != "Siosa")):
                        if reward_row["QuestState"] in all_quest_states:
                            root[npcId]["rewards"][rewardId]["quest_id"] = all_quest_states[reward_row["QuestState"]]
                        else:
                            # BLATANT KLUDGE: Quest state 244 = a2q6, but isn't in QuestStates.dat
                            if reward_row["QuestState"] == 244:
                                root[npcId]["rewards"][rewardId]["quest_id"] = "a2q6"
        write_json(root, data_path, 'vendor_rewards')

if __name__ == '__main__':
    call_with_default_args(vendor_rewards.write)
