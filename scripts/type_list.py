

neutral = 1.0
resist = 0.6
double_resist = 0.2
weak = 1.3
double_weak = 1.8
immune = 0.0


types = [
    [  # Null
        "",
        0,
        neutral,  # Normal
        neutral,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Normal Type
        "Normal",
        1,
        neutral,  # Normal
        weak,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        immune,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Fighting Type
        "Fighting",
        2,
        neutral,  # Normal
        neutral,  # Fighting
        weak,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        resist,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        weak,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        resist,  # Dark
        weak,  # Fairy
    ],

    [  # Flying Type
        "Flying",
        3,
        neutral,  # Normal
        resist,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        immune,  # Ground
        weak,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        resist,  # Grass
        weak,  # Electric
        neutral,  # Psychic
        weak,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Poison Type
        "Poison",
        4,
        neutral,  # Normal
        resist,  # Fighting
        neutral,  # Flying
        resist,  # Poison
        weak,  # Ground
        neutral,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        resist,  # Grass
        neutral,  # Electric
        weak,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        resist,  # Fairy
    ],

    [  # Ground Type
        "Ground",
        5,
        neutral,  # Normal
        neutral,  # Fighting
        neutral,  # Flying
        resist,  # Poison
        neutral,  # Ground
        resist,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        weak,  # Water
        weak,  # Grass
        immune,  # Electric
        neutral,  # Psychic
        weak,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Rock Type
        "Rock",
        6,
        resist,  # Normal
        weak,  # Fighting
        resist,  # Flying
        resist,  # Poison
        weak,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        weak,  # Steel
        resist,  # Fire
        weak,  # Water
        weak,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Bug Type
        "Bug",
        7,
        neutral,  # Normal
        resist,  # Fighting
        weak,  # Flying
        neutral,  # Poison
        resist,  # Ground
        weak,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        weak,  # Fire
        neutral,  # Water
        resist,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Ghost
        "Ghost",
        8,
        immune,  # Normal
        immune,  # Fighting
        neutral,  # Flying
        resist,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        resist,  # Bug
        weak,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        weak,  # Dark
        neutral,  # Fairy
    ],

    [  # Steel Type
        "Steel",
        9,
        resist,  # Normal
        weak,  # Fighting
        resist,  # Flying
        immune,  # Poison
        weak,  # Ground
        resist,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        resist,  # Steel
        weak,  # Fire
        neutral,  # Water
        resist,  # Grass
        neutral,  # Electric
        resist,  # Psychic
        resist,  # Ice
        resist,  # Dragon
        neutral,  # Dark
        resist,  # Fairy
    ],

    [  # Fire Type
        "Fire",
        10,
        neutral,  # Normal
        neutral,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        weak,  # Ground
        weak,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        resist,  # Steel
        resist,  # Fire
        weak,  # Water
        resist,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        resist,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        resist,  # Fairy
    ],

    [  # Water Type
        "Water",
        11,
        neutral,  # Normal
        neutral,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        resist,  # Steel
        resist,  # Fire
        resist,  # Water
        weak,  # Grass
        weak,  # Electric
        neutral,  # Psychic
        resist,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Grass Type
        "Grass",
        12,
        neutral,  # Normal
        neutral,  # Fighting
        weak,  # Flying
        weak,  # Poison
        resist,  # Ground
        neutral,  # Rock
        weak,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        weak,  # Fire
        resist,  # Water
        resist,  # Grass
        resist,  # Electric
        neutral,  # Psychic
        weak,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Electric Type
        "Electric",
        13,
        neutral,  # Normal
        neutral,  # Fighting
        resist,  # Flying
        neutral,  # Poison
        weak,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        resist,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        resist,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Psychic Type
        "Psychic",
        14,
        neutral,  # Normal
        resist,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        weak,  # Bug
        weak,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        resist,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        weak,  # Dark
        neutral,  # Fairy
    ],

    [  # Ice Type
        "Ice",
        15,
        neutral,  # Normal
        weak,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        weak,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        weak,  # Steel
        weak,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        resist,  # Ice
        neutral,  # Dragon
        neutral,  # Dark
        neutral,  # Fairy
    ],

    [  # Dragon Type
        "Dragon",
        16,
        neutral,  # Normal
        neutral,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        neutral,  # Bug
        neutral,  # Ghost
        neutral,  # Steel
        resist,  # Fire
        resist,  # Water
        resist,  # Grass
        resist,  # Electric
        neutral,  # Psychic
        weak,  # Ice
        weak,  # Dragon
        neutral,  # Dark
        weak,  # Fairy
    ],

    [  # Dark Type
        "Dark",
        17,
        neutral,  # Normal
        weak,  # Fighting
        neutral,  # Flying
        neutral,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        weak,  # Bug
        resist,  # Ghost
        neutral,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        immune,  # Psychic
        neutral,  # Ice
        neutral,  # Dragon
        resist,  # Dark
        weak,  # Fairy
    ],

    [  # Fairy Type
        "Fairy",
        18,
        neutral,  # Normal
        resist,  # Fighting
        neutral,  # Flying
        weak,  # Poison
        neutral,  # Ground
        neutral,  # Rock
        resist,  # Bug
        neutral,  # Ghost
        weak,  # Steel
        neutral,  # Fire
        neutral,  # Water
        neutral,  # Grass
        neutral,  # Electric
        neutral,  # Psychic
        neutral,  # Ice
        immune,  # Dragon
        resist,  # Dark
        neutral,  # Fairy
    ]

]

typelist = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
]


# ['Null',
#         'Normal',
#         'Fighting',
#         'Flying',
#         'Poison',
#         'Ground',
#         'Rock',
#         'Bug',
#         'Ghost',
#         'Steel',
#         'Fire',
#         'Water',
#         'Grass',
#         'Electric',
#         'Psychic',
#         'Ice',
#         'Dragon',
#         'Dark',
#         'Fairy'
#         ]

