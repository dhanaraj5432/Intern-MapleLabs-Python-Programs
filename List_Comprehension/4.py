def checkVowel(s1):
    s1=s1.lower()
    if(('a' in s1) and ('e' in s1) and ('i' in s1) and ('o' in s1) and ('u' in s1)):
        print("Accepted")
    else:
        print("Not Accepted")
if __name__=="__main__":
    checkVowel("aaaaeeiiuuu")
    checkVowel("ABeeIghiObhkUul")