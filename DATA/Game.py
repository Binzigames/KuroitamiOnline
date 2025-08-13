import sys
import time
try:
    from colorama import just_fix_windows_console, init as colorama_init
    from colorama import Fore
    try:
        just_fix_windows_console()
    except Exception:
        colorama_init()
except Exception:
    pass

ESC = "\033["

# ---------- Сервісні функції ----------

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


# ---------- Ваш ігровий цикл ----------

IsRunning = True


def update_screen() -> None:
    move_home()
    sys.stdout.write( Fore.LIGHTBLACK_EX + "Привіт з кросплатформеного екрана!\n")
    sys.stdout.flush()


def while_running() -> None:
    hide_cursor()
    try:
        while IsRunning:
            update_screen()
            time.sleep(0.1)
    finally:
        show_cursor()


