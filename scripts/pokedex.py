from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from settings import *
from status_widgets import *
from adventure_widgets import *
from pokemon_select import *
from route_select import *
from title_screen import *
from results import *
from pokemon_list import *
import party as pty
from move_list import *
from type_list import *
from gacha import *

displayed_pokemon = Pokemon(*empty, level=100, party_index=1)
pokedex_storage = ''


def what(new_mon):
    global displayed_pokemon
    displayed_pokemon = Pokemon(*new_mon, level=100, party_index=1)
    pty.displayed_pokemon = displayed_pokemon
    pokedex_storage.display_pokemon(displayed_pokemon)


class PokedexScreen(ctk.CTkFrame):
    def __init__(self, parent):
        self.bg_color = background_color
        super().__init__(parent, fg_color=self.bg_color, width=1280, height=720)
        self.app = parent
        # variable to store pokemon currently being displayed
        # self.displayed_pokemon = Pokemon(*bulbasaur, level=100, party_index=1)

        # create list of buttons for the pokedex
        self.pokedex_list = PokedexList(self)
        # self.pokedex_list.list_pokemon()

        # status
        self.displayed_sprite = PhotoImage(file='Images/Sprites/0.png')

        # create sprite displayer
        self.poke_canvas = Canvas(self, background=button_color, width=300, height=300, border=0, highlightthickness=0,)
        self.poke_canvas.create_image(0, 0, image=self.displayed_sprite, anchor=NW)

        # create stat frame
        self.stat_frame = StatsFrame(self)
        self.stat_graph = StatsGraph(self)

        # create moves frame
        self.moves_frame = MoveSelector(self)

        # menu buttons
        self.back_button = ctk.CTkButton(self,
                                         command=self.back_to_title,
                                         text='back to title',
                                         corner_radius=0,
                                         width=146,
                                         font=poke_font_tuple,
                                         fg_color=button_color,
                                         text_color=button_text_color,
                                         hover_color=text_color)

        # layout
        self.pokedex_list.place(x=60, y=84)
        self.poke_canvas.place(x=240, y=84)
        self.stat_frame.place(x=540, y=84)
        self.stat_graph.place(x=540, y=155)
        self.moves_frame.place(x=940, y=84)
        self.back_button.place(x=240, y=400)

        self.display_pokemon(displayed_pokemon)

    def display_pokemon(self, new_mon):
        global displayed_pokemon
        if new_mon.name != '':
            # self.displayed_pokemon = new_mon
            displayed_pokemon = new_mon

            # update sprite
            self.displayed_sprite = PhotoImage(file=f'Images/Sprites/{displayed_pokemon.dex}.png')
            self.poke_canvas.create_image(0, 0, image=self.displayed_sprite, anchor=NW)

            # update stats box
            self.stat_frame.name_label.configure(text=displayed_pokemon.name)
            self.stat_frame.level_label.configure(text=f'Lv. {displayed_pokemon.lv}')

            # set hp bar
            self.hp_archive = displayed_pokemon.cur_hp
            self.stat_frame.hp_bar.set(displayed_pokemon.cur_hp / displayed_pokemon.hp)
            self.stat_frame.hp_label.configure(text=f'{int(displayed_pokemon.cur_hp)}')

            # update type icon
            self.type_icon_pillow = Image.open(f'Images/TypeIcons/{displayed_pokemon.type1[1] - 1}.png')
            self.type_icon_pillow = self.type_icon_pillow.resize((self.stat_frame.icon_size, self.stat_frame.icon_size))
            self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
            self.type_icon_sprite = self.stat_frame.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

            self.type2_icon_pillow = Image.open(f'Images/TypeIcons/{displayed_pokemon.type2[1] - 1}.png')
            self.type2_icon_pillow = self.type2_icon_pillow.resize((self.stat_frame.icon_size, self.stat_frame.icon_size))
            self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
            self.type2_icon_sprite = self.stat_frame.type_icon_canvas.create_image(25, 0, image=self.type2_icon, anchor=NW)

            # update stat graph
            self.stat_graph.update_graf(dex=True)

            # update moves frame
            self.moves_frame.update_move_selector(displayed_pokemon, dex=True)

    def back_to_title(self):
        what(empty)
        self.display_pokemon(displayed_pokemon)
        self.app.change_screen('title')


class PokedexList(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        self.parent = parent
        self.dex_width = 130
        super().__init__(parent, width=self.dex_width, height=589, corner_radius=0, border_width=0, fg_color=background_color)
        self.chosen_mon = ''
        self.PI_list = []
        self.icon_list = []
        self.creation_loop = 0

        self.list_pokemon()

    def list_pokemon(self):
        for i in pokedex_list:
            new_icon = Image.open(f'Images/Icons/{i[0]}.png')
            new_icon = new_icon.resize((32, 32))
            # new_icon = PhotoImage(file=f'Images/Icons/{i[0]}.png')
            new_icon = ImageTk.PhotoImage(new_icon)
            self.icon_list.append(new_icon)
            exec(f"""{i[1]}_button = ctk.CTkButton(self,
                          width=self.dex_width,
                          text=f'{i[1]}',
                          image=self.icon_list[self.creation_loop],
                          compound = 'left',
                          anchor='w',
                          text_color=button_text_color,
                          font=poke_font_tuple,
                          fg_color=button_color,
                          hover_color=hover_color,
                          corner_radius=0,
                          command=lambda: what({i})
                          )""")
            exec(f"{i[1]}_button.pack(pady=1)")
            self.creation_loop += 1

    def change_displayed_mon(self, new_mon):
        wtf = new_mon
        # self.parent.displayed_pokemon = Pokemon(*new_mon, level=100, party_index=1),
        self.parent.displayed_pokemon = Pokemon(*wtf, level=100, party_index=1)
        self.parent.display_pokemon(self.parent.displayed_pokemon)

    def what(self, new_mon):
        global displayed_pokemon
        displayed_pokemon = new_mon
