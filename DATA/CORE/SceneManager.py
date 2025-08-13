#------------->importing
import DATA.Drawer as D
import time as T

#-------------> booling
sceneInt = 0
#------------->Scene manager logic
def handle():
    global sceneInt
    if sceneInt == 0:
        D.intro_draw()
        T.sleep(5)
        sceneInt += 1
    elif sceneInt == 1:
        D.menu_draw()