import asyncio
import websockets
import time

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
           await websocket.send("Hello world!")
           await websocket.recv()
           print(websocket.messages)
           time.sleep(5)

asyncio.run(hello())