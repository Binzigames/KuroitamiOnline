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
    LOADING = 1488

#-------------> booling
sceneInt = ScenesEnum.INTRO
toScreen = 0

#------------->Scene manager logic
def handle():
    global sceneInt
    global toScreen
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
            sceneInt = ScenesEnum.LOADING
            toScreen = ScenesEnum.CREDITS
    elif sceneInt == ScenesEnum.CREDITS:
        D.credit_draw()
        a = input()
        if a == 'b':
            sceneInt = ScenesEnum.MENU
    
    elif sceneInt == ScenesEnum.LOADING:
        D.loading_scene()
        T.sleep(5)
        sceneInt = toScreen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")