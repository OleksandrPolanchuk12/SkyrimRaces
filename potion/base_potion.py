from abc import ABC
from typing import Optional


class AbstractPotion(ABC):
    name:str = None
    ingredients:dict = {}
    effect:dict = {}
    duration:str = None

    def get_bonus(self) -> Optional[dict]:
        raise NotImplementedError

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Ingredients: {', '.join(f'{k}: {v}' for k, v in self.ingredients.items())}\n"
            f"Effect: {', '.join(f'{k}: {v}' for k, v in self.effect.items())}\n"
            f"Duration: {self.duration}"
        )

