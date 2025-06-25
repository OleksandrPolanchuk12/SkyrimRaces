from abc import ABC
from typing import Optional


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

    def __str__(self):
        return (
            f"Race: {self.name}\n"
            f"Domain: {self.domain}\n"
            f"Health: {self.health}, Magic: {self.magic}, Endurance: {self.endurance}\n"
            f"Skills: {self.skills}\n"
            f"Abilities: {self.abilities}\n"
            f"Power: {self.power}\n"
            f"Initial Bonuses: {self.initial_bonuses}\n"
            f"Survival Bonuses: {self.survival_mode_bonuses}\n"
            f"Weaknesses: {self.weaknesses}"
        )

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

    def damage_from_weaknesses_and_resist(self, type_damage:str, strength:float) -> Optional[float]:
        raise NotImplementedError
