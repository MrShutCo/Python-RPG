import grid
import character as char
import graphics as g
import level_reader
import camera as c
from entity import Item_Container
import inventory as i

def main():
    print("Start")
    win = g.GraphWin("RPG", 500, 500, autoflush=False)
    Grid = grid.Grid(win,64,64,32)
    win.setBackground("green")
    #Grid.SetTileAt(3,3,"wall.gif",False)
    
    is_playing = True
    
    #Load in all the data
    level_reader.load_level(win,Grid,"Rooms/room_1.gif")
    item_list, char.monster_list = level_reader.load_defenitions(win,"Rooms/room_1_info.json")
    npcs = level_reader.load_objects(win,"Rooms/room_1_data.json")
    
    for npc in npcs:
        Grid.SetTileAt(npc)
    
    #TODO: Change this so it reads from JSON
    Grid.SetTileAt(Item_Container(win,15,15,None,i.getItemByName("Potion", item_list),True))
    Grid.SetTileAt(Item_Container(win,17,15,None,i.getItemByName("Apple", item_list),True))
    Grid.SetTileAt(Item_Container(win,19,15,None,i.getItemByName("Potion", item_list),True))
    Grid.SetTileAt(Item_Container(win,13,15,None,i.getItemByName("Apple", item_list),True))
    Grid.SetTileAt(Item_Container(win,45,45,"Sprites/sword_wooden.gif",i.getItemByName("Wooden Sword", item_list),False))
    
    #Grid.SetTileAt(Teleporter(win,Grid,4,4,"npc.gif",("Rooms/room_2.gif",15,15)))
    Camera = c.Camera(Grid)
    hero = char.character(win,Grid,8,8,"Sprites/hero.gif",Camera)
    Camera.character = hero
    while (is_playing):
        hero.update()
    win.getMouse()
    win.close()
    
if __name__ == "__main__":
    main()