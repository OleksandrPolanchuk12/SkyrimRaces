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
        'Alchemy': 15,
        'Alteration': 15,
        'Archery': 15,
        'Block': 15,
        'Conjuration': 15,
        'Destruction': 15,
        'Enchanting': 15,
        'Heavy Armor': 15,
        'Illusion': 15,
        'Light Armor': 15,
        'Lockpicking': 15,
        'One-Handed': 15,
        'Pickpocket': 15,
        'Restoration': 15,
        'Smithing': 15,
        'Sneak': 15,
        'Speech': 15,
        'Two-Handed': 15
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

    def receive_damage(self, type_damage:str, strength:float) -> None:
        if type_damage not in TYPES_DAMAGES:
            raise ValueError(f'Damage type {type_damage} does not exists')

    def get_main_characteristic(self) -> Optional[dict]:
        return {
            'health': self.health,
            'magic': self.magic,
            'endurance': self.endurance
        }