from tkinter import *
import customtkinter as ctk

from settings import *
import party as pty
from pokemon_list import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from move_list import *


class StatusScreen(ctk.CTkFrame):
    def __init__(self, parent):
        self.bg_color = background_color
        super().__init__(parent, fg_color=self.bg_color, width=1280, height=720)
        self.app = parent

        # data
        self.displayed_pokemon = Pokemon(*empty, level=0, party_index=6)
        self.displayed_sprite = PhotoImage(file='Images/Sprites/0.png')

        # Create background buttons
        self.party_buttons = PartyButtons(self, self.display_pokemon)

        # create sprite displayer
        self.poke_canvas = Canvas(self, background=button_color, width=300, height=300, border=0, highlightthickness=0,)
        self.poke_canvas.create_image(0, 0, image=self.displayed_sprite, anchor=NW)

        # create stat frame
        self.stat_frame = StatsFrame(self)
        self.stat_graph = StatsGraph(self)

        # create move boxes
        self.move1 = MoveBox(self, 1)
        self.move2 = MoveBox(self, 2)

        self.move_selector = MoveSelector(self)

        # menu buttons
        self.status_screen_button = ctk.CTkButton(self,
                                                  command=lambda: self.app.change_screen('adv'),
                                                  text='back to game',
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
        self.party_buttons.place(x=60, y=159)
        self.poke_canvas.place(x=240, y=159)
        self.stat_frame.place(x=540, y=159)
        self.stat_graph.place(x=540, y=230)

        self.move1.place(x=250, y=469)
        self.move2.place(x=550, y=469)
        self.move_selector.place(x=1300, y=84)

        self.status_screen_button.place(x=61, y=390)
        self.back_button.place(x=61, y=422)

        # Display first mon
        self.display_pokemon(pty.active_pokemon)

    def display_pokemon(self, new_mon):
        if new_mon.name != '':
            self.displayed_pokemon = new_mon

            # update sprite
            self.displayed_sprite = PhotoImage(file=f'Images/Sprites/{self.displayed_pokemon.dex}.png')
            self.poke_canvas.create_image(0, 0, image=self.displayed_sprite, anchor=NW)

            # update stats box
            self.stat_frame.name_label.configure(text=self.displayed_pokemon.name)
            self.stat_frame.level_label.configure(text=f'Lv. {self.displayed_pokemon.lv}')

            # set hp bar
            self.hp_archive = self.displayed_pokemon.cur_hp
            self.stat_frame.hp_bar.set(self.displayed_pokemon.cur_hp / self.displayed_pokemon.hp)
            self.stat_frame.hp_label.configure(text=f'{int(self.displayed_pokemon.cur_hp)}')

            # set exp bar
            self.stat_frame.exp_bar.set(self.displayed_pokemon.exp / self.displayed_pokemon.exp_cap)
            self.exp_bar_archive = self.stat_frame.exp_bar.get()

            # update type icon
            self.type_icon_pillow = Image.open(f'Images/TypeIcons/{self.displayed_pokemon.type1[1] - 1}.png')
            self.type_icon_pillow = self.type_icon_pillow.resize((self.stat_frame.icon_size, self.stat_frame.icon_size))
            self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
            self.type_icon_sprite = self.stat_frame.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

            self.type2_icon_pillow = Image.open(f'Images/TypeIcons/{self.displayed_pokemon.type2[1] - 1}.png')
            self.type2_icon_pillow = self.type2_icon_pillow.resize((self.stat_frame.icon_size, self.stat_frame.icon_size))
            self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
            self.type2_icon_sprite = self.stat_frame.type_icon_canvas.create_image(25, 0, image=self.type2_icon, anchor=NW)

            # update exp bar
            self.stat_frame.exp_bar.set(new_mon.exp / new_mon.exp_cap)

            # update move boxes
            # self.move_frame.move1.move_name.configure(text=new_mon.move1[0])
            # self.move_frame.move1.move_power.configure(text=new_mon.move1[2])
            # self.move_frame.move1.move_acc.configure(text=f'{new_mon.move1[3]}%')
            # self.move_frame.move1.move_crit.configure(text=f'{new_mon.move1[4]}%')
            # self.move_frame.move1.move_charge.configure(text=new_mon.move1[5])
            # self.move1_type = PhotoImage(file=f'Images/TypeIcons/{new_mon.move1[1] - 1}.png')
            # self.move_frame.move1.move_type_canvas.create_image(4, 4, image=self.move1_type, anchor=NW)
            #
            # self.move_frame.move2.move_name.configure(text=new_mon.move2[0])
            # self.move_frame.move2.move_power.configure(text=new_mon.move2[2])
            # self.move_frame.move2.move_acc.configure(text=f'{new_mon.move2[3]}%')
            # self.move_frame.move2.move_crit.configure(text=f'{new_mon.move2[4]}%')
            # self.move_frame.move2.move_charge.configure(text=new_mon.move2[5])
            # self.move2_type = PhotoImage(file=f'Images/TypeIcons/{new_mon.move2[1] - 1}.png')
            # self.move_frame.move2.move_type_canvas.create_image(4, 4, image=self.move2_type, anchor=NW)
            #
            # # update move list
            # self.move_frame.pokemon_moves.clear()
            # for move in new_mon.moves:
            #     self.move_frame.pokemon_moves.append(move[0])
            #
            # self.move_frame.move1_selector.configure(values=self.move_frame.pokemon_moves)
            # self.move_frame.move2_selector.configure(values=self.move_frame.pokemon_moves)

            # update stat graph
            self.stat_graph.update_graf()

            # update move boxes
            self.move1.update_movebox(1)
            self.move2.update_movebox(2)

            self.move_selector.update_move_selector(new_mon)
            if self.move_selector.window_pos == 1:
                self.move_selector.move_out()

    def back_to_title(self):
        self.app.change_screen('title')


class PartyButtons(ctk.CTkFrame):
    def __init__(self, parent, display_pokemon_func):
        super().__init__(parent, fg_color='transparent')

        # Receive "Display Pokemon" method from parent
        self.display_pokemon = display_pokemon_func

        # Import party icons (Temporary: will create an "update party member" function that will do this
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
                             command=lambda: self.display_pokemon(party_slot),
                             text='',
                             image=dex_image,
                             width=40,
                             height=40,
                             corner_radius=0,
                             fg_color=button_color,
                             hover_color=hover_color,)

    def initialize_buttons(self):
        for child in self.winfo_children():
            child.destroy()

        # Import party icons (Temporary: will create an "update party member" function that will do this
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


class StatsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        self.bg_color = frame_bg_color
        super().__init__(parent, fg_color=frame_bg_color, corner_radius=0, width=360)
        self.icon_size = 22

        # create labels
        self.name_label = ctk.CTkLabel(self, text="", width=100, anchor='e', text_color=text_color, font=(poke_font, 16))
        self.level_label = ctk.CTkLabel(self, text="", width=50, anchor='w', text_color=text_color, font=(poke_font, 16))

        # create HP bar
        self.hp_bg = ctk.CTkFrame(self, width=206, height=20, corner_radius=0, fg_color='black')
        self.hp_bar = ctk.CTkProgressBar(self, width=202, height=16, corner_radius=0, progress_color='#18c020', fg_color='#484848')
        self.hp_label = ctk.CTkLabel(self, text='', width=1, anchor='e', text_color='#18c020', font=poke_font_tuple)
        self.hp_archive = 0

        # create exp bar
        self.exp_bar = ctk.CTkProgressBar(self, corner_radius=0, width=75, height=6, progress_color='#4890f8', fg_color='#484848')
        self.exp_bar.set(0)
        self.exp_archive = 0
        self.exp_bar_archive = 0

        # create type canvas
        self.type_icon_pillow = Image.open('Images/TypeIcons/-1.png')
        self.type_icon_pillow = self.type_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type_icon = ImageTk.PhotoImage(self.type_icon_pillow)
        self.type_icon_canvas = Canvas(self, width=((self.icon_size * 2) + 5), height=self.icon_size, border=0, highlightthickness=0, bg=self.bg_color)
        self.type_icon_sprite = self.type_icon_canvas.create_image(0, 0, image=self.type_icon, anchor=NW)

        self.type2_icon_pillow = Image.open(f'Images/TypeIcons/-1.png')
        self.type2_icon_pillow = self.type2_icon_pillow.resize((self.icon_size, self.icon_size))
        self.type2_icon = ImageTk.PhotoImage(self.type2_icon_pillow)
        self.type2_icon_sprite = self.type_icon_canvas.create_image(0, 25, image=self.type2_icon, anchor=NW)

        # create stat graph
        self.graph_canvas = Canvas(self, width=75, height=75, border=0, highlightthickness=0, bg=self.bg_color)
        self.graph = ''

        self.hp_bg.place(x=8, y=8)
        self.hp_bar.place(x=10, y=10)
        self.hp_label.place(x=220, y=4)
        self.exp_bar.place(x=10, y=34)
        self.level_label.place(x=10, y=40)
        self.type_icon_canvas.place(x=170, y=42)
        self.name_label.place(x=65, y=40)
        # self.graph_canvas.place(x=10, y=56)

    def place_point(self, start, end, percentage):
        return eval(f'{start}+{percentage}*({end}-{start})')


