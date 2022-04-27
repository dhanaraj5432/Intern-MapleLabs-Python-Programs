
marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
filterValue = 170
temp={}
for x,y in marks.items():
    if y>filterValue:
        temp[x]=y
print(temp)