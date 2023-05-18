import multiprocessing
import time



def mensagem01():
    name = multiprocessing.current_process().name
    print('Iniciando o processo --> %s \n' %name)
    time.sleep(3)
    print('Encerrando o processo --> %s \n' %name)

if __name__ == "__main__":
    # Nomeando multiprocessing
    p1 = multiprocessing.Process(name='mensagem01', target=mensagem01)
    p2 = multiprocessing.Process(target=mensagem01)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

