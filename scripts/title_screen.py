import threading
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import random
import os
import time

from settings import *
from pokemon_list import *
from status_widgets import *
import settings as stg
import party as pty
import routes as rt
from move_list import *


class TitleScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=1280, height=720, fg_color=background_color)
        self.parent = parent

        # set up list of pokemon sprites
        self.sprite_dir = 'Images/Sprites'
        self.sprite_list = []
        for sprite in os.listdir(self.sprite_dir):
            self.sprite_list.append(sprite)
        self.sprite_list.remove('0.png')

        # sprite canvas
        self.title_canvas = Canvas(self, width=1280, height=300, highlightthickness=0, bg=background_color)
        self.random_sprite = ''
        self.shuffle_sprite()
        self.title_sprite = self.title_canvas.create_image(1290, 0, image=self.random_sprite, anchor='nw')

        # title label
        self.title_label = ctk.CTkLabel(self, text='pythomon', text_color=text_color, font=(poke_font, 112))
        self.credits_label = ctk.CTkLabel(self, text='made by João Adriano Bastos Lao\njoaoadriano.bl@gmail.com\ngithub.com/jab-lao', text_color=text_color, font=poke_font_tuple, justify='right')

        # buttons
        self.new_game_button = ctk.CTkButton(self, text='new game',
                                             corner_radius=0,
                                             font=poke_font_tuple,
                                             fg_color=button_color,
                                             text_color=button_text_color,
                                             hover_color=text_color,
                                             command=self.new_game)
        self.quit_button = ctk.CTkButton(self, text='quit',
                                         corner_radius=0,
                                         font=poke_font_tuple,
                                         fg_color=button_color,
                                         text_color=button_text_color,
                                         hover_color=text_color,
                                         command=lambda: exit())
        self.pokedex_button = ctk.CTkButton(self, text='pokédex',
                                            corner_radius=0,
                                            font=poke_font_tuple,
                                            fg_color=button_color,
                                            text_color=button_text_color,
                                            hover_color=text_color,
                                            command=self.open_pokedex)
        self.hardcore_button = ctk.CTkButton(self, text='hardcore mode',
                                             corner_radius=0,
                                             font=poke_font_tuple,
                                             fg_color=button_color,
                                             text_color=button_text_color,
                                             hover_color=text_color,
                                             command=self.new_game_hardcore)
        self.achievements_button = ctk.CTkButton(self, text='achievements',
                                                 corner_radius=0,
                                                 font=poke_font_tuple,
                                                 fg_color=button_color,
                                                 text_color=button_text_color,
                                                 hover_color=text_color,)

        # layout
        self.title_label.place(x=100, y=70)
        self.title_canvas.place(x=0, y=170)
        self.credits_label.place(x=1000, y=640)

        self.new_game_button.place(x=900, y=300)
        self.hardcore_button.place(x=900, y=332)
        self.pokedex_button.place(x=900, y=364)
        self.achievements_button.place(x=900, y=396)
        self.quit_button.place(x=900, y=428)

    def sprite_move_in(self):
        if self.title_canvas.coords(self.title_sprite)[0] >= 190:
            self.title_canvas.move(self.title_sprite, -2, 0)
            self.title_canvas.after(1, self.sprite_move_in)
        else:
            self.after(3000, self.sprite_move_out)

    def sprite_move_out(self):
        if self.title_canvas.coords(self.title_sprite)[0] >= -200:
            self.title_canvas.move(self.title_sprite, -2, 0)
            self.title_canvas.after(1, self.sprite_move_out)
        else:
            self.title_canvas.coords(self.title_sprite, 1290, 0)
            self.shuffle_sprite()

    def shuffle_sprite(self):
        rng_sprite = random.choice(self.sprite_list)
        self.random_sprite = PhotoImage(file=f'Images/Sprites/{rng_sprite}')
        self.title_sprite = self.title_canvas.create_image(1290, 0, image=self.random_sprite, anchor='nw')
        self.after(600, self.sprite_move_in)

    def new_game(self):
        stg.harcore_mode = False
        self.parent.change_screen('picker')

    def open_pokedex(self):
        self.parent.change_screen('pokedex')

    def new_game_hardcore(self):
        stg.harcore_mode = True
        self.parent.change_screen('picker')



