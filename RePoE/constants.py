from enum import IntEnum, unique, Enum


@unique
class ActiveSkillType(IntEnum):
    # Gem tag equivalent
    attack = 1
    # Gem tag equivalent
    spell = 2
    # Gem tag equivalent (skills which fire projectiles)
    projectile = 3
    # Skill can only be used when dual wielding (Dual Strike only atm)
    dual_wield_only = 4
    # Skill gives a buff (Molten Shell and golems do not have this type)
    buff = 5
    # Skill can be used when dual wielding
    # When it does not have either of the following two, hands are random (Reckoning,
    # Whirling Blades) or alternating (everything else).
    can_dual_wield = 6
    # Skill only uses main hand when dual wielding
    uses_main_hand_when_dual_wielding = 7
    # Skill uses both hands at once when dual wielding (missing Riposte)
    uses_both_at_once_when_dual_wielding = 8
    # Gem tag equivalent
    minion = 9
    # Set for skills that hit and are not attacks
    hits = 10
    # Gem tag equivalent
    aoe = 11
    # Gem tag equivalent
    duration = 12
    # Skill can only be used when a shield is equipped
    shield_only = 13
    # Set for bow skills without projectile tag (implicit in projectile);
    # allows Faster/Slower Projectiles Support
    explicit_deals_projectile_damage = 14
    # The skill's mana cost is reserved on casting
    # Can also be interpreted as "skill is toggle".
    # Ignore this for totems, Rejuvenation Totem has this type but is no reservation/toggle skill.
    mana_cost_is_reservation = 15
    # Skill costs percentage mana
    mana_cost_is_percentage = 16
    # Skill can be turned into a trap with Trap Support
    trap_supportable = 17
    # Skill can be turned into a totem with Spell Totem Support
    spell_totem_supportable = 18
    # Skill can be turned into a mine with Remote Mine Support
    remote_mine_supportable = 19
    # St for Herald of Ash, which cannot hit but causes elemental status effects (implicit in hit);
    # allows Elemental Proliferation Support
    explicit_causes_elemental_status = 20
    # Skill summons mobs
    summons_mobs = 21
    # Skill can be turned into a totem with Ranged Attack Totem Support
    ranged_attack_totem_supportable = 22
    # Gem tag equivalent
    chaining = 23
    # Gem tag equivalent
    melee = 24
    # Skill is melee and the initial (or only) hit is single target; allows Melee Splash Support
    melee_single_target_initial_hit = 25
    # Skill can be repeated with Spell Echo Support
    spell_echo_supportable = 26
    # Set for all skills with mana_cost_is_reservation, plus vaal auras and a few more;
    # unknown purpose
    unknown_27 = 27
    # Skill can be repeated with Multistrike Support
    multistrike_supportable = 28
    # Skill directly applies burning (fire damage over time)
    applies_burning = 29
    # Gem tag equivalent
    totem = 30
    # Set for Molten Shell, Vaal Molten Shell and Of Thunder glove enchant; unknown purpose
    unknown_31 = 31
    # Gem tag equivalent
    curse = 32
    # Gem tag equivalent
    fire = 33
    # Gem tag equivalent
    cold = 34
    # Gem tag equivalent
    lightning = 35
    # Skill can be triggered by trigger gems
    triggerable = 36
    # Gem tag equivalent
    trap = 37
    # Gem tag equivalent
    movement = 38
    # Gem tag equivalent
    cast = 39
    # Skill directly deals damage over time
    deals_damage_over_time = 40
    # Gem tag equivalent
    mine = 41
    # Gem has Trigger tag and is a spell
    # (missing EnchantmentOfFlamesOnHit and EnchantmentOfTempestOnHit)
    trigger_spell = 42
    # Gem tag equivalent
    vaal = 43
    # Gem tag equivalent
    aura = 44
    # Skill can be cast by Mjölner's trigger when socketed in it
    castable_by_mjolner = 45
    # Unused for skill gems
    unknown_46 = 46
    # Gem has Trigger tag and is an attack
    trigger_attack = 47
    # Skill is a projectile attack;
    # allows Iron Grip, Physical Projectile Attack Damage and Point Blank Support
    projectile_attack = 48
    # Skill can be cast by Null's Inclination's trigger when socketed in it
    castable_by_nulls_inclination = 49
    # Gem tag equivalent
    chaos = 50
    # Unused for skill gems
    unknown_51 = 51
    # Set for Blight, Contagion, Scorching Ray; allows Iron Will Support
    unknown_52 = 52
    # Set for Burning Arrow, Cleave, Dual Strike, Glacial Hammer, Vigilant Strike;
    # these have threshold jewels that add AoE components;
    # allows Increased AoE and Concentrated Effect Support
    can_have_aoe = 53
    # Unused for skill gems
    unknown_54 = 54
    # Set for Burning Arrow, Vaal Burning Arrow;
    # these have threshold jewels that add duration components;
    # allows Increased/Less Duration and Rapid Decay Support
    can_have_duration = 55
    # Unused for skill gems
    unknown_56 = 56
    # Same as trigger_attack (47) plus Blast Rain; unknown purpose
    unknown_57 = 57
    # Gem tag equivalent
    channelling = 58
    # Set for Blight, Contagion, Scorching Ray; allows Iron Will and Controlled Destruction Support
    unknown_59 = 59
    # Skill can be cast by Cospri's Malice's trigger when socketed in it
    castable_by_cospris_malice = 60
    # Set for automatically triggered spells granted by item;
    # prevents Cast on/when/while x, Spell Totem, Remote Mine and Trap Support
    trigger_item_granted = 61
    # Gem tag equivalent
    golem = 62
    # Gem tag equivalent
    herald = 63
    # Only used for Death's Oath's aura; unknown purpose
    unknown_64 = 64


