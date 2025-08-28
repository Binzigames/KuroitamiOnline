# GameUI developed to draw in game screens.
# use this one only for "in game" content
#-------------> importing
import sys
import time
from colorama import Fore
import DATA.CORE.storage as s
import DATA.CORE.ArtsUI as art
import DATA.CORE.Character as C

#-------------> draw functions
avatar = C.Character()
IsCharCreation = False
points = 20
def main_screen():
    global IsCharCreation

    if s.FirsTime == True and not IsCharCreation:
        sys.stdout.write(Fore.WHITE + f"welcome to the zone , {Fore.RED + s.Pname}\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "Welcome to the Exclusion Zone - a post-apocalyptic world where the catastrophe of 2000 has changed reality.\n Explore abandoned cities, forests and rifts, survive among mutants, fight for rare materials and uncover the secret of the Soul of the Zone.\n Create a character, join a faction and become a legend of the Zone. Only you decide which path to choose.\n Dare to challenge the Zone.\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "enter 'C' to continue\n")
        a = input()
        if a == "c" and s.FirsTime:
            IsCharCreation = True
    else:
        char_create()

def char_create():
    global points
    # > draw
    sys.stdout.write(Fore.WHITE + "\n".join(line[0] for line in art.peoples) + "\n")
    sys.stdout.write(Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "CREATE YOUR CHARACTER...\n")
    sys.stdout.write(Fore.WHITE + f"points : {Fore.YELLOW + str(points)} / {Fore.WHITE}20\n")

    stats = avatar.to_dict()
    sys.stdout.write(Fore.RED + "CHARACTER STATS\n")
    for k, v in stats.items():
        sys.stdout.write(f"{k}: {v} \n")


    sys.stdout.write(Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "enter 'add <option>' to in-cris\n")
    sys.stdout.write(Fore.WHITE + "enter 'min <option>' to de-cris\n")

    # >func
    a = input()

    if a.startswith("add "):
        opt = a.split(" ", 1)[1]
        if opt == "strength" and avatar.strength < 10:
            avatar.strength += 1
            points -= 1
        elif opt == "agility" and avatar.agility < 10:
            avatar.agility += 1
            points -= 1
        elif opt == "intelligence" and avatar.intelligence < 10:
            avatar.intelligence += 1
            points -= 1
        elif opt == "charisma" and avatar.charisma < 10:
            avatar.charisma += 1
            points -= 1
        elif opt == "endurance" and avatar.endurance < 10:
            avatar.endurance += 1
            points -= 1
        elif opt == "luck" and avatar.luck < 10:
            avatar.luck += 1
            points -= 1

    elif a.startswith("min "):
        opt = a.split(" ", 1)[1]
        if opt == "strength" and avatar.strength > 0:
            avatar.strength -= 1
            points += 1
        elif opt == "agility" and avatar.agility > 0:
            avatar.agility -= 1
            points += 1
        elif opt == "intelligence" and avatar.intelligence > 0:
            avatar.intelligence -= 1
            points += 1
        elif opt == "charisma" and avatar.charisma > 0:
            avatar.charisma -= 1
            points += 1
        elif opt == "endurance" and avatar.endurance > 0:
            avatar.endurance -= 1
            points += 1
        elif opt == "luck" and avatar.luck > 0:
            avatar.luck -= 1
            points += 1


def zone_enter():
    






def reconect_screen():
    sys.stdout.write(Fore.GREEN + "trying to reconnect...")
    time.sleep(2)

