from enum import Enum


class TypeWeaponsEnum(Enum):
    SPELL = 'spell'
    TWO_HANDED = 'two-handed'
    ONE_HANDED = 'one-handed'
    HANDGRIPS = 'handgrips'
    ARCHERY = 'archery'


class TypeDamagesEnum(Enum):
    FIRE = "fire"
    FROST = "frost"
    MAGIC = "magic"
    PHYSICAL = "physical"
    LIGHTNING = "lightning"
    POISON = "poison"



class TypeArmorEnum(Enum):
    HEAVY = 'heavy'
    LIGHT = 'light'


class PartArmorEnum(Enum):
    HELMET = 'helmet'
    BREASTPLATE = 'breastplate'
    LEGGINGS = 'leggings'
    BOOTS = 'boots'


class ItemTypeEnum(Enum):
    WEAPON = 'weapon'
    ARMOR = 'armor'
    POTION = 'potion'
    ENCHANT = 'enchant'