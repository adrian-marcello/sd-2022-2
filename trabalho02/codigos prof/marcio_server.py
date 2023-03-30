import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send('###### Bem-vindo ao chat ####')
        print(message)
        await websocket.send('Sua mensagem')
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())