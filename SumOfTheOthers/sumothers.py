#!/usr/bin/env python3
import sys

def main():
    for l in sys.stdin:
        vals = [int(i) for i in l.split()]
        print(sum(vals) //2)

if __name__ == "__main__":
    main()
