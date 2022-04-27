list1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
k=0
for i in range(len(list1)):
    if(list1[i]==0):
        temp = list1[k]
        list1[k] = list1[i]
        list1[i] = temp
        k+=1
print(list1)

