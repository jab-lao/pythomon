# key = attack name
# values = attack type, attack level, damage,
#                                            accuracy coefficient, critical chance, speed coefficient,

# 0 Null
# 1 Normal
# 2 Fighting
# 3 Flying
# 4 Poison
# 5 Ground
# 6 Rock
# 7 Bug
# 8 Ghost
# 9 Steel
# 10 Fire
# 11 Water
# 12 Grass
# 13 Electric
# 14 Psychic
# 15 Ice
# 16 Dragon
# 17 Dark
# 18 Fairy

# attack type, damage,
#                    accuracy, critical chance, charge time

power_very_weak = 0.6
power_weak = 0.8
power_normal = 1
power_strong = 1.2
power_very_strong = 1.4
power_super = 1.6
power_hyper = 2

# very weak
# weak
# tough
# strong
# very strong
# super strong
# powerful

# very slow
# slow
# quick
# fast
# very fast
# super fast
# blinding

speed_very_slow = 16
speed_slow = 12
speed_normal = 8
speed_fast = 6
speed_very_fast = 4
# speed_super_fast =
# speed_blinding =

# base_speed = 8
# speed1 = 2
# speed2 = 4
# speed3 = 6
# speed4 = 8

power_strings = ['very weak', 'weak', 'average', 'strong', 'very strong', 'super strong', 'powerful']
speed_strings = ['very fast', 'fast', 'average', 'slow', 'very slow']

