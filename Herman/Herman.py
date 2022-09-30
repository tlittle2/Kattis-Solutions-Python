#/usr/bin/env python3
import sys
import math


def main():
    n= int(sys.stdin.readline())

    num1 = math.pi * pow(n, 2)

    num2= pow(n, 2) * 2

    print('%.6f'% num1)
    print('%.6f' % num2)

if __name__ == "__main__":
    main()