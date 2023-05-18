# SuperFastPython.com
# example of daemon processes being terminated abruptly
from time import sleep
import multiprocessing
from multiprocessing import current_process
from multiprocessing import Process
 
def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'background_process':
        for i in range(0,5):
            print('---> %d \n' %i)
            sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
            sleep(1)
    print ("Exiting %s \n" %name)
 
# entry point
if __name__ == '__main__':
    background_process          = multiprocessing.Process(name='background_process',target=foo)
    background_process.daemon   = True
    NO_background_process       = multiprocessing.Process(name='NO_background_process',target=foo)
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
    sleep(5)