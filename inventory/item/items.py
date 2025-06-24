from armor.base_armor import AbstractArmor
from weapon.base_weapon import AbstractWeapon
from potion.base_potion import AbstractPotion
from enchantment.base_enchantment import AbstractEnchantment
from enums import ItemTypeEnum
from .base_item import AbstractItem


class WeaponItem(AbstractItem):
    def __init__(self, name: str, description: str, item_type: ItemTypeEnum, weight: float,
                 weapon: AbstractWeapon, stackable: bool = False):
        super().__init__(name, description, item_type, weight, stackable)
        self.weapon = weapon

class ArmorItem(AbstractItem):
    def __init__(self, name: str, description: str, item_type: ItemTypeEnum, weight: float,
                 armor: AbstractArmor, stackable: bool = False):
        super().__init__(name, description, item_type, weight, stackable)
        self.armor = armor


class PotionItem(AbstractItem):
    def __init__(self, name: str, description: str, item_type: ItemTypeEnum, weight: float,
                 potion: AbstractPotion, stackable: bool = False):
        super().__init__(name, description, item_type, weight, stackable)
        self.potion = potion


class EnchantItem(AbstractItem):
    def __init__(self, name: str, description: str, item_type: ItemTypeEnum, weight: float,
                 enchant: AbstractEnchantment, stackable: bool = False):
        super().__init__(name, description, item_type, weight, stackable)
        self.enchant = enchant


class OtherItem(AbstractItem):
    pass