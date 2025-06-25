from typing import Optional

from potion.base_potion import AbstractPotion
from enums import TypePotionEnum


class HealPotion(AbstractPotion):
    name = 'Small Heal Potion'
    ingredients = {
        'Butterfly Wing': 1,
        'Blue Mountain Flower': 1
    }
    effect = {
        'heal': 20
    }
    duration = None

    def get_bonus(self) -> Optional[dict]:
        return {
            'type': TypePotionEnum.HEALTH,
            'bonus': 20
        }