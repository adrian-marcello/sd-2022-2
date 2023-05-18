import multiprocessing
import os
import time


def task_sleep(sleep_duration, task_number):
    time_start = time.time()
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Process ID: {os.getpid()}")
    time_end = time.time()
    print(f"Time elapsed inside multiprocessing: {round(time_end - time_start, 2)}s")

if __name__ == "__main__":
    time_start = time.time()

    # Create process
    p1 = multiprocessing.Process(target=task_sleep, args=(12, 1))
    p2 = multiprocessing.Process(target=task_sleep, args=(2, 2))
    p3 = multiprocessing.Process(target=task_sleep, args=(2, 3))
    p4 = multiprocessing.Process(target=task_sleep, args=(2, 4))
    p5 = multiprocessing.Process(target=task_sleep, args=(2, 5))
    p6 = multiprocessing.Process(target=task_sleep, args=(2, 6))
    p7 = multiprocessing.Process(target=task_sleep, args=(2, 7))
    p8 = multiprocessing.Process(target=task_sleep, args=(3, 8))


    # Start task execution
    p1.start()
    p1.join()

    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()


    # Wait for process to complete execution

    '''    
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    '''
    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")