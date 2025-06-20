from abc import ABC
from typing import Optional
import random
from weapon.weapons import TYPES_WEAPONS
from damage.damages import TYPES_DAMAGES


TYPE_CHARACTERISTIC = ['health', 'endurance', 'magic']

class AbstractCharacter(ABC):
    name:str = None
    race:object = None
    weapon:object = None
    suite:object = None
    level:int = None

    def attack(self) -> Optional[dict]:
        critical_chance = self.weapon.type_damage.critical_chance
        critical_multiplier = self.weapon.type_damage.critical_multiplier
        damage = self.weapon.get_damage()
        type_weapon = self.weapon.type

        if random.random() <= critical_chance:
            damage += damage * critical_multiplier

        if type_weapon == 'spell':
            if self.race.magic < self.weapon.cost:
                raise ValueError('Not enough mana')
            self.race.magic -= self.weapon.cost

        result = {
            'damage': self.skill_damage_bonus(type_weapon, damage),
            'type_damage': self.weapon.type_damage,
            'effect': None,
            'effect_worked': False
        }

        if self.weapon.type_damage.name_special_effect:
            chance = self.weapon.type_damage.chance_special_effect
            if random.random() <= chance:
                result['effect'] = self.weapon.type_damage.name_special_effect
                result['effect_worked'] = True

        return result

    def receive_damage(self, type_damage:str, strength:float) -> None:
        if type_damage not in TYPES_DAMAGES:
            raise ValueError(f'Damage type {type_damage} does not exists')

        damage = self.race.damage_from_weaknesses_and_resist(type_damage, strength)
        dmg = self.suite.get_total_damage(damage)
        self.race.health -= dmg

    def skill_damage_bonus(self, weapon_type:str, damage:float) -> Optional[float]:
        if weapon_type not in TYPES_WEAPONS:
            raise ValueError(f'Type weapon {weapon_type} does not exists')

        skill_value = ''
        if weapon_type == 'spell':
            skill_value = self.race.skills['destruction']
        elif weapon_type == 'handgrips':
            return damage
        else:
            skill_value = self.race.skills[weapon_type]

        damage += damage * skill_value / 100

        return damage

    def level_up(self, type_characteristic:str) -> None:
        if type_characteristic not in TYPE_CHARACTERISTIC:
            raise ValueError(f'Type characteristic {type_characteristic} does not exists')

        if type_characteristic == 'health':
            self.race.health += 10

        if type_characteristic == 'endurance':
            self.race.endurance += 10

        if type_characteristic == 'magic':
            self.race.magic += 10

    def level_up_skill(self, type_skill:str) -> None:
        if type_skill not in self.race.skills:
            raise ValueError(f'Type skill {type_skill} does not exists')

        self.race.skills[type_skill] += 1