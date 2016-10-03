import graphics as g
import entity
import time
import inventory
import stats as s

import battle

class character(entity.Entity):
    
    def __init__(self, win, grid, tile_x, tile_y, sprite, camera):
        entity.Entity.__init__(self,win,tile_x,tile_y,sprite,True)
        self._grid = grid
        self.camera = camera
        self.can_move = True
        self.direction = "North"
        self.inv_open = False
        self.actions = ["attack","guard"]
        self.inventory = inventory.Inventory()
        self.stats = s.Stats(100,10,10,10,0,0)

    def getActions(self):
        return self.actions

    def getActionAt(self,index):
        if (index < len(self.actions)):
            return self.actions[index]
        return None


    def perform_action(self,action,enemies):
        return_action = None
        if action == "attack":
            return_action = self.attack(enemies)
        if action == "guard":
            return_action = self.guard()
        return return_action

    #-------------------------------#
    #Here we will define all actions#
    def attack(self,enemies):
        print("Who do you want to attack?")
        while(True):
            enemy = self.window.getKey()
            if enemy.isdigit():
                if int(enemy) <= len(enemies)-1:
                    return ["attack",self,enemies[int(enemy)]]

    def guard(self):
        return ["guard",self,self]

    #-------------------------------#


    def add_gold(self,amount):
        self.stats.Gold += amount
        print("You have gained {} gold".format(amount))

    def add_xp(self,amount):
        self.stats.Xp += amount
        print("You have gained {} xp".format(amount))
        #TODO: Add levelup checking here
        
    def update(self):
        key_press = self.window.checkKey()
        if (key_press != None):
            
            if self.can_move:
                if key_press == 'a' or key_press == "Left":
                    self.direction = "West"
                    if self._grid.GetTileAt(self.x - 1, self.y).is_passable():
                        self.x -= 1
                        self.camera.update_position(-1,0)
                        self._check_floor()
                if key_press == 's' or key_press == "Down":
                    self.direction = "South"
                    if self._grid.GetTileAt(self.x, self.y + 1).is_passable():
                        self.y += 1
                        self.camera.update_position(0,1)
                        self._check_floor()
                if key_press == 'd' or key_press == "Right":
                    self.direction = "East"
                    if self._grid.GetTileAt(self.x + 1, self.y).is_passable():
                        self.x += 1
                        self.camera.update_position(1,0)
                        self._check_floor()
                if key_press == 'w' or key_press == "Up":
                    self.direction = "North"
                    if self._grid.GetTileAt(self.x, self.y - 1).is_passable():
                        self.y -= 1
                        self.camera.update_position(0,-1)
                        self._check_floor()
                        
                if key_press == 'e' and self.inv_open != True:
                    self.inv_open = True
                    self.inventory.open_inventory(self)
                    self.inv_open = False
                    
                if key_press == 'r':
                    battle.Battle(self)
            if key_press == "Return":
                self._interact()
            time.sleep(1/30)
        
    def _check_floor(self):
        tile = self._grid.GetTileAt(self.x,self.y).entity
        for t in tile:
            if type(t) == entity.Teleporter:
                
                t.activate(self)
            
    def _interact(self):
        dx, dy = 0, 0
        if (self.direction == "North"):
                dx, dy = 0,-1
        if (self.direction == "East"):
                dx, dy = 1,0
        if (self.direction == "West"):
                dx, dy = -1,0
        if (self.direction == "South"):
                dx, dy = 0,1
        
        tile = self._grid.GetTileAt(self.x+dx,self.y+dy)
        for ent in tile.entity:
            if type(ent) is entity.Talkable:
                ent.interact(self)
            if type(ent) is entity.Item_Container and ent.taken == False:
                print("You have picked up a {}".format(ent.containing_item.Name))
                self.inventory.add_item(ent.containing_item, 1)
                ent.textbox.interact(self)
                
                ent.use(self)
            
    def __repr__(self):
        return "Hero"
        
        
    
import random

class Monster(entity.Entity):

    def __init__(self,win,_id,name,x,y,image_name,stats,actions):
        entity.Entity.__init__(self,win,x,y,image_name,True)
        self.image = g.Image(g.Point(x,y), image_name)
        self.id = _id
        self.name = name
        self.stats = s.Stats(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5])
        self.actions = actions
        
    def create_action(self):
        action = random.randrange(len(self.actions))
        return self.actions[action]

    def update_formation(self):
        self.image.undraw()
        self.image = g.Image(g.Point(self.x,self.y),self.image_name)
        self.image.draw(self.window)

    def __repr__(self):
        return self.name
        
monster_list = []
formation_1 = [g.Point(350,250)]
formation_2 = [[g.Point(350,250), g.Point(350-64,314)],[g.Point(350,314+32), g.Point(350-64,314)]]
formation_3 = [[g.Point(350,250), g.Point(350-64,314), g.Point(350,314+32)]]
        
def CreateBattleFormation(monster_count):
    print(monster_list)
    monsters = []
    formation = None
    
    if monster_count == 1:
            formation = formation_1
    if monster_count == 2:
        formation = formation_2[random.randrange(len(formation_2)-1)]
    if monster_count == 3:
        formation = formation_3[0]

    for i in range(monster_count):
        monster = monster_list[random.randrange(len(monster_list))]
        new_monster = Monster(monster.window,monster.id,monster.name,monster.x,monster.y,monster.image_name,[0,0,0,0,0,0],monster.actions)
        new_monster.stats = monster.stats
        new_monster.x = formation[i].getX()
        new_monster.y = formation[i].getY()
        monsters.append(new_monster)
        
    return monsters
        
        

    return monsters
    