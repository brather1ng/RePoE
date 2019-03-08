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
    # Gem tag equivalent
    minion = 6
    # Set for skills that hit and are not attacks
    hits = 7
    # Gem tag equivalent
    aoe = 8
    # Gem tag equivalent
    duration = 9
    # Skill can only be used when a shield is equipped
    shield_only = 10
    # Set for bow skills without projectile tag (implicit in projectile);
    # allows Faster/Slower Projectiles Support
    explicit_deals_projectile_damage = 11
    # The skill's mana cost is reserved on casting
    # Can also be interpreted as "skill is toggle".
    # Ignore this for totems, Rejuvenation Totem has this type but is no reservation/toggle skill.
    mana_cost_is_reservation = 12
    # Skill costs percentage mana
    mana_cost_is_percentage = 13
    # Skill can be turned into a trap with Trap Support
    trap_supportable = 14
    # Skill can be turned into a totem with Spell Totem Support
    spell_totem_supportable = 15
    # Skill can be turned into a mine with Remote Mine Support
    remote_mine_supportable = 16
    # Set for Herald of Ash, which cannot hit but causes elemental status effects (implicit in hit);
    # allows Elemental Proliferation Support
    explicit_causes_elemental_status = 17
    # Skill summons mobs
    summons_mobs = 18
    # Skill can be turned into a totem with Ranged Attack Totem Support
    ranged_attack_totem_supportable = 19
    # Gem tag equivalent
    chaining = 20
    # Gem tag equivalent
    melee = 21
    # Skill is melee and the initial (or only) hit is single target; allows Melee Splash Support
    melee_single_target_initial_hit = 22
    # Skill can be repeated with Spell Echo Support
    spell_echo_supportable = 23
    # Set for all skills with mana_cost_is_reservation, plus vaal auras and a few more;
    # unknown purpose
    unknown_24 = 24
    # Skill can be repeated with Multistrike Support
    multistrike_supportable = 25
    # Skill directly applies burning (fire damage over time)
    applies_burning = 26
    # Gem tag equivalent
    totem = 27
    # Set for Molten Shell, Vaal Molten Shell and Of Thunder glove enchant; added by Blasphemy Support; unknown purpose
    unknown_28 = 28
    # Gem tag equivalent
    curse = 29
    # Gem tag equivalent
    fire = 30
    # Gem tag equivalent
    cold = 31
    # Gem tag equivalent
    lightning = 32
    # Skill can be triggered by trigger gems
    triggerable = 33
    # Gem tag equivalent
    trap = 34
    # Gem tag equivalent
    movement = 35
    # Skill directly deals damage over time
    deals_damage_over_time = 36
    # Gem tag equivalent
    mine = 37
    # Gem has Trigger tag and is a spell
    # (missing EnchantmentOfFlamesOnHit and EnchantmentOfTempestOnHit)
    trigger_spell = 38
    # Gem tag equivalent
    vaal = 39
    # Gem tag equivalent
    aura = 40
    # Skill can be cast by Mjölner's trigger when socketed in it
    castable_by_mjolner = 41
    # Unused for skill gems
    unknown_42 = 42
    # Gem has Trigger tag and is an attack
    trigger_attack = 43
    # Skill is a projectile attack;
    # allows Iron Grip, Physical Projectile Attack Damage and Point Blank Support
    projectile_attack = 44
    # Skill can be cast by Null's Inclination's trigger when socketed in it
    castable_by_nulls_inclination = 45
    # Gem tag equivalent
    chaos = 46
    # Unused for processed active skills; excluded by Faster and Slower Projectiles Support
    unknown_47 = 47
    # Allows Iron Will Support for skills that don't have hits but should be supportable, e.g. Blight
    iron_will_supportable_not_hit = 48
    # Set for Burning Arrow, Cleave, Dual Strike, Glacial Hammer, Vigilant Strike;
    # these have threshold jewels that add AoE components;
    # allows Increased AoE and Concentrated Effect Support
    can_have_aoe = 49
    # Set in minion_types for skills that summon minions that might use projectile skills, e.g. Animate Weapon.
    # Allows the same support gems as the projectile tag.
    minion_maybe_projectile = 50
    # Set for Burning Arrow, Vaal Burning Arrow;
    # these have threshold jewels that add duration components;
    # allows Increased/Less Duration and Rapid Decay Support
    can_have_duration = 51
    # Set for Animate Weapon and related item skills (the triggered version, Animate Guardian's Weapon).
    # Allows some projectile and attack related supports.
    animate_weapon = 52
    # Skill can be cast by Maloney's Mechanism's trigger when socketed in it
    castable_by_maloneys_mechanism = 53
    # Gem tag equivalent
    channelling = 54
    # Allows Controlled Destruction Support for skills that don't have attack or hits but should be supportable, e.g.
    # Blight. Also allows Iron Will Support. Only Siphoning Trap has this tag and not iron_will_supportable_not_hit.
    controlled_destruction_supportable_not_hit = 55
    # Skill can be cast by Cospri's Malice's trigger when socketed in it
    castable_by_cospris_malice = 56
    # Set for automatically triggered spells granted by item;
    # prevents Cast on/when/while x, Spell Totem, Remote Mine and Trap Support
    trigger_item_granted = 57
    # Gem tag equivalent
    golem = 58
    # Gem tag equivalent
    herald = 59
    # Used for Death's Oath's aura and added by Blasphemy
    aura_debuff = 60
    # Skill can not be supported by Ruthless Support. Only used for Cyclone and Vaal Cyclone.
    not_ruthless_supportable = 61
    # Set for the minions of Summon Skeleton and Vaal Summon Skeletons; required by Iron Will Support
    iron_will_supportable_minion = 62
    # Skill can be supported by Spell Cascade Support. Seems to be only set for very few spells?
    spell_cascade_supportable = 63
    # Skill can be supported by Volley Support
    volley_supportable = 64
    # Skill can be supported by Mirage Archer Support
    mirage_archer_supportable = 65
    # Set for Vaal Fireball and Vaal Spark, disallows Volley Support
    volley_exclude_66 = 66
    # Set for Spectral Shield Throw, disallows Volley Support
    volley_exclude_67 = 67
    # Set for Manifest Dancing Dervish, disallows Summon Phantasm on Kill Support
    phantasm_on_kill_exclude = 68
    # Set for Rain of Arrows and Vaal Rain of Arrows, allows Lesser and Greater Multiple Projectiles
    rain_of_arrows = 69
    # Gem tag equivalent
    warcry = 70
    # Skill cast is instant
    instant = 71
    # Set for the brand skills, not Brand Recall
    brand = 72
    # Set for Detonated Dead, unknown purpose
    unknown_73 = 73
    # Skill chills without counting as a hit
    non_hit_chill = 74
    # Skill creates chilling areas
    chilling_area = 75
    # Skill is a Curse (compared to "curse", Bane and Raise Spectre's minions don't have this)
    curse_skill = 76
    # Skill can be supported by Unleash Support
    unleash_supportable = 77
    # Added and allowed by SupportAuraDuration, not used anywhere else.
    unknown_78 = 78
    # Skill can be supported by Intensify Support
    intensify_supportable = 79
    # Allowed by SupportAuraDuration, not used anywhere else.
    unknown_80 = 80
    # Allowed by SupportAuraDuration and Maloney's Mechanism's trigger skill, not used anywhere else.
    unknown_81 = 81
    # Allowed by SupportAuraDuration, not used anywhere else.
    unknown_82 = 82


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


