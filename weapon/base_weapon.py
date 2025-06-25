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

    def __str__(self):
        return (
            f"Weapon Type: {self.type}\n"
            f"Damage Type: {self.type_damage}\n"
            f"Damage: {self.damage}\n"
            f"Enchantment: {self.enchantment if self.enchantment else 'None'}"
        )

    def get_damage(self) -> Optional[float]:
        damage = self.enchantment.get_bonus(self.damage)
        self.type_damage = damage['type_damage']
        return damage['damage']