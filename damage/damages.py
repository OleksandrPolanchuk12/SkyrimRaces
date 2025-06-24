from .base_damage import AbstractDamage
from enums import TypeDamagesEnum


class Physical(AbstractDamage):
    type = TypeDamagesEnum.PHYSICAL
    name_special_effect = 'stun'
    critical_chance = 0.1
    critical_multiplier = 2


class Frost(AbstractDamage):
    type = TypeDamagesEnum.FROST
    name_special_effect = 'freeze'
    chance_special_effect = 0.2


class Magic(AbstractDamage):
    type = TypeDamagesEnum.MAGIC
    critical_chance = 0.15
    critical_multiplier = 1.8


class Fire(AbstractDamage):
    type = TypeDamagesEnum.FIRE
    chance_to_light:float = 0.2
    name_special_effect = 'fire'
    chance_special_effect = 0.2


class Lightning(AbstractDamage):
    type = TypeDamagesEnum.LIGHTNING
    chance_to_rechange:float = 0.1


class Poison(AbstractDamage):
    type = TypeDamagesEnum.POISON
    chance_to_poison:float = 0.2