from character.characters import Character1

character = Character1()
print(character.race.magic)
damage = character.attack()
print(damage)
print(character.race.get_main_characteristic(self=character.race))

character.race.receive_damage(self=character.race, type_damage='fire', strength=20)

print(character.race.get_main_characteristic(self=character.race))