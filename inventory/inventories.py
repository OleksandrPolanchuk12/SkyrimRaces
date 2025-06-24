from inventory.base_inventory import AbstractInventory


class CharacterInventory(AbstractInventory):
    def __init__(self):
        super().__init__()
        cargo_capacity = 100