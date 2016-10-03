class Stats:
    
    def __init__(self,_hp,_atk,_def,_spd,_gold,_xp):
        self.CurrentHp = _hp
        self.MaxHp = _hp
        self.Attack = _atk
        self.Defense = _def 
        self.Speed = _spd
        self.Gold = _gold
        self.Xp = _xp
        self.IsDead = False
        
    def Damage(self,dmg):
        self.CurrentHp -= dmg
        self.CurrentHp = max(0,self.CurrentHp)
        if self.CurrentHp == 0:
            self.IsDead = True
            
    def Heal(self,amount):
        self.CurrentHp += amount
        self.CurrentHp = min(self.CurrentHp, self.MaxHp)
        
    
        
    