from .base_armor import AbstractSuite, AbstractArmor
from .armors import SteelBoots, SteelHelmet, SteelBreastplate, SteelLeggings


class Suite(AbstractSuite):
    def __init__(self, helmet: AbstractArmor, breastplate: AbstractArmor, leggings: AbstractArmor, boots: AbstractArmor):
        self.helmet = helmet
        self.breastplate = breastplate
        self.leggings = leggings
        self.boots = boots


class SteelSuite(AbstractSuite):
    helmet = SteelHelmet()
    breastplate = SteelBreastplate()
    leggings = SteelLeggings()
    boots = SteelBoots()