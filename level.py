import config

class Level:
    def __init__(self, level):
        if level == 1:
            self.monsters_row = [1, 1, config.rows-2, config.rows-2]
            self.monsters_col = [1, config.cols-2, 1, config.cols-2]
            self.monsters_speed_factor = 10

        if level == 2:
            self.monsters_row = [1, 1, config.rows-2, config.rows-2, int(config.rows/2), int(config.rows/2)]
            self.monsters_col = [1, config.cols-2, 1, config.cols-2, 1, config.cols-2]
            self.monsters_speed_factor = 5

        if level == 3:
            self.monsters_row = [1, 1, config.rows-2, config.rows-2, int(config.rows/2), int(config.rows/2), 1, config.rows-2]
            self.monsters_col = [1, config.cols-2, 1, config.cols-2, 1, config.cols-2, int(config.cols/2), int(config.cols/2)]
            self.monsters_speed_factor = 3