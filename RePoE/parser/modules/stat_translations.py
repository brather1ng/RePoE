from PyPoE.poe.file.translations import get_custom_translation_file
from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser.constants import STAT_TRANSLATION_DICT
from RePoE.parser import Parser_Module

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
        r_dict = {}
        if r.min is not None:
            r_dict['min'] = r.min
        if r.max is not None:
            r_dict['max'] = r.max
        if r.negated:
            r_dict['negated'] = True
        rs.append(r_dict)
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


def _get_stat_translations(tag_set, translations, custom_translations):
    previous = set()
    root = []
    for tr in translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate id", tr.ids)
            continue
        previous.add(id_str)
        root.append(_convert(tr, tag_set))
    for tr in custom_translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            continue
        previous.add(id_str)
        result = _convert(tr, tag_set)
        result['hidden'] = True
        root.append(result)
    return root

class stat_translations(Parser_Module):
    @staticmethod
    def write(ggpk, data_path, relational_reader, translation_file_cache, ot_file_cache):
        tag_set = set()
        for in_file, out_file in STAT_TRANSLATION_DICT.items():
            translations = translation_file_cache[in_file].translations
            result = _get_stat_translations(tag_set, translations,
                                            get_custom_translation_file().translations)
            write_json(result, data_path, out_file)
        print("Possible format tags: {}".format(tag_set))

if __name__ == '__main__':
    call_with_default_args(stat_translations.write)
