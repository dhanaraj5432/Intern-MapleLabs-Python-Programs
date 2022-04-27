def replaceRightGreatestElement(list1):
    def maxInList(arr):
        max=-1
        for i in arr:
            if(max<i):
                max=i
        return max
    for i in range(len(list1)):
        list1[i]=maxInList(list1[i+1:])
    print(list1)

if __name__=="__main__":
    list1 = [16, 17, 4, 3, 5, 2]
    replaceRightGreatestElement(list1)