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
import party as pty
import settings as stg
from gacha import *
import routes as rt
from move_list import *


class ResultsScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=background_color, width=1280, height=720)
        self.parent = parent
        self.result_label = ctk.CTkLabel(self, text='', text_color=text_color, font=(poke_font, 42), anchor='center', width=1280)
        self.lose_string = 'you were defeated'
        self.win_string = 'you are the champion!'
        self.result_label.configure(text=self.win_string)

        self.statistics = Statistics(self)

        self.back_to_title_button = ctk.CTkButton(self,
                                                  text='back to title',
                                                  text_color=button_text_color,
                                                  fg_color=button_color,
                                                  font=poke_font_tuple,
                                                  corner_radius=0,
                                                  command=self.back_to_title,
                                                  )

        # layout
        self.result_label.place(x=0, y=140)
        self.statistics.place(x=500, y=260)
        self.back_to_title_button.place(x=570, y=442)

    def get_results(self, result):
        if result == 'won':
            self.result_label.configure(text=self.win_string)
        else:
            self.result_label.configure(text=self.lose_string)

        self.statistics.stages_cleared_value.configure(text=pty.stages_cleared)
        self.statistics.battles_won_value.configure(text=pty.battles_won)
        self.statistics.battles_lost_value.configure(text=pty.battles_lost)
        self.statistics.damage_dealt_value.configure(text=pty.damage_dealt)
        self.statistics.damage_taken_value.configure(text=pty.damage_taken)

    def back_to_title(self):
        self.clear_party()
        self.parent.change_screen('title')

    def clear_party(self):
        # global picked_starter
        # clear party
        loop = 0
        for key, value in pty.party.items():
            loop += 1
            pty.party[key] = Pokemon(*empty, level=0, party_index=loop)

        # reset statistics
        stg.picked_starter = False
        stg.route_option_number = 2
        pty.battles_won = 0
        pty.party_size = 0
        pty.battles_lost = 0
        pty.damage_dealt = 0
        pty.damage_taken = 0
        pty.stages_cleared = 0
        pty.fainted_mons = 0
        pty.completed_routes = []
        pty.gacha_level = g_pokeball


class Statistics(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=frame_bg_color, width=280, height=152, corner_radius=0)
        self.label_width = 140

        self.stages_cleared_label = ctk.CTkLabel(self, text='stages cleared:', text_color=stat_label_color, width=self.label_width, anchor='e', font=poke_font_tuple)
        self.battles_won_label = ctk.CTkLabel(self, text='battles won:', text_color=stat_label_color, width=self.label_width, anchor='e', font=poke_font_tuple)
        self.battles_lost_label = ctk.CTkLabel(self, text='battles lost:', text_color=stat_label_color, width=self.label_width, anchor='e', font=poke_font_tuple)
        self.damage_dealt_label = ctk.CTkLabel(self, text='damage dealt:', text_color=stat_label_color, width=self.label_width, anchor='e', font=poke_font_tuple)
        self.damage_taken_label = ctk.CTkLabel(self, text='damage taken:', text_color=stat_label_color, width=self.label_width, anchor='e', font=poke_font_tuple)

        self.stages_cleared_value = ctk.CTkLabel(self, text=pty.stages_cleared, text_color=text_color, width=self.label_width, anchor='w', font=poke_font_tuple)
        self.battles_won_value = ctk.CTkLabel(self, text=pty.battles_won, text_color=text_color, width=self.label_width, anchor='w', font=poke_font_tuple)
        self.battles_lost_value = ctk.CTkLabel(self, text=pty.battles_lost, text_color=text_color, width=self.label_width, anchor='w', font=poke_font_tuple)
        self.damage_dealt_value = ctk.CTkLabel(self, text=pty.damage_dealt, text_color=text_color, width=self.label_width, anchor='w', font=poke_font_tuple)
        self.damage_taken_value = ctk.CTkLabel(self, text=pty.damage_taken, text_color=text_color, width=self.label_width, anchor='w', font=poke_font_tuple)

        # layout
        self.stages_cleared_label.place(x=4, y=4)
        self.battles_won_label.place(x=4, y=32)
        self.battles_lost_label.place(x=4, y=60)
        self.damage_dealt_label.place(x=4, y=88)
        self.damage_taken_label.place(x=4, y=116)

        self.stages_cleared_value.place(x=150, y=4)
        self.battles_won_value.place(x=150, y=32)
        self.battles_lost_value.place(x=150, y=60)
        self.damage_dealt_value.place(x=150, y=88)
        self.damage_taken_value.place(x=150, y=116)
