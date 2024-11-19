import random
import pygame
import datetime
import tkinter
import sys
import os
from tkinter import *
movements = ["rock", "paper", "scissors"]
mymovement = ""
enemymovemnt = ""
wins = 0
defeats = 0
draw = 0

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) 
    return os.path.join(base_path, relative_path)

sound_path_win = resource_path("assets/sounds/win.ogg")
sound_path_defeat = resource_path("assets/sounds/defeat.ogg")
icon_path = resource_path("assets/images/cotr.ico")

window = Tk()
window.title("Rock, Paper, Scissors")
window.iconbitmap(icon_path)
window.geometry("500x500")
window.resizable(0, 0)

main_label = Label(window)
your_movement_label = Label(window)
your_movement_output = Label(window)
enemy_movement_label = Label(window)
enemy_movement_output = Label(window)
by_cotr = Label(window)
score_label = Label(window)
rock_button = Button(window)
paper_button = Button(window)
scissors_button = Button(window)

pygame.init()
pygame.mixer.init()
win_sound = pygame.mixer.Sound(sound_path_win)
defeat_sound = pygame.mixer.Sound(sound_path_defeat)

def pressrock():
    global mymovement
    mymovement = movements[0]
    count()
def presspaper():
    global mymovement
    mymovement = movements[1]
    count()
def pressscissors():
    global mymovement
    mymovement = movements[2]
    count()

def count():
    global wins, defeats, draw, mymovement, enemymovement
    your_movement_output.config(text = mymovement.upper())
    enemymovement = random.choice(movements)
    enemy_movement_output.config(text = enemymovement.upper())
    if (mymovement == enemymovement):
        draw+=1
    elif (mymovement == "rock"):
        if (enemymovement == "paper"):
            defeats+=1
            defeat_sound.play()
        else:
            wins+=1
            win_sound.play()
    elif (mymovement == "paper"):
        if (enemymovement == "scissors"):
            defeats+=1
            defeat_sound.play()
        else:
            wins+=1
            win_sound.play()
    elif (mymovement == "scissors"):
        if (enemymovement == "rock"):
            defeats+=1
            defeat_sound.play()
        else:
            wins+=1
            win_sound.play()
    score_label.config(text="GAME SCORE:\n"+str(wins)+" (You) : "+str(defeats)+" (Bot)")


main_label.config(
    text = "Choose your movement:",
    font = ("ArialBlack", 16, "bold")
)
your_movement_label.config(
    text = "Your movement:",
    font = ("ArialBlack", 16, "bold")
)
your_movement_output.config(
    text = "-",
    font = ("ArialBlack", 16, "bold")
)
enemy_movement_label.config(
    text = "Enemy's movement:",
    font = ("ArialBlack", 16, "bold")
)
enemy_movement_output.config(
    text = "-",
    font = ("ArialBlack", 16, "bold")
)
score_label.config(
    text = "GAME SCORE:\n"+str(wins)+" (You) : "+str(defeats)+" (Bot)",
    font = ("ArialBlack", 16, "bold")
)
by_cotr.config(
    text = "\u00A9 CotR 2022-"+str(datetime.datetime.now().year),
    font = ("ArialBlack", 9, "bold")
)
rock_button.config(
    text = "ROCK",
    font = ("ArialBlack", 10, "bold"),
    width = "25",
    height = "2",
    command = pressrock
)
paper_button.config(
    text = "PAPER",
    font = ("ArialBlack", 10, "bold"),
    width = "25",
    height = "2",
    command = presspaper
)
scissors_button.config(
    text = "SCISSORS",
    font = ("ArialBlack", 10, "bold"),
    width = "25",
    height = "2",
    command = pressscissors
)

score_label.pack()
main_label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
your_movement_label.pack()
your_movement_output.pack()
enemy_movement_label.pack()
enemy_movement_output.pack()
by_cotr.pack(side=tkinter.BOTTOM)

window.mainloop()