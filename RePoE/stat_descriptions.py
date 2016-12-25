from PyPoE.poe.file.translations import TranslationFileCache, get_custom_translation_file
from RePoE.util import write_json, load_ggpk


def _convert_tags(n_ids, tags, tags_types):
    f = ["ignore" for _ in range(n_ids)]
    for tag, tag_type in zip(tags, tags_types):
        if tag_type == "%":
            f[tag] = "#"
        elif tag_type == "$+d":
            f[tag] = "+#"
        elif tag_type == "$d%":
            f[tag] = "#%"
        elif tag_type == "d%":
            f[tag] = "#%"
        else:
            print("Unknown tag type:", tag_type)
    return f


def _convert_range(translation_range):
    rs = []
    for r in translation_range:
        if r.min is None and r.max is None:
            rs.append({})
        elif r.min is None:
            rs.append({
                'max': r.max
            })
        elif r.max is None:
            rs.append({
                'min': r.min
            })
        else:
            rs.append({
                'min': r.min,
                'max': r.max
            })
    return rs


def _convert_handlers(n_ids, index_handlers):
    hs = [[] for _ in range(n_ids)]
    for handler_name, ids in index_handlers.items():
        for i in ids:
            # Indices in the handler dict are 1-based
            hs[i - 1].append(handler_name)
    return hs


def _convert(tr):
    ids = tr.ids
    n_ids = len(ids)
    english = []
    for s in tr.get_language('English').strings:
        english.append({
            'condition': _convert_range(s.range),
            'string': s.as_format_string,
            'format': _convert_tags(n_ids, s.tags, s.tags_types),
            'index_handlers': _convert_handlers(n_ids, s.quantifier.index_handlers)
        })
    return {
        'ids': ids,
        'English': english
    }


def write_stat_descriptions(ggpk, data_path):
    tc = TranslationFileCache(path_or_ggpk=ggpk, files=STAT_FILES)
    previous = set()
    root = []
    for f in STAT_FILES:
        previous_f = set()
        for tr in tc[f].translations:
            id_str = " ".join(tr.ids)
            if id_str in previous:
                if id_str in previous_f:
                    print("Duplicate id", tr.ids, "in file", f)
                continue
            previous.add(id_str)
            previous_f.add(id_str)
            root.append(_convert(tr))
    for tr in get_custom_translation_file().translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate custom id", tr.ids)
            continue
        previous.add(id_str)
        result = _convert(tr)
        result['hidden'] = True
        root.append(result)
    write_json(root, data_path, 'stat_descriptions')


# 'stat_descriptions.txt' tree
# - chest
# - gem
#   - active_skill_gem
#     - skill
#       - aura_skill
#       - beam_skill
#       - curse_skill
#       - debuff_skill
#       - minion_skill
#         - minion_attack_skill
#         - minion_spell_skill
#       - offering_skill
# - map
#   - atlas
# - passive_skill
#   - passive_aura_skill
# 'monster_stat_descriptions.txt' tree
STAT_FILES = [
    'stat_descriptions.txt',
    'gem_stat_descriptions.txt',
    'active_skill_gem_stat_descriptions.txt',
]


if __name__ == '__main__':
    ggpk = load_ggpk('C:/Program Files (x86)/Grinding Gear Games/Path of Exile/Content.ggpk')
    write_stat_descriptions(ggpk, '../data/')

# format: how values are formatted when inserted into the string
# - "#": unchanged
# - "+#": prepend with a "+" char, if values are positive
# - "#%": append "%" char after it
# - "ignored": value is not inserted (but still part of the numbering in the format string)
# - if value is range and both are negative: prepend with "-" ("-(#-#) to ...")
# index_handlers: which handlers to apply to which indexes (before before formatting)
#                 see PyPoE.poe.file.translations, line 861ff
# hidden: if true, stats are not shown in-game (e.g. armour movement speed reduction implicits)
#         Wiki suffixes these with " (Hidden)"
