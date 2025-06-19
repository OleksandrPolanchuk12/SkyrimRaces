from abc import ABC
from typing import Optional


class AbstractDamage(ABC):
    type:str = None
    name_special_effect:str = None
    chance_special_effect:float = 0.5
    critical_chance: float = 0.05
    critical_multiplier: float = 1.5

