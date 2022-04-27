#import os
#import platform
import subprocess
def pingWebsite(s1):
    #res = os.system("ping -n 1 "+ s1)

   ''' res = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', res, '1', s1]

    if subprocess.call(command) == 0:
        print("{} pingable".format(s1))
    else:
        print("{} not pingable".format(s1))'''
   host = s1
   packet = 1
   ping = subprocess.getoutput(f"ping -w {packet} {host}")
   print(ping)

if __name__ == "__main__":
    pingWebsite("http://www.cisco.com")
    pingWebsite("https://google.com")
    pingWebsite("http://hilli.com")
    pingWebsite("4.2.2.2")
    
    #google ip address
    pingWebsite("8.8.8.8")