move_list = {
    "None": ["", 0, "", "", "", 1],

    # Normal Moves
    "Tackle": ["Tackle", 1, power_normal, 100, 5, speed_normal],
    "Scratch": ["Scratch", 1, power_weak, 90, 12, speed_fast],
    "Pound": ["Pound", 1, power_normal, 100, 5, speed_normal],
    "Quick Attack": ["Quick Attack", 1, power_very_weak, 85, 4, speed_very_fast],
    "Rage": ["Rage", 1, power_strong, 85, 16, speed_normal],
    "Swift": ["Swift", 1, power_strong, 999, 5, speed_slow],
    "Fury Swipes": ["Fury Swipes", 1, power_normal, 85, 5, speed_fast],
    "Double Team": ["Double Team", 1, power_normal, 80, 20, speed_very_fast],
    "Rapid Spin": ["Rapid Spin", 1, power_weak, 90, 10, speed_very_fast],
    "Horn Attack": ["Horn Attack", 1, power_strong, 100, 16, speed_normal],
    "Headbutt": ["Headbutt", 1, power_strong, 90, 8, speed_slow],
    "Stomp": ["Stomp", 1, power_strong, 85, 12, speed_slow],
    "Wrap": ["Wrap", 1, power_weak, 90, 7, speed_fast],
    "Constrict": ["Constrict", 1, power_weak, 90, 5, speed_fast],
    "Fury Attack": ["Fury Attack", 1, power_strong, 85, 16, speed_very_fast],
    "Take Down": ["Take Down", 1, power_strong, 80, 8, speed_slow],
    "Skull Bash": ["Skull Bash", 1, power_super, 100, 8, speed_very_slow],
    "Slam": ["Slam", 1, power_very_strong, 80, 10, speed_slow],
    "Flail": ["Flail", 1, power_strong, 85, 18, speed_normal],
    "Splash": ["Splash", 1, 0, 100, 0, speed_fast],
    "Pay Day": ["Pay Day", 1, power_strong, 85, 8, speed_normal],
    "Vice Grip": ["Vice Grip", 1, power_strong, 85, 8, speed_normal],
    "Slash": ["Slash", 1, power_very_strong, 80, 16, speed_normal],
    "Hyper Beam": ["Hyper Beam", 1, power_hyper, 95, 12, speed_very_slow],
    "Double Edge": ["Double Edge", 1, power_super, 90, 6, speed_slow],
    "Extreme Speed": ["Extreme Speed", 1, power_strong, 90, 10, speed_very_fast],
    "Hyper Voice": ["Hyper Voice", 1, power_very_strong, 100, 2, speed_slow],
    "Thrash": ["Thrash", 1, power_very_strong, 75, 8, speed_normal],
    "Egg Bomb": ["Egg Bomb", 1, power_very_strong, 80, 4, speed_normal],
    "Nature Power": ["Nature Power", 1, power_strong, 90, 2, speed_normal],
    "Sonic Boom": ["Sonic Boom", 1, power_weak, 85, 1, speed_fast],
    "Tri Attack": ["Tri Attack", 1, power_very_strong, 90, 10, speed_slow],
    "Mega Punch": ["Mega Punch", 1, power_strong, 90, 8, speed_normal],
    "Mega Kick": ["Mega Kick", 1, power_very_strong, 80, 12, speed_slow],
    "Raging Bull": ["Raging Bull", 1, power_super, 90, 8, speed_fast],
    "Hyper Drill": ["Hyper Drill", 1, power_super, 100, 18, speed_slow],
    "Guillotine": ["Guillotine", 1, power_super, 80, 25, speed_slow],
    "Body Slam": ["Body Slam", 1, power_very_strong, 90, 6, speed_normal],
    "Giga Impact": ["Giga Impact", 1, power_hyper, 90, 12, speed_very_slow],

    # Fighting Moves
    "Karate Chop": ["Karate Chop", 2, power_normal, 100, 8, speed_normal],
    "Rock Smash": ["Rock Smash", 2, power_normal, 90, 4, speed_normal],
    "Double Kick": ["Double Kick", 2, power_very_weak, 85, 2, speed_very_fast],
    "Low Kick": ["Low Kick", 2, power_weak, 85, 4, speed_fast],
    "Superpower": ["Superpower", 2, power_super, 90, 5, speed_slow],
    "Mach Punch": ["Mach Punch", 2, power_very_weak, 80, 8, speed_very_fast],
    "Brick Break": ["Brick Break", 2, power_strong, 90, 4, speed_normal],
    "Seismic Toss": ["Seismic Toss", 2, power_very_strong, 100, 4, speed_slow],
    "Focus Blast": ["Focus Blast", 2, power_hyper, 75, 4, speed_slow],
    "Submission": ["Submission", 2, power_super, 90, 8, speed_slow],
    "Cross Chop": ["Cross Chop", 2, power_hyper, 80, 16, speed_slow],
    "Dynamic Punch": ["Dynamic Punch", 2, power_hyper, 100, 5, speed_slow],
    "Hammer Arm": ["Hammer Arm", 2, power_very_strong, 85, 4, speed_normal],
    "Aura Sphere": ["Aura Sphere", 2, power_very_strong, 999, 4, speed_slow],
    "High Jump Kick": ["High Jump Kick", 2, power_very_strong, 75, 8, speed_normal],
    "Focus Punch": ["Focus Punch", 2, power_very_strong, 85, 15, speed_very_slow],
    "Close Combat": ["Close Combat", 2, power_very_strong, 85, 15, speed_very_slow],
    "Body Press": ["Body Press", 2, power_strong, 80, 6, speed_very_slow],

    # Flying Moves
    "Peck": ["Peck", 3, power_weak, 100, 12, speed_fast],
    "Gust": ["Gust", 3, power_normal, 90, 5, speed_normal],
    "Acrobatics": ["Acrobatics", 3, power_normal, 90, 8, speed_fast],
    "Wing Attack": ["Wing Attack", 3, power_strong, 90, 5, speed_normal],
    "Air Cutter": ["Air Cutter", 3, power_normal, 85, 16, speed_normal],
    "Air Slash": ["Air Slash", 3, power_strong, 90, 10, speed_normal],
    "Aerial Ace": ["Aerial Ace", 3, power_strong, 100, 6, speed_fast],
    "Bounce": ["Bounce", 3, power_very_strong, 90, 3, speed_slow],
    "Fly": ["Fly", 3, power_super, 100, 6, speed_slow],
    "Hurricane": ["Hurricane", 3, power_hyper, 80, 4, speed_slow],
    "Drill Peck": ["Drill Peck", 3, power_super, 90, 10, speed_slow],
    "Sky Attack": ["Sky Attack", 3, power_hyper, 90, 6, speed_very_slow],

    # Poison Moves
    "Acid": ["Acid", 4, power_very_weak, 80, 3, speed_fast],
    "Acid Spray": ["Acid Spray", 4, power_very_weak, 100, 3, speed_fast],
    "Poison Gas": ["Poison Gas", 4, power_very_weak, 80, 2, speed_normal],
    "Poison Powder": ["Poison Powder", 4, power_very_weak, 85, 0, speed_normal],
    "Poison Sting": ["Poison Sting", 4, power_weak, 90, 6, speed_normal],
    "Smog": ["Smog", 4, power_normal, 90, 8, speed_normal],
    "Venoshock": ["Venoshock", 4, power_very_strong, 90, 6, speed_slow],
    "Poison Fang": ["Poison Fang", 4, power_strong, 95, 12, speed_normal],
    "Sludge Bomb": ["Sludge Bomb", 4, power_very_strong, 90, 4, speed_slow],
    "Poison Jab": ["Poison Jab", 4, power_very_strong, 90, 6, speed_normal],
    "Belch": ["Belch", 4, power_super, 85, 6, speed_slow],
    "Gunk Shot": ["Gunk Shot", 4, power_super, 85, 8, speed_slow],

    # Ground Moves
    "Mud Slap": ["Mud Slap", 5, power_very_weak, 90, 5, speed_fast],
    "Sand Attack": ["Sand Attack", 5, power_very_weak, 85, 0, speed_fast],
    "Dig": ["Dig", 5, power_strong, 100, 10, speed_slow],
    "Bulldoze": ["Bulldoze", 5, power_strong, 100, 5, speed_slow],
    "Bone Club": ["Bone Club", 5, power_normal, 85, 8, speed_normal],
    "Bone Rush": ["Bone Rush", 5, power_very_strong, 85, 10, speed_normal],
    "Bonemerang": ["Bonemerang", 5, power_super, 90, 16, speed_slow],
    "Earthquake": ["Earthquake", 5, power_super, 100, 5, speed_slow],
    "Earth Power": ["Earth Power", 5, power_super, 90, 10, speed_slow],
    "Mud Bomb": ["Mud Bomb", 5, power_very_strong, 85, 4, speed_slow],
    "High Horsepower": ["High Horsepower", 5, power_very_strong, 85, 6, speed_normal],
    "Drill Run": ["Drill Run", 5, power_normal, 85, 16, speed_normal],

    # Rock Moves
    "Rollout": ["Rollout", 6, power_very_weak, 85, 6, speed_fast],
    "Rock Throw": ["Rock Throw", 6, power_normal, 90, 8, speed_normal],
    "Rock Blast": ["Rock Blast", 6, power_strong, 80, 10, speed_normal],
    "Rock Tomb": ["Rock Tomb", 6, power_strong, 90, 3, speed_slow],
    "Rock Slide": ["Rock Slide", 6, power_very_strong, 85, 4, speed_slow],
    "Stone Edge": ["Stone Edge", 6, power_super, 80, 4, speed_slow],
    "Ancient Power": ["Ancient Power", 6, power_strong, 85, 10, speed_slow],
    "Power Gem": ["Power Gem", 6, power_very_strong, 90, 6, speed_slow],
    "Head Smash": ["Head Smash", 6, power_super, 90, 8, speed_very_slow],

    # Bug Moves
    "Bug Bite": ["Bug Bite", 7, power_strong, 100, 8, speed_normal],
    "Fury Cutter": ["Fury Cutter", 7, power_normal, 90, 12, speed_fast],
    "Twineedle": ["Twineedle", 7, power_weak, 75, 12, speed_very_fast],
    "Bug Buzz": ["Bug Buzz", 7, power_very_strong, 90, 5, speed_slow],
    "Struggle Bug": ["Struggle Bug", 7, power_strong, 85, 5, speed_normal],
    "Leech Life": ["Leech Life", 7, power_weak, 85, 12, speed_slow],
    "Pin Missile": ["Pin Missile", 7, power_weak, 80, 12, speed_very_fast],
    "Megahorn": ["Megahorn", 7, power_super, 90, 8, speed_slow],
    "U-turn": ["U-turn", 7, power_normal, 90, 6, speed_normal],
    "Signal Beam": ["Signal Beam", 7, power_very_strong, 90, 3, speed_slow],
    "X-Scissor": ["X-Scissor", 7, power_very_strong, 85, 16, speed_normal],
    "Pounce": ["Pounce", 7, power_normal, 90, 8, speed_normal],


    # Ghost Moves
    "Lick": ["Lick", 8, power_very_weak, 100, 4, speed_fast],
    "Astonish": ["Astonish", 8, power_very_weak, 90, 4, speed_very_fast],
    "Hex": ["Hex", 8, power_normal, 100, 6, speed_normal],
    "Shadow Punch": ["Shadow Punch", 8, power_very_strong, 95, 6, speed_normal],
    "Shadow Claw": ["Shadow Claw", 8, power_strong, 85, 17, speed_normal],
    "Shadow Ball": ["Shadow Ball", 8, power_very_strong, 90, 7, speed_slow],
    "Ominous Wind": ["Ominous Wind", 8, power_strong, 100, 2, speed_slow],
    "Night Shade": ["Night Shade", 8, power_super, 100, 4, speed_normal],

    # Steel Moves
    "Metal Claw": ["Metal Claw", 9, power_normal, 90, 20, speed_slow],
    "Iron Tail": ["Iron Tail", 9, power_strong, 85, 10, speed_slow],
    "Iron Head": ["Iron Head", 9, power_very_strong, 90, 4, speed_slow],
    "Steel Wing": ["Steel Wing", 9, power_strong, 90, 6, speed_normal],
    "Gyro Ball": ["Gyro Ball", 9, power_normal, 85, 5, speed_normal],
    "Flash Cannon": ["Flash Cannon", 9, power_very_strong, 90, 5, speed_slow],
    "Meteor Mash": ["Meteor Mash", 9, power_very_strong, 90, 10, speed_slow],
    "Heavy Slam": ["Heavy Slam", 9, power_super, 85, 4, speed_very_slow],
    "Bullet Punch": ["Bullet Punch", 9, power_weak, 80, 6, speed_fast],
    "Smart Strike": ["Smart Strike", 9, power_strong, 80, 6, speed_normal],

    # Fire Moves
    "Ember": ["Ember", 10, power_normal, 100, 5, speed_normal],
    "Flame Wheel": ["Flame Wheel", 10, power_strong, 90, 5, speed_normal],
    "Fire Punch": ["Fire Punch", 10, power_very_strong, 95, 4, speed_normal],
    "Flame Charge": ["Flame Charge", 10, power_normal, 90, 10, speed_fast],
    "Fire Fang": ["Fire Fang", 10, power_strong, 90, 7, speed_normal],
    "Incinerate": ["Incinerate", 10, power_very_strong, 80, 5, speed_slow],
    "Mystical Fire": ["Mystical Fire", 10, power_strong, 90, 12, speed_slow],
    "Flamethrower": ["Flamethrower", 10, power_very_strong, 95, 6, speed_slow],
    "Fire Blast": ["Fire Blast", 10, power_super, 80, 6, speed_very_slow],
    "Blast Burn": ["Blast Burn", 10, power_hyper, 100, 8, speed_very_slow],
    "Flare Blitz": ["Flare Blitz", 10, power_super, 90, 6, speed_slow],
    "Heat Wave": ["Heat Wave", 10, power_very_strong, 85, 9, speed_slow],
    "Fire Spin": ["Fire Spin", 10, power_very_strong, 75, 8, speed_fast],
    "Eruption": ["Eruption", 10, power_super, 100, 4, speed_slow],
    "Blaze Kick": ["Blaze Kick", 10, power_very_strong, 90, 8, speed_normal],
    "Lava Plume": ["Lava Plume", 10, power_strong, 100, 8, speed_normal],
    "Sacred Fire": ["Sacred Fire", 10, power_super, 90, 16, speed_normal],
    "Overheat": ["Overheat", 10, power_super, 70, 4, speed_normal],
    "Inferno": ["Inferno", 10, power_strong, 70, 4, speed_fast],

    # Water Moves
    "Water Gun": ["Water Gun", 11, power_normal, 100, 5, speed_normal],
    "Bubble": ["Bubble", 11, power_very_weak, 85, 6, speed_fast],
    "Bubble Beam": ["Bubble Beam", 11, power_strong, 90, 5, speed_slow],
    "Crabhammer": ["Crabhammer", 11, power_very_strong, 85, 8, speed_normal],
    "Water Pulse": ["Water Pulse", 11, power_strong, 100, 5, speed_normal],
    "Aqua Tail": ["Aqua Tail", 11, power_very_strong, 90, 6, speed_slow],
    "Hydro Pump": ["Hydro Pump", 11, power_super, 80, 6, speed_slow],
    "Hydro Cannon": ["Hydro Cannon", 11, power_hyper, 100, 8, speed_very_slow],
    "Surf": ["Surf", 11, power_very_strong, 100, 4, speed_slow],
    "Muddy Water": ["Muddy Water", 11, power_very_strong, 80, 6, speed_slow],
    "Waterfall": ["Waterfall", 11, power_very_strong, 95, 4, speed_slow],
    "Aqua Jet": ["Aqua Jet", 11, power_weak, 80, 6, speed_very_fast],
    "Razor Shell": ["Razor Shell", 11, power_strong, 90, 16, speed_normal],
    "Octazooka": ["Octazooka", 11, power_very_strong, 85, 16, speed_normal],

    # Grass Moves
    "Vine Whip": ["Vine Whip", 12, power_normal, 100, 5, speed_fast],
    "Absorb": ["Absorb", 12, power_very_weak, 85, 5, speed_normal],
    "Magical Leaf": ["Magical Leaf", 12, power_strong, 999, 6, speed_slow],
    "Trailblaze": ["Trailblaze", 12, power_strong, 85, 6, speed_normal],
    "Energy Ball": ["Energy Ball", 12, power_very_strong, 95, 4, speed_slow],
    "Petal Dance": ["Petal Dance", 12, power_very_strong, 85, 2, speed_slow],
    "Power Whip": ["Power Whip", 12, power_strong, 90, 6, speed_normal],
    "Razor Leaf": ["Razor Leaf", 12, power_strong, 100, 14, speed_normal],
    "Solar Beam": ["Solar Beam", 12, power_super, 90, 6, speed_very_slow],
    "Frenzy Plant": ["Frenzy Plant", 12, power_hyper, 100, 8, speed_very_slow],
    "Grass Knot": ["Grass Knot", 12, power_normal, 100, 15, speed_slow],
    "Giga Drain": ["Giga Drain", 12, power_very_strong, 90, 2, speed_slow],
    "Seed Bomb": ["Seed Bomb", 12, power_very_strong, 85, 8, speed_slow],
    "Wood Hammer": ["Wood Hammer", 12, power_hyper, 85, 6, speed_slow],
    "Leaf Blade": ["Leaf Blade", 12, power_normal, 85, 18, speed_fast],

    # Electric Moves
    "Thunder Shock": ["Thunder Shock", 13, power_normal, 100, 5, speed_fast],
    "Thunder Punch": ["Thunder Punch", 13, power_very_strong, 95, 6, speed_normal],
    "Thunder Fang": ["Thunder Fang", 13, power_strong, 90, 7, speed_normal],
    "Thunderbolt": ["Thunderbolt", 13, power_very_strong, 90, 8, speed_slow],
    "Discharge": ["Discharge", 13, power_very_strong, 95, 4, speed_slow],
    "Electro Web": ["Electro Web", 13, power_very_weak, 100, 3, speed_fast],
    "Shock Wave": ["Shock Wave", 13, power_weak, 999, 10, speed_normal],
    "Electroball": ["Electroball", 13, power_strong, 90, 10, speed_normal],
    "Volt Tackle": ["Volt Tackle", 13, power_hyper, 100, 8, speed_slow],
    "Charge Beam": ["Charge Beam", 13, power_normal, 90, 6, speed_normal],
    "Thunder": ["Thunder", 13, power_super, 80, 8, speed_slow],
    "Zap Cannon": ["Zap Cannon", 13, power_hyper, 75, 12, speed_very_slow],

    # Psychic Moves
    "Psychic": ["Psychic", 14, power_very_strong, 100, 3, speed_slow],
    "Confusion": ["Confusion", 14, power_normal, 100, 4, speed_normal],
    "Extrasensory": ["Extrasensory", 14, power_strong, 100, 10, speed_normal],
    "Psybeam": ["Psybeam", 14, power_strong, 90, 4, speed_slow],
    "Psychic Fangs": ["Psychic Fangs", 14, power_strong, 85, 7, speed_slow],
    "Stored Power": ["Stored Power", 14, power_super, 100, 8, speed_very_slow],
    "Psyshock": ["Psyshock", 14, power_super, 85, 4, speed_slow],
    "Psystrike": ["Psystrike", 14, power_hyper, 80, 5, speed_very_slow],
    "Zen Headbutt": ["Zen Headbutt", 14, power_very_strong, 90, 6, speed_slow],

    # Ice Moves
    "Icy Wind": ["Icy Wind", 15, power_normal, 100, 6, speed_normal],
    "Ice Shard": ["Ice Shard", 15, power_weak, 85, 8, speed_very_fast],
    "Ice Punch": ["Ice Punch", 15, power_very_strong, 95, 5, speed_normal],
    "Avalanche": ["Avalanche", 15, power_very_strong, 100, 5, speed_slow],
    "Blizzard": ["Blizzard", 15, power_super, 80, 6, speed_slow],
    "Aurora Beam": ["Aurora Beam", 15, power_strong, 90, 4, speed_slow],
    "Ice Beam": ["Ice Beam", 15, power_very_strong, 90, 8, speed_slow],
    "Ice Fang": ["Ice Fang", 15, power_strong, 85, 7, speed_normal],
    "Sheer Cold": ["Sheer Cold", 13, power_hyper, 75, 12, speed_very_slow],

    # Dragon Moves
    "Dragon Rage": ["Dragon Rage", 16, power_normal, 90, 5, speed_slow],
    "Dragon Breath": ["Dragon Breath", 16, power_strong, 90, 5, speed_slow],
    "Twister": ["Twister", 16, power_normal, 85, 8, speed_normal],
    "Dragon Claw": ["Dragon Claw", 16, power_strong, 90, 8, speed_normal],
    "Dragon Tail": ["Dragon Tail", 16, power_very_strong, 85, 10, speed_slow],
    "Dragon Rush": ["Dragon Rush", 16, power_super, 80, 10, speed_slow],
    "Dual Chop": ["Dual Chop", 16, power_normal, 85, 5, speed_fast],
    "Dragon Pulse": ["Dragon Pulse", 16, power_very_strong, 90, 6, speed_slow],
    "Outrage": ["Outrage", 16, power_super, 80, 8, speed_normal],

    # Dark Moves
    "Bite": ["Bite", 17, power_normal, 90, 15, speed_normal],
    "Snarl": ["Snarl", 17, power_normal, 90, 15, speed_normal],
    "Pursuit": ["Pursuit", 17, power_normal, 90, 9, speed_fast],
    "Feint Attack": ["Faint Attack", 17, power_normal, 100, 6, speed_normal],
    "Payback": ["Payback", 17, power_strong, 100, 16, speed_normal],
    "Knock Off": ["Knock Off", 17, power_strong, 90, 6, speed_normal],
    "Crunch": ["Crunch", 17, power_very_strong, 90, 10, speed_slow],
    "Fling": ["Fling", 17, power_strong, 85, 5, speed_normal],
    "Brutal Swing": ["Brutal Swing", 17, power_super, 90, 6, speed_very_slow],
    "Foul Play": ["Foul Play", 17, power_very_strong, 90, 12, speed_slow],
    "Dark Pulse": ["Dark Pulse", 17, power_very_strong, 90, 8, speed_slow],
    "Night Slash": ["Night Slash", 17, power_very_strong, 85, 16, speed_normal],
    "Throat Chop": ["Throat Chop", 17, power_very_strong, 90, 10, speed_slow],
    "Sucker Punch": ["Sucker Punch", 17, power_very_strong, 80, 18, speed_slow],

    # Fairy Moves
    "Fairy Wind": ["Fairy Wind", 18, power_normal, 100, 6, speed_normal],
    "Disarming Voice": ["Disarming Voice", 18, power_normal, 100, 3, speed_normal],
    "Draining Kiss": ["Draining Kiss", 18, power_strong, 85, 6, speed_normal],
    "Play Rough": ["Play Rough", 18, power_very_strong, 90, 8, speed_slow],
    "Dazzling Gleam": ["Dazzling Gleam", 18, power_very_strong, 85, 6, speed_slow],
    "Moonblast": ["Moonblast", 18, power_super, 100, 4, speed_slow],
}
