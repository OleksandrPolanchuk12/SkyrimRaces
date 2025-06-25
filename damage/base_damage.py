from abc import ABC
from typing import Optional


class AbstractDamage(ABC):
    type:str = None
    name_special_effect:str = None
    chance_special_effect:float = 0.5
    critical_chance: float = 0.05
    critical_multiplier: float = 1.5

    def __str__(self):
        return (
            f"Type: {self.type}\n"
            f"Name special effect: {self.name_special_effect}\n"
            f"Chance special effect: {self.chance_special_effect}\n"
            f"Critical chance: {self.critical_chance}\n"
            f"Critical multiplier: {self.critical_multiplier}\n"
        )

