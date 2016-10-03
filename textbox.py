import graphics as g

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
        