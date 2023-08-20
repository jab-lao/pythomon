from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


from pokemon_list import *
from move_list import *
from type_list import *


party_slot1 = Pokemon(*bulbasaur)
party_slot1.party_index = 0
party_slot1.move1 = party_slot1.moves[0]
party_slot1.move2 = party_slot1.moves[1]
party_slot1.lv = 4
party_slot1.level_up()

party_slot2 = Pokemon(*charmander)
party_slot2.move1 = party_slot2.moves[0]
party_slot2.move2 = party_slot2.moves[1]
party_slot2.party_index = 1
party_slot2.lv = 4
party_slot2.level_up()

party_slot3 = Pokemon(*squirtle)
party_slot3.move1 = party_slot3.moves[0]
party_slot3.move2 = party_slot3.moves[1]
party_slot3.party_index = 2
party_slot3.lv = 4
party_slot3.level_up()

party_slot4 = Pokemon(*pikachu)
party_slot4.move1 = party_slot4.moves[0]
party_slot4.move2 = party_slot4.moves[1]
party_slot4.party_index = 3
party_slot4.lv = 4
party_slot4.level_up()

party_slot5 = Pokemon(*eevee)
party_slot5.move1 = party_slot5.moves[0]
party_slot5.move2 = party_slot5.moves[1]
party_slot5.party_index = 4
party_slot5.lv = 4
party_slot5.level_up()

party_slot6 = Pokemon(*eevee)
party_slot6.move1 = party_slot6.moves[0]
party_slot6.move2 = party_slot6.moves[1]
party_slot6.party_index = 5
party_slot6.lv = 4
party_slot6.level_up()

party = [party_slot1, party_slot2, party_slot3, party_slot4, party_slot5, party_slot6]

displayed_pokemon = party_slot1


def change_mon(dex, party_index):
    global poke_sprite
    global displayed_pokemon
    pkmon = party[party_index]
    displayed_pokemon = pkmon

    poke_sprite.config(file="Images/Sprites/{}.png".format(dex))

    stats.update_stats(pkmon)

    move1.update_move(pkmon.move1)
    move2.update_move(pkmon.move2)
    move1.update_menu_buttons()

    aff_box.update_affinities(pkmon)


def change_move(move_slot):
    if move_slot == 1:
        prev_list_slot = displayed_pokemon.moves.index(displayed_pokemon.move1)
        if displayed_pokemon.move2 != displayed_pokemon.moves[move1_list_variable.get() - 1]:
            displayed_pokemon.move1 = displayed_pokemon.moves[move1_list_variable.get() - 1]
            move1.update_move(displayed_pokemon.move1)

        else:
            move1_list_variable.set(prev_list_slot)
            move1.update_move(displayed_pokemon.move1)

    elif move_slot == 2:
        prev_list_slot = displayed_pokemon.moves.index(displayed_pokemon.move2)
        if displayed_pokemon.move1 != displayed_pokemon.moves[move2_list_variable.get() - 1]:
            displayed_pokemon.move2 = displayed_pokemon.moves[move2_list_variable.get() - 1]
            move2.update_move(displayed_pokemon.move2)

        else:
            move2_list_variable.set(prev_list_slot)
            move2.update_move(displayed_pokemon.move2)

    move1_list_variable.set(0)
    move2_list_variable.set(0)


class ButtonBox(ctk.CTkFrame):
    def __init__(self, parent):
        bg_color = 'light gray'
        hover_color = 'white'

        super().__init__(parent)
        self.button1 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon0, command=lambda: change_mon(party[0].dex, 0))
        self.button1.grid(row=0, column=0)

        self.button2 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon1, command=lambda: change_mon(party[1].dex, 1))
        self.button2.grid(row=0, column=1)

        self.button3 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon2, command=lambda: change_mon(party[2].dex, 2))
        self.button3.grid(row=1, column=0)

        self.button4 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon3, command=lambda: change_mon(party[3].dex, 3))
        self.button4.grid(row=1, column=1)

        self.button5 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon4, command=lambda: change_mon(party[4].dex, 4))
        self.button5.grid(row=2, column=0)

        self.button6 = ctk.CTkButton(self, text="", fg_color=bg_color, corner_radius=0, hover_color=hover_color,
                                     height=60, width=60, image=icon5, command=lambda: change_mon(party[5].dex, 5))
        self.button6.grid(row=2, column=1)


