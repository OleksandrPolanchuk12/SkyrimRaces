from typing import Optional

from .base_character import AbstractCharacter
from race.races import Khajiit
from weapon.weapons import Handgrips, Sword, FireBoll
import random


class Character1(AbstractCharacter):
    def __init__(self):
        if self.weapon == Handgrips:
            self.weapon.damage += self.race.abilities['Claws']
    name = '1'
    race = Khajiit
    weapon = FireBoll
    level = 1

