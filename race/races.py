from .base_race import AbstractRace


class HighElf(AbstractRace):
    def __init__(self):
        self.magic = super().magic + self.abilities['magicka bonus']

    name = 'Altmer'
    domain = 'Summerset Isles'
    abilities = {
        'magicka bonus': 50,
    }
    power = {
        'highborn': 'Regenerate magicka 25x faster for 60 seconds, once per day'
    }
    initial_bonuses = {
        'Illusion': 10,
        'Alteration': 5
    }
    survival_mode_bonuses = {
        'Resist Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Fire': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        self.health -= damage


class Khajiit(AbstractRace):
    def __init__(self):
        self.magic = super().magic + self.weaknesses['Low Magical Affinity']

    name = 'Altmer'
    domain = 'Summerset Isles'
    abilities = {
        'Claws': 12,
    }
    power = {
        'Night Eye': 'Improved night vision for 60 seconds, can be used multiple times a day.'
    }
    initial_bonuses = {
        'Sneak': 10,
        'Alchemy': 5
    }
    survival_mode_bonuses = {
        'Warmth': 15
    }
    weaknesses = {
        'Low Magical Affinity': -20,
        'Weakness to Fire': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'fire':
            damage += damage/4
        self.health -= damage


class DarkElf(AbstractRace):
    name = 'Dunmer'
    domain = 'Morrowind'
    abilities = {
        'Resist Fire': '25%',
    }
    power = {
        "Ancestor's Wrath": 'Opponents getting too close take 8 points of fire damage per second for 60 seconds, once per day'
    }
    initial_bonuses = {
        'Destruction': 10,
        'Alteration': 5
    }
    survival_mode_bonuses = {
        'Fatigue': '25%'
    }
    weaknesses = {
        'Weakness to Frost': '25%'
    }

    def receive_damage(self, type_damage:str, strength:float):
        super().receive_damage(type_damage, strength)
        damage = strength
        if type_damage == 'frost':
            damage += damage/4
        if type_damage == 'fire':
            damage -= damage/4
        self.health -= damage

