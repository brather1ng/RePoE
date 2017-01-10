from PyPoE.cli.exporter.wiki.parsers.item import ItemsParser
from PyPoE.poe.constants import MOD_DOMAIN
from PyPoE.poe.sim.formula import GemTypes, gem_stat_requirement
from RePoE.constants import ActiveSkillType, ReleaseState, UNRELEASED_GEMS, DROP_DISABLED_GEMS
from RePoE.util import write_json, call_with_default_args


def _handle_dict(representative, per_level):
    static = None
    cleared = True
    cleared_keys = []
    for k, v in representative.items():
        per_level_values = []
        skip = False
        for pl in per_level:
            if k not in pl:
                skip = True
                break
            per_level_values.append(pl[k])
        if skip:
            cleared = False
            continue

        if isinstance(v, dict):
            static_value, cleared_value = _handle_dict(v, per_level_values)
        elif isinstance(v, list):
            static_value, cleared_value = _handle_list(v, per_level_values)
        else:
            static_value, cleared_value = _handle_primitives(v, per_level_values)

        if static_value is not None:
            if static is None:
                static = {}
            static[k] = static_value

        if cleared_value:
            cleared_keys.append(k)
        else:
            cleared = False

    for k in cleared_keys:
        for pl in per_level:
            del pl[k]
    return static, cleared


def _handle_list(representative, per_level):
    static = None
    cleared = True
    cleared_is = []
    for i, v in enumerate(representative):
        per_level_values = [pl[i] for pl in per_level]
        if isinstance(v, dict):
            static_value, cleared_value = _handle_dict(v, per_level_values)
        elif isinstance(v, list):
            static_value, cleared_value = _handle_list(v, per_level_values)
        else:
            static_value, cleared_value = _handle_primitives(v, per_level_values)

        if static_value is not None:
            if static is None:
                static = [None] * len(representative)
            static[i] = static_value

        if cleared_value:
            cleared_is.append(i)
        else:
            cleared = False

    for i in cleared_is:
        for pl in per_level:
            pl[i] = None
    return static, cleared


def _handle_primitives(representative, per_level):
    for pl in per_level:
        if pl != representative:
            return None, False
    return representative, True


