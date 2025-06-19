from abc import ABC
from typing import Optional


class AbstractArmor(ABC):
    name: str = None
    type_armor: str = None
    protection: float = None
    part_armor: str = None


class AbstractSuite(ABC):
    helmet: object = None
    breastplate: object = None
    leggings: object = None
    boots: object = None

    def get_total_protection(self):
        return self.helmet.protection + self.breastplate.protection + self.boots.protection + self.leggings.protection
