import threading
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import random
import time

import settings as stg
from pokemon_list import *
import party as pty
import routes as rt
from move_list import *


class AdventureScreen (ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color, width=1280, height=720)
        self.app = parent
        self.app.game_screen = 'adv'
        # data
        self.bg_image = PhotoImage(file='Images/Stages/Backgrounds/field_day.png')
        self.stage_image = PhotoImage(file='Images/Stages/field.png')

        # create adventure canvas
        self.adv_canvas = Canvas(self, width=460, height=280, highlightbackground='black', highlightthickness=3)

        # draw background elements
        self.bg = self.adv_canvas.create_image(0, 0, image=self.bg_image, anchor=NW)
        self.stage = self.adv_canvas.create_image(40, 130, image=self.stage_image, anchor=NW)

        # draw pokemon
        self.player_pokemon = CanvasPokemon(self, self.adv_canvas, 'player')
        self.enemy_pokemon = CanvasPokemon(self, self.adv_canvas, 'enemy')

        # create PokéSwitcher buttons
        self.poke_switcher = PokeSwitcher(self)

        # create battle log
        self.battle_log_bg = ctk.CTkFrame(self, width=307, height=286, corner_radius=0, fg_color='black')
        self.battle_log = BattleLog(self)

        # create route manager
        self.route_progress = RouteManager(self)
        self.current_route_label = ctk.CTkLabel(self, text='', font=poke_font_tuple, fg_color=background_color, text_color=text_color)

        # create stat boxes
        self.player_stats = AdvStats(self, 'player')
        self.enemy_stats = AdvStats(self, 'enemy')

        # create pokemon move boxes
        self.player_moves_frame = ctk.CTkFrame(self, fg_color=frame_bg_color, corner_radius=0)
        self.player_move1 = AdvMove(self.player_moves_frame, 'player', 1)
        self.player_move2 = AdvMove(self.player_moves_frame, 'player', 2)

        self.player_move1.pack(pady=(0, 4))
        self.player_move2.pack()

        self.enemy_moves_frame = ctk.CTkFrame(self, fg_color=frame_bg_color, corner_radius=0)
        self.enemy_move1 = AdvMove(self.enemy_moves_frame, 'enemy', 1)
        self.enemy_move2 = AdvMove(self.enemy_moves_frame, 'enemy', 2)

        self.enemy_move1.pack(pady=(0, 4))
        self.enemy_move2.pack()

        # create battle director
        self.battle_director = BattleDirector(self)

        # menu buttons
        self.status_screen_button = ctk.CTkButton(self,
                                                  command=lambda: self.app.change_screen('status'),
                                                  text='party menu',
                                                  font=poke_font_tuple,
                                                  fg_color=button_color,
                                                  text_color=button_text_color,
                                                  hover_color=text_color,
                                                  corner_radius=0, width=146)
        self.back_button = ctk.CTkButton(self,
                                         command=self.back_to_title,
                                         text='exit game',
                                         corner_radius=0,
                                         width=146,
                                         font=poke_font_tuple,
                                         fg_color=button_color,
                                         text_color=button_text_color,
                                         hover_color=text_color)

        # layout
        self.current_route_label.place(x=330, y=50)
        self.route_progress.place(x=269, y=70)
        self.poke_switcher.place(x=60, y=159)

        self.player_stats.place(x=330, y=443)
        self.player_moves_frame.place(x=420, y=509)

        self.enemy_stats.place(x=1586, y=443)
        self.enemy_moves_frame.place(x=1676, y=509)

        self.adv_canvas.place(x=330, y=160)
        self.battle_log_bg.place(x=793, y=160)
        self.battle_log.place(x=796, y=163)

        self.status_screen_button.place(x=61, y=390)
        self.back_button.place(x=61, y=422)

    def adv_timer(self, secs):
        return time.sleep(secs)

    def back_to_title(self):
        self.app.change_screen('title')


class RouteManager(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color, height=90, width=588)
        self.parent = parent
        self.cur_route = rt.route_1
        self.cur_route_encounters = list(self.cur_route.keys())

        self.route_progressbar = ctk.CTkProgressBar(self, corner_radius=0, width=460, height=10)
        self.r_progress = 0

        # pokemon icons
        self.filler_icon = PhotoImage(file='Images/Icons/0.png')
        self.progress_canvas = Canvas(self, width=588, height=64, border=0, highlightthickness=0, bg=background_color)
        self.player_icon = self.progress_canvas.create_image(-128, 0, image=self.filler_icon, anchor=NW)
        self.enemy_icon = self.progress_canvas.create_image(-128, 0, image=self.filler_icon, anchor=NW)
        self.boss_icon = self.progress_canvas.create_image(-128, 0, image=self.filler_icon, anchor=NW)
        self.player_icon_sprite = PhotoImage(file='Images/Icons/1.png')
        self.enemy_icon_sprite = PhotoImage(file='Images/Icons/1.png')
        self.boss_icon_sprite = PhotoImage(file='Images/Icons/1.png')

        self.progress_canvas.place(x=0, y=0)
        self.route_progressbar.place(x=64, y=72)

    def stepping(self):
        if self.parent.app.game_screen == 'adv':
            if not pty.in_battle and pty.active_pokemon.cur_hp >= 1:
                self.r_progress += 0.00006
                self.route_progressbar.set(self.r_progress)
                self.progress_canvas.coords(self.player_icon, ((self.r_progress * 460) + 32), 0)

            if self.cur_route_encounters and (self.r_progress >= (self.cur_route_encounters[0] / 100)):
                self.parent.battle_director.generate_enemy(self.cur_route[self.cur_route_encounters[0]])
                self.cur_route_encounters.pop(0)

                # hide boss icon if boss encounter
                if len(self.cur_route_encounters) == 0:
                    self.hide_boss_icon()

            if self.r_progress >= 1:
                self.end_route()

            self.after(1, self.stepping)

    def end_route(self):
        # heals party members
        for key, value in pty.party.items():
            value.cur_hp = value.hp

            # partial heal
            # if value.name != '':
            #     value.cur_hp += round(value.hp * 0.4)
            #     if value.cur_hp > value.hp:
            #         value.cur_hp = value.hp

        pty.stages_cleared += 1
        self.parent.battle_log.clear_log()

        if pty.stages_cleared < 10:
            if pty.stages_cleared in prize_steps:
                self.parent.app.change_screen('picker')
            else:
                self.parent.app.change_screen('route')
        # won game
        else:
            self.parent.app.change_screen('results')
            self.parent.app.results_screen.get_results('won')

    def start_route(self, route_args):
        self.parent.app.game_screen = 'adv'
        new_route = rt.generate_route(route_args)
        self.cur_route = new_route
        self.cur_route_encounters = list(self.cur_route.keys())

        # update stage and background images
        self.parent.bg_image = PhotoImage(file=f"Images/Stages/Backgrounds/{route_args['bg']}.png")
        self.parent.stage_image = PhotoImage(file=f"Images/Stages/{route_args['stage']}.png")

        self.parent.adv_canvas.itemconfig(self.parent.bg, image=self.parent.bg_image)
        self.parent.adv_canvas.itemconfig(self.parent.stage, image=self.parent.stage_image)

        self.r_progress = 0
        self.route_progressbar.set(0)
        self.show_boss_icon()

    def update_player_icon(self):
        player_pil = Image.open(f'Images/Icons/{pty.active_pokemon.dex}.png')
        player_pil = ImageOps.mirror(player_pil)
        self.player_icon_sprite = ImageTk.PhotoImage(player_pil)
        self.player_icon = self.progress_canvas.create_image(((self.r_progress * 460) + 32), 0, image=self.player_icon_sprite, anchor=NW)

    def show_enemy_icon(self):
        self.enemy_icon_sprite = PhotoImage(file=f'Images/Icons/{pty.enemy_pokemon.dex}.png')
        self.enemy_icon = self.progress_canvas.create_image(((self.r_progress * 460) + 96), 0, image=self.enemy_icon_sprite, anchor=NW)

    def hide_enemy_icon(self):
        self.enemy_icon_sprite = PhotoImage(file=f'Images/Icons/0.png')
        self.enemy_icon = self.progress_canvas.create_image(-128, 0, image=self.enemy_icon_sprite, anchor=NW)

    def show_boss_icon(self):
        boss_dex = eval(f'{self.cur_route[boss_route_encounter][0]}[0]')
        boss_pil = Image.open(f'Images/Icons/{boss_dex}.png').convert("RGBA")
        darkener = ImageEnhance.Brightness(boss_pil)
        boss_pil = darkener.enhance(0)
        self.boss_icon_sprite = ImageTk.PhotoImage(boss_pil)
        self.boss_icon = self.progress_canvas.create_image(492, 0, image=self.boss_icon_sprite, anchor=NW)

    def hide_boss_icon(self):
        self.boss_icon_sprite = PhotoImage(file=f'Images/Icons/0.png')
        self.boss_icon = self.progress_canvas.create_image(-128, 0, image=self.boss_icon_sprite, anchor=NW)


