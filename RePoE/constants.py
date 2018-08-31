from enum import IntEnum, unique, Enum


@unique
class ActiveSkillType(IntEnum):
    # Gem tag equivalent
    attack = 1
    # Gem tag equivalent
    spell = 2
    # Skills fires projectiles
    projectile = 3
    # Skill can only be used when dual wielding (Dual Strike only atm)
    dual_wield_only = 4
    # Skill gives a buff (Molten Shell and golems do not have this type)
    buff = 5
    # Skill only uses main hand when dual wielding
    uses_main_hand_when_dual_wielding = 6
    # Only set for Cleave. Probably replaced by the skill_double_hits_when_dual_wielding stat.
    uses_both_at_once_when_dual_wielding = 7
    # Gem tag equivalent
    minion = 8
    # Set for skills that hit and are not attacks
    hits = 9
    # Gem tag equivalent
    aoe = 10
    # Gem tag equivalent
    duration = 11
    # Skill can only be used when a shield is equipped
    shield_only = 12
    # Set for bow skills without projectile tag (implicit in projectile);
    # allows Faster/Slower Projectiles Support
    explicit_deals_projectile_damage = 13
    # The skill's mana cost is reserved on casting
    # Can also be interpreted as "skill is toggle".
    # Ignore this for totems, Rejuvenation Totem has this type but is no reservation/toggle skill.
    mana_cost_is_reservation = 14
    # Skill costs percentage mana
    mana_cost_is_percentage = 15
    # Skill can be turned into a trap with Trap Support
    trap_supportable = 16
    # Skill can be turned into a totem with Spell Totem Support
    spell_totem_supportable = 17
    # Skill can be turned into a mine with Remote Mine Support
    remote_mine_supportable = 18
    # Set for Herald of Ash, which cannot hit but causes elemental status effects (implicit in hit);
    # allows Elemental Proliferation Support
    explicit_causes_elemental_status = 19
    # Skill summons mobs
    summons_mobs = 20
    # Skill can be turned into a totem with Ranged Attack Totem Support
    ranged_attack_totem_supportable = 21
    # Gem tag equivalent
    chaining = 22
    # Gem tag equivalent
    melee = 23
    # Skill is melee and the initial (or only) hit is single target; allows Melee Splash Support
    melee_single_target_initial_hit = 24
    # Skill can be repeated with Spell Echo Support
    spell_echo_supportable = 25
    # Set for all skills with mana_cost_is_reservation, plus vaal auras and a few more;
    # unknown purpose
    unknown_26 = 26
    # Skill can be repeated with Multistrike Support
    multistrike_supportable = 27
    # Skill directly applies burning (fire damage over time)
    applies_burning = 28
    # Gem tag equivalent
    totem = 29
    # Set for Molten Shell, Vaal Molten Shell and Of Thunder glove enchant; added by Blasphemy Support; unknown purpose
    unknown_30 = 30
    # Gem tag equivalent
    curse = 31
    # Gem tag equivalent
    fire = 32
    # Gem tag equivalent
    cold = 33
    # Gem tag equivalent
    lightning = 34
    # Skill can be triggered by trigger gems
    triggerable = 35
    # Gem tag equivalent
    trap = 36
    # Gem tag equivalent
    movement = 37
    # Skill directly deals damage over time
    deals_damage_over_time = 38
    # Gem tag equivalent
    mine = 39
    # Gem has Trigger tag and is a spell
    # (missing EnchantmentOfFlamesOnHit and EnchantmentOfTempestOnHit)
    trigger_spell = 40
    # Gem tag equivalent
    vaal = 41
    # Gem tag equivalent
    aura = 42
    # Skill can be cast by Mjölner's trigger when socketed in it
    castable_by_mjolner = 43
    # Unused for skill gems
    unknown_46 = 44
    # Gem has Trigger tag and is an attack
    trigger_attack = 45
    # Skill is a projectile attack;
    # allows Iron Grip, Physical Projectile Attack Damage and Point Blank Support
    projectile_attack = 46
    # Skill can be cast by Null's Inclination's trigger when socketed in it
    castable_by_nulls_inclination = 47
    # Gem tag equivalent
    chaos = 48
    # Unused for processed active skills; excluded by Faster and Slower Projectiles Support
    unknown_49 = 49
    # Allows Iron Will Support for skills that don't have hits but should be supportable, e.g. Blight
    iron_will_supportable_not_hit = 50
    # Set for Burning Arrow, Cleave, Dual Strike, Glacial Hammer, Vigilant Strike;
    # these have threshold jewels that add AoE components;
    # allows Increased AoE and Concentrated Effect Support
    can_have_aoe = 51
    # Set in minion_types for skills that summon minions that might use projectile skills, e.g. Animate Weapon.
    # Allows the same support gems as the projectile tag.
    minion_maybe_projectile = 52
    # Set for Burning Arrow, Vaal Burning Arrow;
    # these have threshold jewels that add duration components;
    # allows Increased/Less Duration and Rapid Decay Support
    can_have_duration = 53
    # Set for Animate Weapon and related item skills (the triggered version, Animate Guardian's Weapon).
    # Allows some projectile and attack related supports.
    animate_weapon = 54
    # Same as trigger_attack plus Blast Rain; unknown purpose
    unknown_55 = 55
    # Gem tag equivalent
    channelling = 56
    # Allows Controlled Destruction Support for skills that don't have attack or hits but should be supportable, e.g.
    # Blight. Also allows Iron Will Support. Only Siphoning Trap has this tag and not iron_will_supportable_not_hit.
    controlled_destruction_supportable_not_hit = 57
    # Skill can be cast by Cospri's Malice's trigger when socketed in it
    castable_by_cospris_malice = 58
    # Set for automatically triggered spells granted by item;
    # prevents Cast on/when/while x, Spell Totem, Remote Mine and Trap Support
    trigger_item_granted = 59
    # Gem tag equivalent
    golem = 60
    # Gem tag equivalent
    herald = 61
    # Used for Death's Oath's aura and added by Blasphemy
    aura_debuff = 62
    # Skill can not be supported by Ruthless Support. Only used for Cyclone and Vaal Cyclone.
    not_ruthless_supportable = 63
    # Set for the minions of Summon Skeleton and Vaal Summon Skeletons; required by Iron Will Support
    iron_will_supportable_minion = 64
    # Skill can be supported by Spell Cascade Support. Seems to be only set for very few spells?
    spell_cascade_supportable = 65
    # Skill can be supported by Volley Support
    volley_supportable = 66
    # Skill can be supported by Mirage Archer Support
    mirage_archer_supportable = 67
    # Set for Vaal Fireball and Vaal Spark, disallows Volley Support
    volley_exclude_68 = 68
    # Set for Spectral Shield Throw, disallows Volley Support
    volley_exclude_69 = 69
    # Set for Manifest Dancing Dervish, disallows Summon Phantasm on Kill Support
    phantasm_on_kill_exclude = 70
    # Set for Rain of Arrows and Vaal Rain of Arrows, allows Lesser and Greater Multiple Projectiles
    rain_of_arrows = 71


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
    legacy = 2,
    # Item can only be obtained with unique rarity (and is not unreleased).
    # If the unique is not always corrupted (as for Ruby Amulet's unique), a non-unique item with
    # the base can be obtained by corrupting uniques to rares.
    unique_only = 3


