#/usr/bin/env python3

import sys

def main():
    while True:
        inp= sys.stdin.readline().split()
        numOfCases= int(inp[0])
        lengthOfCase= int(inp[1])

        if numOfCases==0 or lengthOfCase==0:
            break

        list1= [[0 for x in range(lengthOfCase)] for y in range(numOfCases)]
        list2= ['' for y in range(lengthOfCase)]

        
        for i in range(numOfCases):
            case= str(sys.stdin.readline()).strip()
            list1[i]= list(case)
            #print(list1)
        for i in range(numOfCases):
            for j in range(lengthOfCase):
                list2[j]+= list1[i][j]
        #print(list2)
        list2= sorted(list2,key = str.casefold)

        for i in range(numOfCases):
            for j in range(lengthOfCase):
                print(list2[j][i],end='')
            print()

if __name__ == "__main__":
    main()