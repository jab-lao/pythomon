import copy
from tkinter import *
import customtkinter as ctk
from settings import *
import party as pty
from pokemon_list import *
from adventure_widgets import *
from move_list import *
from gacha import *
import settings as stg
import random


class PokeSelectScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color, width=1280, height=720)
        self.parent = parent
        self.starter_list = []
        self.prize_list = []
        self.gacha_rolls = 0
        self.rng_memory = []
        self.poke_level = 5

        # title label
        self.title = ctk.CTkLabel(self, text='Choose your starter Pokémon', font=(poke_font, 24), text_color=text_color)

        # frame for gacha buttons
        self.starters_frame = ctk.CTkFrame(self, fg_color=background_color)
        self.prizes_frame = ctk.CTkFrame(self, fg_color=background_color)

        # party buttons
        self.party_buttons = PokeSwitcher(self)
        self.party_buttons.initialize_buttons()
        self.party_buttons.disable_buttons()

        # back to menu button
        self.back_button = ctk.CTkButton(self, command=self.back_to_title, text='exit game', corner_radius=0, width=146, font=poke_font_tuple, fg_color=button_color, text_color=button_text_color, hover_color=text_color)

        # status frame
        self.selector_status = SelectorStatus(self)
        self.move_list = SelectorMoves(self)

        self.randomize_starters()

        # layout
        self.title.place(x=286, y=80)
        self.party_buttons.place(x=60, y=159)
        self.starters_frame.place(x=280, y=155)
        self.selector_status.place(x=600, y=160)
        self.move_list.place(x=960, y=160)
        self.back_button.place(x=61, y=390)

    def randomize_starters(self):
        self.rng_memory.clear()

        starter_pool_dict = copy.deepcopy(g_starters)
        starter_pool_common = list(starter_pool_dict[0].values())
        starter_pool_uncommon = list(starter_pool_dict[1].values())
        starter_pool_rare = list(starter_pool_dict[2].values())

        loop = 1

        # # randomize pokemon pulls
        for i in range(starter_poke_number):
            # guarantee uncommon roll
            if loop == round(starter_poke_number / 2):
                rng = common_starter_rng + 2
            else:
                rng = random.randint(0, 100)
            loop += 1

            # Rolled common pokemon
            if rng <= common_starter_rng:
                # check if common pool is empty
                if len(starter_pool_common) != 0:
                    pulled_mon = random.choice(starter_pool_common)  # pick randomly from gacha pull
                    self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    starter_pool_common.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                else:
                    self.starter_list.append(empty)

            # Rolled uncommon pokemon
            elif common_starter_rng < rng < rare_starter_rng:
                # check if uncommon pool is empty
                if len(starter_pool_uncommon) != 0:
                    pulled_mon = random.choice(starter_pool_uncommon)  # pick randomly from gacha pull
                    self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    starter_pool_uncommon.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                else:
                    if len(starter_pool_common) != 0:
                        pulled_mon = random.choice(starter_pool_common)  # pick randomly from gacha pull
                        self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                        starter_pool_common.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                    else:
                        self.starter_list.append(empty)

            # Rolled rare pokemon
            elif rare_pool_rng <= rng:
                # check if rare pool is empty
                if len(starter_pool_rare) != 0:
                    pulled_mon = random.choice(starter_pool_rare)  # pick randomly from gacha pull
                    self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    starter_pool_rare.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                else:
                    if len(starter_pool_uncommon) != 0:
                        pulled_mon = random.choice(starter_pool_uncommon)  # pick randomly from gacha pull
                        self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                        starter_pool_uncommon.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                    else:
                        if len(starter_pool_common) != 0:
                            pulled_mon = random.choice(starter_pool_common)  # pick randomly from gacha pull
                            self.starter_list.append(pulled_mon)  # append pulled pokemon to the prize list
                            starter_pool_common.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool

                        else:
                            self.starter_list.append(empty)

        # create icons
        for i in range(starter_poke_number):
            exec(f"self.icon{i} = PhotoImage(file=f'Images/Icons/{self.starter_list[i][0]}.png')")

            # create buttons
            exec(f"self.button{i} = self.create_party_button(self.icon{i}, Pokemon(*self.starter_list[{i}], level={self.poke_level}, party_index={i + 1}), self.starters_frame)")

            # layout
            exec(f"self.button{i}.grid(row={gacha_grid_coords[i][0]}, column={gacha_grid_coords[i][1]}, padx=5, pady=5)")

    def randomize_prizes(self, gacha_rolls, gacha_pool):
        self.gacha_rolls = gacha_rolls
        self.prize_list.clear()
        prize_pool_dict = copy.deepcopy(gacha_pool)
        prize_pool_common = list(prize_pool_dict[0].values())
        prize_pool_uncommon = list(prize_pool_dict[1].values())
        prize_pool_rare = list(prize_pool_dict[2].values())
        prize_pool_legendary = list(prize_pool_dict[3].values())

        # get gacha level
        if pty.stages_cleared >= 2:
            self.poke_level = 16
        if pty.stages_cleared >= 4:
            self.poke_level = 30
        if pty.stages_cleared >= 7:
            self.poke_level = 40
        if pty.stages_cleared > 7:
            self.poke_level = 45

        # # randomize pokemon pulls
        for i in range(gacha_rolls):
            rng = random.randint(0, 100)

            # Rolled common pokemon
            if rng <= common_pool_rng:
                # check if common pool is empty
                if len(prize_pool_common) != 0:
                    pulled_mon = random.choice(prize_pool_common)  # pick randomly from gacha pull
                    self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    prize_pool_common.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                else:
                    self.prize_list.append(empty)

            # Rolled uncommon pokemon
            elif common_pool_rng < rng < rare_pool_rng:
                # check if uncommon pool is empty
                if len(prize_pool_uncommon) != 0:
                    pulled_mon = random.choice(prize_pool_uncommon)  # pick randomly from gacha pull
                    self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    prize_pool_uncommon.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                else:
                    if len(prize_pool_common) != 0:
                        pulled_mon = random.choice(prize_pool_common)  # pick randomly from gacha pull
                        self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                        prize_pool_common.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                    else:
                        self.prize_list.append(empty)

            # Rolled rare pokemon
            elif rare_pool_rng <= rng < legendary_pool_rng:
                # check if rare pool is empty
                if len(prize_pool_rare) != 0:
                    pulled_mon = random.choice(prize_pool_rare)  # pick randomly from gacha pull
                    self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    prize_pool_rare.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                else:
                    if len(prize_pool_uncommon) != 0:
                        pulled_mon = random.choice(prize_pool_uncommon)  # pick randomly from gacha pull
                        self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                        prize_pool_uncommon.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                    else:
                        if len(prize_pool_common) != 0:
                            pulled_mon = random.choice(prize_pool_common)  # pick randomly from gacha pull
                            self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                            prize_pool_common.remove(
                                pulled_mon)  # remove pulled pokemon from the local scope prize pool
                        else:
                            self.prize_list.append(empty)

            # Rolled legendary pokemon
            elif rng >= legendary_pool_rng:
                # check if legendary pool is empty
                if len(prize_pool_legendary) != 0:
                    pulled_mon = random.choice(prize_pool_legendary)  # pick randomly from gacha pull
                    self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                    prize_pool_legendary.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                else:
                    if len(prize_pool_rare) != 0:
                        pulled_mon = random.choice(prize_pool_rare)  # pick randomly from gacha pull
                        self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                        prize_pool_rare.remove(pulled_mon)  # remove pulled pokemon from the local scope prize pool
                    else:
                        if len(prize_pool_uncommon) != 0:
                            pulled_mon = random.choice(prize_pool_uncommon)  # pick randomly from gacha pull
                            self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                            prize_pool_uncommon.remove(
                                pulled_mon)  # remove pulled pokemon from the local scope prize pool
                        else:
                            if len(prize_pool_common) != 0:
                                pulled_mon = random.choice(prize_pool_common)  # pick randomly from gacha pull
                                self.prize_list.append(pulled_mon)  # append pulled pokemon to the prize list
                                prize_pool_common.remove(
                                    pulled_mon)  # remove pulled pokemon from the local scope prize pool
                            else:
                                self.prize_list.append(empty)

        # create icons
        for i in range(gacha_rolls):
            exec(f"self.icon{i} = PhotoImage(file=f'Images/Icons/{self.prize_list[i][0]}.png')")

            # create buttons
            exec(f"self.button{i} = self.create_party_button(self.icon{i}, Pokemon(*self.prize_list[{i}], level={self.poke_level}, party_index={i + 1}), self.prizes_frame)")

            # layout
            exec(f"self.button{i}.grid(row={gacha_grid_coords[i][0]}, column={gacha_grid_coords[i][1]}, padx=5, pady=5)")

    def create_party_button(self, icon, new_pokemon, frame):
        return ctk.CTkButton(frame,
                             command=lambda: self.selector_status.update_mon(new_pokemon),
                             text='',
                             image=icon,
                             width=40,
                             height=40,
                             corner_radius=0,
                             fg_color=button_color,
                             hover_color=hover_color,
                             )

    def picked_pokemon(self, new_pokemon):
        # global picked_starter
        if self.selector_status.selected_mon.name != '':
            # pick starter and show prizes
            if not stg.picked_starter:
                pty.party['slot6'] = new_pokemon
                pty.active_pokemon = new_pokemon
                remove_from_pools(new_pokemon)

                # update statistics
                pty.pokemon_obtained.append(self.selector_status.selected_mon.dex)

                pty.sort_party()
                self.party_buttons.initialize_buttons()

                self.show_prizes()

                self.selector_status.selected_mon = Pokemon(*empty, level=0, party_index=1)
                self.selector_status.update_mon(self.selector_status.selected_mon)

                pty.party_size += 1
                stg.picked_starter = True

            # pick prize and start adventure
            else:
                pty.party['slot6'] = new_pokemon
                remove_from_pools(new_pokemon)
                pty.party_size += 1
                pty.sort_party()

                # update statistics
                pty.pokemon_obtained.append(self.selector_status.selected_mon.dex)

                self.parent.start_adventure()
                self.parent.change_screen('route')

        else:
            pass

    def show_prizes(self):
        self.starters_frame.place_forget()
        self.randomize_prizes(gacha_pull_number, g_pokeball)
        self.prizes_frame.place(x=280, y=155)
        self.title.configure(text='Choose your new partner!')

    def disable_prizes(self):
        # self.button_ps_1.configure(state='disabled')
        for i in range(self.gacha_rolls):
            eval(f'self.button{i}.configure(state="disabled")')

    def back_to_title(self):
        self.parent.change_screen('title')


