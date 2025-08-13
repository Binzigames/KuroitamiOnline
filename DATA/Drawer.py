#-------------> import
import pyfiglet
import sys
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

    sys.stdout.write(Fore.WHITE + "welcome to main menu...")

