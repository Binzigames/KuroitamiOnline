#libs
#Colorama ,pyfiglet
#------------->importing
import sys
import time
import os
import platform
import DATA.storage as S

try:
    from colorama import just_fix_windows_console, init as colorama_init
    from colorama import Fore
    try:
        just_fix_windows_console()
    except Exception:
        colorama_init()
except Exception:
    pass

import DATA.CORE.SceneManager as SM
#-------------> booling
IsRunning = True
ESC = "\033["

#-------------> render functions
def when_exit():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def move_home() -> None:
    sys.stdout.write(f"{ESC}H")
    sys.stdout.flush()


def clear_screen() -> None:
    sys.stdout.write(f"{ESC}2J{ESC}H")
    sys.stdout.flush()


def hide_cursor() -> None:
    sys.stdout.write(f"{ESC}?25l")
    sys.stdout.flush()


def show_cursor() -> None:
    sys.stdout.write(f"{ESC}?25h")
    sys.stdout.flush()

#-------------> game cycle
def update_screen() -> None:
    move_home()
    SM.handle()
    sys.stdout.flush()


def while_running() -> None:
    hide_cursor()
    try:
        while IsRunning:
            update_screen()
            time.sleep(0.1)


    finally:
        show_cursor()


