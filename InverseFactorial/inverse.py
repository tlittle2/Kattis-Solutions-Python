#!/usr/bin/env python3

import math

def predefined(n):
    if n == 1:
        return 1
    if n == 2: 
        return 2 
    if n == 6:
        return 3 
    if n == 24:
        return 4 
    if n == 120:
        return 5
    return 6
    
def solve(a):
    i,num = 0,1
    l = []
    while i < a:
        i = math.factorial(num)
        l.append(i)
        num+=1
        if a in l:
            return l.index(a)+1
        


def main():
    a = int(input())

    if len(str(a)) < 4:
        print(predefined(a))
        return 

    num = 6
    logsum = 4 * math.log10(2) + 2 * math.log10(3) + math.log10(5)
    print(logsum)

    while True:
        logsum += math.log10(num);
        if logsum > len(str(a)):
            print(num-1)
            break
        num+=1


    


if __name__ == "__main__":
    main()