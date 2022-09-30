#!/usr/bin/env python3

import sys

def main():
    numOfCases= int(sys.stdin.readline())

    for i in range(1, numOfCases + 1):
        print(i, end= "")
        print("  Abracadabra")

if __name__ == "__main__":
    main()