class StatsGraph(Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(height=229, width=360, borderwidth=0, highlightthickness=0, bg=frame_bg_color)

        self.empty_points = [
            115, 180,
            115, 180,
            115, 180,
            115, 180,
            115, 180,
        ]

        self.pokemon_stats_graph = self.create_polygon(*self.empty_points, fill='', outline='white')

        self.create_polygon(*stat_graph_max, fill='', outline=stat_label_color)

        # create graph guides
        guide_percentage = [
            (max_health/2) / max_health,
            (max_attack/2) / max_attack,
            (max_skill/2) / max_skill,
            (max_evasion/2) / max_evasion,
            (max_speed/2) / max_speed,
        ]

        guide_points = [
            180, self.place_point(135, 66, guide_percentage[0]),
            self.place_point(180, 241, guide_percentage[1]), self.place_point(135, 116, guide_percentage[1]),
            self.place_point(180, 221, guide_percentage[2]), self.place_point(135, 188, guide_percentage[2]),
            self.place_point(180, 139, guide_percentage[3]), self.place_point(135, 188, guide_percentage[3]),
            self.place_point(180, 118, guide_percentage[4]), self.place_point(135, 116, guide_percentage[4]),
        ]

        self.create_polygon(*guide_points, fill='', outline=graph_guide_color)
        self.create_line((180, 136), (180, 66), fill=graph_guide_color)
        self.create_line((180, 136), (241, 116), fill=graph_guide_color)
        self.create_line((180, 136), (221, 188), fill=graph_guide_color)
        self.create_line((180, 136), (139, 188), fill=graph_guide_color)
        self.create_line((180, 136), (118, 116), fill=graph_guide_color)

        # stat labels
        self.hp_label = self.create_text((180, 28),
                                         text='Health',
                                         font=poke_font_tuple,
                                         fill=stat_label_color,)
        self.hp_value_label = self.create_text((180, 52),
                                               text=123,
                                               font=poke_font_tuple,
                                               fill=stat_value_color,)
        self.atk_label = self.create_text((318, 114),
                                          text='Attack',
                                          font=poke_font_tuple,
                                          fill=stat_label_color,)
        self.atk_value_label = self.create_text((262, 114),
                                                text=456,
                                                font=poke_font_tuple,
                                                fill=stat_value_color,)
        self.skill_label = self.create_text((287, 188),
                                            text='Skill',
                                            font=poke_font_tuple,
                                            fill=stat_label_color,)
        self.skill_value_label = self.create_text((244, 188),
                                                  text=789,
                                                  font=poke_font_tuple,
                                                  fill=stat_value_color,)
        self.evasion_label = self.create_text((65, 188),
                                              text='Evasion',
                                              font=poke_font_tuple,
                                              fill=stat_label_color,)
        self.evasion_value_label = self.create_text((119, 188),
                                                    text=111,
                                                    font=poke_font_tuple,
                                                    fill=stat_value_color,)
        self.speed_label = self.create_text((44, 114),
                                            text='Speed',
                                            font=poke_font_tuple,
                                            fill=stat_label_color,)
        self.speed_value_label = self.create_text((96, 114),
                                                  text='222',
                                                  font=poke_font_tuple,
                                                  fill=stat_value_color,)

    def update_graf(self, dex=False):
        self.delete(self.pokemon_stats_graph)

        if dex:
            self.parent.displayed_pokemon = pty.displayed_pokemon

        stats_percentage = [
            self.parent.displayed_pokemon.base_hp / max_health,
            self.parent.displayed_pokemon.base_atk / max_attack,
            self.parent.displayed_pokemon.skill / max_skill,
            self.parent.displayed_pokemon.evasion / max_evasion,
            self.parent.displayed_pokemon.base_spd / max_speed,
        ]

        stat_points = [
            180, self.place_point(135, 66, stats_percentage[0]),
            self.place_point(180, 241, stats_percentage[1]), self.place_point(135, 116, stats_percentage[1]),
            self.place_point(180, 221, stats_percentage[2]), self.place_point(135, 188, stats_percentage[2]),
            self.place_point(180, 139, stats_percentage[3]), self.place_point(135, 188, stats_percentage[3]),
            self.place_point(180, 118, stats_percentage[4]), self.place_point(135, 116, stats_percentage[4]),
        ]

        self.pokemon_stats_graph = self.create_polygon(*stat_points, fill=stat_graph_fill, outline=stat_graph_fill)

        # update stat value labels
        self.itemconfig(self.hp_value_label, text=self.parent.displayed_pokemon.hp)
        self.itemconfig(self.atk_value_label, text=round((self.parent.displayed_pokemon.atk + self.parent.displayed_pokemon.lv) / 2))
        self.itemconfig(self.skill_value_label, text=round((self.parent.displayed_pokemon.skill + self.parent.displayed_pokemon.lv) / 2))
        self.itemconfig(self.evasion_value_label, text=round((self.parent.displayed_pokemon.evasion + self.parent.displayed_pokemon.lv) / 2))
        self.itemconfig(self.speed_value_label, text=round((self.parent.displayed_pokemon.spd + self.parent.displayed_pokemon.lv) / 2))

    def place_point(self, start, end, percentage):
        return eval(f'{start}+{percentage}*({end}-{start})')


class MoveBox(ctk.CTkFrame):
    def __init__(self, parent, move_ind):
        self.bg_color = type_colors[1][1]
        super().__init__(parent, height=64, width=280, fg_color=self.bg_color, corner_radius=0, border_width=2, border_color=type_colors[1][0])
        self.small_size = 13
        self.small_color = '#bdbdbd'
        self.parent = parent
        self.move_ind = -1
        self.color1 = ''
        self.color2 = ''
        self.is_selector = False

        # stat labels
        self.speed_value = ctk.CTkLabel(self, text='', text_color=self.small_color, font=(poke_font, self.small_size))

        self.power_value = ctk.CTkLabel(self, text='', text_color=self.small_color, font=(poke_font, self.small_size))

        self.accuracy_value = ctk.CTkLabel(self, text='', text_color=self.small_color, font=(poke_font, self.small_size))

        self.crit_value = ctk.CTkLabel(self, text='', text_color=self.small_color, font=(poke_font, self.small_size))

        self.move_name = ctk.CTkLabel(self, text='', font=poke_font_tuple, text_color=text_color)

        # type icon canvas
        self.icon_size = 22
        self.icon_canvas = Canvas(self, width=self.icon_size, height=self.icon_size, border=0, highlightthickness=0, bg=self.bg_color)
        self.icon_pillow = Image.open('Images/TypeIcons/-1.png')
        self.icon_pillow = self.icon_pillow.resize((self.icon_size, self.icon_size))
        self.icon_pi = ImageTk.PhotoImage(self.icon_pillow)
        self.icon_sprite = self.icon_canvas.create_image(0, 0, image=self.icon_pi, anchor=NW)

        # UI icons
        self.power_canvas = Canvas(self, width=15, height=15, border=0, highlightthickness=0, bg=self.bg_color)
        self.power_pi = PhotoImage(file='Images/UI/power.png')
        self.power_sprite = self.power_canvas.create_image(0, 0, image=self.power_pi, anchor=NW)

        self.speed_canvas = Canvas(self, width=15, height=15, border=0, highlightthickness=0, bg=self.bg_color)
        self.speed_pi = PhotoImage(file='Images/UI/speed.png')
        self.speed_sprite = self.speed_canvas.create_image(0, 0, image=self.speed_pi, anchor=NW)

        self.crit_canvas = Canvas(self, width=15, height=15, border=0, highlightthickness=0, bg=self.bg_color)
        self.crit_pi = PhotoImage(file='Images/UI/crit.png')
        self.crit_sprite = self.crit_canvas.create_image(0, 0, image=self.crit_pi, anchor=NW)

        self.accuracy_canvas = Canvas(self, width=15, height=15, border=0, highlightthickness=0, bg=self.bg_color)
        self.accuracy_pi = PhotoImage(file='Images/UI/accuracy.png')
        self.accuracy_sprite = self.accuracy_canvas.create_image(0, 0, image=self.accuracy_pi, anchor=NW)

        # events
        self.bind('<Enter>', self.enter_event)
        self.bind('<Leave>', self.leave_event)
        self.bind('<Button>', self.click_event)

        self.move_name.bind('<Enter>', self.enter_event)
        self.move_name.bind('<Leave>', self.leave_event)
        self.move_name.bind('<Button>', self.click_event)

        self.speed_value.bind('<Enter>', self.enter_event)
        self.speed_value.bind('<Leave>', self.leave_event)
        self.speed_value.bind('<Button>', self.click_event)

        self.power_value.bind('<Enter>', self.enter_event)
        self.power_value.bind('<Leave>', self.leave_event)
        self.power_value.bind('<Button>', self.click_event)

        self.accuracy_value.bind('<Enter>', self.enter_event)
        self.accuracy_value.bind('<Leave>', self.leave_event)
        self.accuracy_value.bind('<Button>', self.click_event)

        self.crit_value.bind('<Enter>', self.enter_event)
        self.crit_value.bind('<Leave>', self.leave_event)
        self.crit_value.bind('<Button>', self.click_event)

        self.crit_canvas.bind('<Enter>', self.enter_event)
        self.crit_canvas.bind('<Leave>', self.leave_event)
        self.crit_canvas.bind('<Button>', self.click_event)

        self.accuracy_canvas.bind('<Enter>', self.enter_event)
        self.accuracy_canvas.bind('<Leave>', self.leave_event)
        self.accuracy_canvas.bind('<Button>', self.click_event)

        self.power_canvas.bind('<Enter>', self.enter_event)
        self.power_canvas.bind('<Leave>', self.leave_event)
        self.power_canvas.bind('<Button>', self.click_event)

        self.speed_canvas.bind('<Enter>', self.enter_event)
        self.speed_canvas.bind('<Leave>', self.leave_event)
        self.speed_canvas.bind('<Button>', self.click_event)

        self.icon_canvas.bind('<Enter>', self.enter_event)
        self.icon_canvas.bind('<Leave>', self.leave_event)
        self.icon_canvas.bind('<Button>', self.click_event)

        # layout
        self.icon_canvas.place(x=4, y=8)
        self.move_name.place(x=32, y=4)

        self.accuracy_canvas.place(x=214, y=12)
        self.accuracy_value.place(x=234, y=6)

        self.crit_canvas.place(x=214, y=36)
        self.crit_value.place(x=234, y=31)

        self.power_canvas.place(x=7, y=36)
        self.power_value.place(x=26, y=30)

        self.speed_canvas.place(x=120, y=38)
        self.speed_value.place(x=139, y=30)

    def update_movebox(self, move_ind, selector=False, dex=False):
        updated_move = self.parent.displayed_pokemon.move1 if move_ind == 1 else self.parent.displayed_pokemon.move2
        if selector:
            try:
                updated_move = self.parent.displayed_pokemon.moves[move_ind]
            except: pass
            self.is_selector = True
        if dex:
            # events
            self.unbind('<Enter>')
            self.unbind('<Leave>')
            self.unbind('<Button>')

            self.move_name.unbind('<Enter>')
            self.move_name.unbind('<Leave>')
            self.move_name.unbind('<Button>')

            self.speed_value.unbind('<Enter>')
            self.speed_value.unbind('<Leave>')
            self.speed_value.unbind('<Button>')

            self.power_value.unbind('<Enter>')
            self.power_value.unbind('<Leave>')
            self.power_value.unbind('<Button>')

            self.accuracy_value.unbind('<Enter>')
            self.accuracy_value.unbind('<Leave>')
            self.accuracy_value.unbind('<Button>')

            self.crit_value.unbind('<Enter>')
            self.crit_value.unbind('<Leave>')
            self.crit_value.unbind('<Button>')

            self.crit_canvas.unbind('<Enter>')
            self.crit_canvas.unbind('<Leave>')
            self.crit_canvas.unbind('<Button>')

            self.accuracy_canvas.unbind('<Enter>')
            self.accuracy_canvas.unbind('<Leave>')
            self.accuracy_canvas.unbind('<Button>')

            self.power_canvas.unbind('<Enter>')
            self.power_canvas.unbind('<Leave>')
            self.power_canvas.unbind('<Button>')

            self.speed_canvas.unbind('<Enter>')
            self.speed_canvas.unbind('<Leave>')
            self.speed_canvas.unbind('<Button>')

            self.icon_canvas.unbind('<Enter>')
            self.icon_canvas.unbind('<Leave>')
            self.icon_canvas.unbind('<Button>')
        self.move_ind = move_ind

        self.color1 = type_colors[updated_move[1]][0]
        self.color2 = type_colors[updated_move[1]][1]

        # update name
        self.move_name.configure(text=updated_move[0])

        # update icon
        self.icon_pillow = Image.open(f'Images/TypeIcons/{updated_move[1] - 1}.png')
        self.icon_pillow = self.icon_pillow.resize((self.icon_size, self.icon_size))
        self.icon_pi = ImageTk.PhotoImage(self.icon_pillow)
        self.icon_sprite = self.icon_canvas.create_image(0, 0, image=self.icon_pi, anchor=NW)

        # update stats
        if updated_move[2] == power_very_weak:
            self.power_value.configure(text=power_strings[0])
        elif updated_move[2] == power_weak:
            self.power_value.configure(text=power_strings[1])
        elif updated_move[2] == power_normal:
            self.power_value.configure(text=power_strings[2])
        elif updated_move[2] == power_strong:
            self.power_value.configure(text=power_strings[3])
        elif updated_move[2] == power_very_strong:
            self.power_value.configure(text=power_strings[4])
        elif updated_move[2] == power_super:
            self.power_value.configure(text=power_strings[5])
        elif updated_move[2] == power_hyper:
            self.power_value.configure(text=power_strings[6])

        if updated_move[5] == speed_very_fast:
            self.speed_value.configure(text=speed_strings[0])
        elif updated_move[5] == speed_fast:
            self.speed_value.configure(text=speed_strings[1])
        elif updated_move[5] == speed_normal:
            self.speed_value.configure(text=speed_strings[2])
        elif updated_move[5] == speed_slow:
            self.speed_value.configure(text=speed_strings[3])
        elif updated_move[5] == speed_very_slow:
            self.speed_value.configure(text=speed_strings[4])

        self.accuracy_value.configure(text=f'{updated_move[3]}%')
        self.crit_value.configure(text=f'{updated_move[4]}%')

        # update frame color
        self.configure(fg_color=type_colors[updated_move[1]][1], border_color=type_colors[updated_move[1]][0])
        self.icon_canvas.configure(bg=type_colors[updated_move[1]][1])
        self.power_canvas.configure(bg=type_colors[updated_move[1]][1])
        self.accuracy_canvas.configure(bg=type_colors[updated_move[1]][1])
        self.speed_canvas.configure(bg=type_colors[updated_move[1]][1])
        self.crit_canvas.configure(bg=type_colors[updated_move[1]][1])

    def enter_event(self, event):
        color = text_color
        self.move_name.configure(text_color='black')
        self.power_value.configure(text_color='black')
        self.speed_value.configure(text_color='black')
        self.crit_value.configure(text_color='black')
        self.accuracy_value.configure(text_color='black')
        self.configure(fg_color=color)
        self.icon_canvas.configure(bg=color)
        self.power_canvas.configure(bg=color)
        self.accuracy_canvas.configure(bg=color)
        self.speed_canvas.configure(bg=color)
        self.crit_canvas.configure(bg=color)

    def leave_event(self, event):
        self.move_name.configure(text_color=text_color)
        self.move_name.configure(text_color=self.small_color)
        self.power_value.configure(text_color=self.small_color)
        self.speed_value.configure(text_color=self.small_color)
        self.crit_value.configure(text_color=self.small_color)
        self.accuracy_value.configure(text_color=self.small_color)
        self.configure(fg_color=self.color2)
        self.icon_canvas.configure(bg=self.color2)
        self.power_canvas.configure(bg=self.color2)
        self.accuracy_canvas.configure(bg=self.color2)
        self.speed_canvas.configure(bg=self.color2)
        self.crit_canvas.configure(bg=self.color2)

    def click_event(self, event):
        if self.is_selector:
            self.parent.switch_move(self.move_ind)
        else:
            self.parent.move_selector.toggle_window()
            self.parent.move_selector.move_slot = self.move_ind


class MoveSelector(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=288, height=616, fg_color=frame_bg_color, corner_radius=0)
        self.parent = parent
        self.move_slot = 0
        self.window_pos = -1
        self.x_final_pos = 940
        self.x_current_pos = self.winfo_x()
        self.step = 6
        self.displayed_pokemon = Pokemon(*empty, level=0, party_index=6)

    def update_move_selector(self, mon, dex=False):
        for child in self.winfo_children():
            child.destroy()
        self.displayed_pokemon = self.parent.displayed_pokemon

        # if dex:
        #     is_selector = False
        #     self.parent.displayed_pokemon = pty.displayed_pokemon

        y_pos = 4

        for i in range(len(mon.moves)):
            exec(f'move{i} = MoveBox(self, i)')
            exec(f'move{i}.update_movebox(i, selector=True, dex={dex})')
            exec(f'move{i}.place(x=4, y=y_pos)')
            y_pos += 68

    def switch_move(self, move_ind):
        if self.move_slot == 1:
            if self.parent.displayed_pokemon.move1 != self.parent.displayed_pokemon.moves[move_ind]:
                if self.parent.displayed_pokemon.moves[move_ind] != self.parent.displayed_pokemon.move2:
                    self.parent.displayed_pokemon.move1 = self.parent.displayed_pokemon.moves[move_ind]
                    self.parent.move1.update_movebox(1)
                    self.move_out()
                else:
                    self.parent.displayed_pokemon.move2 = self.parent.displayed_pokemon.move1
                    self.parent.displayed_pokemon.move1 = self.parent.displayed_pokemon.moves[move_ind]
                    self.parent.move1.update_movebox(1)
                    self.parent.move2.update_movebox(2)
                    self.move_out()
        else:
            if self.parent.displayed_pokemon.move2 != self.parent.displayed_pokemon.moves[move_ind]:
                if self.parent.displayed_pokemon.moves[move_ind] != self.parent.displayed_pokemon.move1:
                    self.parent.displayed_pokemon.move2 = self.parent.displayed_pokemon.moves[move_ind]
                    self.parent.move2.update_movebox(2)
                    self.move_out()
                else:
                    self.parent.displayed_pokemon.move1 = self.parent.displayed_pokemon.move2
                    self.parent.displayed_pokemon.move2 = self.parent.displayed_pokemon.moves[move_ind]
                    self.parent.move1.update_movebox(1)
                    self.parent.move2.update_movebox(2)
                    self.move_out()

    def toggle_window(self):
        self.x_current_pos = self.winfo_x()
        if self.window_pos == -1:
            self.move_in()
        else:
            self.move_out()

    def move_in(self):
        if self.winfo_x() > self.x_final_pos:
            self.place(x=self.x_current_pos - self.step)
            self.x_current_pos -= self.step
            self.after(1, self.move_in)
        else:
            self.window_pos = 1

    def move_out(self):
        if self.winfo_x() <= 1300:
            self.place(x=self.x_current_pos + self.step)
            self.x_current_pos += self.step
            self.after(1, self.move_out)
        else:
            self.window_pos = -1

