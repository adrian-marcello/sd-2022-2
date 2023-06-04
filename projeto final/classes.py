import multiprocessing
import random
import time

class garcom(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print ("Process garcom : item %d appended to queue %s"% (item,self.name))
            time.sleep(1)
            print ("The size of queue is %s"% self.queue.qsize())

class departamento(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            if (self.queue.empty()):
                print("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print ('Process departamento : item %d popped from by %s \n'% (item, self.name))
                time.sleep(1)