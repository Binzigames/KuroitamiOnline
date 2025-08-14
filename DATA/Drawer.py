#-------------> import
import pyfiglet
import sys
import random
from colorama import Fore
import DATA.CORE.ArtsUI as art

#-------------> levels functions draw
logo = pyfiglet.figlet_format("Kuroitami Online", font="doom")

def intro_draw():
    sys.stdout.write(Fore.YELLOW+ "Welcome to:\n")
    sys.stdout.write(Fore.YELLOW + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by :" + Fore.RED + "Mizumi Studio\n")

def menu_draw():
    sys.stdout.write( Fore.RED + "welcome to\n" )
    sys.stdout.write( Fore.LIGHTYELLOW_EX + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by : "+ Fore.RED +"Mizumi Studio \n")

    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.YELLOW + "MAIN MENU\n")
    sys.stdout.write(Fore.WHITE + "Choose option...\n")
    sys.stdout.write(Fore.WHITE + "O - Options\nC - Credits\nX - Exit\n")
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write( Fore.WHITE + "waiting for input...\n")


def credit_draw():
    logo_studio = pyfiglet.figlet_format("Mizumi Studio", font="roman")
    sys.stdout.write(Fore.RED + logo_studio)
    sys.stdout.write( Fore.RED + "================\n")

    sys.stdout.write(Fore.YELLOW + "Director, Lead Programmer - "+  Fore.WHITE + "Yehor 'Porko' Kovalenko\n")
    sys.stdout.write( Fore.YELLOW + "========\n")
    sys.stdout.write(Fore.YELLOW + "Game Designer, Writer - " + Fore.WHITE + "Andrii 'TricksterFrid' Lekar\n")
    sys.stdout.write( Fore.YELLOW + "========\n")
    sys.stdout.write(Fore.YELLOW + "Programmer -"+  Fore.WHITE + " Artem 'k_onna' Saveliev\n")
    sys.stdout.write(Fore.YELLOW + "Programmer -"+  Fore.WHITE + " Oleksii 'djighoul29' Ivanyshyn\n")

    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")

def options_draw():
    options_text = pyfiglet.figlet_format("Options", font="roman")
    sys.stdout.write(Fore.RED + options_text)
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "help me! i am dooing some crazy things 3 hours!\n")
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")

def loading_scene():
    loadin_text= pyfiglet.figlet_format("NOW LOADING...", font="roman")
    tips = ["Dinahu1\n", "Dinahu2\n", "Dinahu3\n"]
    sys.stdout.write(Fore.WHITE + "\n".join(line[0] for line in art.loading_screen) + "\n")
    sys.stdout.write( Fore.YELLOW + "========\n")
    sys.stdout.write(Fore.RED + loadin_text)
    sys.stdout.write(Fore.WHITE + random.choice(tips))



