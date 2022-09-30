#/usr/bin/env python3

import sys

def main():
    n= int(sys.stdin.readline())
    b= False
    numList = []
    for i in range(n):
        num= int(sys.stdin.readline())
        numList.append(num)

    for i in range(1, num):
        if i not in numList:
            b= True
            print(i)


    if b== False:
        print("good job")

if __name__ == "__main__":
    main()