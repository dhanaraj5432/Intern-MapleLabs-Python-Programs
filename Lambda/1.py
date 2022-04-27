array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
even,odd=0,0
lambda_fun= lambda x:x%2
for i in array_nums:
    if(lambda_fun(i)==0):
        even+=1
    else:
        odd+=1
print("Number of even numbers in the array: {}".format(even),"Number of odd numbers in the array: {}".format(odd),sep="\n")