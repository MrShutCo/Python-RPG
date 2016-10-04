import random
from graphics import *

class Stats:
    
    def __init__(self,_hp,_atk,_def,_spd,_gold,_xp):
        self.CurrentHp = _hp
        self.level = 1
        self.MaxHp = _hp
        self.Attack = _atk
        self.Defense = _def 
        self.Speed = _spd
        self.Gold = _gold
        self.Xp = _xp
        self.IsDead = False
        self.health_bar = Rectangle(Point(200,425),Point(300,445))
        self.health_bar.setFill("black")
        self.actual_health = None
        

    def DrawHealthBar(self,win):
        self.win = win
        self.actual_health = Rectangle(Point(200,425),Point(200 + self.CurrentHp / self.MaxHp * 100,445))
        self.actual_health.setFill("green")
        self.health_bar.draw(win)
        self.actual_health.draw(win)
        
    def UndrawHealthBar(self):
        self.actual_health.undraw()
        self.health_bar.undraw()

    def Damage(self,dmg):
        self.CurrentHp -= dmg
        self.CurrentHp = max(0,self.CurrentHp)

        if (self.actual_health != None):
            self.actual_health.undraw()
            self.actual_health = Rectangle(Point(200,425),Point(200 + self.CurrentHp / self.MaxHp * 100,445))
            self.actual_health.setFill("green")
            self.actual_health.draw(self.win)

        if self.CurrentHp == 0:
            self.IsDead = True
            
    def CheckLevelUp(self):
        if self.Xp >= self._level_up():
            print("You have leveled up!")
            self.level += 1
            self.Attack += random.randrange(5)
            self.Defense += random.randrange(3)
            self.Speed += random.randrange(2)
            self.Xp = 0

    def _level_up(self):
        return self.level**2 / 4 + 15
            
    def __str__(self):
        return "Hp: {}/{} Atk: {}, Def: {}, Spd: {}".format(self.CurrentHp,self.MaxHp,self.Attack,self.Defense,self.Speed)

    def Heal(self,amount):
        self.CurrentHp += amount
        self.CurrentHp = min(self.CurrentHp, self.MaxHp)
        
    
        
    