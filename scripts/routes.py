from pokemon_list import *
import party as pty
import random
from settings import *
from numpy import add, subtract


def generate_route(route_args):
    route = {}
    if route_args['name'] != "Cerulean Cave":

        # get encounter locations
        encounters = [x for x in range(route_args['battle_number'])]
        encounters = [random.randint(15, 75) for x in encounters]
        encounters.sort()

        # get level scalling
        level_scaling = (0, 1)
        if pty.stages_cleared == 0 or pty.stages_cleared == 3 or pty.stages_cleared == 6:
            level_scaling = (0, 1)
        elif pty.stages_cleared == 1 or pty.stages_cleared == 4 or pty.stages_cleared == 7:
            level_scaling = (2, 3)
        elif pty.stages_cleared == 2 or pty.stages_cleared == 5 or pty.stages_cleared == 8:
            level_scaling = (4, 5)

        for i in range(route_args['battle_number']):
            # get random pokemon
            random_pokemon = random.choice(route_args['poke_pool'])

            route[encounters[i]] = (random_pokemon[0], random.randint(random_pokemon[1][level_scaling[0]], random_pokemon[1][level_scaling[1]]))

        # get route boss
        random_boss = random.choice(route_args['boss_pool'])
        route[boss_route_encounter] = (random_boss[0], random.randint(random_boss[1][level_scaling[0]], random_boss[1][level_scaling[1]]))

    else:
        encounters = [30, 60]
        # level_scaling = (4, 5)

        route[encounters[0]] = (random_bird[0], 40)
        route[encounters[1]] = (random_dog[0], 40)
        route[boss_route_encounter] = ('mewtwo', 50)

    return route


# level ranges
lv1_range = (4, 5,
             6, 8,
             11, 15,)

lv2_range = (17, 20,
             22, 26,
             28, 32,)

lv3_range = (33, 36,
             37, 39,
             40, 44,)

boss_range = (45, 46)

# start route
r1_args = {
    'name': 'test',

    'poke_pool': [('ratatta',    (3, 3)),
                  ('pidgey',     (2, 2)), ],

    'boss_pool': [('meowth',     (5, 5)),
                  ('jigglypuff', (5, 5)),
                  ('spearow',    (5, 5)), ],

    'battle_number': random.randint(0, 0)
}

# level 1 routes
field_1_args = {
    'name': "Field",

    'bg': 'field_day',
    'stage': 'field',

    'poke_pool': [('ratatta',    lv1_range),
                  ('pidgey',     lv1_range),
                  ('nidoran_m',  lv1_range),
                  ('meowth',     lv1_range),
                  ('jigglypuff', lv1_range),
                  ('psyduck',    lv1_range),
                  ('spearow',    lv1_range),
                  ('vulpix',     lv1_range),
                  ('oddish',     lv1_range), ],

    'boss_pool': [('pidgeotto',  (4, 4,
                                  8, 8,
                                  11, 11,)),

                  ('ponyta',     (5, 5,
                                  8, 8,
                                  11, 11,)),

                  ('mankey',     (5, 5,
                                  8, 8,
                                  11, 11,)), ],

    'battle_number': random.randint(3, 3)
}

