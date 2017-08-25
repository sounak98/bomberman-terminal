from random import randint

from person import Person

class Monster(Person):
    def move(self, grid):
        moved = False
        while not moved:
            num = randint(0, 3)
            if num is 0: # left
                if grid.matrix[self.row][self.col-1] in [0, 'bomberman']:
                    grid.matrix[self.row][self.col-1] = 'monster'
                    grid.matrix[self.row][self.col] = 0
                    self.col = self.col-1
                    moved = True
            
            if num is 1: # up
                if grid.matrix[self.row-1][self.col] in [0, 'bomberman']:
                    grid.matrix[self.row-1][self.col] = 'monster'
                    grid.matrix[self.row][self.col] = 0
                    self.row = self.row-1
                    moved = True

            if num is 2: # right
                if grid.matrix[self.row][self.col+1] in [0, 'bomberman']:
                    grid.matrix[self.row][self.col+1] = 'monster'
                    grid.matrix[self.row][self.col] = 0
                    self.col = self.col+1
                    moved = True

            if num is 3: # right
                if grid.matrix[self.row+1][self.col] in [0, 'bomberman']:
                    grid.matrix[self.row+1][self.col] = 'monster'
                    grid.matrix[self.row][self.col] = 0
                    self.row = self.row+1
                    moved = True

    def __init__(self, row, col, grid):
        Person.__init__(self, row, col)
        self.health = 1
        if grid.matrix[row][col] is 0:
            grid.matrix[row][col] = 'monster'
            # grid.display()