class MoveBox(ctk.CTkFrame):
    def __init__(self, parent, move):
        bg_color = 'light gray'
        super().__init__(parent)

        # Move Name and Type
        self.move_name = ctk.CTkLabel(self, text=f"  {move[0]}  ", anchor=W, width=160)
        self.move_name.grid(row=0, column=0, columnspan=2)

        self.type_canvas = ctk.CTkCanvas(self, width=46, height=46, bd=0, highlightthickness=0, background=bg_color)
        self.type_canvas.create_image(2, 2, image=type_icons[move[1] - 1], anchor='nw')

        self.type_canvas.grid(row=0, column=1, columnspan=2)

        # Move Damage
        self.move_damage = ctk.CTkLabel(self, text=f"{move[2]}", anchor=W, width=5)
        self.move_damage.grid(row=1, column=1)

        # Move Accuracy
        self.move_acc = ctk.CTkLabel(self, text=f"{move[3]}%", anchor=W, width=5)
        self.move_acc.grid(row=2, column=1)

        # Move Crit Chance
        self.move_crit = ctk.CTkLabel(self, text=f"{move[4]}%", anchor=W, width=5)
        self.move_crit.grid(row=3, column=1)

        # Move Charge Time
        self.move_charge = ctk.CTkLabel(self, text=f"{move[5]}", anchor=W, width=5)
        self.move_charge.grid(row=4, column=1)

        # Layout
        ctk.CTkLabel(self, text="Damage: ", anchor=W, width=9).grid(row=1, column=0, sticky=E)
        ctk.CTkLabel(self, text="Accuracy: ", anchor=W, width=9).grid(row=2, column=0, sticky=E)
        ctk.CTkLabel(self, text="Critical %: ", anchor=W, width=9).grid(row=3, column=0, sticky=E)
        ctk.CTkLabel(self, text="Charge: ", anchor=W, width=9).grid(row=4, column=0, sticky=E)

    def update_move(self, new_move):
        self.move_name.configure(text=f"    {new_move[0]}  ")
        self.type_canvas.itemconfig(1, image=type_icons[new_move[1] - 1])
        self.move_damage.configure(text=f"{new_move[2]}")
        self.move_acc.configure(text=f"{new_move[3]}%")
        self.move_crit.configure(text=f"{new_move[4]}%")
        self.move_charge.configure(text=f"{new_move[5]}")

    def update_menu_buttons(self):
        move1_list.delete(0, END)
        move2_list.delete(0, END)
        loop = 0

        for i in displayed_pokemon.moves:
            loop += 1
            move1_list.add_checkbutton(variable=move1_list_variable, label=f"{i[0]}", onvalue=loop, offvalue=0,
                                       command=lambda: change_move(1))

            move2_list.add_checkbutton(variable=move2_list_variable, label=f"{i[0]}", onvalue=loop, offvalue=0,
                                       command=lambda: change_move(2))


class StatBox(ctk.CTkFrame):
    def __init__(self, parent, mon):
        super().__init__(parent)
        self.poke_name = ctk.CTkLabel(self, width=12, anchor=W, text="")

        self.poke_type2 = ctk.CTkLabel(self, text="")
        self.poke_type1 = ctk.CTkLabel(self, text="")

        self.lv_label = ctk.CTkLabel(self, width=12, anchor=W, text="Level: ")
        self.poke_lv = ctk.CTkLabel(self, width=12, anchor=W, text="Level: ")

        self.hp_label = ctk.CTkLabel(self, width=12, anchor=W, text="HP: ")
        self.poke_hp = ctk.CTkLabel(self, width=14, anchor=W, text="")

        self.atk_label = ctk.CTkLabel(self, width=12, anchor=W, text="Attack: ")
        self.poke_atk = ctk.CTkLabel(self, width=14, anchor=W, text="")

        self.spd_label = ctk.CTkLabel(self, width=12, anchor=W, text="Speed: ")
        self.poke_spd = ctk.CTkLabel(self, width=14, anchor=W, text="")

        self.exp_bar = ctk.CTkProgressBar(self, orientation=HORIZONTAL)

        # Grid
        self.poke_name.grid(row=0, column=0)
        self.poke_type1.grid(row=0, column=1, rowspan=3, sticky="")
        self.poke_type2.grid(row=0, column=2, rowspan=3, sticky=E)
        self.poke_lv.grid(row=1, column=0)
        self.exp_bar.grid(row=2, column=0)
        self.hp_label.grid(row=3, column=0)
        self.poke_hp.grid(row=3, column=1)
        self.atk_label.grid(row=4, column=0)
        self.poke_atk.grid(row=4, column=1)
        self.spd_label.grid(row=5, column=0)
        self.poke_spd.grid(row=5, column=1)

    def update_stats(self, new_mon):
        self.poke_name.configure(text=f"{new_mon.name}")

        if new_mon.type2[0] == "":
            self.poke_type1.configure(image=type_icons[new_mon.type1[1] - 1])
            self.poke_type1.grid(sticky='')
            self.poke_type2.configure(image=type_icons[new_mon.type2[1] - 1])
        else:
            self.poke_type1.configure(image=type_icons[new_mon.type1[1] - 1])
            self.poke_type1.grid(sticky=W)
            self.poke_type2.configure(image=type_icons[new_mon.type2[1] - 1])

        self.poke_lv.configure(text=f"Level: {new_mon.lv}")

        self.exp_bar.set(displayed_pokemon.exp / displayed_pokemon.exp_cap)
        self.poke_hp.configure(text=f"{new_mon.hp}")
        self.poke_atk.configure(text=f"{new_mon.atk}")
        self.poke_spd.configure(text=f"{new_mon.spd}")

    def gainexp(self, mon):
        mon.exp = mon.exp + 7
        self.exp_bar.set(mon.exp / mon.exp_cap)

        if mon.exp >= mon.exp_cap:
            mon.level_up()
            change_mon(mon.dex, mon.party_index)
            self.exp_bar.set(mon.exp / mon.exp_cap)