class SelectorStatus(ctk.CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        self.bg_color = frame_bg_color
        super().__init__(parent, height=430, width=320, corner_radius=0, fg_color=frame_bg_color)
        self.selected_mon = Pokemon(*empty, level=0, party_index=1)

        # canvas for pokemon sprite
        self.sprite_canvas = Canvas(self, width=300, height=300, bg=self.bg_color, border=0, highlightthickness=0)
        self.poke_sprite = PhotoImage(file='Images/Sprites/1.png')

        # pokemon name label
        self.poke_name_label = ctk.CTkLabel(self, text='', width=100, anchor='w', text_color=text_color)

        # create types canvas
        self.type_icon_pillow = Image.open('Images/TypeIcons/-1.png')
        self.type_icon_pillow = self.type_icon_pillow.resize((22, 22))
        self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
        self.type_icon_canvas = Canvas(self, width=((22 * 2) + 5), height=22, border=0,
                                       highlightthickness=0, bg=self.bg_color)
        self.type_icon_sprite = self.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

        self.type2_icon_pillow = Image.open(f'Images/TypeIcons/-1.png')
        self.type2_icon_pillow = self.type2_icon_pillow.resize((22, 22))
        self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
        self.type2_icon_sprite = self.type_icon_canvas.create_image(0, 25, image=self.type2_icon, anchor=NW)

        # create stat graph
        self.graph_canvas = Canvas(self, width=75, height=75, border=0, highlightthickness=0, bg=self.bg_color)
        self.graph = ''

        # pick pokemon button
        self.pick_button = ctk.CTkButton(self,
                                         command=lambda: self.parent.picked_pokemon(self.selected_mon),
                                         text=f'',
                                         width=110,
                                         height=40,
                                         corner_radius=0,
                                         text_color=button_text_color,
                                         fg_color=button_color,
                                         hover_color=hover_color,
                                         border_width=2
                                         )

        # layout
        self.sprite_canvas.place(x=10, y=10)
        self.poke_name_label.place(x=10, y=320)
        self.type_icon_canvas.place(x=110, y=320)
        self.graph_canvas.place(x=10, y=350)
        self.pick_button.place(x=110, y=365)

    def update_mon(self, new_pokemon):
        updated_mon = new_pokemon
        self.selected_mon = new_pokemon

        # update pokemon sprite
        self.poke_sprite = PhotoImage(file=f'Images/Sprites/{updated_mon.dex}.png')
        self.sprite_canvas.create_image(0, 0, image=self.poke_sprite, anchor=NW)

        # update name label
        self.poke_name_label.configure(text=updated_mon.name, font=poke_font_tuple)

        # update type icon
        self.type_icon_pillow = Image.open(f'Images/TypeIcons/{updated_mon.type1[1] - 1}.png')
        self.type_icon_pillow = self.type_icon_pillow.resize((22, 22))
        self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
        self.type_icon_sprite = self.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

        self.type2_icon_pillow = Image.open(f'Images/TypeIcons/{updated_mon.type2[1] - 1}.png')
        self.type2_icon_pillow = self.type2_icon_pillow.resize((22, 22))
        self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
        self.type2_icon_sprite = self.type_icon_canvas.create_image(25, 0, image=self.type2_icon, anchor=NW)

        # update graph
        self.graph_canvas.delete('all')
        stats_percentage = [
            updated_mon.base_hp / (max_health + min_health),
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

        # configure pick pokemon button
        if updated_mon.name != '':
            self.pick_button.configure(text=f'Choose', font=poke_font_tuple)
        else:
            self.pick_button.configure(text=f'', font=poke_font_tuple)

        # update move list
        self.parent.move_list.list_moves(updated_mon)

    def place_point(self, start, end, percentage):
        return eval(f'{start}+{percentage}*({end}-{start})')


class SelectorMoves(ctk.CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, height=430, width=220, corner_radius=0, fg_color=frame_bg_color)

    def list_moves(self, mon):
        for child in self.winfo_children():
            child.destroy()

        height = 5
        for i in mon.moves:
            MoveBox(self, i).place(x=5, y=height)
            height += 40


class MoveBox(ctk.CTkFrame):
    def __init__(self, parent, move):
        super().__init__(parent, fg_color=frame_bg_color)
        self.icon_canvas = Canvas(self, width=22, height=22, border=0, highlightthickness=0, bg=frame_bg_color)
        self.icon_pillow = Image.open(f'Images/TypeIcons/{move[1] - 1}.png')
        self.icon_pillow = self.icon_pillow.resize((22, 22))
        self.icon_pi = ImageTk.PhotoImage(self.icon_pillow)
        self.icon_sprite = self.icon_canvas.create_image(0, 0, image=self.icon_pi, anchor=NW)

        self.label = ctk.CTkLabel(self, text=move[0], width=160, anchor='w', font=poke_font_tuple, text_color=text_color)

        self.icon_canvas.place(x=5, y=2)
        self.label.place(x=32, y=0)


