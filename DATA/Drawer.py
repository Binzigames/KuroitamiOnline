#-------------> import
import pyfiglet
import sys
import random
from colorama import Fore

#-------------> levels functions draw

def intro_draw():
    logo = pyfiglet.figlet_format("Kuroitami Online" , font="doom")
    sys.stdout.write(Fore.YELLOW + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by : Mizumi Studio\n")

def menu_draw():
    logo = pyfiglet.figlet_format("Kuroitami Online" , font="doom")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by : Mizumi Studio \n")

    sys.stdout.write(Fore.WHITE + "welcome to main menu...\n")
    sys.stdout.write(Fore.WHITE + "Choose option...\n\n")
    sys.stdout.write(Fore.WHITE + "X - Exit\nC - Credits\n")

def credit_draw():
    logo = pyfiglet.figlet_format("Mizumi Studio", font="colossal")
    sys.stdout.write(Fore.RED + logo)

    sys.stdout.write(Fore.WHITE + "Director, Lead Programmer - Porko\n")
    sys.stdout.write(Fore.WHITE + "Programmer - Artem 'k_onna' Saveliev\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")

def loading_scene():
    logo = pyfiglet.figlet_format("Loading...", font="colossal")
    ebubu = ["Dinahu1\n", "Dinahu2\n", "Dinahu3\n"]
    sys.stdout.write(Fore.BLUE + logo)
    sys.stdout.write(Fore.WHITE + random.choice(ebubu))



