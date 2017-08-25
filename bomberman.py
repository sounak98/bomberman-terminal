from person import Person

class Bomberman(Person):
    def move(self, k, grid):
        if k in ['j', 'a']: # left
            if grid.matrix[self.row][self.col-1] not in ['wall', 'block']:
                if grid.matrix[self.row][self.col-1] == 'monster':
                    grid.matrix[self.row][self.col] = 0
                else:
                    grid.matrix[self.row][self.col-1] = 'bomberman'
                    if grid.matrix[self.row][self.col] not in ['bomb0', 'bomb1', 'bomb2', 'bomb3', 'bomb4']:
                        grid.matrix[self.row][self.col] = 0
                    self.col = self.col - 1
        
        elif k in ['i', 'w']: # up
            if grid.matrix[self.row-1][self.col] not in ['wall', 'block']:
                if grid.matrix[self.row-1][self.col] == 'monster':
                    grid.matrix[self.row-1][self.col] = 0
                else:
                    grid.matrix[self.row-1][self.col] = 'bomberman'
                    if grid.matrix[self.row][self.col] not in ['bomb0', 'bomb1', 'bomb2', 'bomb3', 'bomb4']:
                        grid.matrix[self.row][self.col] = 0
                    self.row = self.row - 1
            
        elif k in ['l', 'd']: # right
            if grid.matrix[self.row][self.col+1] not in ['wall', 'block']:
                if grid.matrix[self.row][self.col+1] == 'monster':
                    grid.matrix[self.row][self.col] = 0
                else:
                    grid.matrix[self.row][self.col+1] = 'bomberman'
                    if grid.matrix[self.row][self.col] not in ['bomb0', 'bomb1', 'bomb2', 'bomb3', 'bomb4']:
                        grid.matrix[self.row][self.col] = 0
                    self.col = self.col + 1
            
        elif k in ['k', 's']: # down
            if grid.matrix[self.row+1][self.col] not in ['wall', 'block']:
                if grid.matrix[self.row+1][self.col] == 'monster':
                    grid.matrix[self.row+1][self.col] = 0
                else:
                    grid.matrix[self.row+1][self.col] = 'bomberman'
                    if grid.matrix[self.row][self.col] not in ['bomb0', 'bomb1', 'bomb2', 'bomb3', 'bomb4']:
                        grid.matrix[self.row][self.col] = 0
                    self.row = self.row + 1

    def __init__(self, row, col, grid):
        Person.__init__(self, row, col)
        self.health = 5
        if grid.matrix[row][col] is 0:
            grid.matrix[row][col] = 'bomberman'
            grid.display()