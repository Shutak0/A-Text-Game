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
        if self.vid == 'Magic':  #crit chance
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
class Wizard(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Magic', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Warrior(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Voin', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Archer(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Strelok', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)
class Commander(Unit):
    def __init__(self, name, damage, health, speed, armorlvl):
        super().__init__(vid='Komandir', name=name, damage=damage, health=health, speed=speed, armorlvl=armorlvl)