from abc import ABC
from typing import Optional
import random


class AbstractCharacter(ABC):
    race:object = None
    weapon:object = None
    level:int = None

    def attack(self) -> Optional[dict]:
        critical_chance = self.weapon.type_damage.critical_chance
        critical_multiplier = self.weapon.type_damage.critical_multiplier
        damage = self.weapon.damage

        if random.random() <= critical_chance:
            damage += damage * critical_multiplier

        return {
            'damage': damage,
            'effect': None,
            'effect_worked': False
        }