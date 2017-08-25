import config

class Wall:
    def __init__(self, grid):
        self.rows = grid.rows
        self.cols = grid.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if i in [0, self.rows-1] or j in [0, self.cols-1]:
                    grid.matrix[i][j] = 'wall'

        for i in range(1, grid.rows-1):
            for j in range(1, grid.cols-1):
                if i % 2 is 0 and j % 2 is 0:
                    grid.matrix[i][j] = 'wall'