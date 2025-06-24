from abc import ABC
from typing import Optional
from enums import TypeDamagesEnum


class AbstractWeapon(ABC):
    def __init__(self):
        if self.type_damage.type != TypeDamagesEnum.PHYSICAL and self.enchantment:
            raise ValueError('Weapons is already enchantment')

    type:str = None
    type_damage:object = None
    damage:float = None
    enchantment:object = None

    def get_damage(self) -> Optional[float]:
        damage = self.enchantment.get_bonus(self.damage)
        self.type_damage = damage['type_damage']
        return damage['damage']