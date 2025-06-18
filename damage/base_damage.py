from abc import ABC
from typing import Optional


class AbstractDamage(ABC):
    type:str = None
    critical_chance: float = 0.05
    critical_multiplier: float = 1.5