class CanvasPokemon(ctk.CTkFrame):
    def __init__(self, parent, adv_canvas, pokemon):
        self.loop = 1
        self.anm_bool = True
        self.move_used = 0

        super().__init__(parent)
        self.parent = parent
        self.adv_canvas = adv_canvas
        self.pokemon = pokemon

        self.direction = 1
        # get pokemon sprite
        self.pokemon_sprite_org = Image.open(f'Images/Sprites/0.png')
        self.pokemon_sprite = None
        self.display_pokemon()

    def display_pokemon(self):
        if self.pokemon == 'player':
            self.pokemon_sprite_org = Image.open(f'Images/Sprites/{pty.active_pokemon.dex}.png')
            self.pokemon_sprite_org = ImageOps.mirror(self.pokemon_sprite_org)
        else:
            self.pokemon_sprite_org = Image.open(f'Images/Sprites/{pty.enemy_pokemon.dex}.png')

        self.pokemon_sprite = ImageTk.PhotoImage(self.pokemon_sprite_org)

        # draw sprite on canvas
        if self.pokemon == 'player':
            self.displayed_pokemon = self.adv_canvas.create_image(player_adv_pos[0], player_adv_pos[1],
                                                                 image=self.pokemon_sprite, anchor=NW)
            self.direction = 1

        else:
            self.displayed_pokemon = self.adv_canvas.create_image(enemy_spawn_pos, player_adv_pos[1],
                                                                 image=self.pokemon_sprite, anchor=NW)
            self.direction = -1

    def evolve_pokemon(self):
        self.pokemon_sprite_org = Image.open(f'Images/Sprites/{pty.active_pokemon.dex}.png')
        self.pokemon_sprite_org = ImageOps.mirror(self.pokemon_sprite_org)

        self.pokemon_sprite = ImageTk.PhotoImage(self.pokemon_sprite_org)

        self.displayed_pokemon = self.adv_canvas.create_image(player_battle_pos, player_adv_pos[1],
                                                                 image=self.pokemon_sprite, anchor=NW)
        self.direction = 1

    def move_to_battle_pos(self):
        if self.parent.adv_canvas.coords(self.displayed_pokemon)[0] >= player_battle_pos:
            self.adv_canvas.move(self.displayed_pokemon, -0.25, 0)
            self.adv_canvas.after(1, self.move_to_battle_pos)

    def move_to_adv_pos(self):
        if self.parent.adv_canvas.coords(self.displayed_pokemon)[0] <= player_adv_pos[0]:
            self.adv_canvas.move(self.displayed_pokemon, +0.2, 0)
            self.adv_canvas.after(1, self.move_to_adv_pos)
        else:
            pty.in_battle = False

    def enemy_spawn(self):
        if self.parent.adv_canvas.coords(self.displayed_pokemon)[0] >= enemy_battle_pos:
            self.adv_canvas.move(self.displayed_pokemon, -0.6, 0)
            self.adv_canvas.after(1, self.enemy_spawn)
        else:
            self.loop = 1
            self.parent.battle_director.start_battle()

    def faint(self):
        # change canvas sprite to blank
        self.pokemon_sprite_org = Image.open(f'Images/Sprites/0.png')
        self.pokemon_sprite = ImageTk.PhotoImage(self.pokemon_sprite_org)

        if self.pokemon == 'player':
            self.parent.battle_log.pokemon_fainted(pty.active_pokemon)
            pty.battles_lost += 1

            if stg.harcore_mode:
                pty.party[f'slot{pty.active_pokemon.party_index}'] = Pokemon(*empty, level=0, party_index=pty.active_pokemon.party_index)
                pty.active_pokemon = pty.party[f'slot{pty.active_pokemon.party_index}']
                pty.sort_party()
                self.parent.poke_switcher.initialize_buttons()
                self.parent.route_progress.update_player_icon()
                pty.party_size -= 1

            else:
                empty_mon = Pokemon(*empty, level=0, party_index=1)
                pty.active_pokemon = empty_mon
                pty.fainted_mons += 1

            # check for game over
            if pty.party_size <= 0 or pty.fainted_mons >= pty.party_size:
                self.parent.app.change_screen('results')
                self.parent.app.results_screen.get_results('lost')

        else:
            self.parent.battle_log.pokemon_fainted(pty.enemy_pokemon)
            self.parent.battle_director.end_battle()
            pty.battles_won += 1

    # attack startup
    def atk(self):
        if self.loop <= 128:
            self.adv_canvas.move(self.displayed_pokemon, (-0.06 * self.direction), 0)
            self.loop += 1
            self.adv_canvas.after(1, self.atk)
        else:
            self.loop = 1
            self.atk1()

    # end startup
    def atk1(self):
        if self.loop <= 1:
            self.loop += 1
            self.adv_canvas.after(380, self.atk1)
        else:
            self.loop = 1
            self.atk2()

    # attack dash
    def atk2(self):
        if self.loop <= 64:
            self.adv_canvas.move(self.displayed_pokemon, (+1 * self.direction), 0)
            self.loop += 1
            self.adv_canvas.after(1, self.atk2)
        else:
            self.parent.battle_director.deal_damage(self.move_used)
            self.loop = 1
            self.atk3()

    # hit stop
    def atk3(self):
        if self.loop <= 1:
            self.loop += 1
            self.adv_canvas.after(360, self.atk3)
        else:
            self.loop = 1
            self.atk4()

    # return to battle position
    def atk4(self):
        if (self.pokemon == 'player' and self.parent.adv_canvas.coords(self.displayed_pokemon)[0] >= player_battle_pos) or\
                (self.pokemon != 'player' and self.parent.adv_canvas.coords(self.displayed_pokemon)[0] <= enemy_battle_pos):
            self.adv_canvas.move(self.displayed_pokemon, (-0.25 * self.direction), 0)
            self.adv_canvas.after(1, self.atk4)
        else:
            # check if both combatants are alive
            if (pty.active_pokemon.cur_hp > 0) and (pty.enemy_pokemon.cur_hp > 0):
                self.parent.battle_director.charging = True

    # got hit by attack
    def hurt(self):
        if self.loop <= 5:
            if self.anm_bool:
                # pass
                self.adv_canvas.coords(self.displayed_pokemon, 3000, 0)
            else:
                if self.pokemon == 'player':
                    # pass
                    self.adv_canvas.coords(self.displayed_pokemon, player_battle_pos, player_adv_pos[1])
                else:
                    # pass
                    self.adv_canvas.coords(self.displayed_pokemon, enemy_battle_pos, player_adv_pos[1])

            self.anm_bool = not self.anm_bool
            self.loop += 1
            self.adv_canvas.after(90, self.hurt)
        else:
            if self.pokemon == 'player':
                # pass
                self.adv_canvas.coords(self.displayed_pokemon, player_battle_pos, player_adv_pos[1])
            else:
                # pass
                self.adv_canvas.coords(self.displayed_pokemon, enemy_battle_pos, player_adv_pos[1])
            self.loop = 1

    # dodged attack
    def dodge(self):
        if self.loop <= 42:
            self.adv_canvas.move(self.displayed_pokemon, (-1.2 * self.direction), 0)
            self.loop += 1
            self.adv_canvas.after(1, self.dodge)
        else:
            self.loop = 1
            self.post_dodge()

    # dodged attack
    def post_dodge(self):
        if self.loop <= 1:
            self.loop += 1
            self.adv_canvas.after(300, self.post_dodge)
        else:
            self.loop = 1
            self.dodge_reposition()

    # reposition after dodge
    def dodge_reposition(self):
        if self.pokemon == 'player':
            if self.parent.adv_canvas.coords(self.displayed_pokemon)[0] <= player_battle_pos:
                self.adv_canvas.move(self.displayed_pokemon, +0.3, 0)
                self.adv_canvas.after(1, self.dodge_reposition)
            else:
                self.loop = 1

        else:
            if self.parent.adv_canvas.coords(self.displayed_pokemon)[0] >= enemy_battle_pos:
                self.adv_canvas.move(self.displayed_pokemon, -0.3, 0)
                self.adv_canvas.after(1, self.dodge_reposition)
            else:
                self.loop = 1


