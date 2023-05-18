import asyncio
import websockets

async def echo(websocket):
    print("Conectado\n")
    async for message in websocket:
        print(message+'\n')
        msg = input("> ")
        
        await websocket.send(msg)

async def main():
    print("Aguardando Conexão...")
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())