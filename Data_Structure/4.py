def pairWiseConsecutive(list1):
    listLen=len(list1)
    if(listLen%2!=0):
        list1.pop()
    for i in range(0,len(list1),2):
        if(abs(list1[i]-list1[i+1])!=1):
            print("No, ({0}, {1}) are not consecutive".format(list1[i],list1[i+1]))
            return
    print("Yes")

if __name__=="__main__":
    pairWiseConsecutive([4, 5, -2, -3, 11, 10, 5, 6, 20])
    pairWiseConsecutive([4, 6, 6, 7, 4, 3])