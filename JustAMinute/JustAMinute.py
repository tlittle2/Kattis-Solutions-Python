#/usr/bin/env python3
import sys


def main():
    n= int(sys.stdin.readline())

    mTotal =0
    sTotal = 0
    for i in range(n):
        m, s= map(int, sys.stdin.readline().split())
        mTotal+= m * 60
        sTotal+=s

    total = sTotal/ mTotal

    if(total <= 1):
        print("measurement error")
    else:
        print('%.9f' % total)

if __name__ == "__main__":
    main()