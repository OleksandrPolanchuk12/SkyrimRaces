from abc import ABC
from typing import Optional


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
        types_damage = ['fire', 'frost', 'magic', 'physical', 'lightning', 'poison']
        if type_damage not in types_damage:
            raise ValueError(f'Damage type {type_damage} does not exists')

    def get_main_characteristic(self) -> Optional[dict]:
        return {
            'health': self.health,
            'magic': self.magic,
            'endurance': self.endurance
        }


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
        'Illusion': 10,
        'Alteration': 5
    }
    survival_mode_bonuses = {
        'Resist Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Fire': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        self.health -= damage


class Khajiit(AbstractRace):
    def __init__(self):
        self.magic = super().magic + self.weaknesses['Low Magical Affinity']

    name = 'Altmer'
    domain = 'Summerset Isles'
    abilities = {
        'Claws': 'Claws do 12 damage',
    }
    power = {
        'Night Eye': 'Improved night vision for 60 seconds, can be used multiple times a day.'
    }
    initial_bonuses = {
        'Sneak': 10,
        'Alchemy': 5
    }
    survival_mode_bonuses = {
        'Warmth': 15
    }
    weaknesses = {
        'Low Magical Affinity': -20,
        'Weakness to Fire': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        self.health -= damage


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
        'Destruction': 10,
        'Alteration': 5
    }
    survival_mode_bonuses = {
        'Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Frost': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'frost':
            damage += damage/4
        if type_damage == 'fire':
            damage -= damage/4
        self.health -= damage


# elf = HighElf()
# elf.receive_damage('fire9', 20)
# print(elf.get_skills())
# print(elf.get_characteristic())
#
# khajiit = Khajiit()
# print(khajiit.get_skills())
# print(khajiit.get_characteristic())

dunmer = DarkElf()

dunmer.receive_damage('fire', 20)

print(dunmer.get_main_characteristic())