#------------->importing
import DATA.Drawer as D
import time as T
import os
from enum import Enum
import platform

# Enums
class ScenesEnum(Enum):
    INTRO = 0
    MENU = 1
    CREDITS = 2

#-------------> booling
sceneInt = ScenesEnum.INTRO


#------------->Scene manager logic
def handle():
    global sceneInt
    if sceneInt == ScenesEnum.INTRO:
        D.intro_draw()
        T.sleep(5)
        sceneInt = ScenesEnum.MENU
    elif sceneInt == ScenesEnum.MENU:
        D.menu_draw()
        a = input()
        if a == 'x':
            exit()
        elif a == 'c':
            sceneInt = ScenesEnum.CREDITS
    elif sceneInt == ScenesEnum.CREDITS:
        D.credit_draw()
        a = input()
        if a == 'b':
            sceneInt = ScenesEnum.MENU
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")