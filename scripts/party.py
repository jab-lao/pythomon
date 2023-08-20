import customtkinter as ctk
from move_list import *
from pokemon_list import *
from gacha import *


def sort_party():
    global party
    party_slots = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6']
    empty_slots = []
    occupied_slots = []

    # check for occupied and empty party slots
    for key, value in party.items():
        if value.name == '':
            empty_slots.append((key, value))
        else:
            occupied_slots.append((key, value))

    # move pokemon in party to the top slots in order
    if len(empty_slots) != 0:
        loop = 0
        for i in party_slots:
            try:
                party[i] = occupied_slots[loop][1]
                party[i].party_index = i[4]
            except:
                party[i] = Pokemon(*empty, level=0, party_index=i[4])
            loop += 1


party = {
    'slot1': Pokemon(*empty, level=0, party_index=1),
    'slot2': Pokemon(*empty, level=0, party_index=2),
    'slot3': Pokemon(*empty, level=0, party_index=3),
    'slot4': Pokemon(*empty, level=0, party_index=4),
    'slot5': Pokemon(*empty, level=0, party_index=5),
    'slot6': Pokemon(*empty, level=0, party_index=6)
}

# active_pokemon = party['slot1']
active_pokemon = Pokemon(*empty, level=0, party_index=1)
party_size = 0

# ########## #
# Enemy data #
# ########## #
enemy_pokemon = Pokemon(*squirtle, level=5, party_index=-1)

# ########## #
# Game flow  #
# ########## #
in_battle = False
fainted_mons = 0

pokemon_obtained = []
completed_routes = []

stages_cleared = 0
battles_won = 0
battles_lost = 0
damage_dealt = 0
damage_taken = 0

gacha_level = g_pokeball

#### please
displayed_pokemon = Pokemon(*empty, level=0, party_index=1)
