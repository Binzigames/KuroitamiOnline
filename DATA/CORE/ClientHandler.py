#K_onna fuck you man!
#usage
# use await  for defs
# if not await connect_to_server(cip, port):
import asyncio as A
import base64
import time as T

# -------------> bools
reader = None
writer = None
Clog = ""

IsOnline = False
# -------------> encode
def encrypt(msg: str) -> bytes:
    return base64.b64encode(msg.encode())


def decrypt(data: bytes) -> str:
    return base64.b64decode(data).decode()


# -------------> connect
async def connect_to_server(cip: str, port: int = 8989):
    global reader, writer, Clog , IsOnline
    try:
        IsOnline = True
        reader, writer = await A.open_connection(cip, port)
        Clog = f"[CLIENT] Connected to {cip}:{port}"
        return True
    except Exception as e:
        IsOnline = False
        Clog = f"[CLIENT ERROR] {e}"
        return False


# -------------> send data
async def send_message(msg: str):
    global writer, Clog
    if writer is None:
        Clog = "[CLIENT ERROR] Not connected"
        return
    try:
        enc_msg = encrypt(msg) + b"\n"
        writer.write(enc_msg)
        await writer.drain()
        Clog = f"[CLIENT] Sent (encrypted): {msg}"
    except Exception as e:
        Clog = f"[CLIENT ERROR] {e}"


# -------------> receive data
async def receive_message():
    global reader, Clog
    if reader is None:
        Clog = "[CLIENT ERROR] Not connected"
        return None
    try:
        data = await reader.readline()
        if not data:
            Clog = "[CLIENT] Server closed connection"
            return None
        dec_msg = decrypt(data.strip())
        Clog = f"[SERVER MESSAGE] {dec_msg}"
        return dec_msg
    except Exception as e:
        Clog = f"[CLIENT ERROR] {e}"
        return None


# -------------> disconect
async def disconnect():
    global writer, Clog , IsOnline
    IsOnline = False
    if writer is not None:
        writer.close()
        await writer.wait_closed()
        Clog = "[CLIENT] Disconnected from server"
        writer = None


# -------------> usage
async def client_flow(cip="127.0.0.1", port=8989):
    if not await connect_to_server(cip, port):
        return
    else :
        T.sleep(2)
        await receive_message()


def join_server(cip: str, port: int = 8989):
    try:
        A.run(client_flow(cip, port))
    except KeyboardInterrupt:
        print("\n[CLIENT] Exit client...")
