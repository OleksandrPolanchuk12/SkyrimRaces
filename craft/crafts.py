from .base_craft import AbstractCraft
from potion.posions import HealPotion
from inventory.item.items import PotionItem
from enums import ItemTypeEnum
from inventory.inventories import CharacterInventory


class HealPotionCraft(AbstractCraft):
    def __init__(self):
        self.ingredient = HealPotion.ingredients
    result = HealPotion()

    def craft_item(self, inventory: CharacterInventory) -> None:
        super().craft_item(inventory)

        item = PotionItem(description=self.result.name,
                          item_type=ItemTypeEnum.POTION, weight=1, stackable=True, potion=self.result)

        inventory.add_item(item)