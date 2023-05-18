import asyncio
import websockets
import time

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
           msg = input("> ")
           if (msg == "SAIR"): break
           await websocket.send(msg)
           message = await websocket.recv()
           print(message+'\n')

asyncio.run(hello())