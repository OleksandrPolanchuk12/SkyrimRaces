from .base_enchantment_item import AbstractEnchantmentItem
from inventory.item.items import EnchantItem


class EnchantmentItem(AbstractEnchantmentItem):
    def __init__(self, enchant: EnchantItem, item: object):
        self.enchant = enchant
        self.item = item
        self.enchant_item()


