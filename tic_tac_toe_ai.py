from tkinter import *
import random
import runpy

player_points, computer_points = 0, 0 
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0]for x in range(3)]
played = [[0, 0, 0]for x in range(3)]
font = ("Aerial", 22)
empty = 9
player_row, player_column = [0, 0, 0], [0, 0, 0]
positive_diag, negative_diag = [0, 0, 0], [0, 0, 0]


def check_win():
    global played, empty, player_points, computer_points
    for row in range(3):
        if sum(played[row]) == 3 or sum(played[row]) == 12:
            for p in range(3):
                buttons[row][p].config(bg="#00ff00")
            empty = 0
            return True
        
    for row in range(3):
        if played[0][row] == played[1][row] == played[2][row] and played[row][row]!= 0 :
            for p in range(3):
                buttons[p][row].config(bg="#00ff00")
            empty = 0  
            return True 
        
    if played[0][0] == played[1][1] == played[2][2] != 0 :
        for p in range(3):
            buttons[p][p].config(bg="#00ff00")
        empty = 0
        return True
    
    elif  played[2][0] == played[1][1] == played[0][2] !=0:
        for p in range(3):
            buttons[2-p][p].config(bg="#00ff00")
        empty = 0
        return True
    
    elif empty == 0:
        label.config(text="DRAW !")
        player_points, computer_points = player_points + 1, computer_points + 1
        score_label_player.config(text="player : {}".format(player_points))
        score_label_computer.config(text="comp : {}".format(computer_points))
        
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="#bbbbbb")
                
        return 0 
    return False
            

def strategy(comp_row, comp_col):
    global played
    for row in range(3):
        if sum(played[row]) == 4:
            comp_col = random.randint(0, 2)
            while played[row][comp_col] != 0:
                comp_col = random.randint(0, 2)
            if played[row][comp_col] == 0:
                return row, comp_col
            
            
    return comp_row, comp_col
    
    
    return comp_row, comp_col
    
def check_for_possible_win(comp_row, comp_col):
    for row in range(3):
        if sum(played[row]) == 8:
            for column in range(3):
                if played[row][column] == 0:
                    return row, column
    
    for column in range(3):
        rover = []
        for row in range(3):
            rover.append(played[row][column])
        if sum(rover) == 8:
            for r in range(3):
                if played[r][column] == 0:
                    return r, column
                
    rover = []
    for row in range(3):
        rover.append(played[row][row])
        if sum(rover) == 8:
            for column in range(3):
                if played[column][column] == 0:
                    return column, column
    
    rover = []
    for row in range(3):
        rover.append(played[row][2-row])
        if sum(rover) == 8:
            for column in range(3):
                if played[column][2-column] == 0:
                    return column, 2-column
                
    return comp_row, comp_col
    
    
def play(comp_row, comp_col, attacked):
    global empty, computer_points, played
    comp_row, comp_col = check_for_possible_win(comp_row, comp_col)
    buttons[comp_row][comp_col].config(text=players[1], state=DISABLED)
    label.config(text="{}'s turn".format(players[0]))
    played[comp_row][comp_col] = 4
    empty -= 1 
    if check_win():      
                computer_points += 3
                label.config(text="Computer Wins")
                score_label_computer.config(text="comp : {}".format(computer_points))
                for r in range(3):
                    for c in range(3):
                        buttons[r][c].config(state=DISABLED)
    
    
def computer_mind():
    global empty, played, player_row, player_column
    for rows in range(3):
        if player_row[rows] == 2 and sum(played[rows]) < 3:
            for column in range(3):
                if played[rows][column] == 0:
                    play(rows, column, 1)
                    return 0
                
    for columns in range(3):
        if player_column[columns] == 2:
            for row in range(3):
                if played[row][columns] == 0:
                    play(row, columns, 2)
                    return 0
    
    for row in range(3):
        if negative_diag[row] == 0 and sum(negative_diag) == 2 and played[row][row] == 0:
            play(row, row, 3)
            return 0
        
    for column in range(3):
        if positive_diag[column] == 0 and sum(positive_diag) == 2 and played[2-column][column] == 0:
            play(2-column, column, 4)
            return 0
    
    while True:
        row, column = random.randint(0, 2), random.randint(0, 2)
        if played[row][column] < 1:
            play(row, column, 0)
            return 0 
            
                
def pressed(row, column):
    global empty, played, player_points, player_row, player_column, positive_diag, negative_diag
    player_row[row] += 1
    player_column[column] += 1
    if row == column :
        negative_diag[row] = 1
        if row == 1:
            positive_diag[1] = 1
    elif row + column == 2:
        positive_diag[column] = 1
        
    buttons[row][column].config(state=DISABLED, text=(players[0]))
    label.config(text="{}'s turn".format(players[1]))
    played[row][column] = 1
    empty -= 1 
    if check_win():
        player_points += 3
        label.config(text="You Win")
        score_label_player.config(text="player : {}".format(player_points))
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(state=DISABLED)
    if empty != 0:
        computer_mind()
    


def new_game():
    global played, player, players, empty, player_row, player_column, positive_diag, negative_diag
    
    player_row, player_column = [0, 0, 0], [0, 0, 0]
    positive_diag, negative_diag = [0, 0, 0], [0, 0, 0]
    empty = 9
    for row in range(3):
        for column in range(3):
            played[row][column] = 0
            buttons [row][column].config(state=ACTIVE, bg="#eeeeee", text='')
    player = random.choice(players)
    label.config(text="{}'s turn".format(player))
    if player == players[1]:
        buttons[row := random.randint(0, 2)][column := random.randint(0, 2)].config(
        text="{}".format(players[1]), state=DISABLED)
        played[row][column] = 4
        empty -= 1 


def home():
    window.destroy()
    runpy.run_path(path_name="home.py")
    
window = Tk()
window.geometry("500x650")
frame = Frame(window, bg="black")
frame.pack()

score_label_player = Label(frame, text="player : {}".format(player_points), bg="black",
                           fg="#00ff00", font=font)
score_label_player.grid(row=0, column=0)

score_label_computer = Label(frame, text="comp : {}".format(computer_points), bg="black",
                             fg="#00ff00", font=font)
score_label_computer.grid(row=0, column=2)

label = Label(frame, text="{}'s turn".format(player), font=font, bg="#000000", fg="#00ff00")
label.grid(row=1, column=0, columnspan=3)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, font=font, width=8, height=4, 
                                      command=lambda row=row, column=column: pressed(row, column))
        buttons[row][column].grid(row=row+2, column=column)
        
new_game_button = Button(frame, text="NEW GAME", font=font, width=16, command=new_game)
new_game_button.grid(row=6, column=1, columnspan=2)

home_button = Button(frame, text="HOME",font=font, width=8, command=home)
home_button.grid(row=6, column=0)

if player == players[1]:
    buttons[row := random.randint(0, 2)][column := random.randint(0, 2)].config(
        text="{}".format(players[1]), state=DISABLED)
    played[row][column] = 4
    empty -= 1
window.mainloop()

