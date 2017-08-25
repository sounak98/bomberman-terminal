import os
from termcolor import colored, cprint

class Grid:
    def scaleup(self):
        self.matrix_scaledup = []
        for i in range(self.rows * 2):
            self.matrix_scaledup.append([])
            for j in range(self.cols * 4):
                self.matrix_scaledup[i].append(0)

        for i in range(self.rows):
            for j in range(self.cols):
                i_su = i * 2
                j_su = j * 4

                if self.matrix[i][j] is 'wall':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('X', 'cyan')

                elif self.matrix[i][j] == 'block':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('∆', 'blue')

                elif self.matrix[i][j] == 'monster':
                    self.matrix_scaledup[i_su][j_su] = colored('^', 'magenta')
                    self.matrix_scaledup[i_su][j_su+1] = colored('[', 'magenta')
                    self.matrix_scaledup[i_su][j_su+2] = colored(']', 'magenta')
                    self.matrix_scaledup[i_su][j_su+3] = colored('^', 'magenta')
                    self.matrix_scaledup[i_su+1][j_su] = colored(' ', 'magenta')
                    self.matrix_scaledup[i_su+1][j_su+1] = colored(']', 'magenta')
                    self.matrix_scaledup[i_su+1][j_su+2] = colored('[', 'magenta')
                    self.matrix_scaledup[i_su+1][j_su+3] = colored(' ', 'magenta')

                elif self.matrix[i][j] == 'bomberman':
                    self.matrix_scaledup[i_su][j_su] = colored('[', 'yellow')
                    self.matrix_scaledup[i_su][j_su+1] = colored('^', 'yellow')
                    self.matrix_scaledup[i_su][j_su+2] = colored('^', 'yellow')
                    self.matrix_scaledup[i_su][j_su+3] = colored(']', 'yellow')
                    self.matrix_scaledup[i_su+1][j_su] = colored(' ', 'yellow')
                    self.matrix_scaledup[i_su+1][j_su+1] = colored(']', 'yellow')
                    self.matrix_scaledup[i_su+1][j_su+2] = colored('[', 'yellow')
                    self.matrix_scaledup[i_su+1][j_su+3] = colored(' ', 'yellow')

                elif self.matrix[i][j] == 'bomb4':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('4', 'red')

                elif self.matrix[i][j] == 'bomb3':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('3', 'red')

                elif self.matrix[i][j] == 'bomb2':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('2', 'red')

                elif self.matrix[i][j] == 'bomb1':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('1', 'red')

                elif self.matrix[i][j] == 'bomb0':
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored('0', 'red')

                elif self.matrix[i][j] in ['left', 'up', 'right', 'down', 'center']:
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = colored(':', 'red')

                elif self.matrix[i][j] == 0:
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = ' '

                else:
                    for m in range(i_su, i_su+2):
                        for n in range(j_su, j_su+4):
                            self.matrix_scaledup[m][n] = '!'
                    
    def display(self):
        self.scaleup()
        os.system("clear || cls")
        for i in range(self.rows * 2):
            for j in range(self.cols * 4):
                print(self.matrix_scaledup[i][j], end='')
            print('', end='\n')

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for i in range(rows):
            self.matrix.append([])
            for j in range(cols):
                self.matrix[i].append(0)