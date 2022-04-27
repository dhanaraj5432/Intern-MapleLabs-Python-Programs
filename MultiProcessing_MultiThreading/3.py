import random
import threading
import time

def sleepThread(st,tname):
    
    print(f"{tname} is sleeping for {st} seconds")
    time.sleep(st)

if __name__ == "__main__":
    job_list =list( map(lambda x: (random.randrange(8)), range(20)))
    lenList = len(job_list)
    k=0
    while(k < lenList-2):
        temp = job_list[k]
        t1 = threading.Thread(target = sleepThread, args=(temp,"Thread 1"))

        k+=1
        temp = job_list[k]
        t2 = threading.Thread(target = sleepThread, args=(temp,"Thread 2"))

        k+=1
        temp = job_list[k]
        t3 = threading.Thread(target = sleepThread, args=(temp,"Thread 3"))
        k+=1

        t1.start()
        t1.join()
       
        t2.start()
        t2.join()
        t3.start()
        
        
        
        t3.join()