# Base items with ReleaseState.unreleased
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
    "Metadata/Items/Gems/SkillGemCaptureMonster",
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
    "Metadata/Items/Gems/SkillGemRendingSteel",
    "Metadata/Items/Gems/SkillGemRighteousLightning",
    "Metadata/Items/Gems/SkillGemRiptide",
    "Metadata/Items/Gems/SkillGemShadowBlades",
    "Metadata/Items/Gems/SkillGemSnipe",
    "Metadata/Items/Gems/SkillGemSpectralSpinningWeapon",
    "Metadata/Items/Gems/SkillGemStaticTether",
    "Metadata/Items/Gems/SkillGemSummonSkeletonsChannelled",
    "Metadata/Items/Gems/SkillGemTouchOfGod",
    "Metadata/Items/Gems/SkillGemVaalFleshOffering",
    "Metadata/Items/Gems/SkillGemVaalFireTrap",
    "Metadata/Items/Gems/SkillGemVaalHeavyStrike",
    "Metadata/Items/Gems/SkillGemVaalSweep",
    "Metadata/Items/Gems/SkillGemVortexMine",
    "Metadata/Items/Gems/SkillGemWandTeleport",
    "Metadata/Items/Gems/SupportGemCastLinkedCursesOnCurse",
    "Metadata/Items/Gems/SupportGemHandcastRapidFire",
    "Metadata/Items/Gems/SupportGemReturn",
    "Metadata/Items/Gems/SupportGemSplit",
    "Metadata/Items/Gems/SupportGemTemporaryForTutorial",
    "Metadata/Items/Gems/SupportGemVaalSoulHarvesting",
    # Prototype Incursion currency?
    "Metadata/Items/Currency/CurrencyIncursionCorrupt1",
    "Metadata/Items/Currency/CurrencyIncursionCorrupt2",
    "Metadata/Items/Currency/CurrencyIncursionCorruptGem",
}

# Base items with ReleaseState.legacy
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

# Base items with ReleaseState.unique_only
UNIQUE_ONLY_ITEMS = {
    "Metadata/Items/Amulet/AmuletVictor1",  # Jet Amulet, base for Amulet of the Victor (PvP reward)
    "Metadata/Items/Amulets/Amulet11",  # Ruby Amulet
    "Metadata/items/Weapons/OneHandWeapons/OneHandSwords/OneHandSwordC",  # Charan's Sword
    "Metadata/Items/Quivers/Quiver14",  # Ornate Quiver, base for Maloney's Mechanism
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
