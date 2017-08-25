import os, sys, signal
import time
from random import randint
from termcolor import cprint

import config
import asciiart
from getchunix import GetchUnix
from alarmexception import AlarmException
from grid import Grid
from wall import Wall
from block import Block
from bomberman import Bomberman
from monster import Monster
from bomb import Bomb
from level import Level

getch = GetchUnix()

class Game:
    def alarmHandler(self, signum, frame):
        raise AlarmException

    def input_to(self, timeout=0.1):
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getch()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    def game_won(self):
        os.system('cls || clear')
        asciiart.game_won_screen()
        exit(0)

    def game_lost(self):
        os.system('cls || clear')
        asciiart.game_over_screen()
        exit(0)

    def check_if_dead(self, monsters, bomberman, grid):
        if grid.matrix[bomberman.row][bomberman.col] == 0:
            self.game_lost()

        game_won = True if len(monsters) > 0 else False
        for monster in monsters:
            if grid.matrix[monster.row][monster.col] == 'monster':
                game_won = False
            elif grid.matrix[monster.row][monster.col] == 0:
                monsters.remove(monster)
                self.score += 100

        if game_won is True:
            self.game_won()

    def block_arrangement(self, grid):
        blocks = []
        for i in range(len(config.blocks_row)):
            blocks.append(Block(config.blocks_row[i], config.blocks_col[i], grid))

        return blocks

    def print_score(self):
        cprint("\n\t\t\t\t    SCORE\t%s" % self.score, 'yellow', attrs=['bold', 'blink'])
        cprint("\n  CONTROLS: i/w - UP, j/a - LEFT, k/s - DOWN, l/d - RIGHT, x - Plant Bomb, q - Quit", 'magenta')

    def check_if_block_destroyed(self, blocks, grid):
        for block in blocks:
            if grid.matrix[block.row][block.col] == 0:
                blocks.remove(block)
                self.score += 20

    def __init__(self, level=1):
        level = Level(level)
        
        self.score = 0

        grid = Grid(config.rows, config.cols)

        wall = Wall(grid)

        bomberman = Bomberman(config.init_row, config.init_col, grid)

        monsters = []

        for i in range(len(level.monsters_row)):
            monsters.append(Monster(level.monsters_row[i], level.monsters_col[i], grid))

        blocks = self.block_arrangement(grid)
        
        for i in range(10):
            pass
        
        bombs = []
        
        count = 0

        while True:
            count = count + 1 if count is not level.monsters_speed_factor else 0
            if count is level.monsters_speed_factor:
                if len(bombs) > 0:
                    for bomb in bombs:
                        bomb.seconds_left = bomb.seconds_left - 1
                        grid.matrix[bomb.row][bomb.col] = 'bomb' + str(bomb.seconds_left)
                        if bomb.seconds_left is 0:
                            bomb.explode(grid)
                            bombs.remove(bomb)
                            self.check_if_dead(monsters, bomberman, grid)
                            self.check_if_block_destroyed(blocks, grid)
                
                for monster in monsters:
                    monster.move(grid)
                self.check_if_dead(monsters, bomberman, grid)
                grid.display()
                self.print_score()

            k = self.input_to()

            if k == 'x':
                bombs.append(Bomb(bomberman.row, bomberman.col, grid))
            
            elif k == 'q':
                exit(0)

            elif k in ['w', 'a', 's', 'd', 'i', 'j', 'k', 'l']:
                bomberman.move(k, grid)
                grid.display()
                self.print_score()
