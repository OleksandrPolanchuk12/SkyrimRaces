from abc import ABC
from typing import Optional


class AbstractArmor(ABC):
    name: str = None
    type_armor: str = None
    protection: float = None
    part_armor: str = None
    enchantment: object = None


class AbstractSuite(ABC):
    helmet: object = None
    breastplate: object = None
    leggings: object = None
    boots: object = None

    def get_total_damage(self, damage:float):
        total_protection = self.helmet.protection + self.breastplate.protection + self.boots.protection + self.leggings.protection

        if self.helmet.enchantment:
            bonus = self.helmet.enchantment.get_bonus(damage)
            damage += bonus['damage']

        if self.breastplate.enchantment:
            bonus = self.breastplate.enchantment.get_bonus(damage)
            damage += bonus['damage']

        if self.leggings.enchantment:
            bonus = self.leggings.enchantment.get_bonus(damage)
            damage += bonus['damage']

        if self.boots.enchantment:
            bonus = self.boots.enchantment.get_bonus(damage)
            damage += bonus['damage']

        dmg = 0
        if damage > total_protection:
            dmg = damage - total_protection
        return dmg
