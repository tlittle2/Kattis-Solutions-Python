#/usr/bin/env python3

import sys

def main():
    line = sys.stdin.readline().strip()

    ourList= list()
    for c in line:
        ourList.append(c)

    if ourList.count("W") == ourList.count("B"):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()