from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import pyglet.font
from PIL import Image, ImageTk
from pyglet import font

from settings import *
from status_widgets import *
from adventure_widgets import *
from pokemon_select import *
from route_select import *
from title_screen import *
import pokedex as dex
from results import *
from pokemon_list import *
import party as pty
from move_list import *
from type_list import *
from gacha import *

pyglet.font.add_file('Images/pokemon-gen-4-regular.ttf')


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=background_color)
        self.title("Phytonmon")
        self.geometry('1280x720')
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        self.resizable(width=False, height=False)

        self.iconbitmap("Images/icon.ico")
        self.game_screen = ''

        self.title_screen = TitleScreen(self)
        self.pokemon_selector = PokeSelectScreen(self)
        # self.pokemon_prize = PokePrizeScreen(self)
        self.route_select = RouteSelectScreen(self)
        self.status_screen = ctk.CTkFrame(self)
        self.adv_screen = ctk.CTkFrame(self)
        self.results_screen = ResultsScreen(self)
        self.pokedex_screen = dex.PokedexScreen(self)
        self.start_adventure()
        self.change_screen('title')

        self.mainloop()

    def change_screen(self, new_state):
        if new_state == 'status':
            if not pty.in_battle:
                self.forget_all()
                self.status_screen.pack()
                self.game_screen = 'status'
                self.status_screen.party_buttons.initialize_buttons()
                self.status_screen.display_pokemon(pty.active_pokemon)

        if new_state == 'adv':
            if not pty.in_battle:
                self.forget_all()
                self.adv_screen.pack(expand=True, fill='y')
                self.game_screen = 'adv'
                self.adv_screen.player_move1.update_move_box()
                self.adv_screen.player_move2.update_move_box()
                self.adv_screen.poke_switcher.switch_pokemon(pty.party[f'slot{pty.active_pokemon.party_index}'])
                self.adv_screen.route_progress.stepping()

        if new_state == 'picker':
            self.forget_all()
            self.pokemon_selector.randomize_prizes(6, pty.gacha_level)
            self.pokemon_selector.pack(expand=True, fill='y')
            self.pokemon_selector.party_buttons.initialize_buttons()
            self.pokemon_selector.party_buttons.disable_buttons()
            self.pokemon_selector.selector_status.update_mon(Pokemon(*empty, level=0, party_index=-1))
            self.game_screen = 'picker'

        if new_state == 'route':
            global route_option_number
            self.forget_all()
            # if pty.stages_cleared >= 9: route_option_number = 1
            self.route_select.get_route()
            self.route_select.pack()
            self.route_select.party_buttons.initialize_buttons()
            self.route_select.party_buttons.disable_buttons()
            self.game_screen = 'route'
            self.title_screen.destroy()

        if new_state == 'title':
            pty.in_battle = False
            self.results_screen.clear_party()
            self.title_screen = TitleScreen(self)
            self.forget_all()
            self.title_screen.pack()
            self.game_screen = 'title'

        if new_state == 'results':
            self.forget_all()
            self.results_screen.pack()
            self.game_screen = 'results'

        if new_state == 'pokedex':
            # global pokedex_storage
            dex.pokedex_storage = self.pokedex_screen
            self.forget_all()
            self.pokedex_screen.pack()
            self.game_screen = 'pokedex'

    def start_adventure(self):
        self.forget_all()
        self.adv_screen = AdventureScreen(self)
        self.status_screen = StatusScreen(self)

    def get_prize(self):
        pty.in_battle = False
        self.pokemon_prize.forget()
        self.change_screen('route')

    def new_route(self, new_route):
        self.route_select.forget()
        self.adv_screen.poke_switcher.initialize_buttons()
        self.adv_screen.route_progress.start_route(new_route)
        self.adv_screen.route_progress.stepping()
        self.adv_screen.current_route_label.configure(text=f'Current route: {pty.stages_cleared + 1}')
        self.change_screen('adv')
        self.adv_screen.pack(expand=True, fill='y')

    def forget_all(self):
        for child in self.winfo_children():
            child.forget()


App()
