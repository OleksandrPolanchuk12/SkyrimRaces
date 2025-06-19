from .base_race import AbstractRace
from typing import Optional
from damage.damages import TYPES_DAMAGES


class HighElf(AbstractRace):
    def __init__(self):
        self.magic = super().magic + self.abilities['magicka bonus']

    name = 'Altmer'
    domain = 'Summerset Isles'
    abilities = {
        'magicka bonus': 50,
    }
    power = {
        'highborn': 'Regenerate magicka 25x faster for 60 seconds, once per day'
    }
    initial_bonuses = {
        'illusion': 10,
        'alteration': 5
    }
    survival_mode_bonuses = {
        'Resist Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Fire': '25%'
    }

    def damage_from_weaknesses_and_resist(self, type_damage: str, strength: float) -> Optional[float]:
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        return damage


class Khajiit(AbstractRace):
    def __init__(self):
        self.magic = super().magic + self.weaknesses['Low Magical Affinity']

    name = 'Altmer'
    domain = 'Summerset Isles'
    abilities = {
        'Claws': 12,
    }
    power = {
        'Night Eye': 'Improved night vision for 60 seconds, can be used multiple times a day.'
    }
    initial_bonuses = {
        'sneak': 10,
        'alchemy': 5
    }
    survival_mode_bonuses = {
        'Warmth': 15
    }
    weaknesses = {
        'Low Magical Affinity': -20,
        'Weakness to Fire': '25%'
    }

    def damage_from_weaknesses_and_resist(self, type_damage: str, strength: float) -> Optional[float]:
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        return damage


class DarkElf(AbstractRace):
    name = 'Dunmer'
    domain = 'Morrowind'
    abilities = {
        'Resist Fire': '25%',
    }
    power = {
        "Ancestor's Wrath": 'Opponents getting too close take 8 points of fire damage per second for 60 seconds, once per day'
    }
    initial_bonuses = {
        'destruction': 10,
        'alteration': 5
    }
    survival_mode_bonuses = {
        'Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Frost': '25%'
    }

    def damage_from_weaknesses_and_resist(self,type_damage:str, strength:float) -> Optional[float]:
        damage = strength
        if type_damage == 'frost':
            damage += damage/4
        if type_damage == 'fire':
            damage -= damage/4
        return damage

