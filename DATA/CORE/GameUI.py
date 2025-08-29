# GameUI developed to draw in game screens.
# use this one only for "in game" content
#-------------> importing
import sys
import time
from colorama import Fore
import DATA.CORE.storage as s
import DATA.CORE.ArtsUI as art
import DATA.CORE.Character as C
import os
import platform
import DATA.Items as i

#-------------> draw functions
avatar = C.Character()
IsCharCreation = False
IsCharEnter = False
points = 20
def main_screen():
    global IsCharCreation, IsCharEnter

    while True:
        if s.FirsTime and not IsCharCreation and not IsCharEnter:
            sys.stdout.write(Fore.WHITE + f"welcome to the zone , {Fore.RED + s.Pname}\n")
            sys.stdout.write(Fore.RED + "================\n")
            sys.stdout.write(Fore.WHITE + "Welcome to the Exclusion Zone - a post-apocalyptic world where the catastrophe of 2000 has changed reality.\n"
                                          "Explore abandoned cities, forests and rifts, survive among mutants, fight for rare materials and uncover the secret of the Soul of the Zone.\n"
                                          "Create a character, join a faction and become a legend of the Zone. Only you decide which path to choose.\n"
                                          "Dare to challenge the Zone.\n")
            sys.stdout.write(Fore.RED + "================\n")
            sys.stdout.write(Fore.WHITE + "enter 'C' to continue\n")

            a = input().lower()
            if a == "c":
                IsCharCreation = True

        elif IsCharCreation and not IsCharEnter:
            char_create()
            if IsCharEnter:
                continue

        elif IsCharEnter:
            zone_enter()
            break


def char_create():
    global points , IsCharEnter , IsCharCreation
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
    sys.stdout.write(Fore.WHITE + "enter 'c' to continue\n")

    # >func
    a = input()
    if a == "c":
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        IsCharEnter = True
        IsCharCreation = False
        return
    elif a.startswith("add "):
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


fraction_selected = False
def zone_enter():
    global fraction_selected
    sys.stdout.write(Fore.RED + "============================\n")
    sys.stdout.write(Fore.WHITE + "   CHOOSE YOUR FACTION TO ENTER THE ZONE\n")
    sys.stdout.write(Fore.RED + "============================\n\n")

    # 1. Shadows of the Zone
    sys.stdout.write(Fore.MAGENTA + "1. Shadows of the Zone\n")
    sys.stdout.write(Fore.WHITE + "   Mercenaries smuggle you through secret routes.\n")
    sys.stdout.write("   Provide high-tech weapons.\n")

    # 2. LRR
    sys.stdout.write(Fore.CYAN + "2. LRR\n")
    sys.stdout.write(Fore.WHITE + "   Transfer you through their underground bunkers.\n")
    sys.stdout.write("   Provide anti-radiation medicine and an anomaly detector.\n")

    # 3. Black Border
    sys.stdout.write(Fore.YELLOW + "3. Black Border\n")
    sys.stdout.write(Fore.WHITE + "   Grant legal entry into the Zone.\n")

    # 4. Uranis-235
    sys.stdout.write(Fore.GREEN + "4. Uranis-235\n")
    sys.stdout.write(Fore.WHITE + "   Lead you through highly irradiated paths avoided by others.\n")
    sys.stdout.write("   Provide rare radioactive material.\n")

    # 5. Psi of Ruins
    sys.stdout.write(Fore.RED + "5. Dogs of ruins\n")
    sys.stdout.write(Fore.WHITE + "   Help bypass Black Border patrols.\n")
    sys.stdout.write("   Risk of being exposed by Black Border.\n")
    sys.stdout.write("   Provide black market contacts and basic gear.\n")
    sys.stdout.write(Fore.RED + "============================\n\n")
    if not fraction_selected:
        sys.stdout.write(Fore.WHITE + "Choose a faction (1-5): \n")
    else:
        sys.stdout.write(Fore.WHITE + "enter 'c' to continue \n")
    # >func
    a = input()
    if a ==   "1" and not fraction_selected:
        # >fractions rep
        i.fractions.BBPrep = -50
        i.fractions.ZSPrep = 25
        fraction_selected = True
    elif a == "2"and not fraction_selected:
        # >fractions rep
        i.fractions.ZSPrep = -95
        i.fractions.LRRPrep = 80
        fraction_selected = True
    elif a == "3"and not fraction_selected:
        # >fractions rep
        i.fractions.BBPrep = 85
        i.fractions.ZSPrep = -70
        i.fractions.DRPrep = -95
        fraction_selected = True
    elif a == "4"and not fraction_selected:
        # >fractions rep
        i.fractions.U2Prep = 85
        i.fractions.ZSPrep = -70
        i.fractions.DRPrep = -95
        i.fractions.LRRrep = -95
        fraction_selected = True
    elif a == "5"and not fraction_selected:
        # >fractions rep
        i.fractions.BBPrep = -95
        i.fractions.ZSPrep = -85
        i.fractions.DRPrep = 50
        fraction_selected = True

    if fraction_selected and a == "c":
        i.fractions.BBPrep = -95









def reconect_screen():
    sys.stdout.write(Fore.GREEN + "trying to reconnect...")
    time.sleep(2)

