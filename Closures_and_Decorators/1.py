from time import time

def runTimeDecorator(func):
    
    def wrapperFunction(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()

        print(f"Total run time of the Function {func.__name__!r} is {(t2-t1):.3f}s")
        return result
    return wrapperFunction
  
@runTimeDecorator
def testFun(n):
    for i in range(n):
        for j in range(999999):
            i*i
  
testFun(5)