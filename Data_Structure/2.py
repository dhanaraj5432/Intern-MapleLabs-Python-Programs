def rotateArray(list1,m):
    listLen=len(list1)
    m=m%listLen
    temp=list1[m:]+list1[:m]
    print(temp)

if __name__=="__main__":
    arr = [1, 3, 5, 7, 9]
    m = 14
    rotateArray(arr,m)