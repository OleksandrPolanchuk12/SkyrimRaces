from abc import ABC
from typing import Optional


class AbstractEnchantment(ABC):
    name:str = None
    special_effect:dict = {}

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Special effect: {self.special_effect}\n"
        )

    def get_bonus(self, damage:float) -> Optional[dict]:
        raise NotImplementedError