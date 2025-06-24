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
    status: str = 'not overloaded'

    def add_item(self, item:object) -> None:
        item_list = None

        if item.item_type == ItemTypeEnum.WEAPON:
            item_list = self.weapons
        elif item.item_type == ItemTypeEnum.ARMOR:
            item_list = self.armor
        elif item.item_type == ItemTypeEnum.POTION:
            item_list = self.potion
        elif item.item_type == ItemTypeEnum.ENCHANT:
            item_list = self.enchant
        else:
            item_list = self.other

        if item.stackable:
            for i in item_list:
                if i == item:
                    if hasattr(i, 'number'):
                        i.number += 1
                    else:
                        i.number = 2
                    return
            item.number = 1
            item_list.append(item)

    def update_cargo_status(self):
        total_weight = 0

        for i in [self.weapons, self.armor, self.potion, self.enchant, self.other]:
            for j in i:
                count = getattr(j, 'number', 1)
                total_weight += j.weight * count

        weight = self.cargo_capacity + (self.cargo_capacity * 0.6)

        if total_weight > weight:
            self.status = 'impossible to move'
        elif total_weight > self.cargo_capacity:
            self.status = 'overloaded'
        else:
            self.status = 'not overloaded'

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

    def drop_item(self, item:object) -> None:
        for i in [self.weapons, self.armor, self.potion, self.enchant, self.other]:
            for j in i:
                if j == item:
                    if item.stackable and getattr(j, 'number', 1) > 1:
                        j.number -= 1
                    else:
                        i.remove(item)
                    return