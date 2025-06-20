from .base_armor import AbstractArmor
from enchantment.enchantments import FireProtection


TYPE_ARMOR = ['heavy', 'light']
PART_ARMOR = ['helmet', 'breastplate', 'leggings', 'boots']


class SteelHelmet(AbstractArmor):
    name = 'Steel Helmet'
    type_armor = 'heave'
    protection = 10
    part_armor = 'helmet'
    enchantment = FireProtection()


class SteelBreastplate(AbstractArmor):
    name = 'Steel Breastplate'
    type_armor = 'heavy'
    protection = 30
    part_armor = 'breastplate'


class SteelLeggings(AbstractArmor):
    name = 'Steel Leggings'
    type_armor = 'light'
    protection = 20
    part_armor = 'leggings'


class SteelBoots(AbstractArmor):
    name = 'Steel Boots'
    type_armor = 'light'
    protection = 12
    part_armor = 'boots'


