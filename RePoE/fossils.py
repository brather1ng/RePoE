from RePoE.util import write_json, call_with_default_args


def _convert_mods_keys(mods_keys):
    r = []
    for mod in mods_keys:
        r.append(mod['Id'])
    return r

def _convert_tags_keys(tags_keys):
    r = []
    for tag in tags_keys:
        r.append(tag['Id'])
    return r

def _convert_mod_weights(tags, values):
	r = []
	for tag, value in zip(tags,values):
		r.append({"tag" : tag["Id"], "weight" : value})
	return r


def write_fossils(data_path, relational_reader, **kwargs):
    root = {}
    for row in relational_reader['DelveCraftingModifiers.dat']:
        root[row["BaseItemTypesKey"]] = {
				"added_mods" : _convert_mods_keys(row["AddedModKeys"]),
				"forced_mods" :  _convert_mods_keys(row["ForcedAddModKeys"]),
				"negative_mod_weights" : _convert_mod_weights(row["NegativeWeight_TagsKeys"], row["NegativeWeight_Values"]),
				"positive_mod_weights" : _convert_mod_weights(row["Weight_TagsKeys"], row["Weight_Values"])
				"forbidden_tags" : ,
				"allowed_tags" : , 
				"mirrors" : row["MirrorsItem"],
				"changes_quality" : row["RollQuality"],
				"rolls_lucky" : row["LuckyRolls"],
				"enchants" : row["Enchant"],
				"rolls_white_sockets" : row["RollWhiteSockets"],
				"sell_price_mods" : _convert_mod_keys("SellPrice_ModsKeys"), 
				"descriptions" : [description["Id"] for description in row["DelveCraftingModifierDescriptionsKeys"]],
				"blocked_descriptions" [description["Id"] for description in row["BlockedDelveCraftingModifierDescriptionsKeys"]]: 
                }
            
        
    write_json(root, data_path, 'characters')


if __name__ == '__main__':
    call_with_default_args(write_characters)
