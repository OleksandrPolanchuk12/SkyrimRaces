from abc import ABC


class AbstractWeapon(ABC):
    type:str = None
    type_damage:object = None
    damage:float = None