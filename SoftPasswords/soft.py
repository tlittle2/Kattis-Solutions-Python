#!usr/bin/env python3
from string import ascii_lowercase
from string import ascii_uppercase

def reverseCase(s,p):
    newString = ""
    for i in p:
        if i in ascii_lowercase:
            newString += i.upper()
        elif i in ascii_uppercase:
            newString+= i.lower()
        else:
            newString+=i

    if newString == s:
        return True

def append(s,p):
    placeholder = p[len(p)-1]
    for i in range(0,10):
        newString = "{}{}".format(p,i)
        if newString == s:
            return True
    



def prepend(s,p):
    placeholder = p[0]
    for i in range(0,10):
        newString = "{}{}".format(i,p)
        if newString == s:
            return True

def identical(s,p):
    if s == p:
        return True

def main():
    s= str(input())
    p= str(input())

    if identical(s,p):
        print("Yes")
        exit()
    
    if prepend(s,p):
        print("Yes")
        exit()
    
    
    if append(s,p):
        print("Yes")
        exit()
    
    if reverseCase(s,p):
        print("Yes")
        exit()
    
    print("No")



if __name__ == "__main__":
    main()