@unique
class CooldownBypassType(IntEnum):
    # Cooldown can be bypassed by expending an endurance charge
    expend_endurance_charge = 1,
    # Cooldown can be bypassed by expending a frenzy charge
    expend_frenzy_charge = 2,
    # Cooldown can be bypassed by expending a power charge
    expend_power_charge = 3,
    # Cooldown can not be bypassed
    none = 4


@unique
class ReleaseState(Enum):
    # Item never existed in any released version of the game.
    unreleased = 0,
    # Item currently exists in the in-game.
    released = 1,
    # Item can no longer be obtained (excluding via trade from other players).
    legacy = 2


# gems that could never drop (unreleased mod only effects are not listed)
UNRELEASED_GEMS = {
    # active gems that are not released
    "AncestorTotemSlash",
    "Backstab",
    "BladeTrap",
    "ComboStrike",
    "DamageInfusion",
    "ElementalProjectiles",
    "EnergyBeam",
    "FireWeapon",
    "HeraldOfBlood",
    "Icefire",
    "Ignite",
    "InfernalSwarm",
    "LightningChannel",
    "LightningCircle",
    "RighteousLightning",
    "Riptide",
    "ShadowBlades",
    "SkeletalChains",
    "Snipe",
    "StaticTether",
    "SummonSkeletonsChannelled",
    "ThrownShield",
    "TouchOfGod",
    "VaalFireTrap",
    "VaalHeavyStrike",
    "VaalSoulHarvesting",
    "VaalSweep",
    "VortexMine",
    "WandTeleport",
    # support gems that are not released
    "SupportCastLinkedCursesOnCurse",
    "SupportReturn",
    "SupportSplit",
    "SupportTutorial",
    # rework WIP versions (gems without 'New' in front exist)
    "NewArcticArmour",
    "NewNewBladeVortex",
    # "NewPhaseRun",  ('PhaseRun' does not exist)
    "NewPunishment",
    # "NewShieldCharge",  ('ShieldCharge' does not exist)
    "NewShockNova",
}

# gems that can no longer be obtained
LEGACY_GEMS = {
    "SupportItemQuantity"
}