# Base items with with ReleaseState.unreleased
UNRELEASED_ITEMS = {
    "Metadata/Items/Rings/RingVictor1",  # Jet Ring
    "Metadata/Items/Classic/MysteryLeaguestone",
    "Metadata/Items/Armours/BodyArmours/BodyStrTemp",
    "Metadata/Items/Armours/Boots/BootsStrTemp",
    # Keyblade, one item existed in closed-beta
    "Metadata/Items/Weapons/TwoHandWeapons/TwoHandSwords/TwoHandSwordDev",
    # Gems
    "Metadata/Items/Gems/SkillGemSlashTotem",
    "Metadata/Items/Gems/SkillGemBackstab",
    "Metadata/Items/Gems/SkillGemBladeTrap",
    "Metadata/Items/Gems/SkillGemComboStrike",
    "Metadata/Items/Gems/SkillGemDamageInfusion",
    "Metadata/Items/Gems/SkillGemDiscorectangleSlam",
    "Metadata/Items/Gems/SkillGemElementalProjectiles",
    "Metadata/Items/Gems/SkillGemFireWeapon",
    "Metadata/Items/Gems/SkillGemHeraldOfBlood",
    "Metadata/Items/Gems/SkillGemIcefire",
    "Metadata/Items/Gems/SkillGemIgnite",
    "Metadata/Items/Gems/SkillGemInfernalSwarm",
    "Metadata/Items/Gems/SkillGemInfernalSweep",
    "Metadata/Items/Gems/SkillGemLightningChannel",
    "Metadata/Items/Gems/SkillGemLightningCircle",
    "Metadata/Items/Gems/SkillGemNewBladeVortex",
    "Metadata/Items/Gems/SkillGemNewPunishment",
    "Metadata/Items/Gems/SkillGemNewShockNova",
    "Metadata/Items/Gems/SkillGemRighteousLightning",
    "Metadata/Items/Gems/SkillGemRiptide",
    "Metadata/Items/Gems/SkillGemShadowBlades",
    "Metadata/Items/Gems/SkillGemSnipe",
    "Metadata/Items/Gems/SkillGemSpectralSpinningWeapon",
    "Metadata/Items/Gems/SkillGemStaticTether",
    "Metadata/Items/Gems/SkillGemSummonSkeletonsChannelled",
    "Metadata/Items/Gems/SkillGemTouchOfGod",
    "Metadata/Items/Gems/SkillGemVaalAncestralWarchief",
    "Metadata/Items/Gems/SkillGemVaalFleshOffering",
    "Metadata/Items/Gems/SkillGemVaalFireTrap",
    "Metadata/Items/Gems/SkillGemVaalHeavyStrike",
    "Metadata/Items/Gems/SkillGemVaalSweep",
    "Metadata/Items/Gems/SkillGemVortexMine",
    "Metadata/Items/Gems/SkillGemWandTeleport",
    "Metadata/Items/Gems/SupportGemCastLinkedCursesOnCurse",
    "Metadata/Items/Gems/SupportGemReturn",
    "Metadata/Items/Gems/SupportGemSplit",
    "Metadata/Items/Gems/SupportGemTemporaryForTutorial",
    "Metadata/Items/Gems/SupportGemVaalSoulHarvesting",
    # Prototype Incursion currency?
    "Metadata/Items/Currency/CurrencyIncursionCorrupt1",
    "Metadata/Items/Currency/CurrencyIncursionCorrupt2",
    "Metadata/Items/Currency/CurrencyIncursionCorruptGem",
}

