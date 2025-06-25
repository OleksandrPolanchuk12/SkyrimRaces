from .base_weapon import AbstractWeapon
from damage.damages import Fire, Physical
from enchantment.enchantments import FireDamage
from enums import TypeWeaponsEnum

class FireBoll(AbstractWeapon):
    type = TypeWeaponsEnum.SPELL
    type_damage = Fire()
    cost = 20
    damage = 40


class Sword(AbstractWeapon):
    type = TypeWeaponsEnum.ONE_HANDED
    type_damage = Physical()
    damage = 50
    enchantment = None


class Handgrips(AbstractWeapon):
    type = TypeWeaponsEnum.TWO_HANDED
    type_damage = Physical()
    damage = 20