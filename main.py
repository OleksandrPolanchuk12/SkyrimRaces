from character.characters import Character1
from enums import TypeDamagesEnum
from inventory.inventories import CharacterInventory
from inventory.item.items import WeaponItem, ArmorItem, EnchantItem, PotionItem
from enums import ItemTypeEnum
from weapon.weapons import Sword, FireBoll
from armor.armors import SteelBoots, SteelHelmet, SteelBreastplate, SteelLeggings
from armor.suites import SteelSuite

character =Character1()

inventory = character.inventory

# item1 = ArmorItem(name='1', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelHelmet())
# item2 = ArmorItem(name='1', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelBreastplate())
# item3 = ArmorItem(name='1', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelLeggings())
# item4 = ArmorItem(name='1', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelBoots())
#
# inventory.add_item(item1)
# inventory.add_item(item2)
# inventory.add_item(item3)
# inventory.add_item(item4)
#
#
# character.change_suite(SteelSuite())
#
# print(character.suite)
# print(character.speed_ratio)
#
# item1 = WeaponItem(name='1', description='2', item_type=ItemTypeEnum.WEAPON, weight=10, stackable=True, weapon=Sword())
# item2 = WeaponItem(name='1', description='2', item_type=ItemTypeEnum.WEAPON, weight=10, stackable=True, weapon=FireBoll())
#
# inventory.add_item(item1)
# inventory.add_item(item2)
#
# print(inventory.get_inventory())
#
# print(inventory.get_specific_section(ItemTypeEnum.WEAPON))
#
# character.change_weapon(FireBoll())
#
# print(character.weapon.type)