class AffinitiesBox(ctk.CTkFrame):
    def __init__(self, parent):
        bg_color = 'light gray'
        super().__init__(parent, fg_color=bg_color)

        # Generate affinity type labels
        affinity_row = 1
        affinity_column = 0

        for ind in range(18):
            new_canvas = ctk.CTkCanvas(self, width=50, height=50, background=bg_color, bd=0, highlightthickness=0)
            new_canvas.create_image(6, 2, image=type_icons[ind], anchor='nw')
            new_canvas.grid(row=affinity_row, column=affinity_column, pady=2, padx=2)


            # Reset grid placement to limit frame height
            if ind == 8:
                affinity_row = 0
                affinity_column = 3

            affinity_row = affinity_row + 1

        self.poke_aff_normal = ctk.CTkLabel(self, text="")
        self.poke_aff_normal.grid(row=1, column=1, padx=(0, 10))

        self.poke_aff_fighting = ctk.CTkLabel(self, text="")
        self.poke_aff_fighting.grid(row=2, column=1, padx=(0, 10))

        self.poke_aff_flying = ctk.CTkLabel(self, text="")
        self.poke_aff_flying.grid(row=3, column=1, padx=(0, 10))

        self.poke_aff_poison = ctk.CTkLabel(self, text="")
        self.poke_aff_poison.grid(row=4, column=1, padx=(0, 10))

        self.poke_aff_ground = ctk.CTkLabel(self, text="")
        self.poke_aff_ground.grid(row=5, column=1, padx=(0, 10))

        self.poke_aff_rock = ctk.CTkLabel(self, text="")
        self.poke_aff_rock.grid(row=6, column=1, padx=(0, 10))

        self.poke_aff_bug = ctk.CTkLabel(self, text="")
        self.poke_aff_bug.grid(row=7, column=1, padx=(0, 10))

        self.poke_aff_ghost = ctk.CTkLabel(self, text="")
        self.poke_aff_ghost.grid(row=8, column=1, padx=(0, 10))

        self.poke_aff_steel = ctk.CTkLabel(self, text="")
        self.poke_aff_steel.grid(row=9, column=1, padx=(0, 10))

        self.poke_aff_fire = ctk.CTkLabel(self, text="")
        self.poke_aff_fire.grid(row=1, column=4, padx=(0, 10))

        self.poke_aff_water = ctk.CTkLabel(self, text="")
        self.poke_aff_water.grid(row=2, column=4, padx=(0, 10))

        self.poke_aff_grass = ctk.CTkLabel(self, text="")
        self.poke_aff_grass.grid(row=3, column=4, padx=(0, 10))

        self.poke_aff_electric = ctk.CTkLabel(self, text="")
        self.poke_aff_electric.grid(row=4, column=4, padx=(0, 10))

        self.poke_aff_psychic = ctk.CTkLabel(self, text="")
        self.poke_aff_psychic.grid(row=5, column=4, padx=(0, 10))

        self.poke_aff_ice = ctk.CTkLabel(self, text="")
        self.poke_aff_ice.grid(row=6, column=4, padx=(0, 10))

        self.poke_aff_dragon = ctk.CTkLabel(self, text="")
        self.poke_aff_dragon.grid(row=7, column=4, padx=(0, 10))

        self.poke_aff_dark = ctk.CTkLabel(self, text="")
        self.poke_aff_dark.grid(row=8, column=4, padx=(0, 10))

        self.poke_aff_fairy = ctk.CTkLabel(self, text="")
        self.poke_aff_fairy.grid(row=9, column=4, padx=(0, 10))

    def update_affinities(self, mon):
        self.poke_aff_normal.configure(text=f"{mon.affinities[2]}")
        self.poke_aff_fighting.configure(text=f"{mon.affinities[3]}")
        self.poke_aff_flying.configure(text=f"{mon.affinities[4]}")
        self.poke_aff_poison.configure(text=f"{mon.affinities[5]}")
        self.poke_aff_ground.configure(text=f"{mon.affinities[6]}")
        self.poke_aff_rock.configure(text=f"{mon.affinities[7]}")
        self.poke_aff_bug.configure(text=f"{mon.affinities[8]}")
        self.poke_aff_ghost.configure(text=f"{mon.affinities[9]}")
        self.poke_aff_steel.configure(text=f"{mon.affinities[10]}")
        self.poke_aff_fire.configure(text=f"{mon.affinities[11]}")
        self.poke_aff_water.configure(text=f"{mon.affinities[12]}")
        self.poke_aff_grass.configure(text=f"{mon.affinities[13]}")
        self.poke_aff_electric.configure(text=f"{mon.affinities[14]}")
        self.poke_aff_psychic.configure(text=f"{mon.affinities[15]}")
        self.poke_aff_ice.configure(text=f"{mon.affinities[16]}")
        self.poke_aff_dragon.configure(text=f"{mon.affinities[17]}")
        self.poke_aff_dark.configure(text=f"{mon.affinities[18]}")
        self.poke_aff_fairy.configure(text=f"{mon.affinities[19]}")


