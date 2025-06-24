from .base_armor import AbstractArmor
from enchantment.enchantments import FireProtection
from enums import TypeArmorEnum, PartArmorEnum


class SteelHelmet(AbstractArmor):
    name = 'Steel Helmet'
    type_armor = TypeArmorEnum.HEAVY
    protection = 10
    part_armor = PartArmorEnum.HELMET
    enchantment = FireProtection()


class SteelBreastplate(AbstractArmor):
    name = 'Steel Breastplate'
    type_armor = TypeArmorEnum.HEAVY
    protection = 30
    part_armor = PartArmorEnum.BREASTPLATE


class SteelLeggings(AbstractArmor):
    name = 'Steel Leggings'
    type_armor = TypeArmorEnum.HEAVY
    protection = 20
    part_armor = PartArmorEnum.LEGGINGS


class SteelBoots(AbstractArmor):
    name = 'Steel Boots'
    type_armor = TypeArmorEnum.HEAVY
    protection = 12
    part_armor = PartArmorEnum.BOOTS


