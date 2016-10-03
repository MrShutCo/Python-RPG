
class Camera:

    def __init__(self, grid):
        self.offset_x = 0
        self.offset_y = 0
        self.total_x = 0
        self.total_y = 0
        self.grid = grid
        self.character = None
        
    def update_position(self, dx, dy):

        self.offset_x += dx 
        self.offset_y += dy
        self.total_x += dx
        self.total_y += dy
        for i in self.grid.cells:
            for ent in i.entity:                    
                ent.image.move(-dx*32,-dy*32)
                    
    def restart(self):
        self.offset_x = 0
        self.offset_y = 0
        
    def getTotalX(self):
        return self.total_x * 32
        
    def getTotalY(self):
        return self.total_y * 32
        
    def moveEntity(self,entity):
        entity.image.move(-self.total_x*32,-self.total_y*32)