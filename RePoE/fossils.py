from RePoE.util import write_json, call_with_default_args




def write_fossils(data_path, relational_reader, **kwargs):
	root = {}
	for row in relational_reader['DelveCraftingModifiers.dat']:
		id = row["BaseItemTypesKey"]["Name"]
		obj = {
			"added_mods": [mod['Id'] for mod in row["Mods_Keys0"]],
			"forced_mods": [mod['Id'] for mod in row["Mods_Keys1"]],
			"negative_mod_weights": [{"tag" : tag["Id"], "weight" : value} for tag, value in zip(row["NegativeWeight_TagsKeys"], row["NegativeWeight_Values"])],
			"positive_mod_weights": [{"tag" : tag["Id"], "weight" : value} for tag, value in zip(row["Weight_TagsKeys"], row["Weight_Values"])],
			"forbidden_tags": [tag["TagsKey"]["Id"] for tag in row["DelveCraftingTagsKeys0"]],
			"allowed_tags": [tag["TagsKey"]["Id"] for tag in row["DelveCraftingTagsKeys1"]],
			"corrupted_essence_chance": row["Unknown0"],
			"mirrors": row["Flag0"],
			"changes_quality": row["Flag1"],
			"rolls_lucky": row["Flag3"],
			"enchants": row["Flag2"],
			"rolls_white_sockets": row["Flag4"],
			"sell_price_mods": [mod['Id'] for mod in row["SellPrice_ModsKeys"]],
			"descriptions": [description["Description"] for description in row["DelveCraftingModifierDescriptionsKeys"]]
			# "blocked_descriptions": [description["Id"] for description in
			# 						 row["Keys9"]]
			}

		root[id] = obj
		# print(id)
		# print(obj)
		# input()
		# root[row["BaseItemTypesKey"]] = {
		# 		"added_mods" : _convert_mods_keys(row["AddedModKeys"]),
		# 		"forced_mods" :  _convert_mods_keys(row["ForcedAddModKeys"]),
		# 		"negative_mod_weights" : _convert_mod_weights(row["NegativeWeight_TagsKeys"], row["NegativeWeight_Values"]),
		# 		"positive_mod_weights" : _convert_mod_weights(row["Weight_TagsKeys"], row["Weight_Values"]),
		# 		"forbidden_tags" : [tag["TagsKey"]["Id"] for tag in row["ForbiddenDelveCraftingTagsKeys"]],
		# 		"allowed_tags" : [tag["TagsKey"]["Id"] for tag in row["AllowedDelveCraftingTagsKeys"]],
		# 		"corrupted_essence_chance" : row["CorruptedEssenceChance"],
		# 		"mirrors" : row["MirrorsItem"],
		# 		"changes_quality" : row["RollQuality"],
		# 		"rolls_lucky" : row["LuckyRolls"],
		# 		"enchants" : row["Enchant"],
		# 		"rolls_white_sockets" : row["RollWhiteSockets"],
		# 		"sell_price_mods" : _convert_mods_keys("SellPrice_ModsKeys"),
		# 		"descriptions" : [description["Id"] for description in row["DelveCraftingModifierDescriptionsKeys"]],
		# 		"blocked_descriptions" : [description["Id"] for description in row["BlockedDelveCraftingModifierDescriptionsKeys"]]
		#         }


	write_json(root, data_path, 'fossils')


if __name__ == '__main__':
	call_with_default_args(write_fossils)
