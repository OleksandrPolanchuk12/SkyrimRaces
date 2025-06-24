from abc import ABC
from typing import Optional
import random
from enums import TypeDamagesEnum, TypeWeaponsEnum
from armor.base_armor import AbstractSuite
from weapon.base_weapon import AbstractWeapon


TYPE_CHARACTERISTIC = ['health', 'endurance', 'magic']

class AbstractCharacter(ABC):
    def __init__(self):
        self.health = self.race.health
        self.magic = self.race.magic
        self.endurance = self.race.endurance
        self.speed_ratio = self.suite.get_speed_ratio()

    name:str = None
    race:object = None
    weapon:object = None
    suite:object = None
    level:int = None
    health: float = None
    magic: float = None
    endurance: float = None
    speed_ratio: float = 1
    inventory: object = None

    def attack(self) -> Optional[dict]:
        critical_chance = self.weapon.type_damage.critical_chance
        critical_multiplier = self.weapon.type_damage.critical_multiplier
        damage = self.weapon.get_damage()
        type_weapon = self.weapon.type

        if random.random() <= critical_chance:
            damage += damage * critical_multiplier

        if type_weapon == TypeWeaponsEnum.SPELL:
            if self.magic < self.weapon.cost:
                raise ValueError('Not enough mana')
            self.magic -= self.weapon.cost
        else:
            if self.endurance < 20:
                raise ValueError('Not enough endurance')
            self.endurance -= 20

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

    def receive_damage(self, type_damage:TypeDamagesEnum, strength:float) -> None:
        if type_damage not in TypeDamagesEnum:
            raise ValueError(f'Damage type {type_damage.value} does not exists')

        damage = self.race.damage_from_weaknesses_and_resist(type_damage.value, strength)
        dmg = self.suite.get_total_damage(damage)
        self.health -= dmg

    def skill_damage_bonus(self, weapon_type:TypeWeaponsEnum, damage:float) -> Optional[float]:
        if weapon_type not in TypeWeaponsEnum:
            raise ValueError(f'Type weapon {weapon_type.value} does not exists')

        skill_value = ''
        if weapon_type == TypeWeaponsEnum.SPELL:
            skill_value = self.race.skills['destruction']
        elif weapon_type == TypeWeaponsEnum.HANDGRIPS:
            return damage
        else:
            skill_value = self.race.skills[weapon_type.value]

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

        self.health = self.race.health
        self.magic = self.race.magic
        self.endurance = self.race.endurance

    def level_up_skill(self, type_skill:str) -> None:
        if type_skill not in self.race.skills:
            raise ValueError(f'Type skill {type_skill} does not exists')

        self.race.skills[type_skill] += 1

    def get_main_characteristic(self) -> Optional[dict]:
        return {
            'health': self.health,
            'magic': self.magic,
            'endurance': self.endurance
        }

    def change_weapon(self, weapon:AbstractWeapon):
        if not any(isinstance(i.weapon, type(weapon)) for i in self.inventory.weapons):
            raise ValueError(f"Weapon '{weapon}' does not exist in inventory.")
        self.weapon = weapon


    def change_suite(self, suite:AbstractSuite):
        armors = [suite.helmet, suite.breastplate, suite.leggings, suite.boots]
        for i in armors:
            if not any(isinstance(j.armor, type(i)) for j in self.inventory.armor):
                raise ValueError('Armor does not exists')

        self.suite = suite
        self.speed_ratio = self.suite.get_speed_ratio()