class AdvMove(ctk.CTkFrame):
    def __init__(self, parent, player_or_enemy, move_number):
        self.bg_color = frame_bg_color
        self.icon_size = 22
        super().__init__(parent, height=34, width=128, corner_radius=0, fg_color=self.bg_color)
        self.player_or_enemy = player_or_enemy
        self.move_number = move_number
        self.pokemon = None
        self.move = None

        # create move name label and type icon canvas
        self.move_label = ctk.CTkLabel(self, text='', anchor='w', text_color=text_color, font=(poke_font, 14))

        self.icon_canvas = Canvas(self, width=self.icon_size, height=self.icon_size, border=0, highlightthickness=0, bg=self.bg_color)
        self.icon_pillow = Image.open('Images/TypeIcons/1.png')
        self.icon_pillow = self.icon_pillow.resize((self.icon_size, self.icon_size))
        self.icon_pi = ImageTk.PhotoImage(self.icon_pillow)
        self.icon_sprite = self.icon_canvas.create_image(0, 0, image=self.icon_pi, anchor=NW)

        # create move progress bar
        self.move_progressbar = ctk.CTkProgressBar(self, width=84, corner_radius=0)

        # set progress bar value
        self.move_charge = 0
        self.move_progressbar.set(self.move_charge)

        self.update_move_box()
        # layout
        self.icon_canvas.place(x=0, y=4)
        self.move_label.place(x=25, y=-3)
        self.move_progressbar.place(x=26, y=24)

    def update_move_box(self):
        # check if pokemon is player or enemy
        if self.player_or_enemy == 'player':
            self.pokemon = pty.active_pokemon
        else:
            self.pokemon = pty.enemy_pokemon

        if self.move_number == 1:
            if self.player_or_enemy == 'player':
                self.move_label.configure(text=self.pokemon.move1[0])
                self.move = self.pokemon.move1
            else:
                self.move_label.configure(text=self.pokemon.e_moves[0][0])
                self.move = self.pokemon.e_moves[0]

        else:
            if self.player_or_enemy == 'player':
                self.move_label.configure(text=self.pokemon.move2[0])
                self.move = self.pokemon.move2
            else:
                self.move_label.configure(text=self.pokemon.e_moves[1][0])
                self.move = self.pokemon.e_moves[1]

        # update icon
        self.icon_pillow = Image.open(f'Images/TypeIcons/{self.move[1] - 1}.png')
        self.icon_pillow = self.icon_pillow.resize((self.icon_size, self.icon_size))
        self.icon_pi = ImageTk.PhotoImage(self.icon_pillow)
        self.icon_sprite = self.icon_canvas.create_image(0, 0, image=self.icon_pi, anchor=NW)


