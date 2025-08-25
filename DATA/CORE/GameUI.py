# GameUI developed to draw in game screens.
# use this one only for "in game" content
#-------------> importing
import sys
import time
from colorama import Fore
import DATA.CORE.storage as s
import DATA.CORE.ArtsUI as art
import DATA.CORE.Character as C
import platform
import os
#-------------> draw functions
avatar= C.Character

def main_screen():
    if s.FirsTime == True:
        sys.stdout.write(Fore.WHITE + f"welcome to the zone , {Fore.RED + s.Pname}\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "Welcome to the Exclusion Zone - a post-apocalyptic world where the catastrophe of 2000 has changed reality.\n Explore abandoned cities, forests and rifts, survive among mutants, fight for rare materials and uncover the secret of the Soul of the Zone.\n Create a character, join a faction and become a legend of the Zone. Only you decide which path to choose.\n Dare to challenge the Zone.\n")
        sys.stdout.write(Fore.RED + "================\n")
        sys.stdout.write(Fore.WHITE + "enter 'C' to continue\n")
        a = input()
        if a == "c" and s.FirsTime:
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            char_create()

def char_create():
    # > draw
    sys.stdout.write(Fore.WHITE + "\n".join(line[0] for line in art.peoples) + "\n")
    sys.stdout.write(Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "CREATE YOUR CHARACTER...\n")
    sys.stdout.write(Fore.YELLOW + "OPTIONS :\n")
    sys.stdout.write(Fore.RED + "================\n")
    sys.stdout.write(Fore.RED + f"strength - {avatar.strength}, agility - {avatar.agility}, intelligence - {avatar.intelligence}, charisma - {avatar.charisma}, endurance - {avatar.endurance}, luck - {avatar.luck}")
    sys.stdout.write(Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "enter 'add <option>' to in-cris\n")
    sys.stdout.write(Fore.WHITE + "enter 'min <option>' to de-cris\n")

    # >func
    points = 20
    #incrce
    a = input()
    if a == "add ":
        opt = float(a.split(" ", 1)[1])
        #check in opt(inos) in input
        if opt == "strength" and not avatar.strength > 10 :
            avatar.strength += 1
            points -= 1
        elif opt == "agility" and not avatar.agility > 10 :
            avatar.agility += 1
            points -= 1
        elif opt == "intelligence" and not avatar.intelligence > 10 :
            avatar.intelligence += 1
            points -= 1
        elif opt == "charisma" and not avatar.charisma > 10 :
            avatar.charisma += 1
            points -= 1
        elif opt == "endurance" and not avatar.endurance > 10 :
            avatar.endurance += 1
            points -= 1
        elif opt == "luck" and not avatar.luck > 10 :
            avatar.luck += 1
            points -= 1
    #decrce
    if a == "min ":
        opt = float(a.split(" ", 1)[1])
        #check in opt(inos) in input
        if opt == "strength" and not avatar.strength > 10 :
            avatar.strength -= 1
            points += 1
        elif opt == "agility" and not avatar.agility > 10 :
            avatar.agility -= 1
            points += 1
        elif opt == "intelligence" and not avatar.intelligence > 10 :
            avatar.intelligence -= 1
            points += 1
        elif opt == "charisma" and not avatar.charisma > 10 :
            avatar.charisma -= 1
            points += 1
        elif opt == "endurance" and not avatar.endurance > 10 :
            avatar.endurance -= 1
            points += 1
        elif opt == "luck" and not avatar.luck > 10 :
            avatar.luck -= 1
            points += 1










def reconect_screen():
    sys.stdout.write(Fore.GREEN + "trying to reconnect...")
    time.sleep(2)

