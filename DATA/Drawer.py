#-------------> import
import pyfiglet
import sys
import random
from colorama import Fore
import DATA.CORE.ArtsUI as art
import DATA.storage as s

#-------------> levels functions draw
logo = pyfiglet.figlet_format("Kuroitami Online", font="doom")

def loading_scene():
    # 10 cool words about chornobyl if somebody have more please add
    tips = [
        "You’re confused — RBMK reactor cores don’t explode. — Anatoly Dyatlov\n",
        "Chernobyl is like the war of all wars. There’s nowhere to hide. Not underground, not underwater, not in the air. — Svetlana Alexievich\n",
        "Every lie we tell incurs a debt to the truth. Sooner or later that debt is paid. — Valery Legasov\n",
        "We are on dangerous ground right now, because of our secrets and our lies. They’re practically what defines us. — Valery Legasov\n",
        "In fact, all of us have a piece of Chernobyl in our bodies going back to 1986. — Michio Kaku\n",
        "Death is the fairest thing in the world. No one's ever gotten out of it. The earth takes everyone – the kind, the cruel, the sinners. — Svetlana Alexievich\n",
        "Show me a fantasy novel about Chernobyl — there isn't one! Because reality is more fantastic. — Svetlana Alexievich\n",
        "To be a scientist is to be naive. We are so focused on our search for truth, we fail to consider how few actually want us to find it… What is the cost of lies? — HBO’s Chernobyl <- very cool series\n",
        "Chornobyl is pain of Ukranian Peoples. We need to honor and tell all peoples about it! - Yehor 'Porko' Kovalenko\n",
        "Not great, not terrible. — Anatoly Dyatlov\n",
        "Як нам прийшла пора прощатися. Піду втоплюся у річці глибокій... спасибі за увагу- Андрій Миколайчук\n"
    ]
    sys.stdout.write(Fore.WHITE + "\n".join(line[0] for line in art.loading_screen) + "\n")
    sys.stdout.write( Fore.YELLOW + "========\n")
    sys.stdout.write(Fore.RED + "NOW LOADING...\n")
    sys.stdout.write(Fore.WHITE + random.choice(tips))

def intro_draw():
    sys.stdout.write(Fore.YELLOW+ "Welcome to:\n")
    sys.stdout.write(Fore.YELLOW + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by :" + Fore.RED + "Mizumi Studio\n")
#> main menu
def menu_draw():
    sys.stdout.write( Fore.RED + "welcome to\n" )
    sys.stdout.write( Fore.LIGHTYELLOW_EX + logo)
    sys.stdout.write(Fore.WHITE + "Devleoped by : "+ Fore.RED +"Mizumi Studio \n")

    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.YELLOW + "MAIN MENU\n")
    sys.stdout.write(Fore.WHITE + "Choose option...\n")
    sys.stdout.write(Fore.WHITE + "S - Start\nO - Options\nC - Credits\nX - Exit\n")
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

def game_start_draw():
    text_1 = pyfiglet.figlet_format("Host", font="roman")
    text_2 = pyfiglet.figlet_format("Connect", font="roman")
    if s.SHmode == True :
        sys.stdout.write(Fore.LIGHTYELLOW_EX + text_1)
    else:
        sys.stdout.write(Fore.LIGHTGREEN_EX + text_2)
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.YELLOW + "OPTIONS\n Choose option...\n")
    sys.stdout.write(Fore.WHITE + "press M to change mod\n press B to return\n")
    sys.stdout.write(Fore.RED + "================\n")
    if s.SHmode == True:
        if s.Sstate == False:
         sys.stdout.write(Fore.LIGHTYELLOW_EX + "press H to host server\n")
         sys.stdout.write(Fore.LIGHTYELLOW_EX + f"Current state : {s.server_state}\n")


def options_draw():
    options_text = pyfiglet.figlet_format("Options", font="roman")
    sys.stdout.write(Fore.RED + options_text)
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "help me! i am dooing some crazy things 3 hours!\n")
    sys.stdout.write( Fore.RED + "================\n")
    sys.stdout.write(Fore.WHITE + "Press B(ack) to main menu\n")