class AdvStats(ctk.CTkFrame):
    def __init__(self, parent, player_or_enemy):
        self.bg_color = frame_bg_color
        super().__init__(parent)
        self.configure(height=146, width=222, corner_radius=0, fg_color=self.bg_color, border_width=3, border_color='black')
        self.parent = parent
        self.player_or_enemy = player_or_enemy
        self.icon_size = 22

        # create labels
        self.name_label = ctk.CTkLabel(self, text="", width=100, anchor='e', text_color=text_color, font=(poke_font, 16))
        self.level_label = ctk.CTkLabel(self, text="", width=50, anchor='w', text_color=text_color, font=(poke_font, 16))

        # create HP bar
        self.hp_bg = ctk.CTkFrame(self, width=176, height=20, corner_radius=0, fg_color='black')
        self.hp_bar = ctk.CTkProgressBar(self, width=172, height=16, corner_radius=0, progress_color='#18c020', fg_color='#484848')
        self.hp_label = ctk.CTkLabel(self, text='', width=20, anchor='e', text_color='#18c020', font=poke_font_tuple)
        self.hp_archive = 0

        # create exp bar
        self.exp_bar = ctk.CTkProgressBar(self, corner_radius=0, width=75, height=6, progress_color='#4890f8', fg_color='#484848')
        self.exp_bar.set(0)
        self.exp_archive = 0
        self.exp_bar_archive = 0

        # create type canvas
        self.type_icon_pillow = Image.open('Images/TypeIcons/1.png')
        self.type_icon_pillow = self.type_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
        self.type_icon_canvas = Canvas(self, width=((self.icon_size * 2) + 5), height=self.icon_size, border=0, highlightthickness=0, bg=self.bg_color)
        self.type_icon_sprite = self.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

        self.type2_icon_pillow = Image.open(f'Images/TypeIcons/1.png')
        self.type2_icon_pillow = self.type2_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
        self.type2_icon_sprite = self.type_icon_canvas.create_image(0, 25, image=self.type2_icon, anchor=NW)

        # create stat graph
        self.graph_canvas = Canvas(self, width=75, height=75, border=0, highlightthickness=0, bg=self.bg_color)
        self.graph = ''

        self.update_stats()

        # layout
        self.hp_bg.place(x=8, y=8)
        self.hp_bar.place(x=10, y=10)
        self.hp_label.place(x=188, y=4)
        self.exp_bar.place(x=10, y=30)
        self.level_label.place(x=10, y=32)
        self.type_icon_canvas.place(x=170, y=34)
        self.name_label.place(x=65, y=30)
        self.graph_canvas.place(x=10, y=56)

    def update_stats(self):
        updated_mon = pty.active_pokemon if self.player_or_enemy == 'player' else pty.enemy_pokemon
        canvas_mon = self.parent.player_pokemon if self.player_or_enemy == 'player' else self.parent.enemy_pokemon
        self.name_label.configure(text=updated_mon.name)
        self.level_label.configure(text=f'Lv. {updated_mon.lv}')

        # set hp bar
        self.hp_archive = updated_mon.cur_hp
        self.hp_bar.set(updated_mon.cur_hp / updated_mon.hp)
        self.hp_label.configure(text=f'{int(updated_mon.cur_hp)}')

        # set exp bar
        self.exp_bar.set(updated_mon.exp / updated_mon.exp_cap)
        self.exp_bar_archive = self.exp_bar.get()

        # update type icon
        self.type_icon_pillow = Image.open(f'Images/TypeIcons/{updated_mon.type1[1] - 1}.png')
        self.type_icon_pillow = self.type_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
        self.type_icon_sprite = self.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

        self.type2_icon_pillow = Image.open(f'Images/TypeIcons/{updated_mon.type2[1] - 1}.png')
        self.type2_icon_pillow = self.type2_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
        self.type2_icon_sprite = self.type_icon_canvas.create_image(25, 0, image=self.type2_icon, anchor=NW)

        # update graph
        self.graph_canvas.delete('all')
        stats_percentage = [
            updated_mon.base_hp / max_health,
            updated_mon.base_atk / max_attack,
            updated_mon.skill / max_skill,
            updated_mon.evasion / max_evasion,
            updated_mon.base_spd / max_speed,
        ]

        stat_points = [
            38, self.place_point(38, 5, stats_percentage[0]),
            self.place_point(38, 68, stats_percentage[1]), self.place_point(38, 30, stats_percentage[1]),
            self.place_point(38, 58, stats_percentage[2]), self.place_point(38, 66, stats_percentage[2]),
            self.place_point(38, 17, stats_percentage[3]), self.place_point(38, 66, stats_percentage[3]),
            self.place_point(38, 7, stats_percentage[4]), self.place_point(38, 30, stats_percentage[4]),
        ]

        self.graph = self.graph_canvas.create_polygon(*stat_points, fill=stat_graph_fill, outline=stat_graph_fill)
        self.graph_canvas.create_polygon(*stat_graph_max_mini, fill='', outline=stat_label_color)

    def update_hp(self):
        updated_mon = pty.active_pokemon if self.player_or_enemy == 'player' else pty.enemy_pokemon
        canvas_mon = self.parent.player_pokemon if self.player_or_enemy == 'player' else self.parent.enemy_pokemon

        if self.hp_archive > updated_mon.cur_hp and self.hp_archive > 0:
            self.hp_archive -= (updated_mon.hp / 500)
            self.hp_bar.set(self.hp_archive / updated_mon.hp)
            self.hp_label.configure(text=f'{int(self.hp_archive)}')
            self.level_label.configure(text=f'Lv. {updated_mon.lv}')

            self.after(1, self.update_hp)
        else:
            self.hp_archive = updated_mon.cur_hp
            # check for 0 HP
            if self.hp_archive <= 0:
                self.hp_bar.set(0)
                updated_mon.hp = 1
                canvas_mon.faint()

                # gain exp
                self.exp_bar_archive = pty.active_pokemon.exp / pty.active_pokemon.exp_cap
                if self.player_or_enemy != 'player':
                    # if pty.active_pokemon.cur_hp >= 1:
                    pty.active_pokemon.exp += pty.enemy_pokemon.lv * 6
                    self.check_for_evolution(pty.active_pokemon)

                    # exp share
                    for key, value in pty.party.items():
                        # check if party member is not the active pokemon
                        if value.name != pty.active_pokemon.name and value.name != '':
                            value.exp += pty.enemy_pokemon.lv * 6

                            # check for level up
                            if value.exp >= value.exp_cap:
                                prev_lv = value.lv
                                value.level_up(shared=True)
                                self.parent.battle_log.pokemon_lv_up(value)
                                self.check_for_evolution(value)

                                # check for learned move
                                learnset = list(value.learnset.keys())
                                gained_lvs = range(value.lv - prev_lv)
                                for lv in gained_lvs:
                                    cur_lv = prev_lv + lv
                                    if cur_lv in learnset:
                                        self.parent.battle_log.pokemon_learned_move(value, move_list[value.learnset[cur_lv]])

                    self.parent.player_stats.update_exp()

    def update_exp(self):
        if self.exp_bar_archive < (pty.active_pokemon.exp / pty.active_pokemon.exp_cap):
            self.exp_bar_archive += 0.002
            # self.exp_archive += 1
            self.exp_bar.set(self.exp_bar_archive)

            # check for level up
            if self.exp_bar_archive >= 1:
                pty.active_pokemon.level_up()
                self.level_label.configure(text=f'Lv. {pty.active_pokemon.lv}')
                self.parent.battle_log.pokemon_lv_up(pty.active_pokemon)
                self.hp_bar.set(pty.active_pokemon.cur_hp / pty.active_pokemon.hp)
                self.hp_archive = pty.active_pokemon.cur_hp
                self.hp_label.configure(text=f'{int(pty.active_pokemon.cur_hp)}')
                self.exp_bar.set(0)
                self.exp_bar_archive = 0
                self.flash_stats()

                # check for learned move
                learnset = list(pty.active_pokemon.learnset.keys())
                if pty.active_pokemon.lv in learnset:
                    self.parent.battle_log.pokemon_learned_move(pty.active_pokemon, move_list[pty.active_pokemon.learnset[pty.active_pokemon.lv]])

                # check for evolution
                self.check_for_evolution(pty.active_pokemon)

            self.after(1, self.update_exp)

    def check_for_evolution(self, value):
        if value.evo_level and value.lv >= value.evo_level:
            value.evolve()
            if value == pty.active_pokemon:
                pty.active_pokemon = pty.party[f'slot{pty.active_pokemon.party_index}']
                self.parent.player_pokemon.evolve_pokemon()
                self.parent.player_stats.update_stats()
                pty.active_pokemon.move1 = self.parent.player_move1.move
                pty.active_pokemon.move2 = self.parent.player_move2.move
                prev_exp = value.exp
                pty.active_pokemon.exp = prev_exp
                self.update_exp()
            evolved_mon = value
            value = pty.party[f'slot{value.party_index}']
            self.parent.poke_switcher.initialize_buttons()
            if value.evo_level and value.lv >= value.evo_level:
                self.check_for_evolution(value)
            self.parent.route_progress.update_player_icon()
            pty.pokemon_obtained[pty.pokemon_obtained.index(evolved_mon.dex)] = value.dex

            self.parent.battle_log.pokemon_evolved(evolved_mon, value)

    def place_point(self, start, end, percentage):
        return eval(f'{start}+{percentage}*({end}-{start})')

    def flash_stats(self):
        self.hp_label.configure(text_color='white')
        self.hp_bar.configure(progress_color='white')
        self.exp_bar.configure(progress_color='white')
        self.after(120, self.unflash_stats)
        self.graph_canvas.itemconfig(self.graph, fill='white', outline='white')

    def unflash_stats(self):
        self.hp_label.configure(text_color='#18c020')
        self.hp_bar.configure(progress_color='#18c020')
        self.exp_bar.configure(progress_color='#4890f8')
        self.graph_canvas.itemconfig(self.graph, fill=stat_graph_fill, outline=stat_graph_fill)


