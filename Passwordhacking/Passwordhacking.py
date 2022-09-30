#/usr/bin/env python3

import sys

def main():
    numOfCases= int(sys.stdin.readline())
    attempt= 0
    exp= 0
    passPercent= []

    for i in range(numOfCases):    
        password, probability= sys.stdin.readline().split()
        password= str(password)
        probability= float(probability)
        passPercent.append(probability)
    passPercent.sort(reverse= True)

    for i in range(numOfCases):
        attempt+=1
        exp+= attempt * passPercent[i]
        
    print(exp)