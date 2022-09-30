#/usr/bin/env python3

import sys

def main():
    n= int(sys.stdin.readline())

    integers= []
    floats= []

    for i in range(n):
        ti, vi = map(float, sys.stdin.readline().split())

        integers.append(ti)
        floats.append(vi)

    finalAnswer= 0
    for i in range(1, len(integers)):
        tempAnswer =0
        fractionAnswer= (floats[i-1] + floats[i]) / 2
        #print(fractionAnswer)
        answer2 = integers[i] - integers[i-1]
        tempAnswer+= fractionAnswer * answer2
        finalAnswer += tempAnswer
    print(finalAnswer/1000)

if __name__ == "__main__":
    main()