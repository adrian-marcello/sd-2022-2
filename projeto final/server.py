import multiprocessing
import classes
import asyncio
import websockets

BEBIDA = ['cerveja','refrigerante','suco','caipirinha']
PRATOS = ['macarrão','carne','batata frita']
SANDUICHES = ['x tudo','x ratão']
SOBREMESA = ['pudim','sorvete']

async def echo(websocket):
    print("Conectado")
    async for message in websocket:
        print(message)

async def main():
    print("Aguardando Conexão...")
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever



if __name__ == '__main__':
    asyncio.run(main())



    # queue = multiprocessing.Queue()
    # process_garcom = classes.garcom(queue)
    # process_departamento = classes.departamento(queue)
    # process_garcom.start()
    # process_departamento.start()
    # process_garcom.join()
    # process_departamento.join()