class BattleDirector(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.charging = True
        self.base_charge = 0.002
        self.slow_charge = self.base_charge * 0.7
        self.loop = 1

        # get moves
        self.p1 = self.parent.player_move1
        self.p2 = self.parent.player_move2
        self.e1 = self.parent.enemy_move1
        self.e2 = self.parent.enemy_move2

        self.player_speed_mod = 1
        self.enemy_speed_mod = 0.9

    def generate_enemy(self, enemy):  # enemy = tuple (pokemon, lv)
        pty.in_battle = True
        pty.enemy_pokemon = Pokemon(*eval(f'pty.{enemy[0]}'), enemy[1], -1)
        self.parent.enemy_pokemon = CanvasPokemon(self.parent, self.parent.adv_canvas, 'enemy')
        self.parent.enemy_stats.update_stats()
        self.parent.enemy_move1.update_move_box()
        self.parent.enemy_move2.update_move_box()

        self.enemy_encounter()

    def enemy_encounter(self):
        self.parent.player_pokemon.move_to_battle_pos()
        self.parent.enemy_pokemon.enemy_spawn()
        self.parent.route_progress.show_enemy_icon()

    def start_battle(self):
        self.parent.player_move1.move_progressbar.set((random.randrange(20, 50) / 100))
        self.parent.player_move2.move_progressbar.set((random.randrange(0, 30) / 100))
        self.parent.enemy_move1.move_progressbar.set((random.randrange(20, 30) / 100))
        if pty.enemy_pokemon.e_moves[1][0] != '':
            self.parent.enemy_move2.move_progressbar.set((random.randrange(0, 10) / 100))

        self.charging = True

        # move interface elements to screen
        self.parent.enemy_stats.place(x=574)
        self.parent.enemy_moves_frame.place(x=664)
        self.parent.enemy_move2.pack_forget() if pty.enemy_pokemon.e_moves[1][0] == '' else self.parent.enemy_move2.pack()

        # check speed advantage
        speed_difference = ((pty.active_pokemon.spd + pty.active_pokemon.lv) / 2) - ((pty.enemy_pokemon.spd + pty.enemy_pokemon.lv) / 2)

        # player is faster
        if speed_difference >= 0:
            # neutral
            if speed_difference < speed_threshold[0]:
                pass
            # a bit faster
            elif speed_threshold[0] <= speed_difference < speed_threshold[1]:
                self.parent.battle_log.entry_text(f"{pty.active_pokemon.name} is a bit faster!", 'black', True)
                self.player_speed_mod = speed_tiers[0]
            # is faster
            elif speed_threshold[1] <= speed_difference < speed_threshold[2]:
                self.parent.battle_log.entry_text(f"{pty.active_pokemon.name} is faster!", 'black', True)
                self.player_speed_mod = speed_tiers[1]
            # a lot faster
            elif speed_difference >= speed_threshold[2]:
                self.parent.battle_log.entry_text(f"{pty.active_pokemon.name} is a lot faster!", 'black', True)
                self.player_speed_mod = speed_tiers[2]

        # enemy is faster
        else:
            speed_difference = speed_difference * (-1)
            # neutral
            if speed_difference < speed_threshold[0]:
                pass
            # a bit faster
            elif speed_threshold[0] <= speed_difference < speed_threshold[1]:
                self.parent.battle_log.entry_text(f"{pty.enemy_pokemon.name} is a bit faster!", 'black', True)
                self.enemy_speed_mod = speed_tiers[0] * 0.9
            # is faster
            elif speed_threshold[1] <= speed_difference < speed_threshold[2]:
                self.parent.battle_log.entry_text(f"{pty.enemy_pokemon.name} is faster!", 'black', True)
                self.enemy_speed_mod = speed_tiers[1] * 0.9
            # a lot faster
            elif speed_difference >= speed_threshold[2]:
                self.parent.battle_log.entry_text(f"{pty.enemy_pokemon.name} is a lot faster!", 'black', True)
                self.enemy_speed_mod = speed_tiers[2] * 0.9

        # start battle
        self.battling()

    def battling(self):
        if pty.in_battle:
            self.charge_moves()
            self.after(1, self.battling)

    def charge_moves(self):
        if self.charging:
            self.p1.move_progressbar.set(self.p1.move_progressbar.get()
                                         + (self.base_charge * (self.player_speed_mod / pty.active_pokemon.move1[5])))

            self.p2.move_progressbar.set(self.p2.move_progressbar.get()
                                         + (self.slow_charge * (self.player_speed_mod / pty.active_pokemon.move2[5])))

            self.e1.move_progressbar.set(self.e1.move_progressbar.get()
                                         + (self.base_charge * (self.enemy_speed_mod / pty.enemy_pokemon.e_moves[0][5])))
            if pty.enemy_pokemon.e_moves[1][0] != '':
                self.e2.move_progressbar.set(self.e2.move_progressbar.get()
                                             + (self.slow_charge * (self.enemy_speed_mod / pty.enemy_pokemon.e_moves[1][5])))


            conditions = [self.p1.move_progressbar.get() == 1, (self.p2.move_progressbar.get() == 1),
                               (self.e1.move_progressbar.get() == 1), (self.e2.move_progressbar.get() == 1)]

            if any(conditions):
                self.move_charged(conditions.index(True))

    def move_charged(self, move):
        if move == 0 and pty.active_pokemon.move1[0] != '':
            self.parent.battle_log.used_move(pty.active_pokemon, pty.active_pokemon.move1)
            self.parent.battle_director.charging = False

            self.p1.move_progressbar.set(0)
            self.parent.player_pokemon.move_used = 0
            self.parent.player_pokemon.atk()

            MovePopup(self.parent, pty.active_pokemon.move1)

        elif move == 1:
            self.parent.battle_log.used_move(pty.active_pokemon, pty.active_pokemon.move2)
            self.parent.battle_director.charging = False

            self.p2.move_progressbar.set(0)
            self.parent.player_pokemon.move_used = 1
            self.parent.player_pokemon.atk()

            MovePopup(self.parent, pty.active_pokemon.move2)

        elif move == 2:
            self.parent.battle_log.used_move(pty.enemy_pokemon, pty.enemy_pokemon.e_moves[0])
            self.parent.battle_director.charging = False

            self.e1.move_progressbar.set(0)
            self.parent.enemy_pokemon.move_used = 2
            self.parent.enemy_pokemon.atk()

            MovePopup(self.parent, pty.enemy_pokemon.e_moves[0])

        elif move == 3:
            self.parent.battle_log.used_move(pty.enemy_pokemon, pty.enemy_pokemon.e_moves[1])
            self.parent.battle_director.charging = False

            self.e2.move_progressbar.set(0)
            self.parent.enemy_pokemon.move_used = 3
            self.parent.enemy_pokemon.atk()

            MovePopup(self.parent, pty.enemy_pokemon.e_moves[1])

    def deal_damage(self, move_used):
        # get attacker info
        attacker, attacked, actor = 0, 0, 0
        damage_mod = 1

        if move_used == 0:
            attacker = pty.active_pokemon
            attacked = pty.enemy_pokemon
            actor = 'player'
            crit_color = player_color
            bad_color = enemy_color

        if move_used == 1:
            attacker = pty.active_pokemon
            attacked = pty.enemy_pokemon
            actor = 'player'
            crit_color = player_color
            bad_color = enemy_color

        if move_used == 2:
            attacker = pty.enemy_pokemon
            attacked = pty.active_pokemon
            actor = 'enemy'
            crit_color = enemy_color
            bad_color = player_color
            damage_mod = enemy_damage_mod

        if move_used == 3:
            attacker = pty.enemy_pokemon
            attacked = pty.active_pokemon
            actor = 'enemy'
            crit_color = enemy_color
            bad_color = player_color
            damage_mod = enemy_damage_mod

        # get move info
        attack_used = move_used
        if move_used == 0: attack_used = pty.active_pokemon.move1
        elif move_used == 1: attack_used = pty.active_pokemon.move2
        elif move_used == 2: attack_used = pty.enemy_pokemon.e_moves[0]
        elif move_used == 3: attack_used = pty.enemy_pokemon.e_moves[1]

        # check for hit chance
        rng = random.randint(0, 100)
        # attack hit
        popup_coords = damage_popup_player if actor == 'player' else damage_popup_enemy
        if (attack_used[3] - attacked.evasion) > rng:
            # check for critical hit
            crit = 1
            if (attack_used[4]) + attacker.skill > rng:
                # crit
                self.parent.battle_log.entry_text('A critical hit!', crit_color, False)
                crit = 1.3

            # check for affinity
            if attacked.affinities[attack_used[1] + 1] > 1:
                self.parent.battle_log.entry_text("It's super effective!", crit_color, False)
            elif attacked.affinities[attack_used[1] + 1] < 1:
                self.parent.battle_log.entry_text("It's not very effective...", bad_color, False)

            # Deal damage
            random_mod = round(random.uniform(0.8, 1.2), 2)

            damage_dealt = round(
                (((attack_used[2] * ((attacker.atk + attacker.lv) / 2)) * attacked.affinities[attack_used[1] + 1]) * random_mod) * damage_mod
            )

            attacked.cur_hp -= damage_dealt

            # Damage pop-up
            DamagePopup(self.parent.adv_canvas, damage_dealt, attack_used[1], popup_coords)

            if move_used == 0 or move_used == 1:
                self.parent.enemy_pokemon.hurt()
                self.parent.enemy_stats.update_hp()
                pty.damage_dealt += damage_dealt
            else:
                self.parent.player_pokemon.hurt()
                self.parent.player_stats.update_hp()
                pty.damage_taken += damage_dealt

        # attack miss
        else:
            self.parent.battle_log.entry_text('Attack missed!', bad_color, False)
            if move_used == 0 or move_used == 1:
                self.parent.enemy_pokemon.dodge()
            else:
                self.parent.player_pokemon.dodge()

    def end_battle(self):
        self.charging = False
        self.after(1300, self.restart_adv)

    def restart_adv(self):
        self.parent.player_pokemon.move_to_adv_pos()
        self.parent.player_move1.move_progressbar.set(0)
        self.parent.player_move2.move_progressbar.set(0)
        self.parent.enemy_move1.move_progressbar.set(0)
        self.parent.enemy_move2.move_progressbar.set(0)

        self.player_speed_mod = 1
        self.enemy_speed_mod = 0.9

        # hide interface elements
        self.parent.enemy_stats.place(x=1660)
        self.parent.enemy_moves_frame.place(x=1649)
        self.parent.route_progress.hide_enemy_icon()


class BattleLog(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=280, corner_radius=0)
        self.log = []
        self.line_color = True
        self.pack_propagate(False)
        self.max_lines = 10

        self.clear_log()

    def entry_text(self, text, color, new_line):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        my_font = ctk.CTkFont(family=poke_font, size=16)
        if new_line:
            new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
            line_color = log_line1 if self.line_color else log_line2
            self.line_color = not self.line_color
        else:
            new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
            line_color = log_line2 if self.line_color else log_line1
            ctk.CTkLabel(new_log, text=f'          ', anchor='n', text_color=line_color,
                         font=my_font).pack(side='left')

        # create pokemon name label and get color
        # color = color

        ctk.CTkLabel(new_log, text=f'  {text}', anchor='w', text_color=color, font=my_font).pack(side='left')

        self.log.append(new_log)

        # new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def used_move(self, pokemon, move):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
        self.line_color = not self.line_color
        my_font = ctk.CTkFont(family=poke_font, size=16)

        # create pokemon name label and get color
        color = player_color if pokemon == pty.active_pokemon else enemy_color

        ctk.CTkLabel(new_log, text=f'  {pokemon.name}', anchor='w', text_color=color, font=my_font).pack(side='left')

        # create "used" text label
        ctk.CTkLabel(new_log, text=' used ', anchor='w', text_color=log_color, font=my_font).pack(side='left')

        # create move name label
        ctk.CTkLabel(new_log, text=f'{move[0]}!', anchor='w', text_color=type_colors[move[1]][0], font=my_font).pack(side='left')

        self.log.append(new_log)

        new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def pokemon_fainted(self, pokemon):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        new_log.configure(fg_color=log_line2 if self.line_color else log_line1)
        line_color = log_line2 if self.line_color else log_line1
        # self.line_color = not self.line_color
        my_font = ctk.CTkFont(family=poke_font, size=16)

        # create pokemon name label and get color
        color = enemy_color if pokemon == pty.active_pokemon else player_color

        ctk.CTkLabel(new_log, text=f'            {pokemon.name}', anchor='n', text_color=color, font=my_font).pack(side='left')

        # create "fainted" label
        ctk.CTkLabel(new_log, text=' fainted!', anchor='n', text_color=color, font=my_font).pack(side='left')

        self.log.append(new_log)

        new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def pokemon_lv_up(self, mon):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
        line_color = log_line1 if self.line_color else log_line2
        self.line_color = not self.line_color
        my_font = ctk.CTkFont(family=poke_font, size=16)

        # create pokemon name label and get color
        # ctk.CTkLabel(new_log, text=f'     {pty.active_pokemon.name}', anchor='n', text_color=line_color, font=my_font).pack(side='left')
        ctk.CTkLabel(new_log, text=f'  {mon.name}', anchor='w', text_color=player_color, font=my_font).pack(side='left')

        # create "used" label
        ctk.CTkLabel(new_log, text=f' grew to level {mon.lv}!', anchor='w', text_color=log_color, font=my_font).pack(side='left')

        self.log.append(new_log)

        new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def pokemon_learned_move(self, mon, move):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
        line_color = log_line1 if self.line_color else log_line2
        self.line_color = not self.line_color
        my_font = ctk.CTkFont(family=poke_font, size=16)

        # create pokemon name label and get color
        # ctk.CTkLabel(new_log, text=f'     {pty.active_pokemon.name}', anchor='n', text_color=line_color, font=my_font).pack(side='left')
        ctk.CTkLabel(new_log, text=f'  {mon.name}', anchor='w', text_color=player_color, font=my_font).pack(side='left')

        # create "learned" label
        ctk.CTkLabel(new_log, text=f' learned ', anchor='w', text_color=log_color, font=my_font).pack(side='left')

        # create move name label
        ctk.CTkLabel(new_log, text=move[0], anchor='w', text_color=type_colors[move[1]][0], font=my_font).pack(side='left')

        self.log.append(new_log)

        new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def pokemon_evolved(self, old_pokemon, new_pokemon):
        # create frame for storing labels
        new_log = ctk.CTkFrame(self, width=200, height=28, corner_radius=0)
        new_log.configure(fg_color=log_line1 if self.line_color else log_line2)
        self.line_color = not self.line_color
        my_font = ctk.CTkFont(family=poke_font, size=16)

        # create pokemon name label and get color
        color = player_color

        ctk.CTkLabel(new_log, text=f'  {old_pokemon.name}', anchor='w', text_color=color, font=my_font).pack(side='left')

        # create "used" text label
        ctk.CTkLabel(new_log, text=' evolved into ', anchor='w', text_color=log_color, font=my_font).pack(side='left')

        # create move name label
        ctk.CTkLabel(new_log, text=f'{new_pokemon.name}!', anchor='w', text_color=color, font=my_font).pack(side='left')

        self.log.append(new_log)

        new_log.pack_propagate(False)
        new_log.pack(fill='x', side='top')

        if len(self.log) > self.max_lines:
            # del self.log[0]
            self.log[0].pack_forget()
            self.log.pop(0)

    def clear_log(self):
        for child in self.winfo_children():
            child.destroy()

        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)
        self.entry_text('', 'blue', True)


