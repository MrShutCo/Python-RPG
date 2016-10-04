import graphics as g
import time

class TextBox:

    def __init__(self,win,messages):
        self.window = win
        self.messages = messages
        self.counter = 0
        self.current_message = self.messages[0]
        self.talk_box = None
        self.text = None
      
        
    def interact(self,hero):
        self.talk_box = g.Rectangle(g.Point(0,0),g.Point(self.window.getWidth(), 150))
        self.talk_box.setFill("blue")
        self.talk_box.draw(self.window)
        self.text = g.Text(g.Point(self.window.getWidth()/2,75),self.current_message)
        self.text.draw(self.window)
        self.counter += 1
        
        while (True):
            if (self.window.checkKey() == "Return"):
                if (self.counter == len(self.messages)):
                    break
                self.current_message = self.messages[self.counter]
                self.text.setText(self.current_message)
                self.counter += 1
                
        self.counter = 0
        self.current_message = self.messages[self.counter]
        self.text.undraw()
        self.talk_box.undraw()
        
class MessageBox():

    def __init__(self,win,message):
        self.talk_box = g.Rectangle(g.Point(0,0),g.Point(500,50))
       
        self.talk_box.setFill("blue")
        self.text = g.Text(g.Point(250,25),message)
        self.talk_box.draw(win)
        self.text.draw(win)
        win.update()
        time.sleep(1)
        self.talk_box.undraw()
        self.text.undraw()

class Selection():

    def __init__(self,win,start,options):
        self.option_texts = []
        self.current_option = options[0]
        self.tracker = 0
        self.win = win
        y = start[1]
        for option in range(len(options)):
            self.option_texts.append(g.Text(g.Point(start[0],y),options[option]))
            self.option_texts[option].draw(win)
            y += 15
        self.option_texts[0].setFill("red")

    def undraw(self):
        for option in self.option_texts:
            option.undraw()

    def getSelection(self):
        while True:
            key_press = self.win.getKey()
            if key_press == "Down":
                self.next_option()
            if key_press == "Up":
                self.previous_option()
            if key_press == "Return":
                #self.undraw()
                return self.current_option

    def next_option(self):
        self.option_texts[self.tracker].setFill("black")
        self.tracker += 1
        if self.tracker > len(self.option_texts) - 1:
            self.tracker = 0;
        self.current_option = self.option_texts[self.tracker]
        self.option_texts[self.tracker].setFill("red")

    def previous_option(self):
        self.option_texts[self.tracker].setFill("black")
        self.tracker -= 1
        if self.tracker < 0:
            self.tracker = len(self.option_texts)-1;
        self.current_option = self.option_texts[self.tracker]
        self.option_texts[self.tracker].setFill("red")

