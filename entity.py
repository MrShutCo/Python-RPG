import graphics as g
import level_reader
import textbox

class Entity:

    def __init__(self, window, x, y, image_name, is_passable):
        self.window = window
        self.x = x
        self.y = y
        self.image_name = image_name
        self.is_passable = is_passable
        self.image = g.Image(g.Point(x * 32 + 16, y * 32 + 16),image_name)
        
        self.image.draw(self.window)
        
class Talkable(Entity):
    
    def __init__(self,window,x,y,image_name,messages):
        Entity.__init__(self,window,x,y,image_name,False)
        self.textbox = textbox.TextBox(window,messages)
        
        
    def interact(self, hero):
        self.textbox.interact(hero)
            
        
class Teleporter(Entity):
    
    def __init__(self,window,_map,x,y,image_name,teleporter):
        Entity.__init__(self,window,x,y,image_name,True)
        self.teleporter = teleporter
        self.grid = _map
        
    def activate(self, hero):
        self.grid.ClearGrid()
        hero.image.undraw()
        level_reader.load_level(self.window,self.grid,self.teleporter[0])
        hero.image.draw(self.window)
        hero.camera.restart()
        
        hero.camera.update_position(self.teleporter[1] - hero.x, self.teleporter[2] - hero.y)
        
        hero.x = self.teleporter[1]
        hero.y = self.teleporter[2]

class Item_Container(Entity):
    
    def __init__(self,window,x,y,image_name,item,is_chest):
        if is_chest:
            Entity.__init__(self,window,x,y,"Sprites/chest_closed.gif",False)
        else:
            Entity.__init__(self,window,x,y,image_name,False)
        
        self.containing_item = item
        self.is_chest = is_chest
        self.taken = False
        self.textbox = textbox.TextBox(window,["You have obtained {}".format(item.Name)])
       

    def use(self, hero):
        if self.is_chest:
            #TODO: Convert this code over to when you change a room
            temp_image = g.Image(g.Point(self.x*32+16 - hero.camera.getTotalX(),self.y*32+16 - hero.camera.getTotalY()),"Sprites/chest_open.gif")
            #hero._grid.SetTileAt(self)
            #self.image = temp_image
            self.image.undraw()
            self.image = hero._grid.changeImage(self.image,temp_image)
            self.image.draw(self.window)
        else:
            self.is_passable = True
            self.image.undraw()
        self.taken = True
        
        