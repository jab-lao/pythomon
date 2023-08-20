import random
from math import ceil

from type_list import *
from move_list import *
from settings import *
from random import shuffle
import party as pty


class Pokemon:

    def __init__(self, dex, name, type1, type2,
                 base_hp, base_atk, base_spd, skill, evasion,
                 evo_level, evo_mon, moves, learnset, e_moves,
                 level, party_index):

        self.dex = dex
        self.party_index = party_index
        self.name = name
        self.type1 = type1.copy()
        self.type2 = type2.copy()

        self.lv = 0
        self.exp = 0
        self.exp_cap = 10

        self.base_hp = base_hp
        self.base_atk = base_atk
        self.base_spd = base_spd
        self.evo_level = evo_level
        self.skill = skill
        self.evasion = evasion
        self.evo_mon = evo_mon

        self.affinities = self.type1
        if self.type2[0] != "":
            self.add_type()

        self.moves = moves

        self.learnset = learnset

        self.move1 = self.moves[0]
        self.move2 = self.moves[1] if len(self.moves) > 1 else move_list['None']

        self.e_moves = e_moves

        self.hp = base_hp
        self.cur_hp = base_hp
        self.atk = base_atk
        self.spd = base_spd

        # level up to the level specified in the parameter
        for i in range(level): self.level_up()

    def level_up(self, shared=False):
        self.exp = self.exp - self.exp_cap
        self.exp_cap = round(self.exp_cap * 1.07)
        self.lv = self.lv + 1

        self.hp = round(self.base_hp * (self.lv / 100))

        self.cur_hp = self.hp

        if self.exp < 0:
            self.exp = 0

        # check learnset for learned move
        if self.lv in self.learnset:
            self.moves.extend([move_list[self.learnset[self.lv]]].copy())

        # check for evolution
        # if self.evo_level and self.lv == self.evo_level:
        #     pty.party[f'slot{self.party_index}'] = Pokemon(*self.evo_mon, level=self.lv, party_index=self.party_index)

        # check for double level up
        if shared:
            if self.exp >= self.exp_cap:
                self.level_up(shared=True)

    def add_type(self):
        for i in range(18):
            # self.affinities[i + 2]
            # if second type is weak
            if self.type2[i + 2] > 1:
                # if first type is neutral, set affinity to "weak"
                if self.affinities[i + 2] == 1:
                    self.affinities[i + 2] = weak
                # if first type is also weak, set affinity to "double weak"
                elif self.affinities[i + 2] > 1:
                    self.affinities[i + 2] = double_weak
                # if first type resists, set affinity to "neutral"
                elif self.affinities[i + 2] < 1:
                    self.affinities[i + 2] = neutral

            # if second type resists
            if self.type2[i + 2] < 1 and self.type2[i + 2] != 0:
                # if first type is neutral, set affinity to resist
                if self.affinities[i + 2] == 1:
                    self.affinities[i + 2] = resist
                # if first type is weak, set affinity to neutral
                elif self.affinities[i + 2] > 1:
                    self.affinities[i + 2] = neutral
                # if first type also resists, set affinity to "double resist"
                elif self.affinities[i + 2] < 1:
                    self.affinities[i + 2] = double_resist

            # if second type is immune
            if self.type2[i + 2] == 0:
                # set affinity to "immune"
                self.affinities[i + 2] = immune

    def evolve(self):
        pty.party[f'slot{self.party_index}'] = Pokemon(*self.evo_mon, level=self.lv, party_index=self.party_index)

# Pokemon list
evo_mon = 10
pokemove = 11
pokelearnset = 12
e_moves = 13

rng = random.randint(1, 2)

#############
# Empty
empty = [0, "", types[0], types[0],
         1, 1, 1, 1, 1,
         None, [], [], {}, ()]
empty[pokemove].extend((move_list["None"].copy(), move_list["None"].copy(),))

#############
# Bulbasaur
bulbasaur = [1, "Bulbasaur", types[12], types[4],
             400, 14, 9, 4, 6,
             16, [], [], {}, ()]
bulbasaur[pokemove].extend((move_list["Tackle"].copy(),
                            move_list["Vine Whip"].copy(),
                            ))
bulbasaur[pokelearnset] = {
    8: "Poison Powder",
    12: "Mud Slap"
}
bulbasaur[e_moves] = (move_list["Vine Whip"].copy(),
                      move_list["Poison Powder"].copy(),
                      )
#############
# Ivysaur
ivysaur = [2, "Ivysaur", types[12], types[4],
           520, 32, 24, 10, 9,
           36, [], [], {}, ()]
ivysaur[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Vine Whip"].copy(),
                          move_list["Poison Powder"].copy(),
                          move_list["Mud Slap"].copy(),
                          ))
ivysaur[pokelearnset] = {
    19: "Razor Leaf",
    27: "Power Whip"
}
ivysaur[e_moves] = (move_list["Razor Leaf"].copy(),
                    move_list["None"].copy(),
                    )
bulbasaur[evo_mon] = ivysaur
#############
# Venusaur
venusaur = [3, "Venusaur", types[12], types[4],
            640, 51, 38, 19, 6,
            None, [], [], {}, ()]
venusaur[pokemove].extend((move_list["Poison Powder"].copy(),
                           move_list["Mud Slap"].copy(),
                           move_list["Razor Leaf"].copy(),
                           move_list["Power Whip"].copy(),
                           ))
venusaur[pokelearnset] = {
    38: "Sludge Bomb",
    46: "Solar Beam",
    50: "Earthquake",
    57: "Hyper Beam",
    65: "Frenzy Plant"
}
venusaur[e_moves] = (move_list["Solar Beam"].copy(),
                     move_list["Sludge Bomb"].copy() if rng == 1 else move_list["Earthquake"].copy(),
                     )
ivysaur[evo_mon] = venusaur
#############
# Charmander
charmander = [4, "Charmander", types[10], types[0],
              310, 16, 18, 7, 5,
              16, [], [], {}, ()]
charmander[pokemove].extend((move_list["Scratch"].copy(),
                             move_list["Ember"].copy(),))
charmander[pokelearnset] = {
    8: "Metal Claw",
    12: "Dragon Breath"
}
charmander[e_moves] = (move_list["Scratch"].copy(),
                       move_list["Ember"].copy(),
                       )
#############
# Charmeleon
charmeleon = [5, "Charmeleon", types[10], types[0],
              420, 35, 30, 11, 6,
              36, [], [], {}, ()]
charmeleon[pokemove].extend((move_list["Scratch"].copy(),
                             move_list["Ember"].copy(),
                             move_list["Metal Claw"].copy(),
                             move_list["Dragon Breath"].copy(),
                             ))
charmeleon[pokelearnset] = {
    18: "Fire Fang",
    24: "Slash"
}
charmeleon[e_moves] = (move_list["Fire Fang"].copy(),
                       move_list["None"].copy(),
                       )
charmander[evo_mon] = charmeleon
#############
# Charizard
charizard = [6, "Charizard", types[10], types[3],
             560, 58, 44, 14, 7,
             None, [], [], {}, ()]
charizard[pokemove].extend((move_list["Metal Claw"].copy(),
                            move_list["Dragon Breath"].copy(),
                            move_list["Fire Fang"].copy(),
                            move_list["Slash"].copy(),
                            ))
charizard[pokelearnset] = {
    38: "Air Slash",
    44: "Flamethrower",
    49: "Dragon Claw",
    56: "Seismic Toss",
    65: "Blast Burn",
}
charizard[e_moves] = (move_list["Flamethrower"].copy(),
                      move_list["Dragon Claw"].copy() if rng == 1 else move_list["Seismic Toss"].copy(),
                      )
charmeleon[evo_mon] = charizard
#############
# Squirtle
squirtle = [7, "Squirtle", types[11], types[0],
            440, 14, 7, 6, 2,
            16, [], [], {}, ()]
squirtle[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Water Gun"].copy(),
                           ))
squirtle[pokelearnset] = {
    8: "Bite",
    12: "Rapid Spin"
}
squirtle[e_moves] = (move_list["Rapid Spin"].copy(),
                     move_list["Water Gun"].copy(),
                     )
#############
# Wartortle
wartortle = [8, "Wartortle", types[11], types[0],
             580, 30, 17, 8, 6,
             32, [], [], {}, ()]
wartortle[pokemove].extend((move_list["Tackle"].copy(),
                            move_list["Water Gun"].copy(),
                            move_list["Bite"].copy(),
                            move_list["Rapid Spin"].copy(),
                            ))
wartortle[pokelearnset] = {
    21: "Water Pulse",
    28: "Ice Punch",
}
wartortle[e_moves] = (move_list["Water Pulse"].copy(),
                      move_list["None"].copy(),
                      )
squirtle[evo_mon] = wartortle
#############
# Blastoise
blastoise = [9, "Blastoise", types[11], types[0],
             720, 50, 34, 11, 3,
             None, [], [], {}, ()]
blastoise[pokemove].extend((move_list["Rapid Spin"].copy(),
                            move_list["Water Pulse"].copy(),
                            move_list["Ice Punch"].copy(),
                            ))
blastoise[pokelearnset] = {
    38: "Flash Cannon",
    46: "Hydro Pump",
    51: "Skull Bash",
    58: "Blizzard",
    65: "Hydro Cannon",
}
blastoise[e_moves] = (move_list["Hydro Pump"].copy(),
                      move_list["Skull Bash"].copy() if rng == 1 else move_list["Flash Cannon"].copy(),
                      )
wartortle[evo_mon] = blastoise
#############
# Caterpie
caterpie = [10, "Caterpie", types[7], types[0],
            270, 4, 5, 2, 2,
            12, [], [], {}, ()]
caterpie[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Bug Bite"].copy(),
                           ))
caterpie[pokelearnset] = {
    7: "Electro Web",
}
caterpie[e_moves] = (move_list["Bug Bite"].copy(),
                     move_list["None"].copy(),
                     )
#############
# Metapod
metapod = [11, "Metapod", types[7], types[0],
           450, 4, 1, 3, 0,
           18, [], [], {}, ()]
metapod[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Bug Bite"].copy(),
                          move_list["Electro Web"].copy(),
                          ))
metapod[pokelearnset] = {
    # 7: "Electro Web",
}
metapod[e_moves] = (move_list["Tackle"].copy(),
                    move_list["None"].copy(),
                    )
caterpie[evo_mon] = metapod
#############
# Butterfree
butterfree = [12, "Butterfree", types[7], types[3],
              530, 35, 39, 8, 9,
              None, [], [], {}, ()]
butterfree[pokemove].extend((move_list["Tackle"].copy(),
                             move_list["Bug Bite"].copy(),
                             move_list["Electro Web"].copy(),
                             ))
butterfree[pokelearnset] = {
    18: "Gust",
    25: "Psybeam",
    29: "Bug Buzz",
    36: "Energy Ball",
    42: "Air Slash",
}
butterfree[e_moves] = (move_list["Confusion"].copy(),
                       move_list["None"].copy(),
                       )
metapod[evo_mon] = butterfree
#############
# Kakuna
kakuna = [14, "Kakuna", types[7], types[4],
          420, 8, 1, 3, 0,
          18, [], [], {}, ()]
kakuna[pokemove].extend((move_list["Tackle"].copy(),
                         move_list["Poison Sting"].copy(),
                         ))
kakuna[pokelearnset] = {

}
kakuna[e_moves] = (move_list["Poison Sting"].copy(),
                   move_list["None"].copy(),)
#############
# Beedrill
beedrill = [15, "Beedrill", types[7], types[4],
            485, 39, 42, 14, 7,
            None, [], [], {}, ()]
beedrill[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Poison Sting"].copy(),
                           move_list["Fury Attack"].copy(),))
beedrill[pokelearnset] = {
    24: "Fury Cutter",
    28: "Venoshock",
    35: "Twineedle",
    39: "Pursuit",
    44: "Air Cutter",
}
beedrill[e_moves] = (move_list["Twineedle"].copy(),
                     move_list["None"].copy(),
                     )
kakuna[evo_mon] = beedrill
#############
# Pidgey
pidgey = [16, "Pidgey", types[1], types[3],
          370, 6, 14, 2, 2,
          15, [], [], {}, ()]
