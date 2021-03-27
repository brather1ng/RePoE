"""A module to handle importing the specific stat_translation jsons"""
from RePoE import load_json, _assert_all_json_files_accounted_for, _get_all_json_files, __DATA_PATH__
import os

__STAT_TRANSLATION_PATH__ = os.path.join(__DATA_PATH__, "stat_translations", "")

strongbox = load_json("strongbox.json", __STAT_TRANSLATION_PATH__)
support_gem = load_json("support_gem.json", __STAT_TRANSLATION_PATH__)
skill = load_json("skill.json", __STAT_TRANSLATION_PATH__)
aura_skill = load_json("aura_skill.json", __STAT_TRANSLATION_PATH__)
banner_aura_skill = load_json("banner_aura_skill.json", __STAT_TRANSLATION_PATH__)
beam_skill = load_json("beam_skill.json", __STAT_TRANSLATION_PATH__)
brand_skill = load_json("brand_skill.json", __STAT_TRANSLATION_PATH__)
buff_skill = load_json("buff_skill.json", __STAT_TRANSLATION_PATH__)
curse_skill = load_json("curse_skill.json", __STAT_TRANSLATION_PATH__)
debuff_skill = load_json("debuff_skill.json", __STAT_TRANSLATION_PATH__)
minion_skill = load_json("minion_skill.json", __STAT_TRANSLATION_PATH__)
minion_attack_skill = load_json("minion_attack_skill.json", __STAT_TRANSLATION_PATH__)
minion_spell_skill = load_json("minion_spell_skill.json", __STAT_TRANSLATION_PATH__)
offering_skill = load_json("offering_skill.json", __STAT_TRANSLATION_PATH__)
variable_duration_skill = load_json("variable_duration_skill.json", __STAT_TRANSLATION_PATH__)
areas = load_json("areas.json", __STAT_TRANSLATION_PATH__)
atlas = load_json("atlas.json", __STAT_TRANSLATION_PATH__)
passive_skill = load_json("passive_skill.json", __STAT_TRANSLATION_PATH__)
passive_skill_aura = load_json("passive_skill_aura.json", __STAT_TRANSLATION_PATH__)
monster = load_json("monster.json", __STAT_TRANSLATION_PATH__)

all = [
    strongbox,
    support_gem,
    skill,
    aura_skill,
    banner_aura_skill,
    beam_skill,
    brand_skill,
    buff_skill,
    curse_skill,
    debuff_skill,
    minion_skill,
    minion_attack_skill,
    minion_spell_skill,
    offering_skill,
    variable_duration_skill,
    areas,
    atlas,
    passive_skill,
    passive_skill_aura,
    monster,
]

_assert_all_json_files_accounted_for(__STAT_TRANSLATION_PATH__)
