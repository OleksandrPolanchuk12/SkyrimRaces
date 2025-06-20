from typing import Optional

from .base_enchantment import AbstractEnchantment
from damage.damages import Fire


class FireProtection(AbstractEnchantment):
    name = 'Fire Protection'
    special_effect = {
        'fire resist': '25%'
    }

    def get_bonus(self, damage:float) -> Optional[dict]:
        damage = damage - damage/4
        return {
            'damage': damage
        }


class FireDamage(AbstractEnchantment):
    name = 'Fire Damage'
    special_effect = {
        'fire damage': 10
    }

    def get_bonus(self, damage:float) -> Optional[dict]:
        damage += 10
        return {
            'damage': damage,
            'type_damage': Fire()
        }