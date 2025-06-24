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

    cargo_capacity: float = None
    status: str = 'these is not overloaded'

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
            total_weight = 0
        for i in [self.weapons, self.armor, self.potion, self.enchant, self.other]:
            for j in i:
                total_weight += j.weight

        weight = -(self.cargo_capacity * 0.6)

        if self.cargo_capacity - total_weight < 0:
            self.status = 'overloaded'
        elif self.cargo_capacity - total_weight <= weight:
            self.status = 'impossible to move'
        else:
            self.status = 'these is not overloaded'

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
