import graphics as g

class Inventory:

    def __init__(self):
        self.items = {}
        self.window = None
        
        
    def open_inventory(self, hero):
        self.window = g.Rectangle(g.Point(0,0),g.Point(500,500))
        self.window.setFill("blue")
        self.window.draw(hero.window)
        
        self.item_menu_text = g.Text(g.Point(250,25),"Inventory")
        self.item_menu_text.draw(hero.window)
        
        self.stat_menu_text = g.Text(g.Point(250,250),"Stats")
        #Do all that here
        
        #--------------Draw Items---------------
        item_values = []
        item_images = []
        
        i = 0
        y = 64 + 8
        
        for item in self.items:
            #Make the grid if theres too much
            if (i * 32 + 64 + 8 > 500):
                i = 0
                y += 32
            item_images.append(item.image.clone())
            text = g.Text(g.Point(32 * i + 64 + 8,y), str(self.items[item]))
            item_values.append(text)
            
            item_images[i].draw(hero.window)
            item_images[i].move(32 * i + 64,y - 8)
            
            item_values[i].draw(hero.window)
            i += 1
        #------------Draw Stats-----------------       
        health = g.Text(g.Point(250,290),"Health: {}/{}".format(hero.stats.CurrentHp, hero.stats.MaxHp))
        health.draw(hero.window)
        
        attack = g.Text(g.Point(250,310),"Attack: {}".format(hero.stats.Attack))
        attack.draw(hero.window)
        
        defense = g.Text(g.Point(250,330),"Defense: {}".format(hero.stats.Defense))
        defense.draw(hero.window)
        
        gold = g.Text(g.Point(250,350),"Gold: {}".format(hero.stats.Gold))
        gold.draw(hero.window)
        
        xp = g.Text(g.Point(250,370),"Xp: {}".format(hero.stats.Xp))
        xp.draw(hero.window)
            
        hero.window.getMouse()
        
        for item in item_images:
            item.undraw()
            del(item)
            
        for text in item_values:
            text.undraw()
            del(text)
            
        self.window.undraw()
        self.item_menu_text.undraw()
        health.undraw()
        attack.undraw()
        defense.undraw()
        gold.undraw()
        xp.undraw()
        
    def add_item(self,item, amount):
        if (item not in self.items):
            self.items[item] = amount
        else:
            self.items[item] += amount
        
    def delete_item(self,item):
        self.items.remove(item)
        
    def show_inventory(self):
        for key, value in self.items.items():
            print(key, value)
            
class Item:
    
    def __init__(self,_id,_name,_class,_desc,file_name):
        self.Id = _id
        self.Name = _name
        self.Class = _class
        self.Desc = _desc
        self.File_name = file_name
        self.image = g.Image(g.Point(0,0),file_name)
        #TODO: make this polymorphic
    
    def clone(self):
        other = Item(self.Id,self.Name,self.Class,self.Desc,self.File_name)
        other.image = self.image.clone()
        return other
        
def getItemByName(item_name, prototypes):
    for item in prototypes:
        if item.Name == item_name:
            return item
    return None
        