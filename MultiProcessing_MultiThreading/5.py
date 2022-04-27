import ctypes
from msilib import type_string
import multiprocessing
from ctypes import c_bool

def computeFactorial(n):
    if n==0:
        return 1
    return n* computeFactorial(n-1)
def computeFact(n, retFact):
    #global resDict
    k = computeFactorial(n)
    retFact.value = k
def computeCube(n,retCube):
    #global resDict
    retCube.value = n*n*n

def computeIsPrime(n, retIsPrime):
    #global resDict
    flag = 0
    for i in range(2,n):
        if(n%i == 0):
            retIsPrime.value = 0
            return
    retIsPrime.value = 1

def computeHexaDecimal(n):

    print({"HexaDecimalFormat": str(hex(n).replace("0x","")).upper()})

def computeBinary(n,retBin):
    
    retBin.value = int(bin(n).replace("0b",""))

def mainP(n):
    res = {}

    
    retFact = multiprocessing.Value("L", 0, lock = False)
    retIsPrime = multiprocessing.Value("i", 0, lock = False)
    retBin = multiprocessing.Value("L",0, lock = False)
    retCube = multiprocessing.Value("L",0, lock = False)
    p1 = multiprocessing.Process(target = computeFact, args = (n,retFact))
    p2 = multiprocessing.Process(target = computeCube, args = (n, retCube))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    res['Factorial'] = retFact.value
    res["Cube"] = retCube.value
    p1 = multiprocessing.Process(target = computeIsPrime, args = (n,retIsPrime))
    p2 = multiprocessing.Process(target = computeBinary, args = (n,retBin))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    if retIsPrime.value == 1:
        res["IsPrime"] = True
    else:
        res["IsPrime"] = False

    res["BinaryFormat"] = str(retBin.value)

    print(res)

    p1 = multiprocessing.Process(target= computeHexaDecimal, args= (n,))
    p1.start()
    p1.join()


    
if __name__ == "__main__":
    mainP(2)
    print()
    mainP(10)
    