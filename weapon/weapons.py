from .base_weapon import AbstractWeapon
from damage.damages import Fire, Physical


TYPES_WEAPONS = ['spell', 'two-handed', 'one-handed', 'handgrips', 'archery']

class FireBoll(AbstractWeapon):
    type = 'spell'
    type_damage = Fire()
    cost = 20
    damage = 40


class Sword(AbstractWeapon):
    type = 'one-handed'
    type_damage = Physical()
    damage = 50


class Handgrips(AbstractWeapon):
    type = 'handgrips'
    type_damage = Physical()
    damage = 20