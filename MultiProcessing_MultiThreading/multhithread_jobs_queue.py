import random
import threading
import time

import queue
import threading

q = queue.Queue()

def sleepThread(tname):
    while True:
        i = q.get()
        if i is None:
            break
        print(f"{tname} is sleeping for {i} seconds")
        time.sleep(i)
        q.task_done()

def initiateThreads(num_workers, job_list):
    
    threads = []

    for job in job_list:
        q.put(job)

    for i in range(num_workers):
        
        t = threading.Thread(target=sleepThread, args=(f"thread {i+1}",))
        t.start()
        threads.append(t)
   
    
    for i in range(num_workers):
        q.put(None)
    
    for t in threads:
        t.join()
    
    print("\n All jobs are completed \n")
    return

if __name__ == "__main__":
    num_workers = 3
    job_list =list( map(lambda x: (random.randrange(8)), range(20)))
    initiateThreads(num_workers, job_list)