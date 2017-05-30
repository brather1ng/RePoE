from RePoE.util import write_json, call_with_default_args


def _convert_spawn_weights(tags, weights):
    r = []
    for tag, weight in zip(tags, weights):
        r.append({
            'tag': tag['Id'],
            'weight': weight
        })
    return r


def write_npc_master(data_path, relational_reader, **kwargs):
    root = {}
    for row in relational_reader['NPCMaster.dat']:
        root[row['Id']] = {
            'signature_mod': {
                'id': row['SignatureMod_ModsKey']['Id'],
                'spawn_weights': _convert_spawn_weights(row['SignatureModSpawnWeight_TagsKeys'],
                                                        row['SignatureModSpawnWeight_Values']),
            },
        }
    write_json(root, data_path, 'npc_master')


if __name__ == '__main__':
    call_with_default_args(write_npc_master)
