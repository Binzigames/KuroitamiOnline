# GameUI developed to draw in game screens.
# use this one only for "in game" content
#-------------> importing
import sys
import time
from colorama import Fore
import DATA.CORE.storage as s
#-------------> draw functions

def main_screen():
    if s.FirsTime == True:
        sys.stdout.write(Fore.WHITE + f"welcome to the zone , {Fore.RED + s.Pname}\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "Welcome to the Exclusion Zone - a post-apocalyptic world where the catastrophe of 2000 has changed reality.\n Explore abandoned cities, forests and rifts, survive among mutants, fight for rare materials and uncover the secret of the Soul of the Zone.\n Create a character, join a faction and become a legend of the Zone. Only you decide which path to choose.\n Dare to challenge the Zone.\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "enter 'C' to continue")
        if input() == "c" and s.FirsTime:
            s.FirsTime = False


def reconect_screen():
    sys.stdout.write(Fore.GREEN + "trying to reconnect...")
    time.sleep(2)

