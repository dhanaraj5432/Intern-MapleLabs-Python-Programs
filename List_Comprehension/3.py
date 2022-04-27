def listPositiveNegative(list1):
    temp1=[]
    temp2=[]
    for i in range(len(list1)):
        k=list1[i]
        if(k<0):
            temp1.append(k)
        else:
            temp2.append(k)
    res = temp1+temp2
    print(res)
    
if __name__=="__main__":
    listPositiveNegative([12, 11, -13, -5, 6, -7, 5, -3, -6])
    listPositiveNegative([-12, 11, 0, -5, 6, -7, 5, -3, -6])