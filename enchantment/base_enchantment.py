from abc import ABC
from typing import Optional


class AbstractEnchantment(ABC):
    name:str = None
    special_effect:dict = {}

    def get_bonus(self, damage:float) -> Optional[dict]:
        raise NotImplementedError