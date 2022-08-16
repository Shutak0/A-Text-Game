from random import random
from random import randint

class Unit:
    def __init__(self, vid, name, damage, health, speed, armorlvl):
        self.vid = vid
        self.name = name
        self.damage = damage
        self.health = health
        self.speed = speed
        self.armorlvl = armorlvl
    def hitenemy(self, aname):
        hit = 0
        if self.vid == 'Magic':  #Crit chance
            crit = randint(1, 10)
        elif self.vid == 'Voin':
            crit = randint(1, 7)
        elif self.vid == 'Strelok':
            crit = randint(1, 9)
        elif self.vid == 'Komandir':
            crit = randint(1, 6) 
        if crit <= 2:
            hit = hit + (crit*10)
        ukloneniechance = (aname.speed*10 - aname.armorlvl/2) * randint(0, 5) #evasion chance
        misschance = randint(0, 10) + aname.armorlvl #miss chance
        hit = hit + self.damage - aname.armorlvl
        if misschance > 15:
            hit = 0
        if ukloneniechance >= 50:
            hit = 0
        aname.health = aname.health - hit
        print(self.name, ' did the hit. Current HP: ', self.health, ' Enemy HP: ', aname.health)
class Magic(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Magic', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Voin(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Voin', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Strelok(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Strelok', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Komandir(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Komandir', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
def fstart(dude0, dude1):
    if dude0.health <= 0:
        return(print('Another one bites the dust! Winner: ', dude1.name, ', Loser: ', dude0.name))
    elif dude1.health <= 0:
        return(print('Another one bites the dust! Winner: ', dude0.name, ', Loser: ', dude1.name))
    elif dude1.health == dude0.health:
        return(print('Draw'))
    dude0.hitenemy(dude1)
    dude1.hitenemy(dude0)
    return(fstart(dude0=dude0, dude1=dude1))
guy0 = Magic(name = 'Vasya', damage=20, health=100, speed=1, armorlvl=8)
guy1 = Voin(name = 'Petya', damage=15, health=80, speed=3, armorlvl=6)
guy2 = Strelok(name = 'Ivan', damage=25, health=60, speed=2, armorlvl=9)
guy3 = Komandir(name = 'Kolyan', damage=40, health=50, speed=1, armorlvl=5)
fstart(guy0, guy1)