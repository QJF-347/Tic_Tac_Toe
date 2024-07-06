from tkinter import *
import random
import runpy

players = ["X", "O"]
player = random.choice(players)
p1s, p2s = 0, 0

def check_win():
    global score
    for win in range(3):
        if sum(score[win]) == 3 or sum(score[win]) == 12:
            for p in range(3):
                buttons[win][p].config(bg="#00ff00")
            return True
        
    for row in range(3):
        if score[0][row] == score[1][row] == score[2][row] and score[row][row]!= 0 :
            for p in range(3):
                buttons[p][row].config(bg="#00ff00")
            return True
    if score[0][0] == score[1][1] == score[2][2] != 0 :
        for p in range(3):
            buttons[p][p].config(bg="#00ff00")
        return True
    if  score[2][0] == score[1][1] == score[0][2] !=0:
        for p in range(3):
            buttons[2-p][p].config(bg="#00ff00")
        return True
    carrier = 1
    for row in range(3):
        for column in range(3):
            carrier *= score[row][column]
    if carrier != 0:
        return "draw"
    else:
        return False

def pressed(row, column, play):
    global players, player, p1s, p2s
    buttons[row][column].config(text=play)
    if player == players[0]:
        player = players[1]
        buttons[row][column].config(state = DISABLED)
        score[row][column] = 1
        if check_win() == False:
            label.config(text="{}'s turn".format(player))
        elif check_win() == True:
            p1s += 3
            score_label1.config(text="{} : {}\t".format(players[0],p1s))
            label.config(text="{} wins".format(players[0]))
            for row in range(3):
                for column in range(3):
                    buttons [row][column].config(state=DISABLED)
        else:
            label.config(text=" DRAW !")
            p1s , p2s = p1s+1, p2s+1
            score_label1.config(text="{}: {}\t".format(players[0],p1s))
            score_label2.config(text="{}: {}\t".format(players[1],p2s))
            for row in range(3):
                for column in range(3):
                    buttons [row][column].config(bg="light gray")
            
    elif player == players[1]:
        player = players[0]
        buttons[row][column].config(state = DISABLED)
        score[row][column] = 4
        if check_win() == False:
            label.config(text="{}'s turn".format(player))
        elif check_win() == True:
            p2s += 3
            score_label2.config(text="{} : {}\t".format(players[1],p2s))
            label.config(text="{} wins".format(players[1]))
            for row in range(3):
                for column in range(3):
                    buttons [row][column].config(state=DISABLED)
        else:
            label.config(text=" DRAW !")
            p1s , p2s = p1s+1, p2s+1
            score_label1.config(text="{}: {}\t".format(players[0],p1s))
            score_label2.config(text="{}: {}\t".format(players[1],p2s))
            for row in range(3):
                for column in range(3):
                    buttons [row][column].config(bg="light gray")
                    

def new_game():
    global score
    for row in range(3):
        for column in range(3):
            score[row][column] = 0
            buttons [row][column].config(bg="#dddddd", text='', state=ACTIVE)
    

def home():
    window.destroy()
    runpy.run_path(path_name="home.py")
    
    
window = Tk()
window.geometry("500x700")

frame = Frame(window, bg="black")
frame.pack()

score_label1 = Label(frame, text="{} : {}\t".format(players[0],p1s), font=(None, 23), bg="black", fg="#00ff00")
score_label1.grid(row=0, column=0)

score_label2 = Label(frame, text="{} : {}".format(players[1],p2s), font=(None, 23), bg="black", fg="#00ff00")
score_label2.grid(row=0, column=2)


label = Label(frame, text="{}'s turn".format(player), font=(None, 23), bg="black", fg="#00ff00",)
label.grid(row=1, column=0, columnspan=3)

buttons, score = [[0, 0, 0]for rows in range(3)], [[0, 0, 0]for rows in range(3)]
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=(None, 35), width=5, height=2, fg="#000000",
                                      command=lambda row=row, column=column:pressed(row, column, player))
        buttons[row][column].grid(row=row+2, column=column)

new_game_button = Button(frame, text="NEW GAME", font=(None, 15), bg="#aaaaaa", width=25, height=2, command=new_game)
new_game_button.grid(row=6, column=1, columnspan=2)

home_button = Button(frame, text="HOME",font=(None, 15), bg="#aaaaaa", width=12, height=2 , command=home)
home_button.grid(row=6, column=0)

window.mainloop()