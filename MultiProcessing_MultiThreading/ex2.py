
import queue
import time
import random
import multiprocessing

q = multiprocessing.Queue()

def sleepProcess(pname):
    while True:
        k = q.get()
        if k is None:
            break
        print(f"{pname} is sleeping for {k} seconds")
        time.sleep(k)
        q.task_done()

def initiateProcess(num_workers, job_list):
    
    processes = []

    for job in job_list:
        q.put(job)
    
    for i in range(num_workers):
        q.put(None)
    
    p1 = multiprocessing.Process(target=sleepProcess, args=("Process 1",))
    p1.start()

    p2 = multiprocessing.Process(target=sleepProcess, args=("Process 2",))
    p2.start()

    p3 = multiprocessing.Process(target=sleepProcess, args=("Process 3",))
    p3.start()
    
   
    p1.join()
    #p2.join()
    #p3.join()
    
    print("\n All jobs are completed \n")
    return

if __name__ == "__main__":
    num_workers = 3
    job_list =list( map(lambda x: (random.randrange(8)), range(10)))
    initiateProcess(num_workers, job_list)
    