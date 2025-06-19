from character.characters import Character1

character = Character1()
print(character.race.get_main_characteristic())
print(character.suite.get_total_protection())
character.receive_damage('fire',30)
print(character.race.get_main_characteristic())
character.race.get_characteristic()
