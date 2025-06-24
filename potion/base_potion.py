from abc import ABC
from typing import Optional


class AbstractPotion(ABC):
    name:str = None
    ingredients:dict = {}
    effect:dict = {}
    duration:str = None

    def get_bonus(self) -> Optional[dict]:
        raise NotImplementedError