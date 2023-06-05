import asyncio
import websockets
from time import sleep

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Me conectei ao servidor")
        while True:
           msg = input("> ")
           if (msg == "SAIR"): break
           await websocket.send(msg)

asyncio.run(hello())