from tkinter import *
import runpy

def single_player():
    window.destroy()
    runpy.run_path(path_name="tic_tac_toe_ai.py")

def multiplayer():
    window.destroy()
    runpy.run_path(path_name="tic_tac_toe.py")


font = ("Aerial", 24)
window = Tk()
window.geometry("500x650")
window.config(bg="light gray")

frame = Frame(window, background="light gray")
frame.pack()

game_label = Label(frame, text="TIC-TAC-TOE", font=("Aerial", 34, "bold"), bg="light gray")
game_label.pack(ipady=85)

single_player_button = Button(frame, text="SINGLE PLAYER", font=font, command=single_player)
single_player_button.pack()

empty = Label(frame, bg="light gray")
empty.pack(ipady=25)

two_player_button = Button(frame, text="MULTI - PLAYER", font=font, command=multiplayer)
two_player_button.pack()

empty = Label(frame, bg="light gray")
empty.pack(ipady=25)



window.mainloop()