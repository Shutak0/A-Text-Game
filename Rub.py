from ast import Global  #Made by Viktor Lobashev
from random import random
from random import randint
from tkinter import *
from CRub import Warrior
from CRub import Commander
from CRub import Archer
from CRub import Wizard
def fstart(dude0, dude1):
    global winner
    global loser
    global lhealth
    global whealth
    if dude0.health <= 0:
        winner = dude1.name
        whealth = dude1.health
        loser = dude0.name
        lhealth = dude0.health
        return(print('Another one bites the dust! Winner: ', dude1.name, ', Loser: ', dude0.name))
    elif dude1.health <= 0:
        winner = dude0.name
        whealth = dude0.health
        loser = dude1.name
        lhealth = dude1.health
        return(print('Another one bites the dust! Winner: ', dude0.name, ', Loser: ', dude1.name))
    elif dude1.health == dude0.health and dude0.health < 1:
        winner = 'nope'
        whealth = dude0.health
        loser = 'nope'
        lhealth = dude1.health
        return(print('Draw'))
    dude0.hitenemy(dude1)
    dude1.hitenemy(dude0)
    return(fstart(dude0=dude0, dude1=dude1))
def createperson():
    global guy0
    if y.get() == 'Wizard':
        guy0 = Wizard(name = x.get(), damage=20, health=100, speed=1, armorlvl=8)
    elif y.get() == 'Warrior':
        guy0 = Warrior(name = x.get(), damage=15, health=80, speed=3, armorlvl=6)
    elif y.get() == 'Archer':
        guy0 = Archer(name = x.get(), damage=25, health=60, speed=2, armorlvl=9)
    elif y.get() == 'Commander':
        guy0 = Commander(name = x.get(), damage=40, health=50, speed=1, armorlvl=5)
    return(guy0)
def createperson1():
    global guy1
    if h.get() == 'Wizard':
        guy1 = Wizard(name = z.get(), damage=20, health=100, speed=1, armorlvl=8)
    elif h.get() == 'Warrior':
        guy1 = Warrior(name = z.get(), damage=15, health=80, speed=3, armorlvl=6)
    elif h.get() == 'Archer':
        guy1 = Archer(name = z.get(), damage=25, health=60, speed=2, armorlvl=9)
    elif h.get() == 'Commander':
        guy1 = Commander(name = z.get(), damage=40, health=50, speed=1, armorlvl=5)
    return(guy1)
window = Tk()
window.geometry('1500x450')
window.title("Fight")
lbl1 = Label(window, text="Enter character name", font=("Arial", 10))
lbl1.grid(column=0, row=0)
x = Entry(window,width=10)
x.grid(column=1, row=0)
lbl2 = Label(window, text="Enter character type: Warrior, Commander, Archer, Wizard.", font=("Arial", 10))
lbl2.grid(column=0, row=1)
y = Entry(window,width=10)
y.grid(column=1, row=1)
btn1 = Button(window, width=15, text="Create a character", command=createperson)
btn1.grid(column=1, row=2)

lbl3 = Label(window, text="Enter opponent's name", font=("Arial", 10))
lbl3.grid(column=2, row=0)
z = Entry(window,width=10)
z.grid(column=3, row=0)
lbl4 = Label(window, text="Enter character type: Warrior, Commander, Archer, Wizard.", font=("Arial", 10))
lbl4.grid(column=2, row=1)
h = Entry(window,width=10)
h.grid(column=3, row=1)
btn2 = Button(window, width=15, text="Create a character", command=createperson1)
btn2.grid(column=3, row=2)

def startf():
    fstart(guy0, guy1)
    lbl5 = Label(window, text=("Winner - ", winner, ", Loser - ", loser, ". Lives of the winner - ", whealth, ", Lives of the loser - ", lhealth), font=("Arial", 10))
    lbl5.grid(column=2, row = 4)
btn3 = Button(window, width=15, text="Start a fight!", command=startf)
btn3.grid(column=2, row=3)

window.mainloop()