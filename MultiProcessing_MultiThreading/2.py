import subprocess
import multiprocessing
def pingWebsite(s1):
   host = s1
   packet = 1
   ping = subprocess.getoutput(f"ping -w {packet} {host}")
   print(ping)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=pingWebsite,args=("http://www.cisco.com",))
   # process2 = multiprocessing.Process(target=pingWebsite,args=("http://www.google.com",))
   # process3 = multiprocessing.Process(target=pingWebsite,args=("http://www.hilli.com",))
    # Google IP Adress
    process2 = multiprocessing.Process(target=pingWebsite,args=("8.8.8.8",))
    
    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("\nBoth processes are finished")