from typing import Optional

from .base_character import AbstractCharacter
from race.races import Khajiit
from weapon.weapons import Handgrips
import random


class Character1(AbstractCharacter):
    def __init__(self):
        if self.weapon == Handgrips:
            self.weapon.damage += self.race.abilities['Claws']

    race = Khajiit
    weapon = Handgrips
    level = 1

    def attack(self) -> Optional[dict]:
        result = super().attack()
        chance = self.weapon.type_damage.chance_to_stun
        if random.random() <= chance:
            result['effect'] = "Stun"
            result['effect_worked'] = True
        return result

