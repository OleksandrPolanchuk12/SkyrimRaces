from abc import ABC
from inventory.item.items import EnchantItem



class AbstractEnchantmentItem(ABC):
    enchant: EnchantItem = None
    item: object = None

    def enchant_item(self) -> None:
        self.item.enchantment = self.enchant.enchant