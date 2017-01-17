from PyPoE.poe.file.translations import TranslationFileCache, get_custom_translation_file
from RePoE.util import write_json, call_with_default_args


def _convert_tags(n_ids, tags, tags_types):
    f = ["ignore" for _ in range(n_ids)]
    for tag, tag_type in zip(tags, tags_types):
        if tag_type == '%':
            f[tag] = "#"
        elif tag_type == 'd%':
            f[tag] = "#%"
        elif tag_type.startswith('$') and 'd' in tag_type:
            f[tag] = tag_type[1:].replace('d', "#")
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


def _convert(tr, tag_set):
    ids = tr.ids
    n_ids = len(ids)
    english = []
    for s in tr.get_language('English').strings:
        tags = _convert_tags(n_ids, s.tags, s.tags_types)
        tag_set.update(tags)
        english.append({
            'condition': _convert_range(s.range),
            'string': s.as_format_string,
            'format': tags,
            'index_handlers': _convert_handlers(n_ids, s.quantifier.index_handlers)
        })
    return {
        'ids': ids,
        'English': english
    }


def write_stat_translations(data_path, translation_file_cache, **kwargs):
    previous = set()
    tag_set = set()
    root = []
    for f in STAT_FILES:
        previous_f = set()
        for tr in translation_file_cache[f].translations:
            id_str = " ".join(tr.ids)
            if id_str in previous:
                if id_str in previous_f:
                    print("Duplicate id", tr.ids, "in file", f)
                continue
            previous.add(id_str)
            previous_f.add(id_str)
            root.append(_convert(tr, tag_set))
    for tr in get_custom_translation_file().translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate custom id", tr.ids)
            continue
        previous.add(id_str)
        result = _convert(tr, tag_set)
        result['hidden'] = True
        root.append(result)
    print("Possible format tags: {}".format(tag_set))
    write_json(root, data_path, 'stat_translations')


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
#   - passive_skill_aura
# 'monster_stat_descriptions.txt' tree
STAT_FILES = [
    'skill_stat_descriptions.txt',
    'aura_skill_stat_descriptions.txt',
    'beam_skill_stat_descriptions.txt',
    'curse_skill_stat_descriptions.txt',
    'debuff_skill_stat_descriptions.txt',
    'minion_attack_skill_stat_descriptions.txt',
    'minion_spell_skill_stat_descriptions.txt',
    'offering_skill_stat_descriptions.txt',
    'atlas_stat_descriptions.txt',
    'passive_skill_aura_stat_descriptions.txt',
]


if __name__ == '__main__':
    call_with_default_args(write_stat_translations)
