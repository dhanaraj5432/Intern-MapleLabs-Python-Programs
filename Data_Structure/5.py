class Queue: 
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, x):
        while len(self.stack1) != 0: 
            self.stack2.append(self.stack1[-1]) 
            self.stack1.pop()
        self.stack1.append(x) 

        while len(self.stack2) != 0: 
            self.stack1.append(self.stack2[-1]) 
            self.stack2.pop()

    def deQueue(self):
        if len(self.stack1) == 0: 
            print("Q is Empty")
        x = self.stack1[-1] 
        self.stack1.pop() 
        return x

    def printQueue(self):
        k = len(self.stack1)
        for i in range(len(self.stack1)):
            print(self.stack1[k-i-1],end=" ")
        print()

if __name__ == "__main__":
    que = Queue()
    que.enQueue(10) 
    que.enQueue(20) 
    que.enQueue(30) 
    que.printQueue()
    print(que.deQueue())
    que.printQueue()
    print(que.deQueue())
    que.printQueue()
    print(que.deQueue())
    que.printQueue()