background_color = '#212d41'

frame_bg_color = '#101821'

text_color = '#f7f7f7'

button_color = '#d4dbe4'
hover_color = '#f7f7f7'
button_text_color = 'black'  # '#c268f4'

stat_label_color = 'gray'
stat_value_color = '#f7f7f7'
stat_graph_fill = '#bd66ef'
graph_guide_color = '#222931'


poke_font = 'Pokemon\nGen 4 Regular'
poke_font_tuple = ('Pokemon\nGen 4 Regular', 16)
# status screen options
max_health = 800
max_attack = 80
max_speed = 80
max_skill = 30
max_evasion = 20

min_health = 270

stat_graph_max = (
    (180, 66,
     241, 116,
     221, 188,
     139, 188,
     118, 116,
     )
)

stat_graph_half = (
    (90, 33,
     120, 58,
     110, 94,
     69, 94,
     59, 58,
     )
)

stat_graph_max_mini = (
    (38, 5,
     68, 30,
     58, 66,
     17, 66,
     7, 30,
     )
)

# gacha settings
starter_poke_number = 6
common_starter_rng = 60
rare_starter_rng = 90

gacha_pull_number = 6
common_pool_rng = 60
rare_pool_rng = 90
legendary_pool_rng = 97
gacha_grid_coords = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
]

# route progression options
route_option_number = 2

# adventure canvas positions
player_adv_pos = (72, -50)
player_battle_pos = -36
enemy_spawn_pos = 460
enemy_battle_pos = 200

boss_route_encounter = 86

damage_popup_player = (290, 120)
damage_popup_enemy = (150, 120)

speed_threshold = [5, 15, 20]
speed_tiers = [1.3, 1.6, 2]

# difficulty options
harcore_mode = False
enemy_damage_mod = 0.8

# Battle log colors
player_color = '#4287f5'
enemy_color = '#f54242'

log_color = '#000000'
log_line1 = '#f7f7f7'
log_line2 = '#e6e6e6'

type_colors = [
    ('#a8a878', '#636340'),  # none_color
    ('#a8a878', '#636340'),  # normal_color
    ('#c03028', '#5d1714'),  # fighting_color
    ('#a890f0', '#4c1dd7'),  # flying_color
    ('#a040a0', '#4c1f4c'),  # poison_color
    ('#e0c068', '#876a1d'),  # ground_color
    ('#b8a038', '#5e511d'),  # rock_color
    ('#a8b820', '#545b10'),  # bug_color
    ('#705898', '#392d4d'),  # ghost_color
    ('#b8b8d0', '#49496e'),  # steel_color
    ('#f08030', '#a53009'),  # fire_color
    ('#6890f0', '#103b9d'),  # water_color
    ('#78c850', '#396921'),  # grass_color
    ('#f8d030', '#856b05'),  # electric_color
    ('#f85888', '#9c0734'),  # psychic_color
    ('#98d8d8', '#328585'),  # ice_color
    ('#7038f8', '#2b058a'),  # dragon_color
    ('#705848', '#382c24'),  # dark_color
    ('#ee99ac', '#e0486b'),  # fairy_color
]

# game flow
picked_starter = False
prize_steps = [2, 4, 6, 8, 10]