forest_1_args = {
    'name': "Forest",

    'bg': 'forest_day',
    'stage': 'forest',

    'poke_pool': [('caterpie',  add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('metapod',   add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('kakuna',    add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('pidgey',    lv1_range),
                  ('sandshrew', lv1_range),
                  ('ekans',     subtract(lv1_range, (0, 1, 0, 0, 0, 0))),
                  ('nidoran_f', lv1_range),
                  ('marill',    lv1_range),
                  ('oddish',    add(lv1_range, (1, 2, 3, 4, 5, 6))), ],

    'boss_pool': [('butterfree', (2, 2,
                                  7, 7,
                                  10, 10,)),

                  ('beedrill',   (2, 2,
                                  7, 7,
                                  10, 10,)),

                  ('pikachu',    (3, 3,
                                  9, 9,
                                  14, 14,)), ],

    'battle_number': random.randint(3, 3)
}

cave_1_args = {
    'name': "Cave",

    'bg': 'cave_day',
    'stage': 'cave',

    'poke_pool': [('geodude',   lv1_range),
                  ('zubat',     add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('abra',      lv1_range),
                  ('sandshrew', lv1_range),
                  ('machop',    lv1_range),
                  ('slowpoke',  lv1_range),
                  ('seel',      add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('phanpy',    lv1_range),
                  ('koffing',   add(lv1_range, (1, 2, 3, 4, 5, 6))), ],

    'boss_pool': [('clefairy', (3, 3,
                                7, 7,
                                10, 10,)),

                  ('onix',     (2, 2,
                                5, 5,
                                8, 8,)),

                  ('cubone',   (3, 3,
                                7, 7,
                                10, 10,)),

                  ('larvitar', (3, 3,
                                7, 7,
                                10, 10,)), ],

    'battle_number': random.randint(3, 3)
}

beach_1_args = {
    'name': "Beach",

    'bg': 'beach_day',
    'stage': 'beach',

    'poke_pool': [('magikarp',  add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('psyduck',   lv1_range),
                  ('krabby',    lv1_range),
                  ('tentacool', add(lv1_range, (1, 2, 3, 4, 5, 6))),
                  ('growlithe', lv1_range),
                  ('mareep',    lv1_range), ],

    'boss_pool': [('squirtle',  (3, 3,
                                 7, 7,
                                 10, 10,)),

                  ('dratini',   (3, 3,
                                 7, 7,
                                 10, 10,)),

                  ('staryu',    (3, 3,
                                 7, 7,
                                 10, 10,)), ],

    'battle_number': random.randint(3, 3)
}

# level 2 routes
field_2_args = {
    'name': "Field",

    'bg': 'field_afternoon',
    'stage': 'field',

    'poke_pool': [('nidorino', lv2_range),
                  ('persian',  lv2_range),
                  ('croconaw', lv2_range),
                  ('chansey',  lv2_range),
                  ('hitmonchan', lv2_range),
                  ('mankey',   lv2_range),
                  ('kadabra',  lv2_range),
                  ('ponyta',   lv2_range),
                  ('noctowl',  lv2_range),
                  ('houndour', lv2_range),
                  ('cubone',   lv2_range), ],

    'boss_pool': [('fearow',     (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('tauros',     (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('miltank',    (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('electabuzz', (22, 22,
                                  24, 24,
                                  26, 26,)),
                  ],

    'battle_number': random.randint(3, 4)
}

forest_2_args = {
    'name': "Forest",

    'bg': 'forest_afternoon',
    'stage': 'forest',

    'poke_pool': [('nidorina',   lv2_range),
                  ('beedrill',   add(lv2_range, (-4, -4, -4, -4, -4, -4))),
                  ('butterfree', add(lv2_range, (-4, -4, -4, -4, -4, -4))),
                  ('farfetchd',  lv2_range),
                  ('ivysaur',    lv2_range),
                  ('sudowoodo',  lv2_range),
                  ('dunsparce',  lv2_range),
                  ('quilava',    lv2_range),
                  ],

    'boss_pool': [('pinsir',    (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('scyther',   (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('heracross', (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('hypno',     (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('arbok',     (22, 22,
                                 24, 24,
                                 26, 26,)),
                  ],

    'battle_number': random.randint(3, 4)
}

cave_2_args = {
    'name': "Cave",

    'bg': 'cave_day',
    'stage': 'cave',

    'poke_pool': [('graveler',   lv2_range),
                  ('magnemite',  lv2_range),
                  ('rhyhorn',    lv2_range),
                  ('teddiursa',  lv2_range),
                  ('onix',       lv2_range),
                  ('machoke',    lv2_range),
                  ('charmeleon', lv2_range),
                  ('sneasel',    lv2_range),
                  ('pupitar',    lv2_range),
                  ('kabuto',     lv2_range),
                  ('bayleef',    lv2_range),
                  ],

    'boss_pool': [('sandslash', (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('magmar',    (22, 22,
                                 24, 24,
                                 26, 26,)),

                  ('rhydon',    (22, 22,
                                 24, 24,
                                 26, 26,)),
                  ],

    'battle_number': random.randint(3, 4)
}

beach_2_args = {
    'name': "Beach",

    'bg': 'beach_afternoon',
    'stage': 'beach',

    'poke_pool': [('staryu',     lv2_range),
                  ('quagsire',   lv2_range),
                  ('wartortle',  lv2_range),
                  ('hitmonlee',  lv2_range),
                  ('wigglytuff', lv2_range),
                  ('furret',     lv2_range),
                  ('porygon',    lv2_range),
                  ],

    'boss_pool': [('slowbro',    (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('exeggutor',  (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('tentacruel', (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('bellossom',  (22, 22,
                                  24, 24,
                                  26, 26,)),

                  ('haunter',    (22, 22,
                                  24, 24,
                                  26, 26,)),
                  ],

    'battle_number': random.randint(3, 4)
}

# level 3 routes
field_3_args = {
    'name': "Field",

    'bg': 'field_night',
    'stage': 'field',

    'poke_pool': [('ninetales',  lv3_range),
                  ('ursaring',   lv3_range),
                  ('rapidash',   lv3_range),
                  ('electabuzz', lv3_range),
                  ('raichu',     lv3_range),
                  ('skarmory',   lv3_range),
                  ('tauros',     lv3_range),
                  ('azumarill',  lv3_range),
                  ('miltank',    lv3_range),
                  ('marowak',    lv3_range),
                  ('flareon',    lv3_range), ],

    'boss_pool': [('nidoking',   (33, 33,
                                  34, 34,
                                  36, 36)),

                  ('snorlax',    (33, 33,
                                  34, 34,
                                  36, 36)),

                  ('alakazam',   (33, 33,
                                  34, 34,
                                  36, 36)),

                  ],

    'battle_number': random.randint(3, 4)
}

forest_3_args = {
    'name': "Forest",

    'bg': 'forest_night',
    'stage': 'forest',

    'poke_pool': [('scyther',   lv3_range),
                  ('heracross', lv3_range),
                  ('pinsir',    lv3_range),
                  ('arbok',     lv3_range),
                  ('nidoqueen', lv3_range),
                  ('jolteon',   lv3_range),
                  ('pidgeot',   lv3_range),
                  ('bellossom', lv3_range),
                  ],

    'boss_pool': [('scizor',   (33, 33,
                                34, 34,
                                36, 36)),

                  ('gengar',   (33, 33,
                                34, 34,
                                36, 36)),

                  ('meganium', (33, 33,
                                34, 34,
                                36, 36)),

                  ('ampharos', (33, 33,
                                34, 34,
                                36, 36)),
                  ],

    'battle_number': random.randint(3, 4)
}

cave_3_args = {
    'name': "Cave",

    'bg': 'cave_night',
    'stage': 'cave',

    'poke_pool': [('rhydon',   lv3_range),
                  ('magmar',   lv3_range),
                  ('machoke',  lv3_range),
                  ('slowbro',  lv3_range),
                  ('magneton', lv3_range),
                  ('donphan',  lv3_range),
                  ('houndoom', lv3_range),
                  ('clefable', lv3_range),
                  ('umbreon',  lv3_range),
                  ],

    'boss_pool': [('golem',     (33, 33,
                                 34, 34,
                                 36, 36)),

                  ('machamp',   (33, 33,
                                 34, 34,
                                 36, 36)),

                  ('kabutops',  (33, 33,
                                 34, 34,
                                 36, 36)),

                  ('tyranitar', (33, 33,
                                 34, 34,
                                 36, 36)),
                  ],

    'battle_number': random.randint(3, 4)
}

beach_3_args = {
    'name': "Beach",

    'bg': 'beach_night',
    'stage': 'beach',

    'poke_pool': [('starmie',   lv3_range),
                  ('espeon',    lv3_range),
                  ('kingler',   lv3_range),
                  ('arcanine',  lv3_range),
                  ('octillery', lv3_range),
                  ('dewgong',   lv3_range),
                  ('exeggutor', lv3_range),
                  ('dragonair', lv3_range),
                  ],

    'boss_pool': [('gyarados',  (33, 33,
                                 34, 34,
                                 36, 36)),

                  ('lapras',    (33, 33,
                                 34, 34,
                                 36, 36)),

                  ('dragonite', (33, 33,
                                 34, 34,
                                 36, 36)),
                  ],

    'battle_number': random.randint(3, 4)
}

# Final Boss routes

# get random bird and dog
route_rng = [random.randint(1, 3), random.randint(4, 6)]

random_bird = ''
random_dog = ''

if route_rng[0] == 1:
    random_bird = ('articuno', lv3_range)
elif route_rng[0] == 2:
    random_bird = ('zapdos', lv3_range)
elif route_rng[0] == 3:
    random_bird = ('moltres', lv3_range)

if route_rng[1] == 4:
    random_dog = ('suicune', lv3_range)
elif route_rng[1] == 5:
    random_dog = ('raikou', lv3_range)
elif route_rng[1] == 6:
    random_dog = ('entei', lv3_range)

mewtwo_route_args = {
    'name': "Cerulean Cave",

    'bg': 'cave_day',
    'stage': 'cave',

    'poke_pool': [('magikarp', lv3_range), ],

    'boss_pool': [('mewtwo', boss_range), ],

    'battle_number': random.randint(0, 0)
}

# #############################
# List of level 1 routes
level_1_routes = [field_1_args,
                  forest_1_args,
                  cave_1_args,
                  beach_1_args, ]

# List of level 2 routes
level_2_routes = [field_2_args,
                  forest_2_args,
                  cave_2_args,
                  beach_2_args, ]

# List of level 3 routes
level_3_routes = [field_3_args,
                  forest_3_args,
                  cave_3_args,
                  beach_3_args, ]

# List of final boss routes
level_4_routes = [mewtwo_route_args, mewtwo_route_args]

# generate first route
route_lv = 1
route_1 = generate_route(r1_args)

# empty route
empty_route = {
    'name': "Empty",

    'bg': 'field_day',
    'stage': 'field',

    'poke_pool': [('ratatta',    lv1_range),
                  ('pidgey',     lv1_range),
                  ('nidoran_m',  lv1_range),
                  ('meowth',     lv1_range),
                  ('jigglypuff', lv1_range),
                  ('psyduck',    lv1_range),
                  ('spearow',    lv1_range),
                  ('vulpix',     lv1_range),
                  ('oddish',     lv1_range), ],

    'boss_pool': [('pidgeotto',  (4, 4,
                                  8, 8,
                                  11, 11,)),

                  ('ponyta',     (5, 5,
                                  8, 8,
                                  11, 11,)),

                  ('mankey',     (5, 5,
                                  8, 8,
                                  11, 11,)), ],

    'battle_number': random.randint(3, 3)
}