pidgey[pokemove].extend((move_list["Quick Attack"].copy(),
                         move_list["Gust"].copy(),
                         ))
pidgey[pokelearnset] = {
    7: "Sand Attack",
    14: "Twister"
}
pidgey[e_moves] = (move_list["Gust"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Pidgeotto
pidgeotto = [17, "Pidgeotto", types[1], types[3],
             475, 32, 42, 10, 5,
             30, [], [], {}, ()]
pidgeotto[pokemove].extend((move_list["Quick Attack"].copy(),
                            move_list["Gust"].copy(),
                            move_list["Wing Attack"].copy(),
                            ))
pidgeotto[pokelearnset] = {
    25: "Steel Wing",
}
pidgeotto[e_moves] = (move_list["Wing Attack"].copy(),
                      move_list["None"].copy(),
                      )
pidgey[evo_mon] = pidgeotto
#############
# Pidgeot
pidgeot = [18, "Pidgeot", types[1], types[3],
           570, 48, 57, 15, 10,
           None, [], [], {}, ()]
pidgeot[pokemove].extend((move_list["Quick Attack"].copy(),
                          move_list["Gust"].copy(),
                          move_list["Wing Attack"].copy(),
                          move_list["Steel Wing"].copy(),
                          ))
pidgeot[pokelearnset] = {
    33: "U-turn",
    39: "Heat Wave",
    44: "Fly",
    54: "Ominous Wind",
}
pidgeot[e_moves] = (move_list["Fly"].copy(),
                    move_list["Steel Wing"].copy(),
                    )
pidgeotto[evo_mon] = pidgeot
#############
# Rattata
ratatta = [19, "Rattata", types[1], types[0],
           250, 3, 10, 2, 2,
           20, [], [], {}, ()]
ratatta[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Quick Attack"].copy(),
                          ))
ratatta[pokelearnset] = {
    13: "Bite"
}
ratatta[e_moves] = (move_list["Tackle"].copy(),
                    move_list["None"].copy(),)
#############
# Spearow
spearow = [21, "Spearow", types[1], types[3],
           385, 14, 20, 10, 3,
           27, [], [], {}, ()]
spearow[pokemove].extend((move_list["Fury Attack"].copy(),
                          move_list["Wing Attack"].copy(),
                          ))
spearow[pokelearnset] = {

}
spearow[e_moves] = (move_list["Fury Attack"].copy() if rng == 1 else move_list["Wing Attack"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Fearow
fearow = [22, "Fearow", types[1], types[3],
          470, 50, 48, 17, 6,
          None, [], [], {}, ()]
fearow[pokemove].extend((move_list["Fury Attack"].copy(),
                         move_list["Wing Attack"].copy(),
                         move_list["Drill Peck"].copy(),
                         move_list["Pursuit"].copy(),
                         ))
fearow[pokelearnset] = {

}
fearow[e_moves] = (move_list["Drill Peck"].copy(),
                   move_list["Pursuit"].copy(),
                   )
spearow[evo_mon] = fearow
#############
# Ekans
ekans = [23, "Ekans", types[4], types[0],
         410, 14, 12, 9, 2,
         24, [], [], {}, ()]
ekans[pokemove].extend((move_list["Wrap"].copy(),
                        move_list["Poison Sting"].copy(),
                        ))
ekans[pokelearnset] = {
    16: "Bite",
    20: "Dig",
}
ekans[e_moves] = (move_list["Wrap"].copy(),
                  move_list["Poison Sting"].copy(),
                  )
#############
# Arbok
arbok = [24, "Arbok", types[4], types[0],
         505, 52, 41, 14, 6,
         None, [], [], {}, ()]
arbok[pokemove].extend((move_list["Wrap"].copy(),
                        move_list["Poison Sting"].copy(),
                        move_list["Bite"].copy(),
                        move_list["Dig"].copy(),
                        ))
arbok[pokelearnset] = {
    24: "Poison Fang",
    31: "Iron Tail",
    36: "Crunch",
    42: "Rock Slide",
    55: "Ice Fang",
}
arbok[e_moves] = (move_list["Poison Fang"].copy(),
                  move_list["Iron Tail"].copy(),
                  )
ekans[evo_mon] = arbok
#############
# Pikachu
pikachu = [25, "Pikachu", types[13], types[0],
           375, 18, 32, 12, 13,
           30, [], [], {}, ()]
pikachu[pokemove].extend((move_list["Quick Attack"].copy(),
                          move_list["Thunder Shock"].copy(),
                          ))
pikachu[pokelearnset] = {
    8: "Iron Tail",
    12: "Double Team",
    18: "Electroball"
}
pikachu[e_moves] = (move_list["Thunder Shock"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Raichu
raichu = [26, "Raichu", types[13], types[0],
          500, 58, 52, 16, 18,
          None, [], [], {}, ()]
raichu[pokemove].extend((move_list["Quick Attack"].copy(),
                         move_list["Thunder Shock"].copy(),
                         move_list["Iron Tail"].copy(),
                         move_list["Double Team"].copy(),
                         move_list["Electroball"].copy(),
                         ))
raichu[pokelearnset] = {
    36: "Play Rough",
    42: "Thunderbolt",
    50: "Psychic",
    65: "Volt Tackle",
}
raichu[e_moves] = (move_list["Thunderbolt"].copy(),
                   move_list["Play Rough"].copy(),
                   )
pikachu[evo_mon] = raichu
#############
# Sandshrew
sandshrew = [27, "Sandshrew", types[5], types[0],
             410, 15, 8, 9, 2,
             24, [], [], {}, ()]
sandshrew[pokemove].extend((move_list["Scratch"].copy(),
                            move_list["Poison Sting"].copy(),
                            ))
sandshrew[pokelearnset] = {
    12: "Rollout",
    18: "Fury Cutter",
}
sandshrew[e_moves] = (move_list["Scratch"].copy(),
                      move_list["None"].copy(),
                      )
#############
# Sandslash
sandslash = [28, "Sandslash", types[5], types[0],
             530, 40, 34, 22, 8,
             None, [], [], {}, ()]
sandslash[pokemove].extend((move_list["Scratch"].copy(),
                            move_list["Poison Sting"].copy(),
                            move_list["Rollout"].copy(),
                            move_list["Fury Cutter"].copy(),
                            ))
sandslash[pokelearnset] = {
    25: "Bulldoze",
    31: "Metal Claw",
    36: "Shadow Claw",
    43: "Poison Jab",
    55: "Earthquake",
}
sandslash[e_moves] = (move_list["Bulldoze"].copy(),
                      move_list["Metal Claw"].copy() if rng == 1 else move_list["Shadow Claw"].copy(),
                      )
sandshrew[evo_mon] = sandslash
#############
# Nidoran F
nidoran_f = [29, "Nidoran", types[4], types[0],
             390, 8, 14, 4, 2,
             18, [], [], {}, ()]
nidoran_f[pokemove].extend((move_list["Poison Sting"].copy(),
                            move_list["Bite"].copy(),
                            ))
nidoran_f[pokelearnset] = {
    9: "Take Down",
    16: "Aerial Ace",
}
nidoran_f[e_moves] = (move_list["Poison Sting"].copy(),
                      move_list["Bite"].copy(),
                      )
#############
# Nidorina
nidorina = [30, "Nidorina", types[4], types[0],
            485, 26, 29, 7, 4,
            32, [], [], {}, ()]
nidorina[pokemove].extend((move_list["Poison Sting"].copy(),
                           move_list["Bite"].copy(),
                           move_list["Take Down"].copy(),
                           move_list["Aerial Ace"].copy(),
                           ))
nidorina[pokelearnset] = {
    20: "Poison Fang",
    27: "Crunch",
}
nidorina[e_moves] = (move_list["Poison Fang"].copy(),
                     move_list["None"].copy(),
                     )
nidoran_f[evo_mon] = nidorina
#############
# Nidoqueen
nidoqueen = [31, "Nidoqueen", types[4], types[5],
             635, 48, 41, 10, 5,
             None, [], [], {}, ()]
nidoqueen[pokemove].extend((move_list["Take Down"].copy(),
                            move_list["Aerial Ace"].copy(),
                            move_list["Poison Fang"].copy(),
                            move_list["Crunch"].copy(),
                            ))
nidoqueen[pokelearnset] = {
    34: "Skull Bash",
    38: "Earth Power",
    46: "Iron Tail",
    52: "Blizzard",
    60: "Superpower",
}
nidoqueen[e_moves] = (move_list["Earth Power"].copy(),
                      move_list["Blizzard"].copy() if rng == 1 else move_list["Iron Tail"].copy(),
                      )
nidorina[evo_mon] = nidoqueen
#############
# Nidoran M
nidoran_m = [32, "Nidoran", types[4], types[0],
             365, 10, 13, 4, 3,
             18, [], [], {}, ()]
nidoran_m[pokemove].extend((move_list["Poison Sting"].copy(),
                            move_list["Peck"].copy(),
                            ))
nidoran_m[pokelearnset] = {
    9: "Double Kick",
    16: "Horn Attack"
}
nidoran_m[e_moves] = (move_list["Poison Sting"].copy(),
                      move_list["Peck"].copy(),
                      )
#############
# Nidorino
nidorino = [33, "Nidorino", types[4], types[0],
            430, 32, 31, 7, 4,
            32, [], [], {}, ()]
nidorino[pokemove].extend((move_list["Poison Sting"].copy(),
                           move_list["Peck"].copy(),
                           move_list["Double Kick"].copy(),
                           move_list["Horn Attack"].copy(),
                           ))
nidorino[pokelearnset] = {
    21: "Shadow Claw",
    27: "Poison Jab"
}
nidorino[e_moves] = (move_list["Horn Attack"].copy(),
                     move_list["Double Kick"].copy(),
                     )
nidoran_m[evo_mon] = nidorino
#############
# Nidoking
nidoking = [34, "Nidoking", types[4], types[5],
            580, 57, 42, 13, 5,
            None, [], [], {}, ()]
nidoking[pokemove].extend((move_list["Double Kick"].copy(),
                           move_list["Horn Attack"].copy(),
                           move_list["Shadow Claw"].copy(),
                           move_list["Poison Jab"].copy(),
                           ))
nidoking[pokelearnset] = {
    34: "Megahorn",
    38: "Earth Power",
    44: "Fire Blast",
    52: "Dragon Tail",
    60: "Superpower",
}
nidoking[e_moves] = (move_list["Megahorn"].copy(),
                     move_list["Earth Power"].copy() if rng == 1 else move_list["Fire Blast"].copy(),
                     )
nidorino[evo_mon] = nidoking
#############
# Clefairy
clefairy = [35, "Clefairy", types[18], types[0],
            450, 14, 16, 6, 3,
            28, [], [], {}, ()]
clefairy[pokemove].extend((move_list["Pound"].copy(),
                           move_list["Fairy Wind"].copy(),
                           ))
clefairy[pokelearnset] = {
    12: "Magical Leaf",
    18: "Mystical Fire",
}

clefairy[e_moves] = (move_list["Magical Leaf"].copy() if rng == 1 else move_list["Mystical Fire"].copy(),
                     move_list["Fairy Wind"].copy(),
                     )
#############
# Clefable
clefable = [36, "Clefable", types[18], types[0],
            655, 48, 43, 17, 6,
            None, [], [], {}, ()]
clefable[pokemove].extend((move_list["Pound"].copy(),
                           move_list["Fairy Wind"].copy(),
                           move_list["Magical Leaf"].copy(),
                           move_list["Mystical Fire"].copy(),
                           ))
clefable[pokelearnset] = {
    30: "Moonblast",
    36: "Meteor Mash",
    42: "Stored Power",
    48: "Charge Beam",
    56: "Solar Beam",
}

clefable[e_moves] = (move_list["Moonblast"].copy(),
                     move_list["Stored Power"].copy() if rng == 1 else move_list["Meteor Mash"].copy(),
                     )
clefairy[evo_mon] = clefable
#############
# Vulpix
vulpix = [37, "Vulpix", types[10], types[0],
          385, 14, 15, 7, 5,
          32, [], [], {}, ()]
vulpix[pokemove].extend((move_list["Quick Attack"].copy(),
                         move_list["Ember"].copy(),
                         ))
vulpix[pokelearnset] = {
    10: "Hex",
    16: "Incinerate",
    24: "Extrasensory"
}
vulpix[e_moves] = (move_list["Ember"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Ninetales
ninetales = [38, "Ninetales", types[10], types[0],
             575, 51, 42, 18, 12,
             None, [], [], {}, ()]
ninetales[pokemove].extend((move_list["Quick Attack"].copy(),
                            move_list["Ember"].copy(),
                            move_list["Hex"].copy(),
                            move_list["Incinerate"].copy(),
                            move_list["Extrasensory"].copy(),)
                            )
ninetales[pokelearnset] = {
    34: "Fire Spin",
    39: "Energy Ball",
    47: "Psyshock",
    54: "Shadow Ball",
}
ninetales[e_moves] = (move_list["Fire Spin"].copy(),
                      move_list["Psyshock"].copy(),
                      )
vulpix[evo_mon] = ninetales
#############
# Jigglypuff
jigglypuff = [39, "Jigglypuff", types[1], types[18],
              415, 10, 9, 8, 2,
              26, [], [], {}, ()]
jigglypuff[pokemove].extend((move_list["Pound"].copy(),
                             move_list["Disarming Voice"].copy(),
                             ))
jigglypuff[pokelearnset] = {
    15: "Rollout",
    22: "Gyro Ball",
}
jigglypuff[e_moves] = (move_list["Disarming Voice"].copy(),
                       move_list["None"].copy(),
                       )
#############
# Wigglytuff
wigglytuff = [40, "Wigglytuff", types[1], types[18],
              660, 44, 37, 12, 12,
              None, [], [], {}, ()]
wigglytuff[pokemove].extend((move_list["Pound"].copy(),
                             move_list["Disarming Voice"].copy(),
                             move_list["Rollout"].copy(),
                             move_list["Gyro Ball"].copy(),
                            ))
wigglytuff[pokelearnset] = {
    28: "Hyper Voice",
    33: "Play Rough",
    37: "Zen Headbutt",
    42: "Fire Punch",
    48: "Shadow Ball",
}
wigglytuff[e_moves] = ((move_list["Hyper Voice"].copy(),
                        move_list["Disarming Voice"].copy(),
                        ))
jigglypuff[evo_mon] = wigglytuff
#############
# Zubat
zubat = [41, "Zubat", types[4], types[3],
         220, 2, 18, 2, 10,
         None, [], [], {}, ()]
zubat[pokemove].extend((move_list["Absorb"].copy(),
                        move_list["Astonish"].copy(),
                        ))
zubat[pokelearnset] = {
    14: "Poison Fang",
    20: "Leech Life",
}
zubat[e_moves] = ((move_list["Leech Life"].copy(),
                   move_list["None"].copy(),
                   ))
#############
# Oddish
oddish = [43, "Oddish", types[12], types[4],
          315, 6, 10, 1, 2,
          19, [], [], {}, ()]
oddish[pokemove].extend((move_list["Absorb"].copy(),
                         move_list["Acid"].copy(),
                         ))
oddish[pokelearnset] = {

}
oddish[e_moves] = (move_list["Absorb"].copy(),
                   move_list["Acid"].copy(),)
#############
# Meowth
meowth = [52, "Meowth", types[1], types[0],
          390, 17, 20, 14, 8,
          25, [], [], {}, ()]
meowth[pokemove].extend((move_list["Scratch"].copy(),
                         move_list["Bite"].copy(),
                         ))
meowth[pokelearnset] = {
    11: "Pay Day",
    17: "Aerial Ace"
}
meowth[e_moves] = (move_list["Pay Day"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Persian
persian = [53, "Persian", types[1], types[0],
           540, 51, 60, 24, 12,
           None, [], [], {}, ()]
persian[pokemove].extend((move_list["Scratch"].copy(),
                          move_list["Bite"].copy(),
                          move_list["Pay Day"].copy(),
                          move_list["Aerial Ace"].copy(),
                          ))
persian[pokelearnset] = {
    28: "Slash",
    34: "Power Gem",
    38: "Foul Play",
    42: "Metal Claw",
    48: "Play Rough",
}
persian[e_moves] = (move_list["Slash"].copy(),
                    move_list["Foul Play"].copy(),
                    )
meowth[evo_mon] = persian
#############
# Psyduck
psyduck = [54, "Psyduck", types[11], types[0],
           380, 12, 6, 4, 1,
           28, [], [], {}, ()]
psyduck[pokemove].extend((move_list["Scratch"].copy(),
                          move_list["Water Gun"].copy(),
                          ))
psyduck[pokelearnset] = {
    13: "Confusion",
    19: "Water Pulse",
    24: "Shadow Claw"
}
psyduck[e_moves] = (move_list["Confusion"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Golduck
golduck = [55, "Golduck", types[11], types[14],
           480, 38, 49, 8, 4,
           None, [], [], {}, ()]
golduck[pokemove].extend((move_list["Water Gun"].copy(),
                          move_list["Confusion"].copy(),
                          move_list["Water Pulse"].copy(),
                          move_list["Shadow Claw"].copy(),
                          ))
golduck[pokelearnset] = {
    29: "Psybeam",
    34: "Power Gem",
    39: "Surf",
    44: "Focus Blast",
    50: "Psychic",
}
golduck[e_moves] = (move_list["Psybeam"].copy(),
                    move_list["Surf"].copy(),
                    )
psyduck[evo_mon] = golduck
#############
# Mankey
mankey = [56, "Mankey", types[2], types[0],
          360, 19, 22, 4, 8,
          28, [], [], {}, ()]
mankey[pokemove].extend((move_list["Scratch"].copy(),
                         move_list["Low Kick"].copy(),
                         ))
mankey[pokelearnset] = {
    15: "Dig",
    20: "Acrobatics",
}
mankey[e_moves] = (move_list["Low Kick"].copy(),
                   move_list["Acrobatics"].copy(),
                   )
#############
# Growlithe
growlithe = [58, "Growlithe", types[10], types[0],
             355, 16, 19, 6, 3,
             35, [], [], {}, ()]
growlithe[pokemove].extend((move_list["Bite"].copy(),
                            move_list["Ember"].copy(),
                            ))
growlithe[pokelearnset] = {
    15: "Take Down",
    20: "Flame Wheel",
    27: "Dig",
}
growlithe[e_moves] = (move_list["Flame Wheel"].copy(),
                      move_list["None"].copy(),
                      )
#############
# Arcanine
arcanine = [59, "Arcanine", types[10], types[0],
            555, 54, 59, 13, 8,
            None, [], [], {}, ()]
arcanine[pokemove].extend((move_list["Bite"].copy(),
                           move_list["Take Down"].copy(),
                           move_list["Flame Wheel"].copy(),
                           move_list["Dig"].copy(),
                           ))
arcanine[pokelearnset] = {
    37: "Extreme Speed",
    41: "Thunder Fang",
    46: "Flare Blitz",
    53: "Play Rough",
    60: "Close Combat",
}
arcanine[e_moves] = (move_list["Flare Blitz"].copy(),
                     move_list["Extreme Speed"].copy(),
                     )
growlithe[evo_mon] = arcanine
#############
# Abra
abra = [63, "Abra", types[14], types[0],
        310, 16, 6, 5, 0,
        21, [], [], {}, ()]
abra[pokemove].extend((move_list["Confusion"].copy(),
                       move_list["Headbutt"].copy(),
                       ))
abra[pokelearnset] = {

}
abra[e_moves] = (move_list["Confusion"].copy(),
                 move_list["None"].copy(),
                 )
#############
# Kadabra
kadabra = [64, "Kadabra", types[14], types[0],
           425, 34, 40, 10, 4,
           38, [], [], {}, ()]
kadabra[pokemove].extend((move_list["Confusion"].copy(),
                          move_list["Headbutt"].copy(),
                          ))
kadabra[pokelearnset] = {
    24: "Energy Ball",
    28: "Psybeam",
    32: "Charge Beam",
}
kadabra[e_moves] = (move_list["Psybeam"].copy(),
                    move_list["Energy Ball"].copy() if rng == 1 else move_list["Charge Beam"].copy(),
                    )
abra[evo_mon] = kadabra
#############
# Alakazam
alakazam = [65, "Alakazam", types[14], types[0],
            520, 60, 52, 15, 7,
            None, [], [], {}, ()]
alakazam[pokemove].extend((move_list["Headbutt"].copy(),
                           move_list["Energy Ball"].copy(),
                           move_list["Psybeam"].copy(),
                           move_list["Charge Beam"].copy(),
                           ))
alakazam[pokelearnset] = {
    39: "Focus Blast",
    42: "Signal Beam",
    47: "Psychic",
    56: "Dazzling Gleam",
    65: "Hyper Beam",
}
alakazam[e_moves] = (move_list["Psychic"].copy(),
                     move_list["Focus Blast"].copy() if rng == 1 else move_list["Signal Beam"].copy(),
                     )
kadabra[evo_mon] = alakazam
#############
# Machop
machop = [66, "Machop", types[2], types[0],
          410, 18, 9, 5, 2,
          24, [], [], {}, ()]
machop[pokemove].extend((move_list["Karate Chop"].copy(),
                         move_list["Rock Smash"].copy(),))
machop[pokelearnset] = {
    15: "Knock Off",
}
machop[e_moves] = (move_list["Karate Chop"].copy(),
                   move_list["None"].copy()
                   ,)
#############
# Machoke
machoke = [67, "Machoke", types[2], types[0],
           470, 34, 29, 12, 4,
           38, [], [], {}, ()]
machoke[pokemove].extend((move_list["Karate Chop"].copy(),
                          move_list["Rock Smash"].copy(),
                          move_list["Knock Off"].copy(),
                          ))
machoke[pokelearnset] = {
    26: "Dual Chop",
    29: "Submission",
    34: "Rock Slide",
}
machoke[e_moves] = (move_list["Submission"].copy(),
                    move_list["Dual Chop"].copy(),
                    )
machop[evo_mon] = machoke
#############
# Machamp
machamp = [68, "Machamp", types[2], types[0],
           620, 60, 38, 18, 6,
           None, [], [], {}, ()]
machamp[pokemove].extend((move_list["Knock Off"].copy(),
                          move_list["Dual Chop"].copy(),
                          move_list["Submission"].copy(),
                          move_list["Rock Slide"].copy(),
                          ))
machamp[pokelearnset] = {
    38: "Heavy Slam",
    43: "Poison Jab",
    48: "Dynamic Punch",
    53: "Stone Edge",
    59: "Thunder Punch",
}
machamp[e_moves] = (move_list["Dynamic Punch"].copy(),
                    move_list["Heavy Slam"].copy() if rng == 1 else move_list["Poison Jab"].copy(),
                    )
machoke[evo_mon] = machamp
#############
# Tentacool
tentacool = [72, "Tentacool", types[11], types[4],
             350, 9, 11, 1, 2,
             26, [], [], {}, ()]
tentacool[pokemove].extend((move_list["Wrap"].copy(),
                            move_list["Acid"].copy(),))
tentacool[pokelearnset] = {

}
tentacool[e_moves] = (move_list["Wrap"].copy(),
                      move_list["Acid"].copy(),
                      )
#############
# Tentacruel
tentacruel = [73, "Tentacruel", types[11], types[4],
              590, 45, 37, 14, 5,
              None, [], [], {}, ()]
tentacruel[pokemove].extend((move_list["Wrap"].copy(),
                             move_list["Acid"].copy(),
                             ))
tentacruel[pokelearnset] = {
    26: "Water Pulse",
    29: "Constrict",
    34: "Sludge Bomb",
    41: "Giga Drain",
    48: "Hydro Pump",
}
tentacruel[e_moves] = (move_list["Water Pulse"].copy(),
                       move_list["Sludge Bomb"].copy(),
                       )
tentacool[evo_mon] = tentacruel
#############
# Geodude
geodude = [74, "Geodude", types[6], types[5],
           430, 12, 4, 3, 0,
           24, [], [], {}, ()]
geodude[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Rollout"].copy(),
                          ))
geodude[pokelearnset] = {
    15: "Bulldoze",
    20: "Gyro Ball",
}
geodude[e_moves] = (move_list["Rollout"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Graveler
graveler = [75, "Graveler", types[6], types[5],
            560, 30, 19, 6, 2,
            36, [], [], {}, ()]
graveler[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Rollout"].copy(),
                           move_list["Bulldoze"].copy(),
                           move_list["Gyro Ball"].copy(),
                           ))
graveler[pokelearnset] = {
    26: "Rock Slide",
    30: "Fire Punch",

}
graveler[e_moves] = (move_list["Rock Slide"].copy(),
                     move_list["Bulldoze"].copy(),
                     )
geodude[evo_mon] = graveler
#############
# Golem
golem = [76, "Golem", types[6], types[5],
         650, 56, 28, 17, 5,
         None, [], [], {}, ()]
golem[pokemove].extend((move_list["Bulldoze"].copy(),
                        move_list["Gyro Ball"].copy(),
                        move_list["Rock Slide"].copy(),
                        move_list["Fire Punch"].copy(),
                        ))
golem[pokelearnset] = {
    36: "Heavy Slam",
    40: "Earthquake",
    46: "Stone Edge",
    51: "Double Edge",
    58: "Superpower",
}
golem[e_moves] = (move_list["Stone Edge"].copy(),
                  move_list["Earthquake"].copy(),
                  )
graveler[evo_mon] = golem
#############
# Ponyta
ponyta = [77, "Ponyta", types[10], types[0],
          365, 12, 26, 4, 6,
          24, [], [], {}, ()]
ponyta[pokemove].extend((move_list["Tackle"].copy(),
                         move_list["Ember"].copy(),
                         ))
ponyta[pokelearnset] = {
    15: "Double Kick",
    20: "Flame Charge",
    25: "Stomp",
}
ponyta[e_moves] = (move_list["Double Kick"].copy(),
                   move_list["Flame Charge"].copy(),
                   )
#############
# Rapidash
rapidash = [78, "Rapidash", types[10], types[0],
            590, 47, 63, 12, 14,
            None, [], [], {}, ()]
rapidash[pokemove].extend((move_list["Ember"].copy(),
                           move_list["Double Kick"].copy(),
                           move_list["Flame Charge"].copy(),
                           move_list["Stomp"].copy(),
                           ))
rapidash[pokelearnset] = {
    26: "Smart Strike",
    29: "Megahorn",
    35: "Flare Blitz",
    42: "Bounce",
    53: "High Horsepower",
}
rapidash[e_moves] = (move_list["Flare Blitz"].copy(),
                     move_list["Bounce"].copy() if rng == 1 else move_list["High Horsepower"].copy(),
                     )
ponyta[evo_mon] = rapidash
#############
# Slowpoke
slowpoke = [79, "Slowpoke", types[11], types[14],
            430, 14, 4, 1, 1,
            25, [], [], {}, ()]
slowpoke[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Water Gun"].copy(),
                           ))
slowpoke[pokelearnset] = {
    15: "Confusion",
    19: "Icy Wind",
    24: "Iron Tail",
}
slowpoke[e_moves] = (move_list["Water Gun"].copy() if rng == 1 else move_list["Confusion"].copy(),
                     move_list["None"].copy(),
                     )
#############
# Slowbro
slowbro = [80, "Slowbro", types[11], types[14],
           625, 50, 18, 4, 2,
           None, [], [], {}, ()]
slowbro[pokemove].extend((move_list["Water Gun"].copy(),
                          move_list["Confusion"].copy(),
                          move_list["Icy Wind"].copy(),
                          move_list["Iron Tail"].copy(),
                          ))
slowbro[pokelearnset] = {
    26: "Water Pulse",
    30: "Bulldoze",
    35: "Zen Headbutt",
    41: "Avalanche",
    50: "Aqua Tail",
}
slowbro[e_moves] = (move_list["Aqua Tail"].copy(),
                    move_list["Zen Headbutt"].copy(),
                    )
slowpoke[evo_mon] = slowbro
#############
# Magnemite
magnemite = [81, "Magnemite", types[13], types[9],
             380, 8, 13, 5, 2,
             23, [], [], {}, ()]
magnemite[pokemove].extend((move_list["Thunder Shock"].copy(),
                           move_list["Sonic Boom"].copy(),
                           ))
magnemite[pokelearnset] = {
    15: "Gyro Ball",
}
magnemite[e_moves] = (move_list["Thunder Shock"].copy() if rng == 1 else move_list["Sonic Boom"].copy(),
                      move_list["None"].copy(),
                      )
#############
# Magneton
magneton = [82, "Magneton", types[13], types[9],
            570, 48, 41, 13, 5,
            None, [], [], {}, ()]
magneton[pokemove].extend((move_list["Thunder Shock"].copy(),
                           move_list["Sonic Boom"].copy(),
                           move_list["Gyro Ball"].copy(),
                           ))
magneton[pokelearnset] = {
    24: "Discharge",
    32: "Tri Attack",
    37: "Flash Cannon",
    48: "Signal Beam",
    55: "Zap Cannon",
}
magneton[e_moves] = (move_list["Discharge"].copy(),
                     move_list["Tri Attack"].copy(),
                     )
magnemite[evo_mon] = magneton
#############
# Farfetch'd
farfetchd = [83, "Farfetchd", types[1], types[3],
             450, 20, 32, 12, 8,
             None, [], [], {}, ()]
farfetchd[pokemove].extend((move_list["Peck"].copy(),
                            move_list["Fury Attack"].copy(),
                            ))
farfetchd[pokelearnset] = {
    16: "Fury Cutter",
    20: "Aerial Ace",
    24: "Slash",
    31: "Leaf Blade",
    42: "Night Slash",
}
farfetchd[e_moves] = (move_list["Aerial Ace"].copy(),
                      move_list["None"].copy(),
                      )
#############
# Seel
seel = [86, "Seel", types[11], types[0],
        380, 12, 8, 2, 2,
        21, [], [], {}, ()]
seel[pokemove].extend((move_list["Tackle"].copy(),
                       move_list["Icy Wind"].copy(),
                       ))
seel[pokelearnset] = {
    14: "Water Gun",
    18: "Take Down",
}
seel[e_moves] = (move_list["Icy Wind"].copy(),
                 move_list["None"].copy(),
                 )
#############
# Dewgong
dewgong = [87, "Dewgong", types[11], types[15],
           580, 42, 38, 8, 3,
           None, [], [], {}, ()]
dewgong[pokemove].extend((move_list["Icy Wind"].copy(),
                          move_list["Water Gun"].copy(),
                          move_list["Take Down"].copy(),
                          ))
dewgong[pokelearnset] = {
    22: "Bubble Beam",
    25: "Aurora Beam",
    30: "Signal Beam",
    37: "Drill Run",
    50: "Sheer Cold",
}
dewgong[e_moves] = (move_list["Bubble Beam"].copy(),
                    move_list["Aurora Beam"].copy(),
                    )
seel[evo_mon] = dewgong
#############
# Gastly
gastly = [92, "Gastly", types[8], types[4],
          320, 16, 14, 4, 6,
          22, [], [], {}, ()]
gastly[pokemove].extend((move_list["Lick"].copy(),
                         move_list["Acid Spray"].copy(),
                         ))
gastly[pokelearnset] = {
    18: "Icy Wind",
}
gastly[e_moves] = (move_list["Lick"].copy(),
                   move_list["Acid Spray"].copy(),
                   )
#############
# Haunter
haunter = [93, "Haunter", types[8], types[4],
           420, 34, 46, 8, 11,
           38, [], [], {}, ()]
haunter[pokemove].extend((move_list["Lick"].copy(),
                          move_list["Acid Spray"].copy(),
                          move_list["Icy Wind"].copy(),
                          ))
haunter[pokelearnset] = {
    18: "Shadow Punch",
    27: "Giga Drain",
}
haunter[e_moves] = (move_list["Shadow Punch"].copy(),
                    move_list["Acid Spray"].copy(),
                    )
gastly[evo_mon] = haunter
#############
# Gengar
gengar = [94, "Gengar", types[8], types[4],
          535, 53, 62, 12, 16,
          None, [], [], {}, ()]
gengar[pokemove].extend((move_list["Acid Spray"].copy(),
                         move_list["Icy Wind"].copy(),
                         move_list["Shadow Punch"].copy(),
                         move_list["Giga Drain"].copy(),
                         ))
gengar[pokelearnset] = {
    41: "Sludge Bomb",
    46: "Psychic",
    51: "Focus Blast",
    58: "Thunder",
    65: "Night Shade",
}
gengar[e_moves] = (move_list["Night Shade"].copy(),
                   move_list["Psychic"].copy() if rng == 1 else move_list["Sludge Bomb"].copy(),
                   )
haunter[evo_mon] = gengar
#############
# Onix
onix = [95, "Onix", types[6], types[5],
        460, 28, 22, 7, 3,
        31, [], [], {}, ()]
onix[pokemove].extend((move_list["Slam"].copy(),
                       move_list["Rock Throw"].copy(),
                       ))
onix[pokelearnset] = {
    19: "Bulldoze",
    24: "Dragon Breath",
    30: "Rock Slide",
    36: "Brutal Swing"
}
onix[e_moves] = (move_list["Slam"].copy(),
                 move_list["None"].copy(),
                 )
#############
# Hypno
hypno = [97, "Hypno", types[14], types[0],
         510, 34, 28, 4, 2,
         None, [], [], {}, ()]
hypno[pokemove].extend((move_list["Pound"].copy(),
                        move_list["Psybeam"].copy(),
                        ))
hypno[pokelearnset] = {
    22: "Poison Gas",
    27: "Foul Play",
    34: "Body Press",
    43: "Draining Kiss",
    50: "Psychic"
}
hypno[e_moves] = (move_list["Psybeam"].copy(),
                  move_list["Foul Play"].copy(),
                  )
#############
# Krabby
krabby = [98, "Krabby", types[11], types[0],
          330, 18, 25, 8, 3,
          23, [], [], {}, ()]
krabby[pokemove].extend((move_list["Bubble"].copy(),
                         move_list["Vice Grip"].copy(),
                         ))
krabby[pokelearnset] = {

}
krabby[e_moves] = (move_list["Bubble"].copy() if rng == 1 else move_list["Vice Grip"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Kingler
kingler = [99, "Kingler", types[11], types[0],
           560, 47, 42, 17, 6,
           None, [], [], {}, ()]
kingler[pokemove].extend((move_list["Bubble"].copy(),
                          move_list["Vice Grip"].copy(),
                          ))
kingler[pokelearnset] = {
    23: "Crabhammer",
    27: "Metal Claw",
    35: "Brick Break",
    42: "X-Scissor",
    55: "Guillotine"
}
kingler[e_moves] = (move_list["Crabhammer"].copy(),
                    move_list["Metal Claw"].copy() if rng == 1 else move_list["Brick Break"].copy(),
                    )
krabby[evo_mon] = kingler
#############
# Exeggutor
exeggutor = [103, "Exeggutor", types[12], types[14],
             625, 64, 36, 5, 2,
             None, [], [], {}, ()]
exeggutor[pokemove].extend((move_list["Stomp"].copy(),
                            move_list["Seed Bomb"].copy(),
                            ))
exeggutor[pokelearnset] = {
    28: "Egg Bomb",
    36: "Psychic",
    47: "Wood Hammer",
    60: "Sludge Bomb",
}
exeggutor[e_moves] = (move_list["Seed Bomb"].copy(),
                      move_list["Psychic"].copy(),
                      )
#############
# Hitmonlee
hitmonlee = [106, "Hitmonlee", types[2], types[0],
             490, 49, 52, 13, 10,
             None, [], [], {}, ()]
hitmonlee[pokemove].extend((move_list["Mega Kick"].copy(),
                            move_list["Double Kick"].copy(),
                            ))
hitmonlee[pokelearnset] = {
    21: "Bounce",
    26: "Blaze Kick",
    33: "Pursuit",
    44: "High Jump Kick",
}
hitmonlee[e_moves] = (move_list["Double Kick"].copy(),
                      move_list["None"].copy(),
                      )
#############
# Hitmonchan
hitmonchan = [107, "Hitmonchan", types[2], types[0],
              540, 40, 43, 11, 8,
              None, [], [], {}, ()]
hitmonchan[pokemove].extend((move_list["Mega Punch"].copy(),
                             move_list["Mach Punch"].copy(),
                            ))
hitmonchan[pokelearnset] = {
    21: "Thunder Punch",
    26: "Fire Punch",
    33: "Ice Punch",
    44: "Focus Punch",
}
hitmonchan[e_moves] = (move_list["Mega Punch"].copy(),
                       move_list["None"].copy(),
                       )
#############
# Koffing
koffing = [109, "Koffing", types[4], types[0],
           380, 12, 6, 3, 2,
           None, [], [], {}, ()]
koffing[pokemove].extend((move_list["Poison Gas"].copy(),
                          move_list["Tackle"].copy(),
                          ))
koffing[pokelearnset] = {

}
koffing[e_moves] = (move_list["Poison Gas"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Rhyhorn
rhyhorn = [111, "Rhyhorn", types[5], types[6],
           450, 20, 10, 6, 1,
           28, [], [], {}, ()]
rhyhorn[pokemove].extend((move_list["Horn Attack"].copy(),
                          move_list["Bulldoze"].copy(),
                          ))
rhyhorn[pokelearnset] = {
    17: "Rock Blast",
    24: "Thunder Fang",
}
rhyhorn[e_moves] = (move_list["Horn Attack"].copy(),
                    move_list["Bulldoze"].copy(),
                    )
#############
# Rhydon
rhydon = [112, "Rhydon", types[5], types[6],
          600, 50, 31, 12, 4,
          None, [], [], {}, ()]
rhydon[pokemove].extend((move_list["Horn Attack"].copy(),
                         move_list["Bulldoze"].copy(),
                         move_list["Rock Blast"].copy(),
                         move_list["Thunder Fang"].copy(),
                         ))
rhydon[pokelearnset] = {
    29: "Hammer Arm",
    36: "Rock Slide",
    41: "Megahorn",
    49: "Dragon Rush",
    55: "Earthquake",
}
rhydon[e_moves] = (move_list["Rock Slide"].copy(),
                   move_list["Hammer Arm"].copy() if rng == 1 else move_list["Megahorn"].copy(),
                   )
rhyhorn[evo_mon] = rhydon
#############
# Cubone
cubone = [104, "Cubone", types[5], types[0],
          415, 20, 14, 14, 4,
          30, [], [], {}, ()]
cubone[pokemove].extend((move_list["Bone Club"].copy(),
                         move_list["Headbutt"].copy()
                         ,))
cubone[pokelearnset] = {
    9: "Brick Break",
    16: "Fury Cutter",
    22: "Bone Rush",
    26: "Fling",
}
cubone[e_moves] = (move_list["Bone Club"].copy(),
                   move_list["Brick Break"].copy(),
                   )
#############
# Marowak
marowak = [105, "Marowak", types[5], types[0],
           565, 48, 43, 16, 8,
           None, [], [], {}, ()]
marowak[pokemove].extend((move_list["Brick Break"].copy(),
                          move_list["Fury Cutter"].copy(),
                          move_list["Bone Rush"].copy(),
                          move_list["Fling"].copy(),
                          ))
marowak[pokelearnset] = {
    33: "Iron Head",
    38: "Aerial Ace",
    43: "Skull Bash",
    49: "Thunder Punch",
    55: "Bonemerang",
}
marowak[e_moves] = (move_list["Bonemerang"].copy(),
                    move_list["Iron Head"].copy() if rng == 1 else move_list["Skull Bash"].copy(),
                    )
cubone[evo_mon] = marowak
#############
# Chansey
chansey = [113, "Chansey", types[1], types[0],
           620, 12, 10, 3, 1,
           None, [], [], {}, ()]
chansey[pokemove].extend((move_list["Egg Bomb"].copy(),
                          move_list["Seismic Toss"].copy(),
                          ))
chansey[pokelearnset] = {
}
chansey[e_moves] = (move_list["Egg Bomb"].copy(),
                    move_list["Seismic Toss"].copy(),
                    )
#############
# Staryu
staryu = [120, "Staryu", types[11], types[0],
          340, 9, 22, 8, 6,
          27, [], [], {}, ()]
staryu[pokemove].extend((move_list["Bubble Beam"].copy(),
                         move_list["Swift"].copy(),
                         ))
staryu[pokelearnset] = {
    24: "Psybeam",
}
staryu[e_moves] = (move_list["Swift"].copy(),
                   move_list["Bubble Beam"].copy(),
                   )
#############
# Starmie
starmie = [121, "Starmie", types[11], types[14],
           540, 52, 61, 15, 8,
           None, [], [], {}, ()]
starmie[pokemove].extend((move_list["Bubble Beam"].copy(),
                          move_list["Swift"].copy(),
                          move_list["Psybeam"].copy(),
                          ))
starmie[pokelearnset] = {
    29: "Power Gem",
    35: "Surf",
    43: "Psychic",
    55: "Thunder",
}
starmie[e_moves] = (move_list["Psychic"].copy(),
                   move_list["Surf"].copy(),
                   )
staryu[evo_mon] = starmie
#############
# Scyther
scyther = [123, "Scyther", types[7], types[3],
           520, 50, 66, 26, 9,
           None, [], [], {}, ()]
scyther[pokemove].extend((move_list["Fury Cutter"].copy(),
                          move_list["Wing Attack"].copy(),
                          ))
scyther[pokelearnset] = {
    24: "Slash",
    32: "Steel Wing",
    40: "X-Scissor",
    55: "Night Slash",
}
scyther[e_moves] = (move_list["X-Scissor"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Electabuzz
electabuzz = [125, "Electabuzz", types[13], types[0],
              530, 46, 53, 14, 3,
              None, [], [], {}, ()]
electabuzz[pokemove].extend((move_list["Thunder Punch"].copy(),
                             move_list["Iron Tail"].copy(),
                             ))
electabuzz[pokelearnset] = {
    24: "Ice Punch",
    32: "Cross Chop",
    40: "Thunder",
    55: "Signal Beam",
}
electabuzz[e_moves] = (move_list["Thunder Punch"].copy(),
                       move_list["None"].copy(),
                       )
#############
# Magmar
magmar = [126, "Magmar", types[10], types[0],
          580, 52, 44, 4, 10,
          None, [], [], {}, ()]
magmar[pokemove].extend((move_list["Fire Punch"].copy(),
                         move_list["Feint Attack"].copy(),
                         ))
magmar[pokelearnset] = {
    24: "Seismic Toss",
    32: "Belch",
    40: "Fire Blast",
    55: "Psychic",
}
magmar[e_moves] = (move_list["Fire Punch"].copy(),
                   move_list["None"].copy()
                   )
#############
# Pinsir
pinsir = [127, "Pinsir", types[7], types[0],
          610, 53, 36, 18, 2,
          None, [], [], {}, ()]
pinsir[pokemove].extend((move_list["Vice Grip"].copy(),
                         move_list["Brick Break"].copy(),
                         ))
pinsir[pokelearnset] = {
    24: "Fury Cutter",
    31: "Bulldoze",
    38: "Seismic Toss",
    44: "X-Scissor",
    55: "Superpower",
}
pinsir[e_moves] = (move_list["Seismic Toss"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Tauros
tauros = [128, "Tauros", types[1], types[0],
          585, 55, 42, 14, 7,
          None, [], [], {}, ()]
tauros[pokemove].extend((move_list["Horn Attack"].copy(),
                         move_list["Payback"].copy(),
                         ))
tauros[pokelearnset] = {
    24: "Zen Headbutt",
    33: "Raging Bull",
    38: "Iron Head",
    47: "Outrage",
    55: "Giga Impact",
}
tauros[e_moves] = (move_list["Raging Bull"].copy(),
                   move_list["Iron Head"].copy() if rng == 1 else move_list["Zen Headbutt"].copy(),
                   )
#############
# Magikarp
magikarp = [129, "Magikarp", types[11], types[0],
            380, 1, 1, 0, 1,
            20, [], [], {}, ()]
magikarp[pokemove].extend((move_list["Splash"].copy(),
                           move_list["Flail"].copy(),
                           ))
magikarp[pokelearnset] = {

}
magikarp[e_moves] = (move_list["Splash"].copy(),
                     move_list["None"].copy(),
                     )
#############
# Gyarados
gyarados = [130, "Gyarados", types[11], types[3],
            660, 70, 46, 18, 8,
            None, [], [], {}, ()]
gyarados[pokemove].extend((move_list["Splash"].copy(),
                           move_list["Flail"].copy(),
                           ))
gyarados[pokelearnset] = {
    20: "Aqua Tail",
    22: "Twister",
    27: "Ice Fang",
    35: "Crunch",
    44: "Outrage",
    52: "Hyper Beam",
    65: "Earthquake",
}
gyarados[e_moves] = (move_list["Aqua Tail"].copy(),
                     move_list["Hyper Beam"].copy() if rng == 1 else move_list["Crunch"].copy(),
                     )
#############
# Lapras
lapras = [131, "Lapras", types[11], types[15],
          680, 52, 31, 9, 4,
          None, [], [], {}, ()]
lapras[pokemove].extend((move_list["Water Pulse"].copy(),
                         move_list["Ice Shard"].copy(),
                         ))
lapras[pokelearnset] = {
    24: "Dragon Pulse",
    29: "Surf",
    36: "Ancient Power",
    43: "Blizzard",
    50: "Psychic",
}
lapras[e_moves] = (move_list["Surf"].copy(),
                   move_list["Blizzard"].copy(),
                   )
#############
# Eevee
eevee = [133, "Eevee", types[1], types[0],
         400, 14, 14, 15, 10,
         25, [], [], {}, ()]
eevee[pokemove].extend((move_list["Tackle"].copy(),
                        move_list["Swift"].copy(),
                        ))
eevee_moves = ['Bubble Beam', 'Shock Wave', 'Flame Wheel', 'Confusion', 'Bite']
random.shuffle(eevee_moves)
eevee[pokelearnset] = {
    12: eevee_moves[0],
    19: eevee_moves[1],
    97: eevee_moves[2],
    98: eevee_moves[3],
    99: eevee_moves[4],
}
eevee[e_moves] = (move_list["Swift"].copy(),
                  move_list[eevee_moves[0]].copy(),
                  )
#############
# Vaporeon
vaporeon = [134, "Vaporeon", types[11], types[0],
            675, 44, 34, 8, 10,
            None, [], [], {}, ()]
vaporeon[pokemove].extend((move_list["Swift"].copy(),
                           move_list[eevee_moves[0]].copy(),
                           move_list[eevee_moves[1]].copy(),
                           move_list[eevee_moves[2]].copy(),
                           ))
vaporeon[pokelearnset] = {
    25: "Water Pulse",
    27: "Icy Wind",
    36: "Surf",
    40: "Ice Beam",
    60: "Hydro Pump",
}
vaporeon[e_moves] = (move_list["Surf"].copy(),
                     move_list["Ice Beam"].copy(),
                     )
#############
# Jolteon
jolteon = [135, "Jolteon", types[13], types[0],
           535, 55, 71, 20, 12,
           None, [], [], {}, ()]
jolteon[pokemove].extend((move_list["Swift"].copy(),
                          move_list[eevee_moves[0]].copy(),
                          move_list[eevee_moves[1]].copy(),
                          move_list[eevee_moves[2]].copy(),
                          ))
jolteon[pokelearnset] = {
    25: "Charge Beam",
    27: "Double Kick",
    36: "Pin Missile",
    40: "Thunderbolt",
    60: "Thunder",
}
jolteon[e_moves] = (move_list["Thunderbolt"].copy(),
                    move_list["Pin Missile"].copy(),
                    )
#############
# Flareon
flareon = [136, "Flareon", types[10], types[0],
           590, 58, 42, 10, 16,
           None, [], [], {}, ()]
flareon[pokemove].extend((move_list["Swift"].copy(),
                          move_list[eevee_moves[0]].copy(),
                          move_list[eevee_moves[1]].copy(),
                          move_list[eevee_moves[2]].copy(),
                          ))
flareon[pokelearnset] = {
    25: "Lava Plume",
    27: "Smog",
    36: "Superpower",
    40: "Flare Blitz",
    60: "Fire Blast",
}
flareon[e_moves] = (move_list["Flare Blitz"].copy(),
                    move_list["Superpower"].copy(),
                    )
#############
# Porygon
porygon = [137, "Porygon", types[1], types[0],
           400, 40, 40, 18, 4,
           None, [], [], {}, ()]
porygon[pokemove].extend((move_list["Thunder Shock"].copy(),
                          move_list["Psybeam"].copy(),
                          ))
porygon[pokelearnset] = {
    24: "Signal Beam",
    31: "Tri Attack",
    38: "Blizzard",
    46: "Hyper Beam",
    55: "Solar Beam",
}
porygon[e_moves] = (move_list["Tri Attack"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Kabuto
kabuto = [140, "Kabuto", types[6], types[11],
          420, 17, 7, 10, 2,
          32, [], [], {}, ()]
kabuto[pokemove].extend((move_list["Scratch"].copy(),
                         move_list["Absorb"].copy(),
                         ))
kabuto[pokelearnset] = {
    44: "Aqua Jet",
    50: "Ancient Power",
}
kabuto[e_moves] = (move_list["Scratch"].copy(),
                   move_list["Aqua Jet"].copy(),
                   )
#############
# Kabutops
kabutops = [141, "Kabutops", types[6], types[11],
            565, 61, 53, 24, 5,
            None, [], [], {}, ()]
kabutops[pokemove].extend((move_list["Scratch"].copy(),
                           move_list["Absorb"].copy(),
                           move_list["Aqua Jet"].copy(),
                           move_list["Ancient Power"].copy(),
                           ))
kabutops[pokelearnset] = {
    32: "Slash",
    38: "X-Scissor",
    46: "Night Slash",
    54: "Stone Edge",
    60: "Razor Shell",
}
kabutops[e_moves] = (move_list["Razor Shell"].copy(),
                     move_list["X-Scissor"].copy() if rng == 1 else move_list["Stone Edge"].copy(),
                     )
kabuto[evo_mon] = kabutops
#############
# Aerodactyl
aerodactyl = [142, "Aerodactyl", types[6], types[3],
              480, 62, 58, 18, 5,
              None, [], [], {}, ()]
aerodactyl[pokemove].extend((move_list["Wing Attack"].copy(),
                             move_list["Ancient Power"].copy(),
                             ))
aerodactyl[pokelearnset] = {
    28: "Steel Wing",
    34: "Hyper Beam",
    41: "Stone Edge",
    50: "Sky Attack"
}
aerodactyl[e_moves] = (move_list["Hyper Beam"].copy() if rng == 1 else move_list["Stone Edge"].copy(),
                       move_list["Sky Attack"].copy(),
                       )
#############
# Snorlax
snorlax = [143, "Snorlax", types[1], types[0],
           710, 54, 14, 4, 1,
           None, [], [], {}, ()]
snorlax[pokemove].extend((move_list["Body Slam"].copy(),
                          move_list["Rollout"].copy(),
                          ))
snorlax[pokelearnset] = {
    32: "Crunch",
    38: "Heavy Slam",
    46: "Belch",
    54: "Superpower",
    60: "Giga Impact",
}
snorlax[e_moves] = (move_list["Giga Impact"].copy(),
                    move_list["Heavy Slam"].copy() if rng == 1 else move_list["Belch"].copy(),
                    )
#############
# Articuno
articuno = [144, "Articuno", types[15], types[3],
            720, 65, 48, 21, 11,
            None, [], [], {}, ()]
articuno[pokemove].extend((move_list["Ice Beam"].copy(),
                           move_list["Ancient Power"].copy(),
                           ))
articuno[pokelearnset] = {
    44: "Extrasensory",
    50: "Blizzard",
    58: "Hurricane",
    66: "Ominous Wind",
    70: "Sheer Cold",
}
articuno[e_moves] = (move_list["Ice Beam"].copy(),
                     move_list["Ancient Power"].copy(),
                     )
#############
# Zapdos
zapdos = [145, "Zapdos", types[13], types[3],
          610, 72, 52, 26, 8,
          None, [], [], {}, ()]
zapdos[pokemove].extend((move_list["Thunderbolt"].copy(),
                         move_list["Ancient Power"].copy(),
                         ))
zapdos[pokelearnset] = {
    44: "Drill Peck",
    50: "Thunder",
    58: "Heat Wave",
    66: "Hyper Beam",
    70: "Zap Cannon",
}
zapdos[e_moves] = (move_list["Thunderbolt"].copy(),
                   move_list["Drill Peck"].copy()
                   )
#############
# Moltres
moltres = [146, "Moltres", types[10], types[3],
           655, 69, 58, 15, 11,
           None, [], [], {}, ()]
moltres[pokemove].extend((move_list["Flamethrower"].copy(),
                          move_list["Ancient Power"].copy(),
                          ))
moltres[pokelearnset] = {
    44: "Air Slash",
    50: "Fire Blast",
    58: "Solar Beam",
    66: "Sky Attack",
    70: "Overheat",
}
moltres[e_moves] = (move_list["Flamethrower"].copy(),
                    move_list["Sky Attack"].copy()
                    )
#############
# Dratini
dratini = [147, "Dratini", types[16], types[0],
           370, 12, 14, 3, 6,
           28, [], [], {}, ()]
dratini[pokemove].extend((move_list["Wrap"].copy(),
                          move_list["Dragon Rage"].copy(),
                          ))
dratini[pokelearnset] = {
    22: "Thunder Shock",
}
dratini[e_moves] = (move_list["Wrap"].copy(),
                    move_list["Dragon Rage"].copy(),
                    )
#############
# Dragonair
dragonair = [148, "Dragonair", types[16], types[0],
             510, 34, 41, 12, 6,
             36, [], [], {}, ()]
dragonair[pokemove].extend((move_list["Wrap"].copy(),
                            move_list["Dragon Rage"].copy(),
                            move_list["Thunder Shock"].copy(),
                            ))
dragonair[pokelearnset] = {
    30: "Aqua Tail",
    35: "Dragon Breath",
}
dragonair[e_moves] = (move_list["Dragon Breath"].copy(),
                      move_list["Aqua Tail"].copy(),
                      )
dratini[evo_mon] = dragonair
#############
# Dragonite
dragonite = [149, "Dragonite", types[16], types[3],
             700, 64, 68, 18, 10,
             None, [], [], {}, ()]
dragonite[pokemove].extend((move_list["Dragon Rage"].copy(),
                            move_list["Thunder Shock"].copy(),
                            move_list["Dragon Breath"].copy(),
                            move_list["Aqua Tail"].copy(),
                            ))
dragonite[pokelearnset] = {
    44: "Hurricane",
    51: "Extreme Speed",
    56: "Dragon Rush",
    62: "Thunder Punch",
    69: "Hyper Beam",
}
dragonite[e_moves] = (move_list["Dragon Rush"].copy(),
                      move_list["Hyper Beam"].copy() if rng == 1 else move_list["Extreme Speed"].copy(),
                      )
dragonair[evo_mon] = dragonite
#############
# Mewtwo
mewtwo = [150, "Mewtwo", types[14], types[0],
          600, 80, 74, 24, 11,
          None, [], [], {}, ()]
mewtwo[pokemove].extend((move_list["Psystrike"].copy(),
                         move_list["Aura Sphere"].copy(),
                         ))
mewtwo[pokelearnset] = {

}
mewtwo[e_moves] = (move_list["Psystrike"].copy(),
                   move_list["Aura Sphere"].copy(),
                   )
#############
# Chikorita
chikorita = [152, "Chikorita", types[12], types[0],
             420, 13, 16, 5, 3,
             16, [], [], {}, ()]
chikorita[pokemove].extend((move_list["Tackle"].copy(),
                            move_list["Razor Leaf"].copy(),
                            ))
chikorita[pokelearnset] = {
    9: "Poison Powder",
    13: "Nature Power",
}
chikorita[e_moves] = (move_list["Tackle"].copy(),
                      move_list["Razor Leaf"].copy(),
                      )
#############
# Bayleef
bayleef = [153, "Bayleef", types[12], types[0],
           590, 38, 33, 12, 5,
           36, [], [], {}, ()]
bayleef[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Razor Leaf"].copy(),
                          move_list["Poison Powder"].copy(),
                          move_list["Nature Power"].copy(),
                          ))
bayleef[pokelearnset] = {
    20: "Magical Leaf",
    24: "Iron Tail",
}
bayleef[e_moves] = (move_list["Magical Leaf"].copy(),
                    move_list["None"].copy(),
                    )
chikorita[evo_mon] = bayleef
#############
# Meganium
meganium = [154, "Meganium", types[12], types[0],
            670, 49, 42, 13, 6,
            None, [], [], {}, ()]
meganium[pokemove].extend((move_list["Poison Powder"].copy(),
                           move_list["Nature Power"].copy(),
                           move_list["Magical Leaf"].copy(),
                           move_list["Iron Tail"].copy(),
                           ))
meganium[pokelearnset] = {
    37: "Body Slam",
    41: "Ancient Power",
    45: "Petal Dance",
    54: "Earthquake",
    65: "Frenzy Plant",
}
meganium[e_moves] = (move_list["Petal Dance"].copy(),
                     move_list["Ancient Power"].copy(),
                     )
bayleef[evo_mon] = meganium
#############
# Cyndaquil
cyndaquil = [155, "Cyndaquil", types[10], types[0],
             340, 12, 18, 9, 2,
             16, [], [], {}, ()]
cyndaquil[pokemove].extend((move_list["Tackle"].copy(),
                            move_list["Flame Wheel"].copy(),
                            ))
cyndaquil[pokelearnset] = {
    37: "Quick Attack",
    41: "Rollout",

}
cyndaquil[e_moves] = (move_list["Tackle"].copy(),
                      move_list["Flame Wheel"].copy(),
                      )
#############
# Quilava
quilava = [156, "Quilava", types[10], types[0],
           455, 32, 41, 11, 8,
           36, [], [], {}, ()]
quilava[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Flame Wheel"].copy(),
                          move_list["Quick Attack"].copy(),
                          move_list["Rollout"].copy(),
                          ))
quilava[pokelearnset] = {
    9: "Flame Charge",
    13: "Dig",
}
quilava[e_moves] = (move_list["Flame Charge"].copy(),
                    move_list["None"].copy(),
                    )
cyndaquil[evo_mon] = quilava
#############
# Typhlosion
typhlosion = [157, "Typhlosion", types[10], types[0],
              560, 59, 61, 16, 11,
              None, [], [], {}, ()]
typhlosion[pokemove].extend((move_list["Quick Attack"].copy(),
                             move_list["Rollout"].copy(),
                             move_list["Flame Charge"].copy(),
                             move_list["Dig"].copy(),
                             ))
typhlosion[pokelearnset] = {
    38: "Lava Plume",
    44: "Gyro Ball",
    53: "Thunder Punch",
    59: "Eruption",
    65: "Blast Burn",
}
typhlosion[e_moves] = (move_list["Eruption"].copy(),
                       move_list["Gyro Ball"].copy() if rng == 1 else move_list["Thunder Punch"].copy(),
                       )
quilava[evo_mon] = typhlosion
#############
# Totodile
totodile = [158, "Totodile", types[11], types[0],
            385, 18, 14, 11, 1,
            16, [], [], {}, ()]
totodile[pokemove].extend((move_list["Scratch"].copy(),
                           move_list["Water Gun"].copy(),
                           ))
totodile[pokelearnset] = {
    11: "Bite",
}
totodile[e_moves] = (move_list["Bite"].copy(),
                     move_list["Water Gun"].copy(),
                     )
#############
# Croconaw
croconaw = [159, "Croconaw", types[11], types[0],
            470, 36, 31, 16, 3,
            36, [], [], {}, ()]
croconaw[pokemove].extend((move_list["Scratch"].copy(),
                           move_list["Water Gun"].copy(),
                           move_list["Bite"].copy(),
                           ))
croconaw[pokelearnset] = {
    21: "Ice Fang",
    29: "Crunch",
}
croconaw[e_moves] = (move_list["Crunch"].copy(),
                     move_list["None"].copy(),
                     )
totodile[evo_mon] = croconaw
#############
# Feraligatr
feraligatr = [160, "Feraligatr", types[11], types[0],
              590, 58, 47, 22, 7,
              None, [], [], {}, ()]
feraligatr[pokemove].extend((move_list["Water Gun"].copy(),
                             move_list["Bite"].copy(),
                             move_list["Ice Fang"].copy(),
                             move_list["Crunch"].copy(),
                             ))
feraligatr[pokelearnset] = {
    37: "Waterfall",
    44: "Dragon Claw",
    52: "Shadow Claw",
    59: "Superpower",
    65: "Hydro Cannon",
}
feraligatr[e_moves] = (move_list["Waterfall"].copy(),
                       move_list["Dragon Claw"].copy() if rng == 1 else move_list["Shadow Claw"].copy(),
                       )
croconaw[evo_mon] = feraligatr
#############
# Furret
furret = [162, "Furret", types[1], types[0],
          400, 10, 30, 3, 1,
          None, [], [], {}, ()]
furret[pokemove].extend((move_list["Quick Attack"].copy(),
                         move_list["Fury Swipes"].copy(),
                         ))
furret[pokelearnset] = {
}
furret[e_moves] = (move_list["Quick Attack"].copy(),
                   move_list["Fury Swipes"].copy(),
                   )
#############
# Noctowl
noctowl = [164, "Noctowl", types[1], types[3],
           580, 30, 35, 13, 5,
           None, [], [], {}, ()]
noctowl[pokemove].extend((move_list["Peck"].copy(),
                          move_list["Confusion"].copy(),
                          ))
noctowl[pokelearnset] = {
    21: "Air Slash",
    27: "Extrasensory",
    34: "Night Shade",
    42: "Moonblast",
}
noctowl[e_moves] = (move_list["Extrasensory"].copy(),
                    move_list["Air Slash"].copy(),
                    )
#############
# Ledyba
ledyba = [165, "Ledyba", types[11], types[3],
          420, 8, 17, 13, 5,
          28, [], [], {}, ()]
ledyba[pokemove].extend((move_list["Tackle"].copy(), move_list["Struggle Bug"].copy(),))
ledyba[pokelearnset] = {
    14: "Mach Punch",
    19: "Bug Buzz",
    25: "Air Slash"
}
ledyba[e_moves] = (move_list["Mach Punch"].copy(),
                   move_list["Struggle Bug"].copy(),)
#############
# Mareep
mareep = [179, "Mareep", types[13], types[0],
          370, 15, 10, 3, 2,
          22, [], [], {}, ()]
mareep[pokemove].extend((move_list["Tackle"].copy(),
                         move_list["Thunder Shock"].copy(),
                         ))
mareep[pokelearnset] = {
    14: "Headbutt",
    19: "Signal Beam",
}
mareep[e_moves] = (move_list["Thunder Shock"].copy(),
                   move_list["None"].copy(),
                   )
#############
# Flaaffy
flaaffy = [180, "Flaaffy", types[13], types[0],
           460, 35, 28, 8, 3,
           32, [], [], {}, ()]
flaaffy[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Thunder Shock"].copy(),
                          move_list["Headbutt"].copy(),
                          move_list["Signal Beam"].copy(),
                          ))
flaaffy[pokelearnset] = {
    14: "Discharge",
    19: "Fire Punch",
}
flaaffy[e_moves] = (move_list["Discharge"].copy(),
                    move_list["Headbutt"].copy(),
                    )
mareep[evo_mon] = flaaffy
#############
# Ampharos
ampharos = [181, "Ampharos", types[13], types[0],
            600, 59, 41, 14, 4,
            None, [], [], {}, ()]
ampharos[pokemove].extend((move_list["Thunder Shock"].copy(),
                           move_list["Headbutt"].copy(),
                           move_list["Signal Beam"].copy(),
                           move_list["Discharge"].copy(),
                           move_list["Fire Punch"].copy(),
                          ))
ampharos[pokelearnset] = {
    35: "Power Gem",
    42: "Dragon Pulse",
    48: "Dazzling Gleam",
    55: "Thunder",
}
ampharos[e_moves] = (move_list["Thunder"].copy(),
                     move_list["Power Gem"].copy() if rng == 1 else move_list["Dragon Pulse"].copy(),
                     )
flaaffy[evo_mon] = ampharos
#############
# Bellossom
bellossom = [182, "Bellossom", types[12], types[0],
             590, 46, 32, 8, 6,
             None, [], [], {}, ()]
bellossom[pokemove].extend((move_list["Tackle"].copy(), move_list["Acid"].copy(),))
bellossom[pokelearnset] = {

}
bellossom[e_moves] = (move_list["Petal Dance"].copy(),
                      move_list["Poison Powder"].copy(),)
#############
# Marill
marill = [183, "Marill", types[11], types[18],
          435, 17, 10, 2, 3,
          27, [], [], {}, ()]
marill[pokemove].extend((move_list["Tackle"].copy(), move_list["Water Gun"].copy(),))
marill[pokelearnset] = {
    14: "Rollout",
    16: "Draining Kiss",
    24: "Aqua Tail",
}
marill[e_moves] = (move_list["Rollout"].copy() if rng == 1 else move_list["Water Gun"].copy(),
                   move_list["None"].copy(),)
#############
# Azumarill
azumarill = [184, "Azumarill", types[11], types[18],
             645, 52, 36, 9, 5,
             None, [], [], {}, ()]
azumarill[pokemove].extend((move_list["Water Gun"].copy(),
                            move_list["Rollout"].copy(),
                            move_list["Draining Kiss"].copy(),
                            move_list["Aqua Tail"].copy(),
                            ))
azumarill[pokelearnset] = {
    29: "Bounce",
    36: "Play Rough",
    44: "Body Slam",
    52: "Ice Punch",
    60: "Superpower",
}
azumarill[e_moves] = (move_list["Aqua Tail"].copy(),
                      move_list["Play Rough"].copy(),
                      )
marill[evo_mon] = azumarill
#############
# Sudowoodo
sudowoodo = [185, "Sudowoodo", types[6], types[0],
             560, 39, 17, 3, 1,
             None, [], [], {}, ()]
sudowoodo[pokemove].extend((move_list["Slam"].copy(),
                            move_list["Rock Throw"].copy(),
                            ))
sudowoodo[pokelearnset] = {
    24: "Sucker Punch",
    31: "Hammer Arm",
    36: "Rock Tomb",
    42: "Wood Hammer",
    52: "Head Smash",
}
sudowoodo[e_moves] = (move_list["Rock Tomb"].copy(),
                      move_list["None"].copy()
                      )
#############
# Quagsire
quagsire = [195, "Quagsire", types[11], types[5],
            650, 42, 30, 6, 3,
            None, [], [], {}, ()]
quagsire[pokemove].extend((move_list["Water Pulse"].copy(),
                           move_list["Mud Bomb"].copy(),
                           ))
quagsire[pokelearnset] = {
    17: "Slam",
    23: "Iron Tail",
    28: "Muddy Water",
    37: "Sludge Bomb",
    50: "Earth Power",
}
quagsire[e_moves] = (move_list["Muddy Water"].copy(),
                     move_list["Mud Bomb"].copy(),
                     )
#############
# Espeon
espeon = [196, "Espeon", types[14], types[0],
          510, 66, 58, 16, 12,
          None, [], [], {}, ()]
espeon[pokemove].extend((move_list["Swift"].copy(),
                         move_list[eevee_moves[0]].copy(),
                         move_list[eevee_moves[1]].copy(),
                         move_list[eevee_moves[2]].copy(),
                         ))
espeon[pokelearnset] = {
    25: "Psybeam",
    27: "Shadow Ball",
    36: "Signal Beam",
    40: "Psychic",
    60: "Dazzling Gleam",
}
espeon[e_moves] = (move_list["Psychic"].copy(),
                   move_list["Dazzling Gleam"].copy(),
                   )
#############
# Umbreon
umbreon = [197, "Umbreon", types[17], types[0],
           705, 48, 43, 11, 11,
           None, [], [], {}, ()]
umbreon[pokemove].extend((move_list["Swift"].copy(),
                          move_list[eevee_moves[0]].copy(),
                          move_list[eevee_moves[1]].copy(),
                          move_list[eevee_moves[2]].copy(),
                         ))
umbreon[pokelearnset] = {
    25: "Snarl",
    27: "Iron Tail",
    36: "Trailblaze",
    40: "Dark Pulse",
    60: "Zap Cannon",
}
umbreon[e_moves] = (move_list["Dark Pulse"].copy(),
                    move_list["Iron Tail"].copy(),
                    )
#############
# Dunsparce
dunsparce = [206, "Dunsparce", types[1], types[0],
             560, 37, 28, 6, 1,
             None, [], [], {}, ()]
dunsparce[pokemove].extend((move_list["Rage"].copy(),
                            move_list["Rollout"].copy(),
                            ))
dunsparce[pokelearnset] = {
    19: "Pounce",
    24: "Drill Run",
    32: "Hyper Drill",
    39: "Ancient Power",
    50: "Dragon Rush",
}
dunsparce[e_moves] = (move_list["Rollout"].copy(),
                      move_list["Hyper Drill"].copy(),
                      )
#############
# Steelix
steelix = [208, "Steelix", types[9], types[5],
           765, 52, 24, 8, 2,
           None, [], [], {}, ()]
steelix[pokemove].extend((move_list["Bulldoze"].copy(),
                          move_list["Dragon Breath"].copy(),
                          move_list["Rock Slide"].copy(),
                          move_list["Brutal Swing"].copy(),
                          ))
steelix[pokelearnset] = {
    32: "Iron Tail",
    36: "Drill Run",
    40: "Thunder Fang",
    46: "Head Smash",
    55: "Heavy Slam",
}
steelix[e_moves] = (move_list["Heavy Slam"].copy(),
                    move_list["Head Smash"].copy(),
                    )
onix[evo_mon] = steelix
#############
# Scizor
scizor = [212, "Scizor", types[7], types[9],
          615, 61, 27, 18, 4,
          None, [], [], {}, ()]
scizor[pokemove].extend((move_list["Quick Attack"].copy(),
                         move_list["Fury Cutter"].copy(),
                         ))
scizor[pokelearnset] = {
    23: "Metal Claw",
    27: "Slash",
    33: "Bullet Punch",
    40: "X-Scissor",
    55: "Iron Head",
}
scizor[e_moves] = (move_list["Bullet Punch"].copy(),
                   move_list["X-Scissor"].copy(),
                   )
#############
# Heracross
heracross = [214, "Heracross", types[7], types[2],
             575, 56, 39, 12, 5,
             None, [], [], {}, ()]
heracross[pokemove].extend((move_list["Horn Attack"].copy(),
                            move_list["Brick Break"].copy(),
                            ))
heracross[pokelearnset] = {
    17: "Aerial Ace",
    25: "Megahorn",
    32: "Throat Chop",
    45: "Close Combat",
}
heracross[e_moves] = (move_list["Megahorn"].copy(),
                      move_list["Brick Break"].copy(),
                      )
#############
# Sneasel
sneasel = [215, "Sneasel", types[17], types[15],
           480, 32, 41, 12, 5,
           28, [], [], {}, ()]
sneasel[pokemove].extend((move_list["Scratch"].copy(),
                          move_list["Feint Attack"].copy(),
                          ))
sneasel[pokelearnset] = {
    10: "Icy Wind",
    18: "Metal Claw",
    25: "Ice Shard",
}
sneasel[e_moves] = (move_list["Feint Attack"].copy() if rng == 1 else move_list["Ice Shard"].copy(),
                    move_list["None"].copy(),
                    )
#############
# Teddiursa
teddiursa = [216, "Teddiursa", types[1], types[0],
             410, 16, 11, 12, 2,
             26, [], [], {}, ()]
teddiursa[pokemove].extend((move_list["Fury Swipes"].copy(),
                            move_list["Feint Attack"].copy(),
                            ))
teddiursa[pokelearnset] = {
    10: "Metal Claw",
    16: "Thrash",
    20: "Play Rough",
}
teddiursa[e_moves] = (move_list["Fury Swipes"].copy(),
                      move_list["Feint Attack"].copy() if rng == 1 else move_list["Metal Claw"].copy(),
                      )
#############
# Ursaring
ursaring = [217, "Ursaring", types[1], types[0],
            640, 58, 41, 16, 6,
            None, [], [], {}, ()]
ursaring[pokemove].extend(( move_list["Feint Attack"].copy(),
                           move_list["Metal Claw"].copy(),
                           move_list["Thrash"].copy(),
                           move_list["Play Rough"].copy(),
                           ))
ursaring[pokelearnset] = {
    29: "Hammer Arm",
    36: "Crunch",
    42: "High Horsepower",
    48: "Fire Punch",
    55: "Rock Slide",
}
ursaring[e_moves] = (move_list["Hammer Arm"].copy(),
                     move_list["Play Rough"].copy() if rng == 1 else move_list["Thrash"].copy(),
                     )
teddiursa[evo_mon] = ursaring
#############
# Octillery
octillery = [224, "Octillery", types[11], types[0],
             580, 51, 34, 20, 3,
             None, [], [], {}, ()]
octillery[pokemove].extend((move_list["Bubble Beam"].copy(),
                            move_list["Aurora Beam"].copy(),
                            ))
octillery[pokelearnset] = {
    22: "Energy Ball",
    28: "Gunk Shot",
    32: "Octazooka",
    41: "Flamethrower",
    55: "Ice Beam",
}
octillery[e_moves] = (move_list["Octazooka"].copy(),
                      move_list["Flamethrower"].copy() if rng == 1 else move_list["Gunk Shot"].copy(),
                      )
#############
# Skarmory
skarmory = [227, "Skarmory", types[9], types[3],
            670, 44, 39, 19, 4,
            None, [], [], {}, ()]
skarmory[pokemove].extend((move_list["Peck"].copy(),
                           move_list["Fury Attack"].copy(),
                           ))
skarmory[pokelearnset] = {
    22: "Steel Wing",
    27: "Slash",
    36: "Drill Peck",
    43: "Rock Slide",
    50: "Night Slash",
}
skarmory[e_moves] = (move_list["Steel Wing"].copy(),
                     move_list["Drill Peck"].copy(),
                     )
#############
# Houndour
houndour = [228, "Houndour", types[17], types[10],
            345, 18, 15, 8, 2,
            26, [], [], {}, ()]
houndour[pokemove].extend((move_list["Bite"].copy(),
                           move_list["Ember"].copy(),
                           ))
houndour[pokelearnset] = {
    10: "Smog",
    16: "Thunder Fang",
    20: "Fire Fang",
}
houndour[e_moves] = (move_list["Bite"].copy(),
                     move_list["Ember"].copy(),
                     )
#############
# Houndoom
houndoom = [229, "Houndoom", types[17], types[10],
            535, 54, 60, 17, 6,
            None, [], [], {}, ()]
houndoom[pokemove].extend((move_list["Bite"].copy(),
                           move_list["Ember"].copy(),
                           move_list["Smog"].copy(),
                           move_list["Thunder Fang"].copy(),
                           move_list["Fire Fang"].copy(),
                           ))
houndoom[pokelearnset] = {
    29: "Dark Pulse",
    36: "Psychic Fangs",
    42: "Trailblaze",
    50: "Inferno",
}
houndoom[e_moves] = (move_list["Fire Fang"].copy(),
                     move_list["Dark Pulse"].copy(),
                     )
houndour[evo_mon] = houndoom
#############
# Kingdra
kingdra = [230, "Kingdra", types[11], types[16],
           550, 50, 42, 20, 4,
           None, [], [], {}, ()]
kingdra[pokemove].extend((move_list["Dragon Breath"].copy(),
                          move_list["Bubble Beam"].copy(),
                          move_list["Aurora Beam"].copy(),
                          ))
kingdra[pokelearnset] = {
    29: "Flash Cannon",
    36: "Hydro Pump",
    42: "Ice Beam",
    49: "Dragon Pulse",
    55: "Hyper Beam",
}
kingdra[e_moves] = (move_list["Dragon Pulse"].copy(),
                    move_list["Hydro Pump"].copy(),
                    )
#############
# Phanpy
phanpy = [231, "Phanpy", types[5], types[0],
          425, 13, 18, 4, 2,
          28, [], [], {}, ()]
phanpy[pokemove].extend((move_list["Rapid Spin"].copy(),
                         move_list["Rollout"].copy(),
                         ))
phanpy[pokelearnset] = {
    14: "Bulldoze",
    22: "Rock Smash",
    26: "Ice Shard",
}
phanpy[e_moves] = (move_list["Rollout"].copy(),
                   move_list["Bulldoze"].copy(),
                   )
#############
# Donphan
donphan = [232, "Donphan", types[5], types[0],
           610, 46, 37, 13, 4,
           None, [], [], {}, ()]
donphan[pokemove].extend((move_list["Rapid Spin"].copy(),
                          move_list["Rollout"].copy(),
                          move_list["Bulldoze"].copy(),
                          move_list["Rock Smash"].copy(),
                          move_list["Ice Shard"].copy(),
                         ))
donphan[pokelearnset] = {
    32: "Fire Fang",
    38: "Heavy Slam",
    46: "Thunder Fang",
    53: "Earthquake",
}
donphan[e_moves] = (move_list["Earthquake"].copy(),
                    move_list["Ice Shard"].copy() if rng == 1 else move_list["Heavy Slam"].copy(),
                    )
phanpy[evo_mon] = donphan
#############
# Miltank
miltank = [241, "Miltank", types[1], types[0],
           640, 46, 36, 6, 1,
           None, [], [], {}, ()]
miltank[pokemove].extend((move_list["Stomp"].copy(),
                          move_list["Rollout"].copy(),
                          ))
miltank[pokelearnset] = {
    26: "Zen Headbutt",
    31: "Gyro Ball",
    37: "Ice Punch",
    43: "Hammer Arm",
    55: "Giga Impact",
}
miltank[e_moves] = (move_list["Stomp"].copy(),
                    move_list["Rollout"].copy(),
                    )
#############
# Raikou
raikou = [243, "Raikou", types[13], types[0],
          600, 66, 70, 24, 9,
          None, [], [], {}, ()]
raikou[pokemove].extend((move_list["Thunder Fang"].copy(),
                         move_list["Quick Attack"].copy(),
                         ))
raikou[pokelearnset] = {
    26: "Crunch",
    31: "Extrasensory",
    37: "Iron Head",
    43: "Thunder",
    55: "Zap Cannon",
}
raikou[e_moves] = (move_list["Thunder Fang"].copy(),
                   move_list["Thunder"].copy() if rng == 1 else move_list["Iron Head"].copy(),
                   )
#############
# Entei
entei = [244, "Entei", types[10], types[0],
         660, 60, 58, 14, 18,
         None, [], [], {}, ()]
entei[pokemove].extend((move_list["Fire Fang"].copy(),
                        move_list["Stomp"].copy(),
                        ))
entei[pokelearnset] = {
    26: "Crunch",
    31: "Extreme Speed",
    37: "Iron Head",
    43: "Flare Blitz",
    55: "Sacred Fire",
}
entei[e_moves] = (move_list["Fire Fang"].copy(),
                  move_list["Extreme Speed"].copy() if rng == 1 else move_list["Flare Blitz"].copy(),
                  )
#############
# Suicune
suicune = [245, "Suicune", types[11], types[0],
           780, 55, 51, 10, 14,
           None, [], [], {}, ()]
suicune[pokemove].extend((move_list["Ice Fang"].copy(),
                          move_list["Water Pulse"].copy(),
                          ))
suicune[pokelearnset] = {
    26: "Extrasensory",
    31: "Surf",
    37: "Air Slash",
    43: "Hydro Pump",
    55: "Blizzard",
}
suicune[e_moves] = (move_list["Fire Fang"].copy(),
                    move_list["Extreme Speed"].copy() if rng == 1 else move_list["Flare Blitz"].copy(),
                    )
#############
# Larvitar
larvitar = [246, "Larvitar", types[6], types[5],
            455, 20, 9, 11, 2,
            31, [], [], {}, ()]
larvitar[pokemove].extend((move_list["Tackle"].copy(),
                           move_list["Rock Throw"].copy(),
                           ))
larvitar[pokelearnset] = {
    17: "Payback",
    24: "Bulldoze",
    28: "Brick Break"
}
larvitar[e_moves] = (move_list["Rock Throw"].copy(),
                     move_list["Payback"].copy(),
                     )
#############
# Pupitar
pupitar = [247, "Pupitar", types[6], types[5],
           540, 31, 16, 15, 3,
           36, [], [], {}, ()]
pupitar[pokemove].extend((move_list["Tackle"].copy(),
                          move_list["Rock Throw"].copy(),
                          move_list["Payback"].copy(),
                          move_list["Bulldoze"].copy(),
                          move_list["Brick Break"].copy(),
                          ))
pupitar[pokelearnset] = {
    17: "Ancient Power",
    24: "Iron Head",
}
pupitar[e_moves] = (move_list["Rock Throw"].copy(),
                    move_list["Bulldoze"].copy(),
                    )
larvitar[evo_mon] = pupitar
#############
# Tyranitar
tyranitar = [248, "Tyranitar", types[6], types[17],
             630, 74, 37, 20, 4,
             None, [], [], {}, ()]
tyranitar[pokemove].extend((move_list["Bulldoze"].copy(),
                            move_list["Brick Break"].copy(),
                            move_list["Ancient Power"].copy(),
                            move_list["Iron Head"].copy(),
                            ))
tyranitar[pokelearnset] = {
    42: "Crunch",
    47: "Stone Edge",
    53: "Earthquake",
    59: "Fire Blast",
    65: "Giga Impact",
}
tyranitar[e_moves] = (move_list["Stone Edge"].copy(),
                      move_list["Earthquake"].copy() if rng == 1 else move_list["Crunch"].copy(),
                      )
pupitar[evo_mon] = tyranitar

pokedex_list = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, kakuna, beedrill, pidgey, pidgeotto, pidgeot, ratatta, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoran_f, nidorina, nidoqueen, nidoran_m, nidorino, nidoking, clefairy, clefable, zubat, oddish, meowth, persian, psyduck, golduck, mankey, growlithe, arcanine, abra, kadabra, alakazam, machop, machoke, machamp, tentacool, tentacruel, geodude, graveler, golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, seel, dewgong, gastly, haunter, gengar, onix, hypno, krabby, kingler, exeggutor, cubone, marowak, hitmonlee, hitmonchan, koffing, rhyhorn, rhydon, chansey, staryu, starmie, scyther, electabuzz, magmar, pinsir, tauros, magikarp, gyarados, lapras, eevee, vaporeon, jolteon, flareon, porygon, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, chikorita, bayleef, meganium, cyndaquil, quilava, typhlosion, totodile, croconaw, feraligatr, furret, noctowl, ledyba, mareep, flaaffy, ampharos, bellossom, marill, azumarill, sudowoodo, quagsire, espeon, umbreon, dunsparce, steelix, scizor, heracross, sneasel, teddiursa, ursaring, octillery, skarmory, houndour, houndoom, kingdra, phanpy, donphan, miltank, raikou, entei, suicune, larvitar, pupitar, tyranitar]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# set eevolution
eevee_evo_rng = random.randint(0, 2)
if eevee_evo_rng == 0:
    eevee[evo_mon] = vaporeon
elif eevee_evo_rng == 1:
    eevee[evo_mon] = jolteon
elif eevee_evo_rng == 2:
    eevee[evo_mon] = flareon