class PokeSwitcher(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color)
        self.parent = parent

        icon1 = PhotoImage(file=f'Images/Icons/{pty.party["slot1"].dex}.png')
        icon2 = PhotoImage(file=f'Images/Icons/{pty.party["slot2"].dex}.png')
        icon3 = PhotoImage(file=f'Images/Icons/{pty.party["slot3"].dex}.png')
        icon4 = PhotoImage(file=f'Images/Icons/{pty.party["slot4"].dex}.png')
        icon5 = PhotoImage(file=f'Images/Icons/{pty.party["slot5"].dex}.png')
        icon6 = PhotoImage(file=f'Images/Icons/{pty.party["slot6"].dex}.png')

        self.button_ps_1 = self.create_party_button(pty.party['slot1'], icon1)
        self.button_ps_2 = self.create_party_button(pty.party['slot2'], icon2)
        self.button_ps_3 = self.create_party_button(pty.party['slot3'], icon3)
        self.button_ps_4 = self.create_party_button(pty.party['slot4'], icon4)
        self.button_ps_5 = self.create_party_button(pty.party['slot5'], icon5)
        self.button_ps_6 = self.create_party_button(pty.party['slot6'], icon6)

        # layout
        self.button_ps_1.grid(row=0, column=0, padx=0.5, pady=0.5)
        self.button_ps_2.grid(row=0, column=1, padx=0.5, pady=0.5)
        self.button_ps_3.grid(row=1, column=0, padx=0.5, pady=0.5)
        self.button_ps_4.grid(row=1, column=1, padx=0.5, pady=0.5)
        self.button_ps_5.grid(row=2, column=0, padx=0.5, pady=0.5)
        self.button_ps_6.grid(row=2, column=1, padx=0.5, pady=0.5)

    def create_party_button(self, party_slot, dex_image):
        return ctk.CTkButton(self,
                             command=lambda: self.switch_pokemon(party_slot),
                             text='',
                             image=dex_image,
                             width=40,
                             height=40,
                             corner_radius=0,
                             fg_color=button_color,
                             hover_color=hover_color,
                             )

    def initialize_buttons(self):
        for child in self.winfo_children():
            child.destroy()

        icon1 = PhotoImage(file=f'Images/Icons/{pty.party["slot1"].dex}.png')
        icon2 = PhotoImage(file=f'Images/Icons/{pty.party["slot2"].dex}.png')
        icon3 = PhotoImage(file=f'Images/Icons/{pty.party["slot3"].dex}.png')
        icon4 = PhotoImage(file=f'Images/Icons/{pty.party["slot4"].dex}.png')
        icon5 = PhotoImage(file=f'Images/Icons/{pty.party["slot5"].dex}.png')
        icon6 = PhotoImage(file=f'Images/Icons/{pty.party["slot6"].dex}.png')

        self.button_ps_1 = self.create_party_button(pty.party['slot1'], icon1)
        self.button_ps_2 = self.create_party_button(pty.party['slot2'], icon2)
        self.button_ps_3 = self.create_party_button(pty.party['slot3'], icon3)
        self.button_ps_4 = self.create_party_button(pty.party['slot4'], icon4)
        self.button_ps_5 = self.create_party_button(pty.party['slot5'], icon5)
        self.button_ps_6 = self.create_party_button(pty.party['slot6'], icon6)

        # layout
        self.button_ps_1.grid(row=0, column=0, padx=0.5, pady=0.5)
        self.button_ps_2.grid(row=0, column=1, padx=0.5, pady=0.5)
        self.button_ps_3.grid(row=1, column=0, padx=0.5, pady=0.5)
        self.button_ps_4.grid(row=1, column=1, padx=0.5, pady=0.5)
        self.button_ps_5.grid(row=2, column=0, padx=0.5, pady=0.5)
        self.button_ps_6.grid(row=2, column=1, padx=0.5, pady=0.5)

    def switch_pokemon(self, party_slot):
        if party_slot.name != '':
            if not pty.in_battle:
                pty.active_pokemon = party_slot
                self.parent.player_pokemon.display_pokemon()
                self.parent.player_stats.update_stats()
                self.parent.player_move1.update_move_box()
                self.parent.player_move2.update_move_box()
                # update icon in route progress
                self.parent.route_progress.update_player_icon()

            # if in battle
            else:
                if self.parent.battle_director.charging or pty.active_pokemon.name == '':
                    # if pty.active_pokemon.name == '':
                    #     self.parent.battle_director.charging = True

                    if party_slot.hp > 1:
                        pty.active_pokemon = party_slot
                        self.parent.player_pokemon.display_pokemon()
                        self.parent.player_stats.update_stats()
                        self.parent.player_move1.update_move_box()
                        self.parent.player_move2.update_move_box()

                        self.parent.adv_canvas.coords(self.parent.player_pokemon.displayed_pokemon, player_battle_pos, player_adv_pos[1])

                        self.parent.player_move1.move_progressbar.set((random.randrange(0, 20) / 100))
                        self.parent.player_move2.move_progressbar.set((random.randrange(0, 20) / 100))
                        self.parent.battle_director.charging = True

                        # update icon in route progress
                        self.parent.route_progress.update_player_icon()

    def update_party_button(self, party_slot, dex_image):
        pass

    def disable_buttons(self):
        self.button_ps_1.configure(state='disabled')
        self.button_ps_2.configure(state='disabled')
        self.button_ps_3.configure(state='disabled')
        self.button_ps_4.configure(state='disabled')
        self.button_ps_5.configure(state='disabled')
        self.button_ps_6.configure(state='disabled')


