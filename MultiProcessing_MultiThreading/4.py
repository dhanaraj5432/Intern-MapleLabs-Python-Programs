import time
import random
import multiprocessing
def sleepProcess(st, pname):
    print(f"{pname} is sleeping for {st} seconds")
    time.sleep(st)

if __name__ == "__main__":
    job_list =list( map(lambda x: (random.randrange(8)), range(20)))
    lenList = len(job_list)
    k=0
    while(k < lenList-2):
        temp = job_list[k]
        p1 = multiprocessing.Process(target = sleepProcess, args=(temp,"Process 1"))

        k+=1
        temp = job_list[k]
        p2 = multiprocessing.Process(target = sleepProcess, args=(temp,"Process 2"))

        k+=1
        temp = job_list[k]
        p3 = multiprocessing.Process(target = sleepProcess, args=(temp,"Process 3"))
        k+=1

        p1.start()
       # p1.join()

        p2.start()
       # p2.join()
        
        p3.start()
       # p3.join()
        p1.join()
        p2.join()
        p3.join()