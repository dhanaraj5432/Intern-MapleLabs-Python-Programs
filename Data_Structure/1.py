def checkBalancedBrackets(list1):
    temp=[]
    for i in list1:
        if(i in ['(',')','{','}','[',']']):
            temp.append(i)
    listStack=[]
    for i in temp:
        if(i in ['(','{','[']):
            listStack.append(i)
        else:
            if not listStack:
                print("No")
                return
            c=listStack.pop()
            if(c=='('):
                if(i!=')'):
                    print("No")
                    return
            if(c=='{'):
                if(i!='}'):
                    print("No")
                    return
            if(c=='['):
                if(i!=']'):
                    print("No")
                    return
    if listStack:
        print("No")
    else:
        print("Yes")
    return

if __name__=="__main__":
    checkBalancedBrackets("(A+B)+(C-D)")
    checkBalancedBrackets("((A+B)+(C-D)")