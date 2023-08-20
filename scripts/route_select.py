import copy
from tkinter import *
import customtkinter as ctk

from settings import *
import party as pty
from pokemon_list import *
from adventure_widgets import *
from move_list import *
from gacha import *
from routes import *
import random


class RouteSelectScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color, width=1280, height=720)
        self.parent = parent
        self.route_list = []
        self.rng_memory = []

        # title label
        self.title = ctk.CTkLabel(self, text='Choose your destination', font=(poke_font, 24), text_color=text_color)

        # frame for gacha buttons
        self.route_frame = ctk.CTkFrame(self, fg_color=background_color)

        # party buttons
        self.party_buttons = PokeSwitcher(self)
        self.party_buttons.disable_buttons()

        # status frame
        self.selector_status = SelectorStatus(self)

        # back to menu button
        self.back_button = ctk.CTkButton(self, command=self.back_to_title, text='exit game', corner_radius=0, width=146, font=poke_font_tuple, fg_color=button_color, text_color=button_text_color, hover_color=text_color)

        # layout
        self.title.place(x=286, y=80)
        self.party_buttons.place(x=60, y=159)
        self.route_frame.place(x=280, y=155)
        self.selector_status.place(x=600, y=160)
        self.back_button.place(x=61, y=390)
        # self.move_list.place(x=960, y=160)

        # self.get_route()

    def get_route(self):
        global route_lv
        global route_option_number
        prev_route_lv = route_lv
        if pty.stages_cleared < 3:
            route_lv = 1
            pty.gacha_level = g_pokeball
        elif 3 <= pty.stages_cleared < 6:
            route_lv = 2
            pty.gacha_level = g_greatball
        elif 6 <= pty.stages_cleared < 9:
            route_lv = 3
            pty.gacha_level = g_ultraball
        elif pty.stages_cleared >= 9:
            # route_option_number = 1
            route_lv = 4

        if prev_route_lv != route_lv:
            pty.completed_routes = []

        self.randomize_routes(eval(f'level_{route_lv}_routes'))

    def randomize_routes(self, new_route):
        global route_option_number
        self.route_list.clear()
        self.rng_memory.clear()
        route_pool = copy.deepcopy(new_route)

        # randomize routes
        # if pty.stages_cleared >= 9: route_option_number = 1
        for i in range(route_option_number):
            while len(self.route_list) != route_option_number:
                rng = random.randint(0, (len(route_pool) - 1))

                if rng in self.rng_memory:
                    continue
                else:
                    self.route_list.append(route_pool[rng])
                    self.rng_memory.append(rng)

        # create buttons
        for i in range(route_option_number):
            # create buttons
            exec(f"self.button{i} = self.create_route_button(self.route_list[i])")

            # layout
            exec(f"self.button{i}.grid(row={gacha_grid_coords[i][0]}, column={gacha_grid_coords[i][1]}, padx=5, pady=5)")

    def create_route_button(self, new_route):
        return ctk.CTkButton(self.route_frame,
                             command=lambda: self.selector_status.update_route(new_route),
                             text=new_route['name'],
                             font=poke_font_tuple,
                             width=140,
                             corner_radius=0,
                             fg_color=button_color,
                             hover_color=hover_color,
                             text_color=button_text_color,
                             border_width=2
                             )

    def picked_route(self, new_route):
        if self.selector_status.selected_route['name'] != 'Empty':
            # destroy previous buttons
            for child in self.winfo_children():
                child.forget()
            pty.completed_routes.append(new_route)
            self.selector_status.selected_route = 'Empty'
            self.selector_status.update_route(empty_route)
            self.parent.new_route(new_route)
        else:
            pass

    def back_to_title(self):
        self.parent.change_screen('title')


class SelectorStatus(ctk.CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        self.bg_color = frame_bg_color
        super().__init__(parent, height=430, width=320, corner_radius=0, fg_color=frame_bg_color)
        self.selected_route = {'name': 'Empty'}

        # canvas for pokemon sprite
        self.sprite_canvas = Canvas(self, width=300, height=300, bg=self.bg_color, border=0, highlightthickness=0)
        self.route_sprite = PhotoImage(file='Images/Routes/Field.png')

        # route name and level labels
        self.route_name_label = ctk.CTkLabel(self, text='', width=100, anchor='w', text_color=text_color)
        self.route_level_label = ctk.CTkLabel(self, text='', width=100, anchor='w', text_color=text_color)

        # pick pokemon button
        self.pick_button = ctk.CTkButton(self,
                                         command=lambda: self.parent.picked_route(self.selected_route),
                                         text=f'',
                                         width=110,
                                         height=40,
                                         corner_radius=0,
                                         text_color=button_text_color,
                                         fg_color=button_color,
                                         hover_color=hover_color,
                                         )

        # layout
        self.sprite_canvas.place(x=10, y=10)
        self.route_name_label.place(x=10, y=320)
        self.route_level_label.place(x=184, y=320)
        # self.type_icon_canvas.place(x=110, y=320)
        # self.graph_canvas.place(x=10, y=350)
        self.pick_button.place(x=110, y=365)

    def update_route(self, new_route):
        updated_route = new_route
        self.selected_route = new_route

        # update pokemon sprite
        self.route_sprite = PhotoImage(file=f'Images/Routes/{updated_route["name"]}.png')
        self.sprite_canvas.create_image(0, 0, image=self.route_sprite, anchor=NW)

        # update labels
        if new_route['name'] == 'Empty':
            self.route_name_label.configure(text='', font=poke_font_tuple)
            self.route_level_label.configure(text='', font=poke_font_tuple)
            self.pick_button.configure(text='', font=poke_font_tuple)

        else:
            self.route_name_label.configure(text=updated_route['name'], font=poke_font_tuple)
            self.pick_button.configure(text=f'Choose', font=poke_font_tuple)

            # route level label, check if final boss
            if route_lv < 9:
                self.route_level_label.configure(text=f'Lv. {route_lv}', font=poke_font_tuple)
            else:
                self.route_level_label.configure(text='', font=poke_font_tuple)

    def place_point(self, start, end, percentage):
        return eval(f'{start}+{percentage}*({end}-{start})')
