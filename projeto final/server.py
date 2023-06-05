import multiprocessing
import asyncio
import websockets

BEBIDAS = ['cerveja','refrigerante','suco','caipirinha']
PRATOS = ['macarrão','carne','batata frita']
SANDUICHES = ['x tudo','x ratão']
SOBREMESAS = ['pudim','sorvete']

async def recebepedidos(websocket):
    print("Garçom conectado")
    async for pedido in websocket:
        l_itens = pedido.split(',')
        l_proc = []

        for i in l_itens:
            p = multiprocessing.Process(target=distribuipedidos,args=(i,))
            p.start()
            l_proc.append(p)


        for p in l_proc: p.join()
        print('\n')
        

def distribuipedidos(item):
    item = item.strip()
    if item in BEBIDAS:
        print(f"DEPARTAMENTO DE BEBIDAS:\n{item}")
    elif item in PRATOS:
        print(f"DEPARTAMENTO DE PRATOS:\n{item}")
    elif item in SANDUICHES:
        print(f"DEPARTAMENTO DE SANDUICHES:\n{item}")
    elif item in SOBREMESAS:
        print(f"DEPARTAMENTO DE SOBREMESAS:\n{item}")


async def main():
    print("Aguardando Conexão...")
    async with websockets.serve(recebepedidos, "localhost", 8765):
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