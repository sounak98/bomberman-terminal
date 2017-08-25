import os
from termcolor import cprint

def start_screen():
    os.system('cls || clear')
    text = """********************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*        ______                 _                                              *
*        | ___ \               | |                                             *
*        | |_/ / ___  _ __ ___ | |__   ___ _ __ _ __ ___   __ _ _ __           *
*        | ___ \/ _ \| '_ ` _ \| '_ \ / _ \ '__| '_ ` _ \ / _` | '_ \          *
*        | |_/ / (_) | | | | | | |_) |  __/ |  | | | | | | (_| | | | |         *
*        \____/ \___/|_| |_| |_|_.__/ \___|_|  |_| |_| |_|\__,_|_| |_|         *
*                                                                              *
*                          Select Level (1/2/3):                               *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
********************************************************************************"""

    cprint(text, 'yellow', attrs=['bold'], end='\n')

def game_over_screen():
    os.system('cls || clear')
    text = """********************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*              _____                        _____                              *
*             |  __ \                      |  _  |                             *
*             | |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __               *
*             | | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|              *
*             | |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |                 *
*              \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|                 *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
********************************************************************************"""

    cprint(text, 'red', attrs=['bold'], end='\n')

def game_won_screen():
    os.system('cls || clear')
    text = """********************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*      _    _               _   _            _____                             *
*     | |  | |             | | | |          |  __ \                            *
*     | |  | | ___  _ __   | |_| |__   ___  | |  \/ __ _ _ __ ___   ___        *
*     | |/\| |/ _ \| '_ \  | __| '_ \ / _ \ | | __ / _` | '_ ` _ \ / _ \       *
*     \  /\  / (_) | | | | | |_| | | |  __/ | |_\ \ (_| | | | | | |  __/       *
*      \/  \/ \___/|_| |_|  \__|_| |_|\___|  \____/\__,_|_| |_| |_|\___|       *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
*                                                                              *
********************************************************************************"""

    cprint(text, 'green', attrs=['bold'], end='\n')