import graphics as g

class Tile:

    def __init__(self, window, tileX, tileY, tileSize):
        self.window = window
        self.X = tileX
        self.Y = tileY
        self.TileSize = tileSize
        self.entity = []
        self._drawCell()
        
    def SetEntity(self,entity):
        self.entity.append(entity)
        
    def is_passable(self):
        for i in self.entity:
            if i.is_passable == False:
                return False
        return True
        
    def _drawCell(self):
        
        self.upperL = g.Point(self.X * self.TileSize, self.Y * self.TileSize)
        self.lowerR = g.Point(self.X * self.TileSize + self.TileSize, self.Y * self.TileSize + self.TileSize)
        self.square = g.Rectangle(self.upperL,self.lowerR)
        self.square.draw(self.window)
        
    def __str__(self):
        return str(self.X) + "," + str(self.Y)

class Grid:
    
    def __init__(self, window, x, y, tileSize):
        self.Width = x
        self.Height = y
        self.Window = window
        self.TileSize = tileSize
        self.cells = []
        self.creatures = []        
        self._createGrid()
            
    def ClearGrid(self):
        for tile in self.cells:
            for ent in tile.entity:
                ent.image.undraw()
            tile.entity = []
        
    def changeImage(self,image1,image2):
        for x in range(image1.getWidth()):
            for y in range(image1.getHeight()):
                color = image2.getPixel(x,y)
                if color == [0,0,0]:
                    continue
                image2.setPixel(x,y,g.color_rgb(color[0],color[1],color[2]))
        return image2

        
        
    def GetTileAt(self,x,y):
        return self.cells[y * self.Width + x]
            
    def SetTileAt(self,entity):
        temp = self.GetTileAt(entity.x,entity.y)
        temp.SetEntity(entity)
        
            
    def GetIndexOfTile(self, index):
        return int(index/self.Width), index % self.Width 
        
    def _createGrid(self):
        for x in range(self.Width):
            for y in range(self.Height):
                self.cells.append(Tile(self.Window,y,x,self.TileSize))
                