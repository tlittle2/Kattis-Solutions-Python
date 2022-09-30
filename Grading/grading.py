#/usr/bin/env python3

import sys

def main():
    a,b,c,d,e = map(int, sys.stdin.readline().split())

    g = int(input())

    if g <= e:
        print('F')

    elif g < d and g >= e:
        print('D')
        
    elif g < c and g >= d:
        print('C')

    elif g < b and g >= c:
        print('B')

    elif g < a  and g >= b:
        print('A')

    elif g>=a:
        print('A')


if __name__ == "__main__":
    main()