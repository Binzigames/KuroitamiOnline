# GameUI developed to draw in game screens.
# use this one only for "in game" content
#-------------> importing
import sys
from colorama import Fore
import DATA.CORE.storage as s
#-------------> draw functions

def main_screen():
    if s.FirsTime == True:
        sys.stdout.write(Fore.WHITE + f"welcome to the game , {Fore.RED + s.Pname}\n")
        sys.stdout.write(Fore.WHITE + "enter 'C' to continue")
        if input() == "c" and s.FirsTime:
            s.FirsTime = False


def reconect_screen():
    sys.stdout.write(Fore.GREEN + "trying to reconnect...")

