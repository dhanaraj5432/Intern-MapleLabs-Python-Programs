dict1 = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
print(dict1)
temp = []
for x in dict1.values():
    if x not in temp:
        temp.append(x)
print(temp)
