from graphics import Image,Point,Rectangle,Text
import character
import textbox

import operator
import time
import random

class Battle:


    #TODO: Have all the little info about each monster contained in the monster class, and not cluttering up here
    def __init__(self,hero):
        self.hero = hero
        self.enemies = character.CreateBattleFormation(random.choice([1,2,3]))
        
        self.window = hero.window
        
        self.background = Image(Point(250,250),"Sprites/forest.gif")
        self.background.draw(self.window)
        
        self.options_bar = Rectangle(Point(0,400),Point(500,500))
        self.options_bar.setFill("blue")
        self.options_bar.draw(self.window)
        
        self.select_target = Text(Point(75,314-48),"Select a target 0-{}".format(len(self.enemies)-1))
        
        self._draw_sprites()
        self._start_battle()
        self._undraw_sprites()
        
    def _undraw_sprites(self):
        self.hero_image.undraw()
        self.background.undraw()
        
        self.hero.stats.UndrawHealthBar()

        for enemy in self.enemies:
            enemy.image.undraw()
            enemy.indexer.undraw()
            enemy.name_text.undraw()
            enemy.stats.CurrentHp = enemy.stats.MaxHp

        self.options_bar.undraw()
        
        for option in self.options:
            option.undraw()
        
    def _draw_sprites(self):
        self.hero_image = Image(Point(75,250),"Sprites/hero_battle_2.gif")
        self.hero_image.draw(self.window)

        self.options = []
        y = 415
        for option in range(len(self.hero.getActions())):
            self.options.append(Text(Point(100,y),"{}: {}".format(option,self.hero.getActionAt(option).capitalize())))
            self.options[option].draw(self.window)
            self.options[option].setSize(15)
            y += 25

        self.enemy_names = []
        self.hero.stats.DrawHealthBar(self.window)
        
        y = 415
        for enemy in range(len(self.enemies)):
            curr_enemy = self.enemies[enemy]
            curr_enemy.update_formation()
            curr_enemy.set_battle_formation(400,y,enemy)
            y += 25
            
        for name in self.enemy_names:
            name.draw(self.window)

        
    def _start_battle(self):
        #All logic will go here
        
        is_over = False
        has_won = True
        sum_hp = 0
        for enemy in self.enemies:
            sum_hp += enemy.stats.CurrentHp
        
        average_enemy_hp = float(sum_hp/len(self.enemies))
        
        print("Enemy health", average_enemy_hp)
        print("Your health", self.hero.stats.CurrentHp)
        print("Current enemies fighting: {}".format(self.enemies))

        #Todo, add flag to possibly run away from encounter
        while (is_over == False):
            
            #Orderings
            speeds = []
            action_queue = []
            speeds.append(self.hero)
            for enemy in self.enemies:
                if (enemy.stats.CurrentHp != 0):
                    speeds.append(enemy)
            
            speeds.sort(key=operator.attrgetter("stats.Speed"),reverse=True)

            if average_enemy_hp == 0.0:
                print(average_enemy_hp)
                is_over = True
                break
            
            #Determine what actions everyone is going to take
            for player in speeds:
                
                #Check if its the players turn
                if type(player) == character.character:
                    action = None
                    possible_actions = player.getActions()

                    #Keep getting key presses until something good happens
                    while action == None:
                        key_press = self.window.getKey()
                        #User has selected a number, check if its an ok action
                        if key_press.isdigit():
                           key_value = int(key_press)
                           #Get the action, and check its valid
                           action = player.getActionAt(key_value)
                           if action != None:
                               self.options[key_value].setFill("red")
                               #Queue up and create the proper action
                               action = player.perform_action(action,self.enemies)
                               if action != None:
                                   self.options[key_value].setFill("black")
                                   action_queue.append(action)
                    
                #Otherwise, add a random action based on the enemy
                else:
                    if (~player.stats.IsDead):
                        #Right now it assumes that the target will always be the hero
                        action_queue.append([player.create_action(),player,self.hero])
                        #time.sleep(0.5)
                    
            #Now we process the actions
            #TODO: flesh out more
            if is_over == False:
                print("\nActions taken this turn: ")
                for action in action_queue:
                    if is_over == False:
                        if action[0] == "attack":
                            calc_damage = random.randint(0,4) + action[1].stats.Attack - action[2].stats.Defense / 2
                            textbox.MessageBox(self.window,"{} attacked {} for {} damage".format(action[1],action[2],calc_damage))
                            action[2].stats.Damage(calc_damage)
                            if action[2].stats.CurrentHp == 0:
                                action[2].image.undraw()
                                if type(action[2]) == character:
                                    textbox.MessageBox(self.window,"You dead")
                                    is_over = True
                                    has_won = False
                                action[2].name_text.undraw()
                                action[2].indexer.undraw()
                        if action[0] == "guard":
                            textbox.MessageBox(self.window,"{} guarded".format(action[1]))
                        if action[0] == "run":
                            textbox.MessageBox(self.window,"You ran away like a wimp")
                            is_over = True
                            has_won = False
                        sum_hp = 0
                        for enemy in self.enemies:
                            print("{} has {}/{}hp".format(enemy,enemy.stats.CurrentHp,enemy.stats.MaxHp))
                            sum_hp += enemy.stats.CurrentHp
        
                        average_enemy_hp = float(sum_hp/len(self.enemies))
                        if average_enemy_hp == 0:
                            is_over = True
                            has_won = True
                            #break
                    
            print()
            
            print(average_enemy_hp)
        #Now that we are done, lets do stuff!

        #TODO: Add options for losing, as well as possibly gaining items
        if self.hero.stats.CurrentHp != 0 and has_won:
            textbox.MessageBox(self.window,"Victory!")
            total_gold_won = 0
            total_xp_won = 0
            for enemy in self.enemies:
                total_gold_won += enemy.stats.Gold
                total_xp_won += enemy.stats.Xp
            self.hero.add_gold(total_gold_won)
            textbox.MessageBox(self.window,"You gained {} gold".format(total_gold_won))
            textbox.MessageBox(self.window,"You gained {} xp".format(total_xp_won))

            self.hero.add_xp(total_xp_won)
            self.hero.stats.CheckLevelUp()
