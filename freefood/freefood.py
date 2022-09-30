#/usr/bin/env python3

import sys


def main():
    n = int(sys.stdin.readline())

    l = []

    for i in range(n):
        si, ti = map(int, sys.stdin.readline().split())
        r = range(si, ti + 1)

        for j in r:
            if j not in l:
                l.append(j)

    print(len(l))

if __name__ == "__main__":
    main()