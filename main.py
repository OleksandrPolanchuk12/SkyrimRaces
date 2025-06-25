from character.characters import Character1
from enums import TypeDamagesEnum
from inventory.inventories import CharacterInventory
from inventory.item.items import WeaponItem, ArmorItem, EnchantItem, PotionItem, OtherItem
from enums import ItemTypeEnum
from weapon.weapons import Sword, FireBoll
from armor.armors import SteelBoots, SteelHelmet, SteelBreastplate, SteelLeggings
from armor.suites import SteelSuite
from potion.posions import HealPotion
from craft.crafts import HealPotionCraft
from enchantment.enchantments import FireDamage
from enchantment_item.enchantment_items import EnchantmentItem
from weapon.weapons import Sword

character = Character1()

inventory = character.inventory

item1 = EnchantItem(name='1', description='2', item_type=ItemTypeEnum.ENCHANT, weight=1, stackable=True, enchant=FireDamage())
item2 = WeaponItem(name='1', description='2', item_type=ItemTypeEnum.WEAPON, weight=1, stackable=True, weapon=Sword())
inventory.add_item(item2)
inventory.add_item(item1)
character.change_weapon(Sword())
print(character.weapon)
EnchantmentItem(enchant=inventory.enchant[0], item=character.weapon)
print(character.weapon)





# item1 = OtherItem(name='Butterfly Wing', description='2', item_type=ItemTypeEnum.OTHER, weight=1, stackable=True)
# item2 = OtherItem(name='Blue Mountain Flower', description='2', item_type=ItemTypeEnum.OTHER, weight=1, stackable=True)
# inventory.add_item( item2)
# inventory.add_item(item1)
# inventory.add_item(item2)
# inventory.add_item(item1)
# print(inventory)
# HealPotionCraft().craft_item(inventory)
# print(inventory)




# item3 = ArmorItem(name='13', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelLeggings())
# item4 = ArmorItem(name='14', description='2', item_type=ItemTypeEnum.ARMOR, weight=10, stackable=True, armor=SteelBoots())
# item5 = PotionItem(description='2', item_type=ItemTypeEnum.POTION, weight=1, stackable=True, potion=HealPotion())
#
# inventory.add_item(item1)
# inventory.add_item(item2)
# inventory.add_item(item3)
# inventory.add_item(item4)
# inventory.add_item(item5)
#
# print(inventory)
#
# character.change_suite(SteelSuite())
# print(character.health)
# character.level_up('health')
# character.receive_damage(TypeDamagesEnum.FIRE, 44)
# print(character.health)
# character.use_potion('Small Heal Potion')
# print(character.health)
#
# print(inventory)

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