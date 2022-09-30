#/usr/bin/env python3
import sys


def tC(x):
    for i in range(int(x)):
        newNum= x[i] + 1
    return newNum


def main():
    ip= int(sys.stdin.readline())

    print(tC(bin(ip)))

if __name__ == "__main__":
    main()