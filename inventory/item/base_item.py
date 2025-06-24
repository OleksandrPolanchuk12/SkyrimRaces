from abc import ABC
from typing import Optional
from enums import ItemTypeEnum


class AbstractItem(ABC):
    def __init__(self, name: str, description: str, item_type: ItemTypeEnum, weight: float, stackable: bool = False):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.weight = weight
        self.stackable = stackable

    number: int = 1
