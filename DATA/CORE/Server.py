# -------------> importing
import asyncio as A
import DATA.CORE.storage as D
from colorama import Fore
import pyfiglet
import base64

# -------------> server info handler
UserIP = D.SIP
Srunning = True
DebugMode = False
logo = pyfiglet.figlet_format("Kuroitami Online", font="doom")

# -------------> base64 helpers
def encrypt(msg: str) -> bytes:
    return base64.b64encode(msg.encode())

def decrypt(data: bytes) -> str:
    return base64.b64decode(data).decode()

# -------------> server magic
#> handle and debug
async def server_handle():
    if not D.Sstate:
        print(Fore.RED + logo)
        print(Fore.WHITE + "Welcome to server console. developed by : " + Fore.RED + "Mizumi Studio")
        print(Fore.RED + "[SERVER INIT]")
        await server_init()

    print(Fore.RED + "[SERVER HANDLE]")
    print(Fore.WHITE + "====CONSOLE====")
    await server_cycle()

#> log function
def server_log(arg):
    server_tag = "[SERVER]"
    print(f"{Fore.RED + server_tag} / {Fore.WHITE + arg}")
    print(Fore.WHITE + "===============\n")

#> server init and cycle
async def server_init():
    D.Sstate = True
    server_log(f"start server on {UserIP}:8989...")
    server = await A.start_server(handle_client, UserIP, 8989)
    addr = server.sockets[0].getsockname()
    server_log(f"server ready and listening to {addr}")
    A.create_task(server.serve_forever())

async def server_cycle():
    while True:
        if DebugMode:
            server_log("server : online")
            server_log(str(D.Sstate) + " : server state")
        await A.sleep(5)

#> client handle
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    server_log(f"[CLIENT] connected: {addr}")

    writer.write(encrypt("Connected") + b"\n")
    await writer.drain()

    # читаємо повідомлення від клієнта
    data = await reader.readline()
    if data:
        try:
            msg = decrypt(data.strip())
            server_log(f"[CLIENT {addr}] {msg}")
            # відповідаємо теж у base64
            writer.write(encrypt(f"Server received: {msg}") + b"\n")
            await writer.drain()
        except Exception:
            raw = data.decode().strip()
            server_log(f"[CLIENT RAW {addr}] {raw}")

    server_log(f"[CLIENT] disconnected: {addr}")
    writer.close()
    await writer.wait_closed()

#> starter function
def start():
    try:
        A.run(server_handle())
    except KeyboardInterrupt:
        server_log("\nExiting server...")

# -------------> start
if __name__ == "__main__":
    start()
