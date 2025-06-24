from typing import Optional

from .base_character import AbstractCharacter
from race.races import Khajiit
from weapon.weapons import Handgrips, Sword, FireBoll
from armor.suites import SteelSuite
import random
from inventory.inventories import CharacterInventory


class Character1(AbstractCharacter):
    def __init__(self):
        if isinstance(self.weapon, Handgrips):
            self.weapon.damage += self.race.abilities['Claws']
    name = '1'
    race = Khajiit()
    weapon = Sword()
    suite = None
    level = 1
    inventory = CharacterInventory()

