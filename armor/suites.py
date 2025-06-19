from .base_armor import AbstractSuite
from .armors import SteelBoots, SteelHelmet, SteelBreastplate, SteelLeggings


class SteelSuite(AbstractSuite):
    helmet = SteelHelmet()
    breastplate = SteelBreastplate()
    leggings = SteelLeggings()
    boots = SteelBoots()