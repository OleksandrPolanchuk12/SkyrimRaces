from character.characters import Character1
from enums import TypeDamagesEnum
from inventory.inventories import CharacterInventory
from inventory.item.items import WeaponItem, ArmorItem, EnchantItem, PotionItem
from enums import ItemTypeEnum
from weapon.weapons import Sword, FireBoll
from armor.armors import SteelBoots, SteelHelmet, SteelBreastplate, SteelLeggings
from armor.suites import SteelSuite
from potion.posions import HealPotion

character = Character1()

inventory = character.inventory

item1 = ArmorItem(name='11', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelHelmet())
item2 = ArmorItem(name='12', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelBreastplate())
item3 = ArmorItem(name='13', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelLeggings())
item4 = ArmorItem(name='14', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelBoots())
item5 = PotionItem(name='Small Heal Potion', description='2', item_type=ItemTypeEnum.POTION, weight=1, stackable=True, potion=HealPotion())


inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)
inventory.add_item(item4)
inventory.add_item(item5)

print(inventory)

character.change_suite(SteelSuite())
print(character.health)
character.level_up('health')
character.receive_damage(TypeDamagesEnum.FIRE, 44)
print(character.health)
character.use_potion('Small Heal Potion')
print(character.health)

# inventory.update_cargo_status()
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