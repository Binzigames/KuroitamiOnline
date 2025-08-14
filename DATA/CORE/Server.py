#-------------> importing
import socket as S
import asyncio as A
import DATA.storage as D

#-------------> server info handler
IsServerRunning = True
UserIP = D.SIP

#-------------> server magic
async def server_handle():
    global IsServerRunning
    if IsServerRunning:
        await server_cycle()
    else:
        await server_init()

async def server_init():
    global IsServerRunning
    IsServerRunning = True

    server = await A.start_server(handle_client, UserIP, 8989)

    async with server:
        await server.serve_forever()

async def server_cycle():
    await A.sleep(1)
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')

    writer.write(b"Hello from server!\n")
    await writer.drain()

    writer.close()
    await writer.wait_closed()
