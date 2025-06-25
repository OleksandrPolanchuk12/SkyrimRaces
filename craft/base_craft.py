from abc import ABC
from typing import Optional
from inventory.inventories import CharacterInventory


class AbstractCraft(ABC):
    result: object = None
    ingredient: dict = {}

    def craft_item(self, inventory: CharacterInventory) -> None:
        used_items = []

        for name, value in self.ingredient.items():
            found = False
            for item in inventory.other:
                if item.name == name:
                    if getattr(item, 'number', 1) >= value:
                        used_items.append((item, value))
                        found = True
                        break
                    else:
                        raise ValueError(f'Not enough {name}')
            if not found:
                raise ValueError(f'{name} does not exist in inventory')

        for item, value in used_items:
            if item.stackable:
                if item.number > value:
                    item.number -= value
                else:
                    inventory.other.remove(item)
            else:
                inventory.other.remove(item)