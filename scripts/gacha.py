from pokemon_list import *


def remove_from_pools(removed_mon):
    removed_mon_name = removed_mon.name.lower()

    for i in g_pokeball:
        if removed_mon_name in i:

            i.pop(removed_mon_name)


g_starters = [
    {  # Common
        'nidoran_m': nidoran_m,
        'nidoran_f': nidoran_f,
        'ponyta': ponyta,
        'meowth': meowth,
        'cubone': cubone,
        'marill': marill,
        'vulpix': vulpix,
        'jigglypuff': jigglypuff,
        'mareep': mareep,
        'teddiursa': teddiursa,
        'houndour': houndour
    },

    {  # Uncommon
        'bulbasaur': bulbasaur,
        'charmander': charmander,
        'squirtle': squirtle,
        'pikachu': pikachu,
        'eevee': eevee,
        'clefairy': clefairy,
        'chikorita': chikorita,
        'cyndaquil': cyndaquil,
        'totodile': totodile
    },

    {  # Rare
        'dratini': dratini,
        'larvitar': larvitar,
    },

    # {  # Legendary
    #
    # }
]


g_pokeball = [
    {  # Common
        'pidgey': pidgey,
        'nidoran_m': nidoran_m,
        'nidoran_f': nidoran_f,
        'ponyta': ponyta,
        'abra': abra,
        'machop': machop,
        'geodude': geodude,
        'caterpie': caterpie,
        'ekans': ekans,
        'mankey': mankey,
        'jigglypuff': jigglypuff,
        'slowpoke': slowpoke,
        'sandshrew': sandshrew,
        'meowth': meowth,
        'psyduck': psyduck,
        'magikarp': magikarp,
        'vulpix': vulpix,
        'marill': marill,
        'phanpy': phanpy,
        'mareep': mareep,
        'teddiursa': teddiursa,
        'houndour': houndour,
        'dunsparce': dunsparce,
    },

    {  # Uncommon
        'bulbasaur': bulbasaur,
        "charmander": charmander,
        'squirtle': squirtle,
        'pikachu': pikachu,
        'eevee': eevee,
        'clefairy': clefairy,
        'cubone': cubone,
        'onix': onix,
        'chikorita': chikorita,
        'cyndaquil': cyndaquil,
        'totodile': totodile
    },

    {  # Rare
        'dratini': dratini,
        'larvitar': larvitar
    },

    {  # Legendary

    }

]

g_greatball = [
    {  # Common
        'pidgeotto': pidgeotto,
        'butterfree': butterfree,
        'beedrill': beedrill,
        'haunter': haunter,
        'machoke': machoke,
        'kadabra': kadabra,
        'graveler': graveler,
        'magneton': magneton,
        'nidorino': nidorino,
        'clefable': clefable,
        'golduck': golduck,
        'tentacruel': tentacruel,
        'rapidash': rapidash,
        'electabuzz': electabuzz,
        'magmar': magmar,
        'dewgong': dewgong,
        'hypno': hypno,
        'arbok': arbok,
        'hitmonchan': hitmonchan,
        'hitmonlee': hitmonlee,
        'quagsire': quagsire,
        'sneasel': sneasel,
        'porygon': porygon,

    },

    {  # Uncommon
        'scyther': scyther,
        'exeggutor': exeggutor,
        'rhydon': rhydon,
        'tauros': tauros,
        'dratini': dratini,
        'vaporeon': vaporeon,
        'jolteon': jolteon,
        'flareon': flareon,
        'miltank': miltank,
        'espeon': espeon,
        'umbreon': umbreon,
        'heracross': heracross,
        'skarmory': skarmory,
        'houndoom': houndoom,
        'larvitar': larvitar,

    },

    {  # Rare
        'snorlax': snorlax,
        'kingdra': kingdra,
        'lapras': lapras
    },

    {  # Legendary

    }

]

g_ultraball = [
    {  # Common
        'pidgeot': pidgeot,
        'arcanine': arcanine,
        'steelix': steelix,
        'ampharos': ampharos,
        'scizor': scizor,
        'ursaring': ursaring,
        'rhydon': rhydon,

    },

    {  # Uncommon
        'nidoqueen': nidoqueen,
        'gyarados': gyarados,
        'lapras': lapras,
        'kabutops': kabutops,
        'aerodactyl': aerodactyl,
        'snorlax': snorlax,
        'dragonair': dragonair,
        'pupitar': pupitar,
        'tentacruel': tentacruel

    },

    {  # Rare
        'kingdra': kingdra,
        'articuno': articuno,
        'zapdos': zapdos,
        'moltres': moltres,
        'dragonite': dragonite,
        'raikou': raikou,
        'entei': entei,
        'suicune': suicune,
        'tyranitar': tyranitar,
    },

    {  # Legendary

    }

]