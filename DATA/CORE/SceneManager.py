#------------->importing
import DATA.Drawer as D
import time as T
import DATA.CORE.storage as S
import DATA.CORE.SoundManager as s
import os
from enum import Enum
import platform
import DATA.CORE.ArtsUI as artUi
import DATA.CORE.ClientHandler as C
import DATA.CORE.GameHandler as g


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
    # > game
    GAME = 2
#-------------> booling
sceneInt = ScenesEnum.INTRO
toScreen = 0

MusicManager = s.MusicManager()
#------------->Scene manager logic
def handle():
    global sceneInt
    global toScreen
    
    if sceneInt == ScenesEnum.INTRO:
        D.intro_draw()
        T.sleep(2)
        loadScene(ScenesEnum.MENU, 1)
    elif sceneInt == ScenesEnum.MENU:
        D.menu_draw()
        MusicManager.play(s.MusicEnum.MENU , 1 , S.volume)
        a = input()
        if a == 'x':
            exit()
        elif a == 'c':
            sceneInt = ScenesEnum.CREDITS
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
        if a.startswith("volume "):
            S.volume = float(a.split(" ", 1)[1])
        if a == 'b':
            sceneInt = ScenesEnum.MENU
    # > start game screen
    elif sceneInt == ScenesEnum.GAMESTART:
        D.game_start_draw()
        a = input()
        if a == 'b':
            sceneInt = ScenesEnum.MENU
        if a == 'm':
            S.VCM = not S.VCM
        if S.VCM:
            if a.startswith("sn ") and S.Pname == "":
                S.Pname = a.split(" ", 1)[1]
            if a.startswith("sip "):
                S.CIP = a.split(" ", 1)[1]
            if a == 'c' and not S.Pname == "" :
                C.join_server(S.CIP)

        if C.IsOnline == True:
            sceneInt = ScenesEnum.GAME
    # > game
    elif sceneInt == ScenesEnum.GAME:
        g.Handle()


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
    

def loadScene(scene , int):
    global sceneInt , toScreen
    artUi.unload()
    try:
        sceneInt = ScenesEnum.LOADING
        artUi.loader(int)
    finally:
        toScreen = scene
        