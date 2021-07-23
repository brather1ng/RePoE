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
    # Skill can be turned into a totem with Spell Totem Support or Ranged Attack Totem Support
    totem_supportable = 15
    # Skill can be turned into a mine with Remote Mine Support
    remote_mine_supportable = 16
    # Set for Herald of Ash, which cannot hit but causes elemental status effects (implicit in hit);
    # allows Elemental Proliferation Support
    explicit_causes_elemental_status = 17
    # Skill summons minions and can be supported by Concentrated Effect Support and Increased Area of Effect Support
    aoe_supportable_minion = 18
    # Gem tag equivalent
    chaining = 19
    # Gem tag equivalent
    melee = 20
    # Skill is melee and the initial (or only) hit is single target; allows Melee Splash Support
    melee_single_target_initial_hit = 21
    # Skill can be repeated with Spell Echo Support
    spell_echo_supportable = 22
    # Set for all skills with mana_cost_is_reservation, plus vaal auras and a few more;
    # unknown purpose
    unknown_23 = 23
    # Skill can be repeated with Multistrike Support
    multistrike_supportable = 24
    # Skill directly applies burning (fire damage over time)
    applies_burning = 25
    # Gem tag equivalent
    totem = 26
    # Set for Molten Shell, Vaal Molten Shell and Of Thunder glove enchant; added by Blasphemy Support; unknown purpose
    unknown_27 = 27
    # Gem tag equivalent
    physical = 28
    # Gem tag equivalent
    fire = 29
    # Gem tag equivalent
    cold = 30
    # Gem tag equivalent
    lightning = 31
    # Skill can be triggered by trigger gems
    triggerable = 32
    # Gem tag equivalent
    trap = 33
    # Gem tag equivalent
    movement = 34
    # Skill directly deals damage over time
    deals_damage_over_time = 35
    # Gem tag equivalent
    mine = 36
    # Skill is triggered
    triggered = 37
    # Gem tag equivalent
    vaal = 38
    # Gem tag equivalent
    aura = 39
    # Unused for skill gems
    unknown_40 = 40
    # Skill is a projectile attack;
    # allows Iron Grip, Physical Projectile Attack Damage and Point Blank Support
    projectile_attack = 41
    # Gem tag equivalent
    chaos = 42
    # Unused for processed active skills; excluded by Faster and Slower Projectiles Support
    unknown_43 = 43
    # Set for Burning Arrow, Cleave, Dual Strike, Glacial Hammer, Vigilant Strike;
    # these have threshold jewels that add AoE components;
    # allows Increased AoE and Concentrated Effect Support
    can_have_aoe = 44
    # Set in minion_types for skills that summon minions that might use projectile skills, e.g. Animate Weapon.
    # Allows the same support gems as the projectile tag.
    minion_maybe_projectile = 45
    # Set for Burning Arrow, Vaal Burning Arrow;
    # these have threshold jewels that add duration components;
    # allows Increased/Less Duration and Rapid Decay Support
    can_have_duration = 46
    # Set for Animate Weapon and related item skills (the triggered version, Animate Guardian's Weapon).
    # Allows some projectile and attack related supports.
    animate_weapon = 47
    # Gem tag equivalent
    channelling = 48
    # Allows Controlled Destruction Support for skills that don't have attack or hits but should be supportable, e.g.
    # Blight. Also allows Iron Will Support. Only Siphoning Trap has this tag and not iron_will_supportable_not_hit.
    controlled_destruction_supportable_not_hit = 49
    # Set for automatically triggered spells granted by item;
    # prevents Cast on/when/while x, Spell Totem, Remote Mine and Trap Support
    trigger_item_granted = 50
    # Gem tag equivalent
    golem = 51
    # Gem tag equivalent
    herald = 52
    # Used for Death's Oath's aura and added by Blasphemy
    aura_debuff = 53
    # Skill can not be supported by Ruthless Support. Only used for Cyclone and Vaal Cyclone.
    not_ruthless_supportable = 54
    # Set for the minions of Summon Skeleton and Vaal Summon Skeletons; required by Iron Will Support
    iron_will_supportable_minion = 55
    # Skill can be supported by Spell Cascade Support. Seems to be only set for very few spells?
    spell_cascade_supportable = 56
    # Skill can be supported by Volley Support
    volley_supportable = 57
    # Skill can be supported by Mirage Archer Support
    mirage_archer_supportable = 58
    # Set for Vaal Fireball and Vaal Spark, disallows Volley Support
    volley_exclude_59 = 59
    # Set for Spectral Shield Throw, disallows Volley Support
    volley_exclude_60 = 60
    # Set for Manifest Dancing Dervish, disallows Summon Phantasm on Kill Support
    phantasm_on_kill_exclude = 61
    # Set for Rain of Arrows and Vaal Rain of Arrows, allows Lesser and Greater Multiple Projectiles
    rain_of_arrows = 62
    # Gem tag equivalent
    warcry = 63
    # Skill cast is instant
    instant = 64
    # Set for the brand skills, not Brand Recall
    brand = 65
    # Set for Detonated Dead, unknown purpose
    unknown_66 = 66
    # Skill chills without counting as a hit
    non_hit_chill = 67
    # Skill creates chilling areas
    chilling_area = 68
    # Skill is a Curse (compared to "curse", Bane and Raise Spectre's minions don't have this)
    curse_skill = 69
    # Skill can be supported by Unleash Support
    unleash_supportable = 70
    # Added and allowed by SupportAuraDuration, not used anywhere else.
    unknown_71 = 71
    # Skill can be supported by Intensify Support
    intensify_supportable = 72
    # These three types change how allowed_types and excluded_types of support gems are interpreted. The types are
    # processed in
    # order. Except for the following three, they are checked against the active skill's types and the result (true or
    # false) is pushed onto a stack. These three types instead change the values that are already on the stack:
    # - Pops two values from the stack and pushes the result of or'ing them
    boolean_or = 73
    # - Pops two values from the stack and pushes the result of and'ing them
    boolean_and = 74
    # - Pops one value from the stack and pushes the inverted value
    boolean_not = 75
    # Skill is no attack but can be supported by Maim Support
    maim_supportable_aura = 76
    # Skill summons mions
    summons_minions = 77
    # Gem tag equivalent
    guard = 78
    # Gem tag equivalent
    travel = 79
    # Gem tag equivalent
    blink = 80
    aura_duration_supportable = 81
    # Skill fires secondary projectiles and can't be supported by Arrow Nova or Volley Support
    secondary_projectile = 82
    # Skill is a ballista totem skill (natively, not via support gem)
    ballista = 83
    # Gem tag equivalent
    nova = 84
    # Similar to buff, not used on support gems
    unknown_85 = 85
    # Similar to buff, not used on support gems
    unknown_86 = 86
    # Set for 4 of the 5 mine active skill gems (not for Smoke Mine), which all deal damage
    damaging_mine = 87
    # Gem tag equivalent (not translated, see gem_tags.json)
    banner = 88
    # Set for the Bow skills that shoot upwards (Rain of Arrows, Blast Rain, Mirror Arrow, Blink Arrow)
    shoots_arrows_upwards = 89
    # Allows Second Wind Support
    second_wind_supportable = 90
    # Set for Molten Strike, allows Chain Support without the Chaining type/tag
    chain_supportable = 91
    # Set for Vaal skills, excludes Archmage Support
    archmage_exclude = 92
    # Allows Fist of War Support; set for all Slam skills except Vaal Ancestral Warchief
    fist_of_war_supportable = 93
    # Gem tag equivalent
    stance = 94
    # Added by GeneralsCrySupport, excludes Multistrike Support and Spell Echo Support
    generals_cry_support_repeat_exclude = 95
    # Added by GeneralsCrySupport, excludes Fist of War Support
    generals_cry_support_fist_of_war_exclude = 96
    steel = 97
    hex = 98
    mark = 99
    aegis = 100
    orb = 101


