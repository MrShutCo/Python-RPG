import grid as g
import graphics as graph

import inventory as i
import entity as e

import character as c

import json

def load_level(win, grid, file_name):
    image = graph.Image(graph.Point(0,0), file_name)
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            color = image.getPixel(x,y)
            if color == [0,0,0]:
                grid.SetTileAt(e.Entity(win,x,y,"Sprites/tree.gif",False))
            if color == [255,255,0]:
                grid.SetTileAt(e.Entity(win,x,y,"Sprites/floor.gif",True))
            #if color == [255,255,255]:
            #    grid.SetTileAt(e.Entity(win,x,y,"Sprites/grass.gif",True))
            if color == [255,0,0]:
                grid.SetTileAt(e.Entity(win,x,y,"Sprites/brick.gif",False))
            if color == [0,255,0]:
                grid.SetTileAt(e.Entity(win,x,y,"Sprites/npc.gif",False))
            
                
def load_defenitions(win,file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
    prototypes_items = []
    prototypes_monsters = []
    #TODO: Make dynamic
    for item in range(5):
        item_data = data["items"][item]
        new_item = i.Item(item_data["id"],item_data["name"],item_data["class"],item_data["description"], item_data["file_name"])
        prototypes_items.append(new_item)
    
    
    for monster in range(4):
        monster_data = data["monsters"][monster]
        monster_info = monster_data["stats"].split(",")
        monster_stats = []

        monster_actions = list(monster_data["actions"].keys())
        monster_chances = list(monster_data["actions"].values())

        print(monster_actions,monster_chances)
        
        for stats in monster_info:
            monster_stats.append(int(stats))
        print(monster_stats)
        new_monster = c.Monster(win,monster_data["id"],monster_data["name"],-50,-50,monster_data["file_name"],monster_stats,monster_actions,monster_chances)
        prototypes_monsters.append(new_monster)
        
    return prototypes_items, prototypes_monsters
    
def load_objects(win,file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
    objects = []
    for obj in range(2):
        obj_data = data["npcs"][obj]
        obj_coord = obj_data["position"].split(",")
        print(obj_coord)
        new_obj = e.Talkable(win,int(obj_coord[0]),int(obj_coord[1]),obj_data["file_name"],obj_data["text"])
        objects.append(new_obj)
    return objects
    
    