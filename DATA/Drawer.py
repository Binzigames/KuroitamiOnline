#-------------> import
import pyfiglet
import sys
from colorama import Fore

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

    sys.stdout.write(Fore.WHITE + "Director, Lead Programmer - Yehor 'Porko' Kovalenko\n")
    sys.stdout.write(Fore.WHITE + "Programmer - Artem 'k_onna' Saveliev\n")
    sys.stdout.write(Fore.WHITE + "Programmer - Oleksii 'djighoul29' Ivanyshyn\n")

    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")

def options_draw():
    options_text = pyfiglet.figlet_format("Options", font="roman")
    sys.stdout.write(Fore.RED + options_text)
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "help me! i am dooing some crazy things 3 hours!\n")
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")

