dict1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
topThreeValues=[]
topThreeKeys=[]
for i in range(3):
    maxValue = -9999
    maxKey = None
    for x,y in dict1.items():
        if(x not in topThreeKeys and y>maxValue):
            maxValue = y
            maxKey = x
    topThreeValues.append(maxValue)
    topThreeKeys.append(maxKey)
for i in range(len(topThreeKeys)):
    print(topThreeKeys[i],topThreeValues[i],sep = " ",end = "\n")