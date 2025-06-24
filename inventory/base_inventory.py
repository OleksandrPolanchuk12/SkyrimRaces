from abc import ABC
from typing import List

from inventory.item.items import WeaponItem, ArmorItem, EnchantItem, PotionItem, OtherItem
from enums import ItemTypeEnum


class AbstractInventory(ABC):
    def __init__(self):
        self.weapons: List[WeaponItem] = []
        self.armor: List[ArmorItem] = []
        self.potion: List[PotionItem] = []
        self.enchant: List[EnchantItem] = []
        self.other: List[OtherItem] = []

    def add_item(self, item:object) -> None:
        if item.item_type.value == ItemTypeEnum.WEAPON.value:
            self.weapons.append(item)
        elif item.item_type.value == ItemTypeEnum.ARMOR.value:
            self.armor.append(item)
        elif item.item_type.value == ItemTypeEnum.POTION.value:
            self.potion.append(item)
        elif item.item_type.value == ItemTypeEnum.ENCHANT.value:
            self.enchant.append(item)
        else:
            self.other.append(item)

    def get_inventory(self):
        return [self.weapons, self.armor, self.potion, self.enchant, self.other]

    def get_specific_section(self, section: ItemTypeEnum):
        if section.value == ItemTypeEnum.WEAPON.value:
            return self.weapons
        elif section.value == ItemTypeEnum.ARMOR.value:
            return self.armor
        elif section.value == ItemTypeEnum.POTION.value:
            return self.potion
        elif section.value == ItemTypeEnum.ENCHANT.value:
            return self.enchant
        else:
            return self.other
