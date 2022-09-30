#!/usr/bin/env python3

from collections import Counter

def main():

    s = input()

    c = Counter(s)

    odds = [None for n in c.values() if n % 2]

    if odds:
        print(len(odds) - 1)
    else:
        print(0)

if __name__ == "__main__":
    main()