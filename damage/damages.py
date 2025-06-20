from .base_damage import AbstractDamage

TYPES_DAMAGES = ['fire', 'frost', 'magic', 'physical', 'lightning', 'poison']

class Physical(AbstractDamage):
    type = 'physical'
    name_special_effect = 'stun'
    critical_chance = 0.1
    critical_multiplier = 2


class Frost(AbstractDamage):
    type = 'frost'
    name_special_effect = 'freeze'
    chance_special_effect = 0.2


class Magic(AbstractDamage):
    type = 'magic'
    critical_chance = 0.15
    critical_multiplier = 1.8


class Fire(AbstractDamage):
    type = 'fire'
    chance_to_light:float = 0.2
    name_special_effect = 'fire'
    chance_special_effect = 0.2


class Lightning(AbstractDamage):
    type = 'lightning'
    chance_to_rechange:float = 0.1


class Poison(AbstractDamage):
    type = 'poison'
    chance_to_poison:float = 0.2