#/usr/bin/env python3

import sys


def main():
    low= int(sys.stdin.readline())
    high= int(sys.stdin.readline())
    value= int(sys.stdin.readline())
    listOfNums= list()
    for i in range(low, high+1):
        ourList= [int(i) for i in str(i)]
        for j in ourList:
            if sum(ourList) == value:
                listOfNums.append(i)

    print(listOfNums[0])
    print(listOfNums[len(listOfNums)-1])

if __name__ == "__main__":
    main()