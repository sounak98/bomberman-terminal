from entity import Entity
import time

class Bomb(Entity):
    def explode(self, grid):
        grid.matrix[self.row][self.col] = 0
        if grid.matrix[self.row][self.col-1] in ['block', 'monster', 'bomberman', 0]:
            grid.matrix[self.row][self.col-1] = 'left'

        if grid.matrix[self.row-1][self.col] in ['block', 'monster', 'bomberman', 0]:
            grid.matrix[self.row-1][self.col] = 'up'
        
        if grid.matrix[self.row][self.col+1] in ['block', 'monster', 'bomberman', 0]:
            grid.matrix[self.row][self.col+1] = 'right'

        if grid.matrix[self.row+1][self.col] in ['block', 'monster', 'bomberman', 0]:
            grid.matrix[self.row+1][self.col] = 'down'

        if grid.matrix[self.row][self.col] in ['block', 'monster', 'bomberman', 0]:
            grid.matrix[self.row][self.col] = 'center'
        
        grid.display()
        time.sleep(0.3)

        grid.matrix[self.row][self.col] = 0

        if grid.matrix[self.row][self.col-1] == 'left':
            grid.matrix[self.row][self.col-1] = 0

        if grid.matrix[self.row-1][self.col] == 'up':
            grid.matrix[self.row-1][self.col] = 0
        
        if grid.matrix[self.row][self.col+1] == 'right':
            grid.matrix[self.row][self.col+1] = 0

        if grid.matrix[self.row+1][self.col] == 'down':
            grid.matrix[self.row+1][self.col] = 0

        grid.display()

    def __init__(self, row, col, grid):
        Entity.__init__(self, row, col)
        grid.matrix[row][col] = 'bomb' + str(4)
        self.seconds_left = 4
        grid.display()