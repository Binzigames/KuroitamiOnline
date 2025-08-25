#-------------> importing
import DATA.CORE.ClientHandler as c
import DATA.CORE.storage as s
import asyncio as A
import DATA.CORE.SceneManager as S
#-------------> cycle
def Handle():
    while c.IsOnline:
            A.run(c.client_flow(s.CIP, 8989))
    else :
        S.loadScene(S.ScenesEnum.MENU , 1)

