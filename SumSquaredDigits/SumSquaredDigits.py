#/usr/bin/env python3
import sys


def main():
    cases = int(sys.stdin.readline())

    for i in range(cases):
        thiscase, base, num = map(int, sys.stdin.readline().split())

        sum = 0

        while num > 0:
            modulo = num % base
            sum += int(modulo * modulo)
            num = (num - modulo) / base

        print(str(thiscase) + " " + str(sum))


if __name__ == "__main__":
    main()