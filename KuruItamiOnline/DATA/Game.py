#-------------> importing
import time
#-------------> Bools
IsRunning = True

#-------------> game handel
def update_screen():
    print("\033[H", end="")
def while_running():
    update_screen()

    time.sleep(0.1)