# Base items with with ReleaseState.legacy
LEGACY_ITEMS = {
    "Metadata/Items/Currency/CurrencyImprintOrb",  # Eternal Orb
    "Metadata/Items/Currency/CurrencyImprint",  # Eternal Orb imprint
    "Metadata/Items/DivinationCards/DivinationCardBirthOfTheThree",
    "Metadata/Items/Gems/SupportGemItemQuantity",
    # Legacy Quivers
    "Metadata/Items/Quivers/Quiver1",
    "Metadata/Items/Quivers/Quiver2",
    "Metadata/Items/Quivers/Quiver3",
    "Metadata/Items/Quivers/Quiver4",
    "Metadata/Items/Quivers/Quiver5",
}

# Base items with with ReleaseState.unique_only
UNIQUE_ONLY_ITEMS = {
    "Metadata/Items/Amulet/AmuletVictor1",  # Jet Amulet, base for Amulet of the Victor (PvP reward)
    "Metadata/Items/Amulets/Amulet11",  # Ruby Amulet
    "Metadata/items/Weapons/OneHandWeapons/OneHandSwords/OneHandSwordC",  # Charan's Sword
    "Metadata/Items/Quivers/QuiverDescent",  # Base for a Descent only unique
    "Metadata/Items/Jewels/JewelPrismatic",
    # Race rewards (bases of Demigod uniques)
    "Metadata/Items/Belts/BeltDemigods1",
    "Metadata/Items/Rings/RingDemigods1",
    "Metadata/Items/Armours/Shields/ShieldDemigods",
    "Metadata/Items/Armours/Boots/BootsDemigods1",
    "Metadata/Items/Armours/BodyArmours/BodyDemigods1",
    "Metadata/Items/Armours/Gloves/GlovesDemigods1",
    "Metadata/Items/Armours/Helmets/HelmetWreath1",
}
