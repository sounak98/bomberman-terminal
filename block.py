from entity import Entity

class Block(Entity):
    def __init__(self, row, col, grid):
        Entity.__init__(self, row, col)
        if grid.matrix[row][col] == 0:
            grid.matrix[row][col] = 'block'
