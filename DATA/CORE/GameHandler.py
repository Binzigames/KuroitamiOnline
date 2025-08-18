#-------------> importing
import DATA.CORE.ClientHandler as c
import DATA.CORE.storage as s
import asyncio as A
#-------------> cycle
def Handle():
    while c.IsOnline:
            A.run(c.client_flow(s.CIP, 8989))