@unique
class CooldownBypassType(IntEnum):
    # Cooldown can be bypassed by expending an endurance charge
    expend_endurance_charge = (1,)
    # Cooldown can be bypassed by expending a frenzy charge
    expend_frenzy_charge = (2,)
    # Cooldown can be bypassed by expending a power charge
    expend_power_charge = (3,)
    # Cooldown can not be bypassed
    none = 4


@unique
class ReleaseState(Enum):
    # Item never existed in any released version of the game.
    unreleased = (0,)
    # Item currently exists in the in-game.
    released = (1,)
    # Item can no longer be obtained (excluding via trade from other players).
    legacy = (2,)
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
    "Metadata/Items/Gems/SkillGemBlitz",
    "Metadata/Items/Gems/SkillGemBloodWhirl",
    "Metadata/Items/Gems/SkillGemBoneArmour",
    "Metadata/Items/Gems/SkillGemCaptureMonster",
    "Metadata/Items/Gems/SkillGemCoilingAssault",
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
    "Metadata/Items/Gems/SkillGemQuickBlock",
    "Metadata/Items/Gems/SkillGemProjectilePortal",
    "Metadata/Items/Gems/SkillGemRendingSteel",
    "Metadata/Items/Gems/SkillGemReplicate",
    "Metadata/Items/Gems/SkillGemRighteousLightning",
    "Metadata/Items/Gems/SkillGemRiptide",
    "Metadata/Items/Gems/SkillGemSerpentStrike",
    "Metadata/Items/Gems/SkillGemShadowBlades",
    "Metadata/Items/Gems/SkillGemSliceAndDice",
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
    "Metadata/Items/Jewels/JewelTimeless",
    # Race rewards (bases of Demigod uniques)
    "Metadata/Items/Belts/BeltDemigods1",
    "Metadata/Items/Rings/RingDemigods1",
    "Metadata/Items/Armours/Shields/ShieldDemigods",
    "Metadata/Items/Armours/Boots/BootsDemigods1",
    "Metadata/Items/Armours/BodyArmours/BodyDemigods1",
    "Metadata/Items/Armours/Gloves/GlovesDemigods1",
    "Metadata/Items/Armours/Helmets/HelmetDemigods1",
    "Metadata/Items/Armours/Helmets/HelmetWreath1",
}


# The stat description files can include each other and can override stats from included files. E.g. the same stat
# may have different translations on active and support gems. Because of that, they can't simply be merged together
# Therefore, each stat_descriptions file is written into a different file
STAT_DESCRIPTION_NAMING_EXCEPTIONS = {
    "stat_descriptions.txt": "",
    "chest_stat_descriptions.txt": "/strongbox",
    "gem_stat_descriptions.txt": "/support_gem",
    "map_stat_descriptions.txt": "/areas",
}