class DamagePopup(ctk.CTkFrame):
    def __init__(self, parent, damage, dmg_type, coords):
        super().__init__(parent)
        self.parent = parent
        self.loop = 0

        self.dmg_type = dmg_type
        self.my_font = ctk.CTkFont(family='Arial', size=36, weight='bold')
        self.pop_up = self.parent.create_text(coords, text=damage, fill=type_colors[dmg_type][0], font=self.my_font)

        self.dmg_timer()
        self.float_up()
        self.label_flash()

    def dmg_timer(self):
        self.after(900, self.dmg_del)

    def float_up(self):
        self.parent.move(self.pop_up, 0, -0.025)
        self.after(1, self.float_up)

    def label_flash(self):
        if self.loop % 2:
            # self.parent.itemconfig(self.pop_up, fill='white')
            self.parent.itemconfig(self.pop_up, fill=type_colors[self.dmg_type][0])
        else:
            # self.parent.itemconfig(self.pop_up, fill=type_colors[self.dmg_type])
            self.parent.itemconfig(self.pop_up, fill='white')
        self.loop += 1

        if self.loop < 6:
            self.after(120, self.label_flash)
        else:
            self.parent.itemconfig(self.pop_up, fill=type_colors[self.dmg_type][0])

    def dmg_del(self):
        self.parent.delete(self.pop_up)
        self.destroy()


class MovePopup(ctk.CTkFrame):
    def __init__(self, parent, move_used):
        super().__init__(parent)
        self.parent = parent
        self.move_used = move_used
        self.my_font = ctk.CTkFont(family='Arial', size=18, weight='bold')

        self.label_bg = ctk.CTkLabel(self,
                                     text=move_used[0],
                                     text_color=type_colors[self.move_used[1]][1],
                                     font=self.my_font,
                                     bg_color=type_colors[self.move_used[1]][1],
                                     padx=12, pady=10,
                                     )

        self.move_label = ctk.CTkLabel(self,
                                       text=move_used[0],
                                       text_color=type_colors[self.move_used[1]][1],
                                       font=self.my_font,
                                       bg_color=type_colors[self.move_used[1]][0],
                                       padx=8, pady=6,
                                       )

        self.label_bg.place(x=0, y=0)
        self.move_label.place(x=4, y=4)

        self.parent.app.update()
        self.configure(height=self.label_bg.winfo_height(), width=self.label_bg.winfo_width())
        self.place(x=560, y=183, anchor='center')

        self.self_timer()

    def self_timer(self):
        self.after(1200, self.self_del)

    def self_del(self):
        self.destroy()

