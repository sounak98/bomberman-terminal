#!/usr/local/bin/python3

import signal, sys

from alarmexception import AlarmException
from getchunix import GetchUnix
from game import Game
import asciiart
import time

getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=100):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

if __name__ == "__main__":
    asciiart.start_screen()
    l = input_to()
    while l not in ['1', '2', '3']:
        l = input_to()
    
    Game(level=int(l))