class GemConverter:

    def __init__(self, relational_reader):
        self.relational_reader = relational_reader

        self.gepls = {}
        for gepl in self.relational_reader['GrantedEffectsPerLevel.dat']:
            ge_id = gepl['GrantedEffectsKey']['Id']
            if ge_id not in self.gepls:
                self.gepls[ge_id] = []
            self.gepls[ge_id].append(gepl)

        self.max_totem_id = relational_reader['SkillTotems.dat'].table_rows

    def _convert_active_skill(self, active_skill):
        stat_conversions = {}
        for in_stat, out_stat in zip(active_skill['Input_StatKeys'], active_skill['Output_StatKeys']):
            stat_conversions[in_stat['Id']] = out_stat['Id']
        return {
            'id': active_skill['Id'],
            'display_name': active_skill['DisplayedName'],
            'description': active_skill['Description'],
            'types': [ActiveSkillType(t).name.lower() for t in active_skill['ActiveSkillTypeData']],
            'weapon_restrictions': [ic['Id'] for ic in active_skill['WeaponRestriction_ItemClassesKeys']],
            'is_skill_totem': (active_skill['SkillTotemId'] <= self.max_totem_id),
            'is_manually_casted': active_skill['IsManuallyCasted'],
            'stat_conversions': stat_conversions
        }

    def _convert_gepl(self, gepl, multipliers, is_support):
        level = gepl['Level']
        r = {
            'required_level': gepl['LevelRequirement'],
        }
        if gepl['Cooldown'] > 0:
            r['cooldown'] = gepl['Cooldown']
            charge_type = gepl['Unknown29']
            if charge_type == 1:
                r['expend_charge_to_bypass_cooldown'] = 'endurance'
            elif charge_type == 2:
                r['expend_charge_to_bypass_cooldown'] = 'frenzy'
            elif charge_type == 3:
                r['expend_charge_to_bypass_cooldown'] = 'power'
        if gepl['StoredUses'] > 0:
            r['stored_uses'] = gepl['StoredUses']

        if is_support:
            r['mana_multiplier'] = gepl['ManaMultiplier']
        else:
            r['mana_cost'] = gepl['ManaCost']
            if gepl['DamageEffectiveness'] != 0:
                r['damage_effectiveness'] = gepl['DamageEffectiveness']
            if gepl['DamageMultiplier'] != 0:
                r['damage_multiplier'] = gepl['DamageMultiplier']
            if gepl['CriticalStrikeChance'] > 0:
                r['crit_chance'] = gepl['CriticalStrikeChance']
            if gepl['VaalSouls'] > 0:
                r['vaal'] = {
                    'souls': gepl['VaalSouls'],
                    'stored_uses': gepl['VaalStoredUses']
                }

        stats = []
        for k, v in gepl['Stats']:
            stats.append({
                'id': k['Id'],
                'value': v
            })
        for k in gepl['StatsKeys2']:
            stats.append({
                'id': k['Id'],
                'value': 1
            })
        r['stats'] = stats

        q_stats = []
        for k, v in gepl['QualityStats']:
            q_stats.append({
                'id': k['Id'],
                'value': v
            })
        r['quality_stats'] = q_stats

        if multipliers is not None:
            stat_requirements = {}
            gtype = GemTypes.support if is_support else GemTypes.active
            for stat_type, multi in multipliers.items():
                if multi == 0 or multi == 33 or multi == 34:
                    # 33 and 34 are from white gems (Portal, Vaal Breach, Detonate Mine), which have no requirements
                    req = 0
                else:
                    req = gem_stat_requirement(level, gtype, multi)
                stat_requirements[stat_type] = req
            r['stat_requirements'] = stat_requirements

        return r

    def _convert_base_item_specific(self, base_item_type, granted_effect, obj):
        if base_item_type is None:
            obj['base_item'] = None
            return

        if granted_effect['Id'] in UNRELEASED_GEMS:
            release_state = ReleaseState.UNRELEASED
        elif granted_effect['Id'] in DROP_DISABLED_GEMS:
            release_state = ReleaseState.DROP_DISABLED
        else:
            release_state = ReleaseState.RELEASED
        obj['base_item'] = {
            'id': base_item_type['Id'],
            'display_name': base_item_type['Name'],
            'release_state': release_state.name.lower(),
        }

        key = ItemsParser._skill_gem_to_projectile_map.get(base_item_type['Name'])
        if key:
            obj['projectile_speed'] = \
                self.relational_reader['Projectiles.dat'].index['Id']['Metadata/Projectiles/' + key]['ProjectileSpeed']

    def convert(self, base_item_type, granted_effect, gem_tags, multipliers):
        is_support = granted_effect['IsSupport']
        ge_id = granted_effect['Id']
        obj = {
            'is_support': is_support
        }
        if gem_tags is None:
            obj['tags'] = None
        else:
            obj['tags'] = [tag['Id'] for tag in gem_tags]

        if is_support:
            obj['support_gem_letter'] = granted_effect['SupportGemLetter']
        else:
            obj['cast_time'] = granted_effect['CastTime']
            obj['active_skill'] = self._convert_active_skill(granted_effect['ActiveSkillsKey'])

        # GrantedEffectsPerLevel
        gepls = self.gepls[ge_id]
        gepls.sort(key=lambda g: g['Level'])
        gepls_dict = {}
        for gepl in gepls:
            gepls_dict[gepl['Level']] = self._convert_gepl(gepl, multipliers, is_support)
        obj['per_level'] = gepls_dict

        # GrantedEffectsPerLevel that do not change with level
        # makes using the json harder, but makes the json *a lot* smaller (would be like 3 times larger)
        obj['static'] = {}
        if len(gepls) > 1:
            representative = gepls_dict[gepls[0]['Level']]
            static, _ = _handle_dict(representative, gepls_dict.values())
            if static is not None:
                obj['static'] = static

        self._convert_base_item_specific(base_item_type, granted_effect, obj)

        return obj


def write_gems(data_path, relational_reader, **kwargs):
    root = {}
    converter = GemConverter(relational_reader)

    for gem in relational_reader['SkillGems.dat']:
        granted_effect = gem['GrantedEffectsKey']
        ge_id = granted_effect['Id']
        if ge_id in root:
            print("Duplicate GrantedEffectsKey.Id '%s'" % ge_id)
        multipliers = {
            'str': gem['Str'],
            'dex': gem['Dex'],
            'int': gem['Int']
        }
        root[ge_id] = converter.convert(gem['BaseItemTypesKey'], granted_effect, gem['GemTagsKeys'], multipliers)

    for mod in relational_reader['Mods.dat']:
        if mod['GrantedEffectsPerLevelKey'] is None:
            continue
        domain = MOD_DOMAIN(mod['Domain'])
        if (domain is MOD_DOMAIN.AREA or domain is MOD_DOMAIN.ATLAS or domain is MOD_DOMAIN.CHEST
                or domain is MOD_DOMAIN.MONSTER or domain is MOD_DOMAIN.STANCE):
            continue
        granted_effect = mod['GrantedEffectsPerLevelKey']['GrantedEffectsKey']
        ge_id = granted_effect['Id']
        if ge_id in root:
            # mod effects may exist as gems, those are handled above
            continue
        root[ge_id] = converter.convert(None, granted_effect, None, None)

    write_json(root, data_path, 'gems')


if __name__ == '__main__':
    call_with_default_args(write_gems)
