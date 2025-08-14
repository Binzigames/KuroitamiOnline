#------------->importing
import DATA.Drawer as D
import time as T
import DATA.storage as S
import DATA.CORE.Server as ser
import os
from enum import Enum
import platform

# Enums
class ScenesEnum(Enum):
    INTRO = 0
    LOADING = 0.1
    # > main menu
    MENU = 1
    CREDITS = 1.1
    OPTIONS = 1.2
    # > start menu
    GAMESTART = 1.3

#-------------> booling
sceneInt = ScenesEnum.INTRO
toScreen = 0

#------------->Scene manager logic
def handle():
    global sceneInt
    global toScreen
    if sceneInt == ScenesEnum.INTRO:
        D.intro_draw()
        T.sleep(3)
        sceneInt = ScenesEnum.MENU
    elif sceneInt == ScenesEnum.MENU:
        D.menu_draw()
        a = input()
        if a == 'x':
            exit()
        elif a == 'c':
            sceneInt = ScenesEnum.LOADING
            toScreen = ScenesEnum.CREDITS
        elif a == 'o':
            sceneInt = ScenesEnum.OPTIONS
        elif a == "s":
            sceneInt = ScenesEnum.GAMESTART
    elif sceneInt == ScenesEnum.CREDITS:
        D.credit_draw()
        a = input()
        if a == 'b':
            sceneInt = ScenesEnum.MENU

    elif sceneInt == ScenesEnum.OPTIONS:
        D.options_draw()
        a = input()
        if a == 'b':
            sceneInt = ScenesEnum.MENU
    # > start game screen
    elif sceneInt == ScenesEnum.GAMESTART:
        D.game_start_draw()
        a = input()
        if a == 'm':
            S.SHmode = not S.SHmode
        if a == 'b':
            sceneInt = ScenesEnum.MENU
        if a == 'h' and S.SHmode == True and S.Sstate == True :
            ser.server_init()
    # > loading screan
    elif sceneInt == ScenesEnum.LOADING:
        D.loading_scene()
        T.sleep(3)
        sceneInt = toScreen

    # > clear-cross platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")