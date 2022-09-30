#/usr/bin/env python3
import sys


def main():
    cases = int(sys.stdin.readline())

    for i in range(cases):
        inputs = list(map(int, sys.stdin.readline().split()))
        tempValue = None
        sum = 0
        for j in inputs:
            tempValue = inputs[0] - 1
            sum += j
        sum-= tempValue
        sum-=inputs[0]
        print(sum)

if __name__ == "__main__":
    main()