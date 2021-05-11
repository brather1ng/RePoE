"""A module to handle importing the specific stat_translation jsons"""
from RePoE import load_json, _assert_all_json_files_accounted_for, __DATA_PATH__
import os

__STAT_TRANSLATION_PATH__ = os.path.join(__DATA_PATH__, "stat_translations", "")


stat_translations = {}


def _load_json_and_add_to_stat_translations(path, dir):
    name, _, _ = path.partition(".json")
    loaded_json = load_json(path, dir)
    stat_translations[name] = loaded_json
    return loaded_json


strongbox = _load_json_and_add_to_stat_translations("strongbox.json", __STAT_TRANSLATION_PATH__)
support_gem = _load_json_and_add_to_stat_translations("support_gem.json", __STAT_TRANSLATION_PATH__)
skill = _load_json_and_add_to_stat_translations("skill.json", __STAT_TRANSLATION_PATH__)
aura_skill = _load_json_and_add_to_stat_translations("aura_skill.json", __STAT_TRANSLATION_PATH__)
banner_aura_skill = _load_json_and_add_to_stat_translations("banner_aura_skill.json", __STAT_TRANSLATION_PATH__)
beam_skill = _load_json_and_add_to_stat_translations("beam_skill.json", __STAT_TRANSLATION_PATH__)
brand_skill = _load_json_and_add_to_stat_translations("brand_skill.json", __STAT_TRANSLATION_PATH__)
buff_skill = _load_json_and_add_to_stat_translations("buff_skill.json", __STAT_TRANSLATION_PATH__)
curse_skill = _load_json_and_add_to_stat_translations("curse_skill.json", __STAT_TRANSLATION_PATH__)
debuff_skill = _load_json_and_add_to_stat_translations("debuff_skill.json", __STAT_TRANSLATION_PATH__)
minion_skill = _load_json_and_add_to_stat_translations("minion_skill.json", __STAT_TRANSLATION_PATH__)
minion_attack_skill = _load_json_and_add_to_stat_translations("minion_attack_skill.json", __STAT_TRANSLATION_PATH__)
minion_spell_skill = _load_json_and_add_to_stat_translations("minion_spell_skill.json", __STAT_TRANSLATION_PATH__)
offering_skill = _load_json_and_add_to_stat_translations("offering_skill.json", __STAT_TRANSLATION_PATH__)
variable_duration_skill = _load_json_and_add_to_stat_translations(
    "variable_duration_skill.json", __STAT_TRANSLATION_PATH__
)
areas = _load_json_and_add_to_stat_translations("areas.json", __STAT_TRANSLATION_PATH__)
atlas = _load_json_and_add_to_stat_translations("atlas.json", __STAT_TRANSLATION_PATH__)
passive_skill = _load_json_and_add_to_stat_translations("passive_skill.json", __STAT_TRANSLATION_PATH__)
passive_skill_aura = _load_json_and_add_to_stat_translations("passive_skill_aura.json", __STAT_TRANSLATION_PATH__)
monster = _load_json_and_add_to_stat_translations("monster.json", __STAT_TRANSLATION_PATH__)
heist_equipment = _load_json_and_add_to_stat_translations("heist_equipment.json", __STAT_TRANSLATION_PATH__)
leaguestone = _load_json_and_add_to_stat_translations("leaguestone.json", __STAT_TRANSLATION_PATH__)
active_skill_gem = _load_json_and_add_to_stat_translations("active_skill_gem.json", __STAT_TRANSLATION_PATH__)
advanced_mod = _load_json_and_add_to_stat_translations("advanced_mod.json", __STAT_TRANSLATION_PATH__)
secondary_debuff_skill = _load_json_and_add_to_stat_translations(
    "secondary_debuff_skill.json", __STAT_TRANSLATION_PATH__
)

_assert_all_json_files_accounted_for(__STAT_TRANSLATION_PATH__, globals=globals())
