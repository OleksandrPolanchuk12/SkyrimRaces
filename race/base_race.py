from abc import ABC
from typing import Optional
from damage.damages import TYPES_DAMAGES


class AbstractRace(ABC):
    name:str = None
    domain:str = None
    health:float = 100
    magic:float = 100
    endurance:float = 100
    skills:dict = {
        'alchemy': 15,
        'alteration': 15,
        'archery': 15,
        'block': 15,
        'conjuration': 15,
        'destruction': 15,
        'enchanting': 15,
        'heavy armor': 15,
        'illusion': 15,
        'light armor': 15,
        'lockpicking': 15,
        'one-handed': 15,
        'pickpocket': 15,
        'restoration': 15,
        'smithing': 15,
        'sneak': 15,
        'speech': 15,
        'two-handed': 15
    }
    abilities:dict = {}
    power:dict = {}
    initial_bonuses:dict = {}
    survival_mode_bonuses:dict = {}
    weaknesses:dict = {}

    def get_characteristic(self) -> Optional[dict]:
        return {
            'name': self.name,
            'domain': self.domain,
            'health': self.health,
            'magic': self.magic,
            'endurance': self.endurance,
            'abilities': self.abilities,
            'power': self.power,
            'initial_bonuses': self.initial_bonuses,
            'survival_mode_bonuses': self.survival_mode_bonuses,
            'skills': self.get_skills()
        }

    def get_skills(self) -> Optional[dict]:
        skills = self.skills
        for key, value in self.initial_bonuses.items():
            skills[key] += value
        return skills

    def get_main_characteristic(self) -> Optional[dict]:
        return {
            'health': self.health,
            'magic': self.magic,
            'endurance': self.endurance
        }