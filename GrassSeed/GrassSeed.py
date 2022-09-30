#/usr/bin/env python3
import sys


def main():
    const = float(sys.stdin.readline())
    sum= 0


    numOfIn= int(sys.stdin.readline())
    for i in range(numOfIn):
        num1, num2 = map(float,sys.stdin.readline().split())
        product = num1 * num2
        sum += product

    answer = sum * const

    print(float(answer))

if __name__ == "__main__":
    main()