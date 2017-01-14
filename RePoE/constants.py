from enum import IntEnum, unique, Enum


@unique
class ActiveSkillType(IntEnum):
    # Gem tag equivalent
    ATTACK = 1
    # Gem tag equivalent
    SPELL = 2
    # Gem tag equivalent
    PROJECTILE = 3
    # Skill can only be used when dual wielding (Dual Strike only atm)
    DUAL_WIELD_ONLY = 4
    # Skill gives a buff (Molten Shell and golems do not have this type)
    BUFF = 5
    # Skill can be used when dual wielding
    # When it does not have either of the following two, hands are random (Reckoning, Whirling Blades) or alternating
    # (everything else).
    CAN_DUAL_WIELD = 6
    # Skill only uses main hand when dual wielding
    USES_MAIN_HAND_WHEN_DUAL_WIELDING = 7
    # Skill uses both hands at once when dual wielding (missing Riposte)
    USES_BOTH_AT_ONCE_WHEN_DUAL_WIELDING = 8
    # Gem tag equivalent
    MINION = 9
    # Seems to be set for skills that are not attacks and deal non-duration damage, unknown purpose.
    UNKNOWN_10 = 10
    # Gem tag equivalent
    AOE = 11
    # Gem tag equivalent
    DURATION = 12
    # Skill can only be used when a shield is equipped
    SHIELD_ONLY = 13
    # Set for bow skills where arrows come from above, unknown purpose
    UNKNOWN_14 = 14
    # The skill's mana cost is reserved on casting
    # Can also be interpreted as "skill is toggle".
    # Ignore this for totems, Rejuvenation Totem has this type but is no reservation/toggle skill.
    MANA_COST_IS_RESERVATION = 15
    # Skill costs percentage mana
    MANA_COST_IS_PERCENTAGE = 16
    # Skill can be turned into a trap with Trap Support
    TRAP_SUPPORTABLE = 17
    # Skill can be turned into a totem with Spell Totem Support
    SPELL_TOTEM_SUPPORTABLE = 18
    # Skill can be turned into a mine with Remote Mine Support
    REMOTE_MINE_SUPPORTABLE = 19
    # Only set for Herald of Ash
    UNKNOWN_20 = 20
    # Skill summons mobs
    SUMMONS_MOBS = 21
    # Skill can be turned into a totem with Ranged Attack Totem Support
    RANGED_ATTACK_TOTEM_SUPPORTABLE = 22
    # Gem tag equivalent
    CHAINING = 23
    # Gem tag equivalent
    MELEE = 24
    # Skill is melee and the initial (or only) hit is single target
    MELEE_SINGLE_TARGET_INITIAL_HIT = 25
    # Skill can be repeated with Spell Echo Support
    SPELL_ECHO_SUPPORTABLE = 26
    # Set for all skills with `PERMANENT_BUFF`, plus vaal auras and a few more, unkown purpose
    UNKNOWN_27 = 27
    # Skill can be repeated with Multistrike Support
    MULTISTRIKE_SUPPORTABLE = 28
    # Skill directly applies burning (fire damage over time)
    APPLIES_BURING = 29
    # Gem tag equivalent
    TOTEM = 30
    # Set for Molten Shell, Vaal Molten Shell and Of Thunder glove enchant, unknown purpose
    UNKNOWN_31 = 31
    # Gem tag equivalent
    CURSE = 32
    # Gem tag equivalent
    FIRE = 33
    # Gem tag equivalent
    COLD = 34
    # Gem tag equivalent
    LIGHTNING = 35
    # Skill can be triggered by trigger gems
    TRIGGERABLE = 36
    # Gem tag equivalent
    TRAP = 37
    # Gem tag equivalent
    MOVEMENT = 38
    # Gem tag equivalent
    CAST = 39
    # Skill directly deals damage over time
    DEALS_DAMAGE_OVER_TIME = 40
    # Gem tag equivalent
    MINE = 41
    # Gem has Trigger tag and is a spell (missing EnchantmentOfFlamesOnHit and EnchantmentOfTempestOnHit)
    TRIGGER_SPELL = 42
    # Gem tag equivalent
    VAAL = 43
    # Gem tag equivalent
    AURA = 44
    # Skill can be cast by Mjölner's trigger when socketed in it
    CASTABLE_BY_MJOLNER = 45
    # Unused for skill gems
    UNKNOWN_46 = 46
    # Gem has Trigger tag and is an attack
    TRIGGER_ATTACK = 47
    # Skill can be supported with Physical Projectile Attack Damage Support
    PPAD_SUPPORTABLE = 48
    # Skill can be cast by Null's Inclination's trigger when socketed in it
    CASTABLE_BY_NULLS_INCLINATION = 49
    # Gem tag equivalent
    CHAOS = 50
    # Unused for skill gems
    UNKNOWN_51 = 51
    # Set for Blight, Contagion, Scorching Ray, unknown purpose
    UNKNOWN_52 = 52
    # Set for Burning Arrow, Vigilant Strike, unknown purpose
    UNKNOWN_53 = 53
    # Unused for skill gems
    UNKNOWN_54 = 54
    # Set for Burning Arrow, Vaal Burning Arrow, unknown purpose
    UNKNOWN_55 = 55
    # Unused for skill gems
    UNKNOWN_56 = 56
    # Same as TRIGGER_ATTACK (47), unknown purpose
    UNKNOWN_57 = 57
    # Gem tag equivalent
    CHANNELLING = 58
    # Set for Blight, Contagion, Scorching Ray, unknown purpose
    UNKNOWN_59 = 59
    # Skill can be cast by Cospri's Malice's trigger when socketed in it
    CASTABLE_BY_COSPRIS_MALICE = 60


@unique
class CooldownBypassType(IntEnum):
    # Cooldown can be bypassed by expending an endurance charge
    EXPEND_ENDURANCE_CHARGE = 1,
    # Cooldown can be bypassed by expending a frenzy charge
    EXPEND_FRENZY_CHARGE = 2,
    # Cooldown can be bypassed by expending a power charge
    EXPEND_POWER_CHARGE = 3,
    # Cooldown can not be bypassed
    NONE = 4


@unique
class ReleaseState(Enum):
    # Item never existed in any released version of the game.
    UNRELEASED = 0,
    # Item currently exists in the in-game.
    RELEASED = 1,
    # Item can no longer be obtained (excluding via trade from other players).
    LEGACY = 2


# gems that could never drop (unreleased mod only effects are not listed)
UNRELEASED_GEMS = {
    # active gems that are not released
    "AncestorTotemSlash",
    "Backstab",
    "BladeTrap",
    "ComboStrike",
    "DamageInfusion",
    "EnergyBeam",
    "FireWeapon",
    "HeraldOfBlood",
    "LightningChannel",
    "LightningCircle",
    "RighteousLightning",
    "Riptide",
    "ShadowBlades",
    "Snipe",
    "StaticTether",
    "VaalFireTrap",
    "VaalHeavyStrike",
    "VaalSweep",
    "VortexMine",
    "WandTeleport",
    # support gems that are not released
    "SupportCastLinkedCursesOnCurse",
    "SupportReturn",
    "SupportSplit",
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