# ############
# Root Frame
root = ctk.CTk()
root.config(background="gray")

status_frame = ctk.CTkFrame(root, fg_color="gray")

status_frame.pack(expand=True, fill="y")

# get type icons
type_icons = []

for i in range(18):
    new_icon = PhotoImage(file=f"Images/TypeIcons/{i}.png")
    type_icons.append(new_icon)
# insert "empty" icon
type_icons.append(PhotoImage(file=f"Images/TypeIcons/18.png"))

icon0 = PhotoImage(file="Images/Icons/{}.png".format(party[0].dex))
icon1 = PhotoImage(file="Images/Icons/{}.png".format(party[1].dex))
icon2 = PhotoImage(file="Images/Icons/{}.png".format(party[2].dex))
icon3 = PhotoImage(file="Images/Icons/{}.png".format(party[3].dex))
icon4 = PhotoImage(file="Images/Icons/{}.png".format(party[4].dex))
icon5 = PhotoImage(file="Images/Icons/{}.png".format(party[5].dex))


# ##########
# Stat frame
stat_frame = ctk.CTkFrame(status_frame)

stats = StatBox(stat_frame, displayed_pokemon)
stats.pack()

# Buttons
button_frame = ctk.CTkFrame(status_frame)

buttons = ButtonBox(button_frame)
buttons.pack()


# Canvas BG
canvas = ctk.CTkCanvas(status_frame, background="cornflowerblue", width=168, height=168,
                       border=12, highlightthickness=0, relief=RAISED)

poke_sprite = PhotoImage()

pokemon = canvas.create_image(-24, -25, image=poke_sprite, anchor=NW)


# Affinities frame
affinity_frame = ctk.CTkFrame(status_frame)

aff_box = AffinitiesBox(affinity_frame)
aff_box.pack()


# Attacks Frame
attack_frame = ctk.CTkFrame(status_frame)


move1_button = ttk.Menubutton(attack_frame, text="Move 1")
move1_list_variable = IntVar()
move1_list = Menu(move1_button, tearoff=0)
move1_button["menu"] = move1_list

move2_button = ttk.Menubutton(attack_frame, text="Move 2")
move2_list_variable = IntVar()
move2_list = Menu(move2_button, tearoff=0)
move2_button["menu"] = move2_list

move1 = MoveBox(attack_frame, move_list["None"])
move2 = MoveBox(attack_frame, move_list["None"])

move1_button.pack(fill="x")
move1.pack()
move2_button.pack(fill="x")
move2.pack()


# Layout
button_frame.pack(side="left", anchor=N, expand=True)
canvas.pack(side="left", anchor=N, expand=True)
stat_frame.pack(side="left", anchor=N, expand=True)
attack_frame.pack(side="left", anchor=N, expand=True)
affinity_frame.pack(side="left", anchor=N, expand=True)


levelup_button = ctk.CTkButton(status_frame, text="+6 exp", command=lambda: stats.gainexp(displayed_pokemon))
levelup_button.place(relx=0, rely=1, anchor=SW)

root.mainloop()
